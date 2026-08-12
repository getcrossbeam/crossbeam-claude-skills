#!/usr/bin/env python3
"""Eval harness for the Crossbeam skills in this repo.

Executing an eval requires an AI agent, so this tool does the parts a script can do
reliably: it validates every suite, inventories the cases, and emits the exact
blind-executor prompt for a case so runs stay comparable between people.

    python3 evals/run.py validate            # check every evals.json (exit 1 on error)
    python3 evals/run.py list                # inventory all cases
    python3 evals/run.py list elg-advisor    # inventory one skill
    python3 evals/run.py prompt elg-advisor 1   # emit the executor prompt for one case
    python3 evals/run.py rubric elg-advisor 1   # emit the grading rubric for one case

No third-party dependencies. Python 3.8+.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"

REQUIRED_CASE_KEYS = ("id", "name", "prompt", "expected_output")

EXECUTOR_TEMPLATE = """\
You are Claude Code responding to a real user. A skill applies to their request.

STEP 1: Read {skill_md} in full and treat it as your governing instructions.
Follow its own guidance about reading any files in its references/ directory.

STEP 2: Respond to this user request:
"{prompt}"

HARD CONSTRAINTS (sandboxed evaluation run):
- Read-only. Do NOT send email, create inbox drafts, post to Slack, or write to any
  CRM, MAP, or sequencer. Do not modify files outside a temp directory.
- You MAY use read-only MCP tools and web search where the skill directs you to.
- If a source or dependency the skill wants is unavailable, follow whatever the skill
  says to do. Do NOT invent data to fill the gap.

OUTPUT: Return your complete final user-facing response, verbatim, exactly as it would
appear in chat. No meta-commentary about being evaluated.
"""


def discover():
    """Yield (skill_dir, suite_path, suite_or_None, error_or_None) for every skill."""
    if not SKILLS.is_dir():
        sys.exit(f"error: no skills/ directory at {SKILLS}")
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        suite_path = skill_dir / "evals" / "evals.json"
        if not suite_path.exists():
            yield skill_dir, suite_path, None, "no evals/evals.json"
            continue
        try:
            with suite_path.open(encoding="utf-8") as fh:
                yield skill_dir, suite_path, json.load(fh), None
        except json.JSONDecodeError as exc:
            yield skill_dir, suite_path, None, f"invalid JSON: {exc}"


def frontmatter_name(skill_dir):
    """Read `name:` out of the SKILL.md frontmatter, or None."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return None
    text = skill_md.read_text(encoding="utf-8")
    match = re.search(r"^name:\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def validate():
    problems, case_total, suite_total = [], 0, 0

    for skill_dir, suite_path, suite, error in discover():
        rel = suite_path.relative_to(REPO)
        slug = skill_dir.name

        if error:
            problems.append(f"{rel}: {error}")
            continue
        if not isinstance(suite, dict):
            problems.append(f"{rel}: top level must be an object")
            continue

        suite_total += 1

        declared = suite.get("skill_name")
        if declared != slug:
            problems.append(f"{rel}: skill_name {declared!r} != folder name {slug!r}")
        fm = frontmatter_name(skill_dir)
        if fm is not None and declared is not None and fm != declared:
            problems.append(f"{rel}: skill_name {declared!r} != SKILL.md frontmatter {fm!r}")
        if fm is None:
            problems.append(f"{slug}/SKILL.md: missing or unreadable `name:` frontmatter")

        cases = suite.get("evals")
        if not isinstance(cases, list) or not cases:
            problems.append(f"{rel}: 'evals' must be a non-empty list")
            continue

        seen_ids, seen_names = set(), set()
        for pos, case in enumerate(cases):
            label = f"{rel}[{pos}]"
            if not isinstance(case, dict):
                problems.append(f"{label}: case must be an object")
                continue
            case_total += 1

            for key in REQUIRED_CASE_KEYS:
                if key not in case:
                    problems.append(f"{label}: missing required key {key!r}")

            cid = case.get("id")
            if not isinstance(cid, int):
                problems.append(f"{label}: 'id' must be an integer, got {cid!r}")
            elif cid in seen_ids:
                problems.append(f"{label}: duplicate id {cid}")
            else:
                seen_ids.add(cid)

            name = case.get("name")
            if isinstance(name, str):
                if name in seen_names:
                    problems.append(f"{label}: duplicate name {name!r}")
                seen_names.add(name)
                if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
                    problems.append(f"{label}: name {name!r} is not kebab-case")

            for key in ("prompt", "expected_output"):
                val = case.get(key)
                if not isinstance(val, str) or not val.strip():
                    problems.append(f"{label}: {key!r} must be a non-empty string")

            # A prompt naming its own skill leaks the rubric and invalidates the run.
            prompt = case.get("prompt")
            if isinstance(prompt, str) and slug in prompt:
                problems.append(f"{label}: prompt names the skill slug; executors must be blind")

    print(f"{suite_total} suite(s), {case_total} case(s)")
    if problems:
        print(f"\n{len(problems)} problem(s):", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1
    print("all suites valid")
    return 0


def list_cases(only=None):
    found = False
    for skill_dir, _, suite, error in discover():
        if only and skill_dir.name != only:
            continue
        found = True
        if error:
            print(f"\n{skill_dir.name}\n  ! {error}")
            continue
        cases = suite.get("evals") or []
        print(f"\n{skill_dir.name}  ({len(cases)} case(s))")
        for case in cases:
            marker = "R" if "regression" in str(case.get("name", "")) else "-"
            print(f"  {marker} [{case.get('id')}] {case.get('name')}")
            print(f"      {str(case.get('prompt', ''))[:96]}...")
    if only and not found:
        print(f"no skill named {only!r}", file=sys.stderr)
        return 1
    print("\n(R = regression test guarding a specific fix)")
    return 0


def get_case(skill, case_id):
    for skill_dir, _, suite, error in discover():
        if skill_dir.name != skill:
            continue
        if error:
            sys.exit(f"error: {skill}: {error}")
        for case in suite.get("evals") or []:
            if case.get("id") == case_id:
                return skill_dir, case
        sys.exit(f"error: {skill} has no case with id {case_id}")
    sys.exit(f"error: no skill named {skill!r}")


def emit_prompt(skill, case_id):
    skill_dir, case = get_case(skill, case_id)
    print(EXECUTOR_TEMPLATE.format(
        skill_md=(skill_dir / "SKILL.md"),
        prompt=case["prompt"],
    ))
    return 0


def emit_rubric(skill, case_id):
    _, case = get_case(skill, case_id)
    print(f"# {skill} / [{case['id']}] {case['name']}\n")
    print("## Prompt given to the executor\n")
    print(case["prompt"] + "\n")
    print("## Grading rubric (never show this to the executor)\n")
    print(case["expected_output"])
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Validate, inventory, and emit prompts for the skill evals.",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="check every evals.json")
    p_list = sub.add_parser("list", help="inventory cases")
    p_list.add_argument("skill", nargs="?")
    p_prompt = sub.add_parser("prompt", help="emit the blind executor prompt for a case")
    p_prompt.add_argument("skill")
    p_prompt.add_argument("id", type=int)
    p_rubric = sub.add_parser("rubric", help="emit the grading rubric for a case")
    p_rubric.add_argument("skill")
    p_rubric.add_argument("id", type=int)

    args = parser.parse_args()
    if args.command == "validate":
        return validate()
    if args.command == "list":
        return list_cases(args.skill)
    if args.command == "prompt":
        return emit_prompt(args.skill, args.id)
    if args.command == "rubric":
        return emit_rubric(args.skill, args.id)
    return 1


if __name__ == "__main__":
    sys.exit(main())
