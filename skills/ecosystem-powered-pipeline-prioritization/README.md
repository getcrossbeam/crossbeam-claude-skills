# README — Ecosystem-Powered Pipeline Prioritization

Find the accounts on your list that are worth acting on now — surfaced by real partner deal activity, not modeled intent.

## What it does

Takes a list of accounts you care about, scans Crossbeam's ecosystem intelligence and signals across each one, and returns a ranked list of the accounts with the most meaningful partner activity — with an optional outreach angle per account so your team knows how to engage.

This isn't a report you build once. Run it on a schedule and you'll know every morning which accounts just moved.

## What Crossbeam Ecosystem Signals are

Ecosystem Signals are partner-driven events that surface real buying motion on your accounts. When a partner opens or closes a deal on an account you're tracking, that's a signal. When multiple partners are active on the same account in the same window, that's a convergence — and convergences tend to mean something is actually happening.

Unlike intent data or behavioral signals, Ecosystem Signals come from actual deal activity inside your partner network. They're not modeled or inferred — a partner worked this account, or they didn't.

## The value of layering Ecosystem Signals with your existing signals

Most teams already have a way to qualify accounts — intent scores, engagement data, pipeline stage, product usage. Crossbeam Ecosystem Signals add a layer those sources can't see.

An account that scores high on intent but also has three partners with active deals is a fundamentally different conversation than intent alone. That convergence — your existing signals plus Crossbeam's ecosystem layer — surfaces accounts that no single source would show you. Ecosystem Signals are valuable on their own. Combined with what you already know, they give you the most complete picture of which accounts have real buying motion happening right now.

## What you need

**Required**
- **Crossbeam connector** — the source of ecosystem intelligence and signals. Connect from the Claude connector directory or at crossbeam.com. Make sure you're authenticated to the right org before running.

**Required — account source**
You need a list of accounts to scan. Configure where that list comes from in the skill's Configuration section before running. This can be a segment from your CRM, a prospect list, a set of open opportunities, or any account list your team maintains.

**Optional but recommended**
Crossbeam Ecosystem Signals stand on their own — real partner deal activity is a signal worth acting on regardless of what else you know about an account. But if you want a 360-degree view, layering Ecosystem Signals with your existing qualification and intent data gives you a more complete picture. An account showing partner activity AND scoring high on intent AND having recent engagement is a convergence of signals that no single source could surface alone.

## Before this works — what your partners need to share

Ecosystem Signals depend on your partners sharing their CRM deal data with you in Crossbeam. If a partner isn't sharing the right fields, their activity on your accounts won't surface as a signal — even if they're active on those accounts.

**For signals to appear, your partner must:**

- **Have a CRM connected to Crossbeam**
- **Be syncing and sharing the following fields with you:**
  - **Deal open date**
  - **Deal close date**
  - **Deal is closed**
  - **Deal is won**

> **Note:** Your company only needs to sync these fields with Crossbeam — you do not need to share them back with your partner.

**To receive contact information on signals, your partner must also:**

- **Be syncing and sharing CRM contact data**

**If contact data is included, signals may contain:**

- **Contact Name**
- **Contact Title**

**What this means in practice:** If you scan 300 accounts and a key partner isn't sharing deal fields, their activity on those accounts won't appear. Before running at scale, check with your Crossbeam admin or partnerships lead which of your key partners have data sharing active. Partners who are connected but not sharing deal fields are worth a conversation — the signal value goes up on both sides.

## Setup: what to configure before your first run

**Step 1 — Connect Crossbeam**
Connect from the Claude connector directory or at crossbeam.com. Authenticate to the right org. If you're unsure, just ask Claude.

**Step 2 — Define your account source**
Decide which list of accounts to scan and fill it into the Configuration section of this skill. This is your starting list — Crossbeam Ecosystem Signals will be layered on top to show which accounts have active partner motion.

> **Fill in before sharing:** `Account source: [describe your account list here]`

**Step 3 — Set your signal lookback window**
How far back should the scanner look for partner activity? 30, 60, or 90 days is typical. Fill this into the Configuration section.

> **Fill in before sharing:** `Signal lookback window: [e.g. 90 days]`

**Step 4 — Set your Crossbeam partner tags (optional)**
If you want the scanner to focus on signals from specific partners — Tier 1s, co-sell partners, strategic ISVs — fill in which Crossbeam tags identify them. If left blank, signals from all partners are included.

> **Fill in before sharing:** `Strategic partner tags: [e.g. Tier 1, Co-Sell]`

**Step 5 — Decide on output format**
Where do you want the ranked list delivered? In chat, to a Slack channel, or somewhere else? Fill in your preference. You can also set this up as a scheduled daily or weekly scan.

> **Fill in before sharing:** `Output destination: [e.g. chat, Slack channel name]`

**Step 6 — Set your volume confirmation threshold (optional)**
If your account list is large, this sets a limit at which Claude will pause and ask you to confirm before scanning. Useful if you're connecting to a large segment and want to avoid accidentally running the scanner across thousands of accounts on the first try. If you're confident in your list size, you can leave this blank.

> **Fill in before sharing:** `Volume confirmation threshold: [e.g. 100 accounts — or leave blank for no limit]`

**Step 7 — Run it once and adjust**
After your first run, ask Claude to help you refine the scoring weights, adjust the lookback window, or trim the output format for your team.

## How to run it

> "Run the ecosystem pipeline scanner"
> "Scan my account list for partner signals"
> "Which of my accounts have ecosystem activity this week?"
> "Run the scanner and give me outreach angles for the top accounts"

## What to expect

- **Ranked output:** accounts sorted by signal strength — number of active partners, recency, event types. Closed-won signals from a partner weigh more than open deals. Multiple partners on the same account weigh more than one.
- **Signal summaries per account:** what's moving, which partners, what it likely means for the buying situation.
- **Outreach angles (optional):** if requested, a suggested entry point per account based on the partner activity context.
- **No partner contact details surfaced directly:** if a signal suggests a partner play, the scanner notes that contact details are available and recommends looping in your partnerships lead. They'll have the relationship context for the right intro.
- **Accounts with no signals:** noted in the output so you know the scan ran — not silently dropped.
- **Partnerships lead note:** before acting on any ecosystem signal, check with your partnerships lead. They may already have an active motion with that partner on that account, and coordinating through them gets you a warmer path.

## Not sure how to set something up?

Just ask Claude — it can walk you through connecting tools, finding your Crossbeam partner tags, setting up a scheduled run, or adapting the output format for your team.

## Related

- **Ecosystem-Informed Account Brief** — once the scanner surfaces an account worth a deeper look, use this skill to get the full picture.
- **Partner Alignment Outreach** — for post-close partner alignment on accounts you've already won.
