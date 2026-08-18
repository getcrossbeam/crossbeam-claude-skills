# Evals

Each skill carries its own suite at `skills/<skill>/evals/evals.json`. There are 26 cases
across the 10 skills.

```bash
python3 evals/run.py validate                 # check every suite, exit 1 on error
python3 evals/run.py list                     # inventory all cases
python3 evals/run.py list elg-advisor         # inventory one skill
python3 evals/run.py prompt elg-advisor 1     # emit the blind executor prompt for a case
python3 evals/run.py rubric elg-advisor 1     # emit the grading rubric for a case
```

No dependencies, Python 3.8+.

## What the script does and does not do

Executing a case means running a skill against a real request, which needs an AI agent, not a
script. So `run.py` does the parts a script can do reliably — validating suites, inventorying
cases, and emitting the exact executor prompt so two people running the same case run the same
thing. The execution and grading steps are below and are performed by an agent.

## Case shape

```json
{
  "id": 0,
  "name": "kebab-case-name",
  "prompt": "a realistic first-person request, as a user would actually type it",
  "expected_output": "what a correct response must contain, and what it must not do",
  "files": [],
  "assertions": []
}
```

`files` and `assertions` are reserved and currently empty everywhere.

Every suite has at least one **happy path** case and at least one case that probes a
**guardrail the SKILL.md explicitly commits to** — a "never do X" rule, a degradation path when
data is missing, a required clarifying question, or a scope boundary. Cases named
`regression-*` guard a specific defect that was found and fixed; they are the ones to run first
after editing a skill.

## How to run a case

The method matters more than the tooling. Three properties keep results honest:

1. **The executor is blind to the rubric.** Give the agent only the skill path and the
   `prompt` — never `expected_output`. An agent that knows what is being measured will satisfy
   the rubric rather than reveal how the skill actually behaves. `run.py prompt` emits exactly
   what the executor should receive; the validator rejects any prompt that names its own skill
   slug, since that leaks the answer.
2. **Each case runs in a fresh context.** One subagent per case. Cases share no history, so a
   skill cannot benefit from a previous case's corrections.
3. **Grading is a separate step from execution.** Whoever grades reads the response against
   `expected_output` and checks factual claims back against the skill files and reference docs
   rather than trusting the executor's own account of what it did.

Run it like this:

```bash
python3 evals/run.py prompt crossbeam-co-sell-copilot 1   # paste into a fresh agent
python3 evals/run.py rubric crossbeam-co-sell-copilot 1   # grade the response against this
```

Every case is read-only by construction: no sends, no inbox drafts, no CRM or sequencer writes.
Skills that normally create drafts are constrained to chat output. Keep it that way — an eval
suite that mails real partner reps is worse than no eval suite.

## No customer data in this repo

This repository is public. **No account names, partner names, contacts, metrics, or report
links from a real Crossbeam instance belong in a skill or an eval fixture.** Retrieving that
data at runtime is the whole point of these skills; committing it as content is not.

Cases that genuinely need a real account ship a placeholder instead:

```
<ACCOUNT>      a single account
<ACCOUNT_1>…   a list of accounts
```

Substitute your own before running. Each such case says in its `expected_output` what kind of
account to pick, because the choice affects whether the case tests anything — the scoring
regression, for example, is meaningless unless one of your accounts has high partner overlap
but no recent activity. `run.py prompt` prints a warning listing any placeholders it finds,
and `run.py validate` fails a case that has placeholders without a substitution note.

Company names that appear literally in fixtures are **invented** and meant not to resolve to a
real business. If one collides with a real company, rename it — a fixture that attaches a
fabricated scenario to a real named company is the same problem in a different direction.

## Before you run

Five skills need the Crossbeam MCP connected and authenticated (Co-Sell Copilot, Ecosystem
Prospecting, Account Brief, Pipeline Prioritization, Partner Alignment Outreach). Confirm it
returns real data *before* running their cases, otherwise you are measuring auth failures rather
than skill behavior. Those five also need their Configuration block filled in — except for the
cases that deliberately test the unconfigured hard-stop, which must be run against an
unconfigured copy.

Some cases name deliberately fictional companies (Globex, Kestrelline, Sableway Logistics,
Halden Freight, Calderon Health, Northmark) to test whether a skill invents data for something
it cannot find. Do not "fix" these to real accounts and do not substitute placeholders for them
— refusing to fabricate is the behavior under test, and it only works if the company genuinely
does not resolve.

## Writing a new case

- Ground the rubric in what the SKILL.md actually promises. Quote the line a guardrail case
  probes. Do not invent requirements the skill never states.
- Make the rubric checkable by reading a response: name the required sections, the honesty
  requirements, and the specific failure modes.
- Write the prompt the way a salesperson would type it. No skill names, no hints about what is
  being measured, and never a request to send anything.
- Prefer a countable check over a stated preference. "Exactly one question mark in the body" is
  gradeable; "the tone should be human" is not.
- Run `python3 evals/run.py validate` before committing.
