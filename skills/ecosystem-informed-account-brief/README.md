# README — Ecosystem-Informed Account Brief

Get a structured picture of any account — what's happening in your conversations, where your partners are moving on this account, and what to do next.

## What it does

Combines your configured account and sales intelligence with Crossbeam's ecosystem intelligence and signals to produce a single structured brief. Crossbeam brings a layer no other source has — which partners overlap on this account, what population they're in, who owns the relationship on their side, and what's actually moving in your ecosystem around this account (deals opened, deals closed, greenfield signals). The brief works with Crossbeam alone, but those ecosystem signals become significantly more actionable when layered with your account intelligence and sales intelligence tools — deal stage, recent activity, sentiment, and usage data all add context that turns an ecosystem signal into a concrete next step.

## What you need

**Required**
- **Crossbeam connector** — the ecosystem layer that makes this brief different from any single data source. Connect from the Claude connector directory or at crossbeam.com. Make sure you're authenticated to the right org before running.

**Optional but recommended**
Crossbeam's ecosystem intelligence and signals become significantly more actionable when layered with your account intelligence and sales intelligence tools. A partner with an open opportunity on this account means something different depending on where you are in the deal, what sentiment looks like, and how engaged the account has been. Configure your other sources to get that full picture. The brief notes what wasn't configured so you know where the gaps are.

## Setup: what to configure before your first run

**Step 1 — Connect your sources**
Connect the tools your team uses from the Claude connector directory. Start with what you have. If you're unsure what's connected or how to add something, just ask Claude.

**Step 2 — Define your configured sources**
Decide which sources you want included in every brief and fill them into the Configuration section of the skill under "Configured sources." These become your defaults — Claude will use them without asking each time.

If nothing is configured, Claude will stop and ask before pulling anything.

**Step 3 — Set your Crossbeam partner tags (optional)**
If you want the brief to focus on specific partners — Tier 1s, active co-sell partners, strategic ISVs — fill in which Crossbeam tags identify them in the Configuration section of the skill.

Tags need to match what's already applied in Crossbeam. If left blank, the brief surfaces all ecosystem relationships with no filter.

**Step 4 — Customize the brief template (optional)**
The brief template is a starting point. Remove sections that don't apply, replace `[your product]` with your product name, and ask Claude to help you adapt it for your team's workflow.

**Step 5 — Run it once and adjust**
After your first run, ask Claude to refine any sections based on what was most useful.

## How to run it

> "Brief me on [Account]"
> "Give me an overview of [Account]"
> "What do we know about [Account]?"

## What to expect

- **Ecosystem intelligence called out explicitly** — where Crossbeam data changes the picture (a partner with an open deal, movement in the ecosystem, a greenfield signal, a risk), the brief calls it out rather than burying it.
- **Crossbeam-only runs:** the brief works with just Crossbeam configured — you'll still get full ecosystem intelligence. Adding account and sales intelligence sources makes those signals more actionable.
- **Missing sources:** the brief notes what wasn't configured rather than failing.
- **No ecosystem relationships found:** normal for some accounts. The brief notes it clearly.
- **Partner contact details:** partner owner contact information is available in Crossbeam but isn't surfaced directly in the brief. Where an ecosystem signal suggests a partner play, the brief will recommend looping in your partnerships lead — they'll have the relationship context and can make the right intro.
- **One-off lookups** aren't what this skill is for — ask Claude to query your source directly.

## Not sure how to set something up?

Just ask Claude — it can walk you through connecting tools, finding your Crossbeam partner tags, or adapting the brief template for your team.

## Related

- **Meeting prep** — if you have a specific upcoming meeting with known attendees, use the meeting-prep skill instead.
- **One-off lookups** — ask Claude to query your source directly for time-windowed or count-bounded requests.
