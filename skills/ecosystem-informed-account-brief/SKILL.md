---
name: ecosystem-informed-account-brief
description: Produce a structured account brief enriched with Crossbeam's ecosystem intelligence and signals — partner overlap, ecosystem relationships, and recent partner activity signals. Uses the sources the user has configured plus Crossbeam MCP and recent news. Use whenever someone asks to be "briefed on" an account, wants an "overview" or "context" on an account, or asks "what do we know about X". For one-off lookups or qualitative questions across communications, use a direct query to the relevant source instead.
---

# README — Ecosystem-Informed Account Brief

Get a structured picture of any account — what's happening in your conversations, where your partners are moving on this account, and what to do next.

## What it does

Combines your configured account and sales intelligence with Crossbeam's ecosystem intelligence and signals to produce a single structured brief. Crossbeam brings a layer no other source has — which partners overlap on this account, what population they're in, who owns the relationship on their side, and what's actually moving in your ecosystem around this account (deals opened, deals closed, greenfield signals). That context sits alongside everything else you know about the account so you can act on it.

## What you need

**Required**
- **Crossbeam connector** — the ecosystem layer that makes this brief different from any single data source. Connect from the Claude connector directory or at crossbeam.com. Make sure you're authenticated to the right org before running.

**Optional but recommended**
Crossbeam's ecosystem intelligence and signals become even more valuable when layered with your account intelligence and sales intelligence tools. It notes what wasn't configured so you know where the brief has gaps.

## Setup: what to configure before your first run

**Step 1 — Connect your sources**
Connect the tools your team uses from the Claude connector directory. Start with what you have. If you're unsure what's connected or how to add something, just ask Claude.

**Step 2 — Define your configured sources**
Decide which sources you want included in every brief and fill them into the Configuration section of this skill under "Configured sources." These become your defaults — Claude will use them without asking each time.

> **Fill in before sharing:** `Configured sources: [list your sources here]`

You can still override on a per-run basis ("brief me on Acme, skip [source] this time") but the configured list is the default. If nothing is configured, Claude will stop and ask before pulling anything.

**Step 3 — Set your Crossbeam partner tags (optional)**
If you want the brief to focus on specific partners — Tier 1s, active co-sell partners, strategic ISVs — fill in which Crossbeam tags identify them in the Configuration section.

> **Fill in before sharing:** `Strategic partner tags: [e.g. Tier 1, Co-Sell]`

Tags need to match what's already applied in Crossbeam. If left blank, the brief surfaces all ecosystem relationships with no filter.

**Step 4 — Customize the brief template (optional)**
The brief template in Step 5 is a starting point. Remove sections that don't apply to your team, rename fields to match your product, and fill in `[your product]` wherever it appears. Ask Claude to help you adapt it.

**Step 5 — Run it once and adjust**
After your first run, ask Claude to help you refine any sections based on what was most useful.

## How to run it

> "Brief me on [Account]"
> "Give me an overview of [Account]"
> "What do we know about [Account]?"

## What to expect

- **Ecosystem intelligence called out explicitly** — where Crossbeam data changes the picture (a partner with an open deal, a greenfield signal, a risk from ecosystem movement), the brief calls it out rather than burying it.
- **Crossbeam-only runs:** the brief works without account or sales intelligence sources configured — you'll still get full ecosystem intelligence. Adding those sources layers in account context that makes the ecosystem signals more actionable.
- **Missing sources:** the brief notes what wasn't configured rather than failing.
- **No ecosystem relationships found:** normal for some accounts. The brief notes it clearly.
- **One-off lookups** aren't what this skill is for — ask Claude to query your source directly.

## Not sure how to set something up?

Just ask Claude — it can walk you through connecting tools, finding your Crossbeam partner tags, or adapting the brief template for your team.

## Related

- **Meeting prep** — if you have a specific upcoming meeting with known attendees, use the meeting-prep skill instead.
- **One-off lookups** — ask Claude to query your source directly for time-windowed or count-bounded requests.

---

# Skill Instructions

Produces a structured account brief by combining configured data sources with Crossbeam's ecosystem intelligence and signals. One output: the brief.

---

## Configuration
> These values are set once by whoever deploys this skill. Claude reads them at runtime — do not change them mid-conversation.

**Configured sources:** [list your sources here]

**Strategic partner tags (optional):** [fill in — e.g. Tier 1, Co-Sell. Leave blank to surface all ecosystem relationships.]

**Your product name:** [fill in — e.g. Crossbeam]

---

Crossbeam MCP is required. The brief works with Crossbeam alone — but ecosystem signals become significantly more actionable when layered with your account intelligence and sales intelligence tools. The more context you configure, the more complete the picture.

Configured sources are the default for every run. Individual runs can override ("skip [source] this time", "include [source] for this one"). If configured sources are blank, stop and tell the user they need to be defined in the Configuration section before the skill can run — do not pull from any source that is not explicitly listed there.

---

## Step 1 — Resolve the account

Infer the domain from the account name if not provided. If ambiguous, ask once.

---

## Step 2 — Gather account data

Use only the sources explicitly listed in the Configuration section above. Do not pull from any source not listed there, even if it is connected. If only Crossbeam is configured, the brief will reflect ecosystem intelligence only — account and sales intelligence sources are optional but make the ecosystem signals more actionable when included.

If the user overrides for this run ("skip [source] this time", "include [source]"), apply that override for this run only.

If a configured source isn't connected, tell the user and ask if they'd like to connect it or skip it for this run.

---

## Step 3 — Pull ecosystem data via Crossbeam MCP

Run all three calls. If the account isn't found in Crossbeam, note it and skip to Step 4.

**3a — Resolve the account**
```
Crossbeam:get_own_account_info(account_domain: "example.com")
```
Extract the `record_id`.

**3b — Get partner overlap**
```
Crossbeam:get_account_overlap_info(account_id: "<record_id>")
```
If strategic partner tags are configured, also call:
```
Crossbeam:find_partners(partner_tag_id: "<tag_id>")
```
Then intersect — keep only overlaps where the partner matches a tagged partner. If no tags configured, use all overlapping partners.

For each match capture: partner name, population name, and partner owner name if available. Do not surface partner owner contact details (email, phone) in the brief. If a signal suggests a partner motion, note in NEXT STEPS that partner owner contact details are available but recommend coordinating with their partnerships lead before reaching out — they may already have an active relationship or motion with this partner.

**3c — Get ecosystem activity signals**
```
Crossbeam:get_ecosystem_activity(account_domain: "example.com")
```
If strategic partner tags are configured, filter to those partners by name. If any partner name is ambiguous, resolve the ClarificationRequired before proceeding.

Capture: event type (deal opened / deal closed won / greenfield), partner name, date, contact context if available.

Flag signals that should surface in the brief:
- A partner with an open opportunity on this account = co-sell signal, surface in ECOSYSTEM RELATIONSHIPS and NEXT STEPS
- A partner who closed won on this account = mutual customer signal, surface in ECOSYSTEM RELATIONSHIPS
- A greenfield signal = net new opportunity via partner, surface in GROWTH OPPORTUNITIES
- A partner going dark or no recent activity where there was previously overlap = risk signal, surface in RISKS & CONCERNS

---

## Step 4 — Pull recent news

Web search for the account name + "funding", "acquisition", "leadership", "launch", "news" scoped to the last 30 days. Capture a 1–2 sentence summary. If nothing material, note "nothing notable."

---

## Step 5 — Synthesize the brief

Using all data gathered, produce the brief below. Rules:
- **Surface Crossbeam's contribution explicitly.** Where ecosystem data changes the picture — a partner with an open deal, movement in the ecosystem, a greenfield signal, a risk — call it out directly. Don't let it disappear into a bullet. The rep should be able to see at a glance what Crossbeam added to this brief that they couldn't get anywhere else.
- **Where account or sales intelligence sources are configured**, use them to add context around the ecosystem signals — a partner with an open opp means more when you also know the account's deal stage, sentiment, or recent activity.
- Lead with what's most actionable.
- When sources conflict, trust the most recent.
- If you can't answer something with confidence, write "No information" — never guess.
- Be succinct. No filler. No generic statements that apply to any account.
- Tailor next steps and discovery questions to any context the user provided.
- Risks & Concerns must be affirmatively justified — if no risks, cite the evidence. An empty section without justification is a failed brief.

---
## TLDR
**[Account]** — [Status] — $[ARR/contract value] — Last touch: [X days ago / never]

Scores: [health/engagement scores, or "not available"] · Usage: [seats/exports/key metric]
Ecosystem: [overlapping partners, or "none identified"] · Recent ecosystem activity: [most notable signal, or "none"]

📰 [1–2 sentence recent news, or "nothing notable"]
⚡ [Recommended next action — one sentence.]

---
## ACCOUNT CONTEXT
**Domain:**
**Account status:**
**Segment:**

---
## PRODUCT USAGE
[Usage metrics and product data from configured sources. If unavailable, say so.]

---
## OVERVIEW
**What they do:**
**Business model:**
**Tech stack:**

---
## THE TEAM
- [Name] — [Role] — [Champion / Sponsor / User / Unknown]

---
## CLIENT OBJECTIVES
- Problem they're solving with [your product name from Configuration]:
- KPIs they're measured on:
- Main use cases today:
- Other potential use cases:
- Compelling event or upcoming initiative:

---
## ECOSYSTEM RELATIONSHIPS
**What Crossbeam shows:**
- [Partner name] — [Population]

**Recent ecosystem activity:**
- [Date] — [Partner name] — [Event: deal opened / deal closed won / greenfield] — [Contact context if available]

**Why it matters:**
Call out specifically what the ecosystem data means for this account — a partner with an open opp is a co-sell opportunity, a closed won is a mutual customer worth aligning on, a greenfield is a net new intro. If nothing is actionable, say so plainly. Where a signal suggests a partner play, note that partner contact details are available and recommend looping in their partnerships lead before engaging — they'll have the relationship context and can make the right intro.

If no overlap: "No ecosystem relationships identified in Crossbeam."
If no activity: "No recent ecosystem activity."

---
## RISKS & CONCERNS
Tag each with severity: 🔴 High / 🟡 Medium / 🟢 Low.

- **Single points of failure:** [severity] — who/what, why it matters
- **Competing tools in use:** [severity]
- **Adoption gaps:** [severity]
- **Negative sentiment or churn signals:** [severity] — source and summary
- **Ecosystem risk signals:** [severity] — e.g. partner closing competing deal, key partner going dark, no ecosystem movement where expected
- **Other risks:** [severity]

---
## GROWTH OPPORTUNITIES
- Known expansion signals:
- Untapped use cases:
- Ecosystem opportunities: [partner-influenced plays, co-sell potential, greenfield signals from Crossbeam]

---
## NEXT STEPS
### If sales process active:
- Decision process:
- Timeline / milestones:
- Blockers:
- Action items:
- Ecosystem plays: [which partners to loop in and why, based on Step 3 data]

### If existing customer:
- Next steps:
- Actions needed from both sides:
- Ecosystem plays: [which partners to loop in and why]

---
## DISCOVERY QUESTIONS
5–8 sharp, specific questions based on gaps in the data and the account's profile.

---
## SUPPORT & SENTIMENT
**Help desk:** [count, date range, issue types, tone, recurring patterns. Or "not configured — skipped."]
**Negative sentiment:** [any frustration, dissatisfaction, or loss of confidence across any source]
**Churn signals:** [cancellation mentions, contract review, evaluating alternatives, low usage, champion departure]
If none detected: "No negative sentiment or churn signals detected."

---
## INTERNAL CONTEXT
[2–4 bullets from configured internal messaging source, with dates. Or "not configured — skipped." Or "No dedicated channel found."]

---

## Rules

- One output: the brief.
- Always run the Crossbeam ecosystem steps (Step 3) — skip only if the account isn't found in Crossbeam.
- Surface Crossbeam's contribution explicitly in the brief — ecosystem signals should never be invisible.
- **Never pull from a source not explicitly listed in the Configuration section.** Connected does not mean configured — only sources the user has defined in Configuration are used.
- Strategic partner tag IDs are set by the user in Configuration — do not hardcode them.
- Risks & Concerns must be affirmatively justified, never empty.
- The brief is for internal use only.
- If the user mentions a specific upcoming meeting with known attendees, suggest the meeting-prep skill instead.
