# Partner Alignment Outreach

Turn recent closed-won deals into partner alignment emails — one per deal, addressed to the right rep at the right partner.

## What it does

1. Pulls your recent closed-won deals from your CRM or data warehouse
2. Looks up each won account in Crossbeam to find which partners overlap on it and who owns the relationship on their side
3. Drafts a short, rep-to-rep alignment email for each deal
4. Saves drafts to your Gmail or Outlook inbox (or delivers them as text if no email connector is available)

Nothing is sent automatically. You review every draft before it goes anywhere.

## What you need

**Required**
- **Crossbeam connector** — connect it from the Claude connector directory or at crossbeam.com. The skill won't run without it. Make sure you're authenticated to the right org before starting.

**At least one of these (for pulling deals)**
- Salesforce connector
- HubSpot connector
- Snowflake or warehouse connector
- Or just paste a list of account names — the skill handles that too

**Optional**
- Gmail or Outlook connector — if connected, drafts are saved directly to your inbox. If not, Claude will ask how you'd like to receive them before generating anything.

## Before your first run: two things to configure

### 1. Deal source
Tell the skill where to pull closed-won deals from. If you have a CRM or warehouse connector, it will detect that automatically. If you use multiple sources or want to pull from a specific pipeline or team, specify it when you run the skill:

> "Run partner alignment outreach, pull deals from Salesforce"
> "Run partner alignment outreach using our Snowflake warehouse"

If you don't specify anything and only one source is connected, it'll use that.

### 2. Strategic partner tags (optional but recommended)
If you have partners you're most focused on — Tier 1s, active co-sell partners, specific ISVs — tell the skill which Crossbeam tags identify them. The skill will weight those partners higher in scoring, so when multiple partners overlap on the same account, your strategic partners surface first.

Your tags need to match what's already in Crossbeam. Common examples: "Tier 1", "Tier 2", "Co-Sell", "Strategic", "ISV", "SI".

Set them when you run the skill:

> "Run partner alignment outreach, prioritize partners tagged Tier 1 and Co-Sell"

Or you can skip this and the skill will consider all partners equally.

## Defaults (all adjustable)

| Setting | Default |
|---|---|
| Lookback window | [e.g. last 4 weeks] |
| Minimum deal size | [e.g. $5,000] |
| Deal types | [e.g. new business + expansion, renewals excluded] |
| Max deals per run | [e.g. 100] |
| Emails per deal | [e.g. 1 — best-positioned partner rep only] |
| Strategic partner tags | [e.g. none — all partners weighted equally] |
| Partner scoring priority | [e.g. open opportunities first, then customers, then prospects] |
| Volume confirmation threshold | [e.g. 25 deals] |

The partner scoring priority determines which partner gets the draft when multiple partners overlap on the same account. The default weights open opportunities highest — but if your strategy is more focused on mutual customer alignment or tag-based filtering, you can adjust this. Claude will ask if you want to change it before running.

The volume confirmation threshold is a safety check — if more deals qualify than this number, Claude will pause and ask you to confirm before generating drafts. This prevents accidentally running a large batch against an unintended scope.

## How to run it

The skill detects your connected tools automatically. You have a few options for how to kick it off:

- **Run it as-is** — uses all defaults: "Run partner alignment outreach"
- **Specify a time window** — "Run partner alignment outreach for deals closed this week"
- **Filter by deal size** — "Run partner alignment outreach for deals over $20k"
- **Focus on specific partners** — "Run partner alignment outreach, prioritize partners tagged Tier 1"
- **Include renewals** — "Run partner alignment outreach, include renewals"
- **Limit the run** — "Run partner alignment outreach, just the top 5 deals"
- **Specify the deal source** — "Run partner alignment outreach, pull deals from Salesforce"

Mix and match any of these in a single request.

## What to expect

- **Recipient confirmation:** before any drafts are created, Claude will show you a list of who it plans to draft to — one line per deal. You confirm before anything is generated. If a recipient looks wrong, you can remove them from the run.
- **Volume check:** if more deals qualify than your confirmation threshold, Claude will pause and tell you the count before proceeding.
- **Deals with no overlap:** normal outcome. Not every won account has a partner in Crossbeam. These are noted in the summary.
- **Overlaps with no owner email:** also normal. Partner data quality varies — some partners don't share owner fields. The skill filters these out and explains why in the summary so you're not left wondering why a particular partner was skipped.
- **Multiple overlapping partners per deal:** the skill picks the single best-positioned rep based on partner population (open opportunity > customer > prospect), owner title, and whether the partner matches your strategic tags. One draft per deal.

## Setting it up as a recurring run

Once you've run it once and are happy with the output, ask Claude to schedule it as a weekly task (e.g., Monday mornings to catch the prior week's wins).

## A note on the data

All overlap data comes from what your partners have chosen to share with you in Crossbeam. The skill only surfaces what's already visible to you under your sharing rules — it won't surface or guess at data your partners haven't shared.

## Not sure how to set something up?

If you're unsure how to connect a tool, find your Crossbeam partner tags, or adapt the defaults for your team's workflow, just ask Claude — it can walk you through any of it.
