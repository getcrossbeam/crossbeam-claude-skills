#!/usr/bin/env bash
# Build one distributable .zip per skill into dist/skill-bundles/.
#
# These are the bundles published at crossbeam.com/claudeskills for people who upload a
# skill by hand rather than installing the plugin. dist/ is gitignored, so this is a local
# build step: rerun it whenever a SKILL.md, a references/ file, or an eval suite changes.
#
#   ./scripts/build-bundles.sh
#
# Requires `zip`. Each archive contains the skill folder itself (SKILL.md plus any
# references/ subfolder), so unzipping yields a directory ready to upload.
#
# evals/ is deliberately excluded. Each evals.json carries `expected_output`, which is the
# grading rubric, and evals/README.md is explicit that the executing agent must never see it.
# Shipping the rubric inside the folder a user uploads to Claude would put it in front of the
# very agent it is meant to measure. The runner that makes a suite usable (evals/run.py) lives
# at the repo root and is not in the bundle either, so the file would be dead weight regardless.
# Anyone who wants to run the suites should clone the repo.

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="$repo_root/skills"
out_dir="$repo_root/dist/skill-bundles"

if ! command -v zip > /dev/null 2>&1; then
  echo "error: 'zip' is not installed" >&2
  exit 1
fi

if [ ! -d "$skills_dir" ]; then
  echo "error: no skills/ directory at $skills_dir" >&2
  exit 1
fi

# Validate before packaging, so a broken eval suite never ships in a bundle.
if [ -f "$repo_root/evals/run.py" ]; then
  echo "Validating eval suites..."
  python3 "$repo_root/evals/run.py" validate
  echo
fi

rm -rf "$out_dir"
mkdir -p "$out_dir"

count=0
for skill_path in "$skills_dir"/*/; do
  skill="$(basename "$skill_path")"

  if [ ! -f "$skill_path/SKILL.md" ]; then
    echo "  skip $skill (no SKILL.md)"
    continue
  fi

  # Zip from skills/ so the archive contains the folder, not its bare contents.
  ( cd "$skills_dir" && zip -qr "$out_dir/$skill.zip" "$skill" -x '*.DS_Store' -x "$skill/evals/*" )

  size="$(du -h "$out_dir/$skill.zip" | cut -f1 | tr -d ' ')"
  printf '  built %-46s %s\n' "$skill.zip" "$size"
  count=$((count + 1))
done

echo
echo "$count bundle(s) in ${out_dir#"$repo_root"/}"
