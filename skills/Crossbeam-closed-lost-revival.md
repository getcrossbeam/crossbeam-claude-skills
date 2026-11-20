---
name: crossbeam-closed-lost-revival
description: >
  Find closed-lost deals that are worth re-engaging because a partner relationship on the account
  just changed — the account moved into a partner's open-opportunity or customer segment, or a new
  decision-maker surfaced on the partner side. Flags the account, pulls the partner contact and deal
  context, and drafts the ask: should the rep re-engage, with the partner's help or without it. Built
  on Crossbeam's "fast follow" play and the pattern Tabs used to turn lost deals back into
  partner-sourced pipeline. Read-only and draft-only: it hands off to the rep's own CRM, chat, or
  partner workspace and never sends. Use whenever someone wants to revive lost pipeline, scan
  closed-lost deals for partner signals, or asks "which of our lost deals are worth another look",
  "did any lost deal move into a buying cycle with a partner", "can a partner get us back into this
  account". The user does not need to mention partners or Crossbeam by name.
---

<readme>

# Closed-Lost Revival (powered by Crossbeam)

Find the lost deals worth a second look, because something changed on the partner side — then draft the ask to re-engage.

## What it does

1. Takes your closed-lost accounts — a saved Crossbeam list, a pasted list, or named accounts — and checks each one against your partner ecosystem
2. Flags any account where a partner's relationship to it just changed: the partner now has it as an open opportunity or a customer, or a new decision-maker showed up on the partner's side
3. Pulls the partner contact worth reaching (prioritizing economic buyers and decision-makers) and the partner's deal detail where they share it
4. Scores how strong the signal is, and drops anything too thin to act on
5. Drafts the ask: loop in the partner with real context on why this account matters, or — when there is no partner angle — a direct re-approach built on whatever public signal is available
6. Reports what was flagged, what was skipped, and why

Read-only and draft-only. Nothing is sent; you review every draft and the actual outreach happens in your own tools.

## Why this works

Deals usually go cold for timing, not product fit — a prospect locked into a contract elsewhere, asked you to check back later, and then nobody did, because nobody was watching for the moment the timing changed. Crossbeam's ecosystem data is the thing that watches: a partner opening an opportunity on a company you already lost, or picking up a decision-maker you never got to, is a concrete, timed reason to come back — not a cold re-touch. This is the same mechanic behind Crossbeam's "fast follow" play (catch a shared prospect right as it becomes a partner's customer and ask for an assist), applied to your closed-lost pipeline instead of your active one. One Crossbeam customer, Tabs, built this exact workflow with Claude and the Crossbeam MCP and reported partner conversations going from one or two a week to a dozen or more, and problem-sourced deals increasing four to five times — their numbers, not a guarantee of yours.

## What you need

**Required**
- **Crossbeam connector** — the source of partner overlap, contacts, and activity. Connect from the Claude connector directory or at crossbeam.com. Authenticate to the right org before running. The skill will not run without it.

**For the closed-lost accounts — any one of these works**
- A saved Crossbeam list of your closed-lost accounts, if you keep one
- A pasted list of account names or domains
- Named accounts in your request ("check if Acme is worth another look")

This skill does not query your CRM directly. If your closed-lost deals live in a CRM, export or paste the list, or save a Crossbeam list from it ahead of time.

**Optional but recommended**
- A partner-manager mapping (which of your team owns each partner relationship) — lets the draft route to the right internal person instead of just naming the partner
- Deal history or notes on why the account was lost — a stronger ask always says why the deal matters to the partner, not just "can you introduce us." Paste what you have; this skill does not pull call or email history itself
- Strategic partner tags, if you want to focus on specific partners first

## Before your first run: what to configure

### 1. Closed-lost source
Where your closed-lost accounts come from — a saved Crossbeam list name, or "user will paste."

> **Fill in before sharing:** `Closed-lost source: [e.g. "Crossbeam list: Closed Lost Q3" or "user will paste"]`

### 2. Revival trigger (optional, sharpens the scan)
Which partner-side change counts as worth a look. Default: the partner now has the account as an open opportunity or a customer. Narrow it if you only care about one of those.

> **Fill in before sharing:** `Revival trigger: [open opportunities / customers / both — default both]`

### 3. Partner-manager mapping (optional)
Who on your team owns each partner relationship, if you want the draft to name them instead of just the partner.

> **Fill in before sharing:** `Partner-manager mapping: [e.g. "Acme Corp -> Jamie Lee", or leave blank]`

### 4. Strategic partner tags (optional)
Partners to weight up so their signals surface first.

> **Fill in before sharing:** `Strategic partner tags: [e.g. Tier 1, Co-Sell — or leave blank for all partners]`

## Defaults (all adjustable)

| Setting | Default |
|---|---|
| Revival trigger | Partner has the account as an open opportunity or customer |
| Signal-strength floor | Medium — accounts where the signal is Weak are reported but not drafted |
| Max accounts per run | 100 |
| Lookback for "just changed" framing | 30 days |
| Sending | Never. Drafts only. |

## How to run it

- **Full scan:** "Scan our closed-lost deals for partner signals" / "Which lost deals are worth another look?"
- **One account:** "Did Acme ever move into a buying cycle with a partner?"
- **Pasted list:** "Run closed-lost revival on these accounts: [paste]"
- **Saved list:** "Run this against our Closed Lost Q3 list in Crossbeam"

## What to expect

- **Most lost deals won't flag.** That's normal — the point is to surface the few where something concrete changed, not to re-litigate every loss.
- **One artifact per flagged account:** what changed, the partner, the contact worth reaching, and a draftable ask.
- **No partner angle found:** still reported, with a direct re-approach option built from whatever public signal is available, instead of silence.
- **Drafts only**, never sent.

## Setting it up as a recurring run

This is built to run daily or weekly, the way Tabs runs it — a short digest of what changed, not a one-time sweep. Ask Claude to schedule it after a clean manual run.

## A note on the data

All partner data comes from what your partners have shared with you in Crossbeam under your sharing rules. The skill only surfaces what is already visible to you, and never guesses at a partner's deal stage, contact, or activity it cannot see.

</readme>

<instructions>

> **Structural tags.** `<readme>` and `<instructions>` delimit sections of this file for the agent
> reading it. They are not content: never echo a tag in your output.

## Grounding

This skill operationalizes two things Crossbeam has already published, and should not improvise
past either of them:

1. **"Fast follow"** (Crossbeam ELG play): the moment a shared prospect becomes a partner's
   customer is a high-leverage, time-boxed moment to ask that partner for an assist — not a generic
   "let's catch up" outreach. The ask needs real context (why this deal matters, what stage it was
   at, the ICP fit), not just a request for an introduction.
2. **The Tabs pattern** (customer case study): apply the same logic to a *closed-lost* population
   instead of an active one. The trigger is a lost account moving past the first sales stage with a
   partner — becoming their open opportunity or customer — or a new economic buyer surfacing on the
   partner side. The workflow runs on a recurring cadence (Tabs ran it daily), flags the account,
   and asks a simple yes/no: should the rep re-engage. A partner manager only takes it from there if
   the rep says yes.

Do not invent plays, proof points, or mechanics beyond these two sources. Where this skill extends
the published pattern (e.g. a direct-outreach fallback when no partner can help), say so rather than
presenting it as a documented Crossbeam play.

## Configuration
> Set once by whoever deploys this skill. Claude reads these at runtime — do not change them mid-conversation.

**Closed-lost source:** [fill in — a saved Crossbeam list name, or "user will paste"]
**Revival trigger:** [fill in — open_opportunities / customers / both. Default: both]
**Partner-manager mapping (optional):** [fill in — partner name -> internal owner, or blank]
**Strategic partner tags (optional):** [fill in — e.g. Tier 1, Co-Sell. Leave blank for all partners.]

## Defaults

Apply unless the user overrides.

| Setting | Default |
|---|---|
| Revival trigger | open_opportunities and customers (both) |
| Signal-strength floor | Medium (Weak accounts reported, not drafted) |
| Max accounts per run | 100 |
| Lookback for "just changed" framing | 30 days |
| Sending | Never. Drafts only. |

**Volume guardrail:** if the closed-lost source exceeds 100 accounts, stop and tell the user how many were found, and ask whether to proceed, narrow, or sample.

**Scoping guardrail (two checkpoints):**
1. **Before the first scan (Step 2a).** State what's about to be checked, in plain terms — how many accounts, from Step 1, and which partner populations or tags it's being checked against. Let the user narrow before anything runs. This is always knowable up front, since it's just reflecting back the request.
2. **Before pulling full detail on every match (Step 2b/2c).** Once the first scan comes back, this skill pulls contact and deal detail on every account that matched — so a 100-account match means detailed lookups on all 100. If that's a lot of accounts (over 50, even if under the Step 1 cap) or this is a recurring run that hasn't been sized before, flag it plainly, the way you'd flag a big data pull before running it: "this matched a lot of accounts, want full detail on all of them, a count first, or a narrower slice?" Don't just run it silently because the first scan came back small. This is the checkpoint that actually matters, since how much there is to dig into isn't known until after the first scan returns.

## Step 0 — Inventory available tools

1. **Crossbeam MCP (required).** The verified tools on the current surface: `get_list_context` (a saved list), `get_account_context` (resolve one or more named accounts), `find_overlapping_accounts_and_leads` (bulk scan: which of our accounts overlap a partner's open-opportunity or customer segment), `get_ecosystem_activity` (recent partner events — deal opened, deal closed won, greenfield — for the "just changed" framing), `find_partner_recommendations` (EI signals on a specific account: recent wins, new contacts, long-term relationship, missing contacts), `find_partner_shared_contacts` (the partner's contacts at the account, ranked by role), `get_partner_opportunity_context` (the partner's deal detail on the account — stage, amount, dates, owner — where they share it), `search_crossbeam_knowledge` (Crossbeam's own ELG/product content, if the user asks what "fast follow" means or wants the source cited). Confirm what's present on the first call; tool names can vary by install. If no Crossbeam MCP is connected, stop and tell the user to connect and authenticate.
2. **A closed-lost source (required, flexible).** A saved Crossbeam list (via `get_list_context`), a pasted list, or named accounts. This skill does not query a CRM directly.
3. **A partner-manager mapping (optional).** Only if configured.
4. **Deal history or context (optional).** Only if the user pastes it. This skill does not pull call or email history itself.

Detect, do not interrogate. Only ask if there is genuinely no way to get the closed-lost accounts.

## Step 1 — Resolve the closed-lost accounts

- **A saved list is configured or named:** call `get_list_context(list_name: ...)`. If it returns `ClarificationRequired`, present the candidates and retry with the confirmed `list_id`. If it returns `RetryLater`, follow the retry cadence the tool gives you.
- **A pasted list or named accounts:** for each, call `get_account_context(account_name/account_domain/account_id)` to resolve it in Crossbeam. Present `ClarificationRequired` candidates to the user rather than guessing.
- **Neither:** ask the user to name, paste, or point to a saved list. Do not guess.

Capture account name, domain, and `account_id` for each. If the set exceeds the volume threshold, stop and confirm before continuing.

## Step 2 — Scan for the revival trigger

**Before pulling full detail:** apply the scoping guardrail above. If a lot of accounts matched, or this cadence hasn't been run before at this size, flag it plainly and confirm before pulling detail on all of them.

**2a — Bulk pass.** Call `find_overlapping_accounts_and_leads` with `our_populations` or the resolved account set, and `partners.segments` set to the configured revival trigger (default `["open_opportunities", "customers"]`). This returns which of the closed-lost accounts now overlap a partner in one of those segments — the core trigger: a partner has picked this account up since you lost it. If strategic partner tags are configured, also pass `partners.tag_name` and prefer those matches.

**2b — Recency pass.** For the accounts that cleared 2a (or for a scheduled/recurring run, for the whole closed-lost set), call `get_ecosystem_activity(record_ids: [...], event_types: ["partner_deal_opened", "partner_deal_closed_won"])` scoped to the configured lookback window (default 30 days). This is what makes the digest "what changed recently" rather than a static report, and gives you `triggered_at` for the "date it moved forward" field.

**2c — Signal pass.** For each flagged account, call `find_partner_recommendations(deal_or_account_name)` to get the EI signals per partner: `recent_wins`, `new_contacts`, `long_term_relationship`, `missing_contacts`. `new_contacts` or `missing_contacts` on a closed-lost account is the "a new decision-maker surfaced" signal from the Tabs pattern — treat it as a trigger on its own even without a 2a/2b hit, since a new contact can predate a population change in Crossbeam's data.

An account flags for Step 3 if it cleared 2a, has a 2b event inside the lookback window, or has an active `new_contacts` / `missing_contacts` / `recent_wins` signal in 2c. Everything else is a non-event: report it as scanned, not flagged, not a failure.

## Step 3 — Qualify the signal and pull the contact

For each flagged account:

**3a — Score the signal.** Strong: a 2b event inside the lookback window, or `recent_wins` / `long_term_relationship` active. Medium: cleared 2a (partner has it as an open opp or customer) without a fresh event or strong EI signal. Weak: only a `new_contacts` or `missing_contacts` signal with no population-level confirmation. Accounts below the configured floor (default Medium) are reported, not drafted.

**3b — Pull the contact worth reaching.** Call `find_partner_shared_contacts(account_id, partner_name)`. Prioritize contacts the tool ranks for priority roles — economic buyer, decision-maker, executive sponsor — over any contact you already worked with when you lost the deal the first time. A new priority-role contact is the single strongest reason this is worth another look, not just a process reminder.

**3c — Pull the partner's deal detail, if they share it.** Call `get_partner_opportunity_context(account_id, partner_name)`. Capture stage, amount, dates, and the partner-side owner where present. An empty result means the partner hasn't shared this, or doesn't have an open deal there — not that nothing is happening; say so rather than treating it as a dead end.

## Step 4 — Classify the play

- **Partner assist** — the default when a partner is positioned (3a Medium or Strong): loop in the partner, with the real context from Step 3, and ask for an assist, intel, or an introduction to the new contact. This is the "fast follow" ask applied to a lost deal.
- **Direct re-approach** — the account flagged but no partner is well-positioned (3a Weak, or no contact worth reaching in 3b): skip the partner ask and go straight to re-engaging the account directly, using whatever context Step 5 can add.
- **No action** — below the floor and no usable contact or public signal either. Report it; do not manufacture an ask.

## Step 5 — Build the ask

**5a — Partner assist draft.** The recipient is the partner manager (from Configuration, if mapped) or a note to loop in whoever owns that partner relationship — never the partner's customer contact directly, and never the prospect. State: the account, why it was lost, what changed (the Step 2/3 signal, with date), and the specific ask — an introduction to the surfaced contact, intel on where the account's buying cycle stands, or an assist getting back in. If the user pasted deal history or notes on why it was lost, use them; a plain "can you introduce us" is not enough on its own — the ask needs to say why this account matters, per the grounding above. If nothing was pasted, say plainly that the draft is missing that context and ask the user to add it before sending.

**5b — Direct re-approach draft.** Use web search for a current, specific public signal on the account (funding, leadership change, a relevant hire) to ground the re-approach — a generic "checking back in" email is the failure mode this is meant to avoid. If search turns up nothing specific, say so; do not invent a signal.

**Voice:** plain, specific, no em dashes, no partnership jargon ("synergy," "leverage," "unlock"). Reference only facts Crossbeam's data, the user's pasted context, or a just-verified search result actually show.

## Step 6 — De-AI pass (hard gate before delivery)

Re-read every draft. No draft is delivered until it passes:
1. **Zero em dashes.**
2. **No machine-written filler** — cut "I hope this finds you well," "just reaching out," "touching base," "circle back," "excited to," "thrilled to," generic compliments.
3. **No invented context.** If a claim in the draft isn't traceable to a Step 2/3 signal, pasted context, or a cited search result, cut it.

## Step 7 — Confirm, then deliver

Before producing full drafts, show one summary line per flagged account: `[Account] -> [Partner or "direct"] / Signal: [Strong/Medium/Weak] / Changed: [what, date] / Play: [partner assist / direct re-approach]`. Let the user drop any line. Only draft after confirmation.

Deliver copy-ready text: one block per account, with recipient, subject, and body, for the user to send through their own tools. This skill does not create drafts in an email tool or post to chat tools itself.

## Step 8 — Report

- Accounts scanned / flagged / drafted / below floor / no action, with the reason for each skip.
- One line per draft: `[Account] -> [Partner or "direct"] · Play: [type] · Signal: [what changed, date]`.
- Any tool errors or partners that didn't share enough to qualify ("not shared by the partner," never "no overlap").

## Setting up a recurring run

If the user wants the Tabs-style daily or weekly cadence, offer to schedule it once a manual run looks right. Each scheduled run repeats Steps 1–8 against the same closed-lost source and reports only what's new since the last run (use the lookback window in Step 2b to bound this).

## Guardrails

- Read-only and draft-only. The Crossbeam MCP exposes `find_*` / `get_*` tools only. Never send, never post to chat or email on the user's behalf.
- Only surface partner data Crossbeam's sharing rules already expose to this user. Absence of data is not absence of overlap — say "not shared by the partner," never "no overlap."
- A partner having an open opportunity or a new contact at an account is a signal, not proof the deal is winnable again. Say what changed; do not promise an outcome.
- Every partner ask must carry real context on why the deal matters to the partner, per the grounding above. A bare "can you introduce us" is the failure mode this skill exists to avoid.
- Never draft a partner ask to the partner's customer contact or to the prospect. The recipient is always the partner manager or whoever owns that relationship.
- Never invent a public signal for the direct re-approach play. If search finds nothing, say so.
- Accounts below the signal-strength floor are reported, not drafted.
- Deal amounts, contact details, and partner data are sensitive — keep them out of any output not going to the user.
- Apply the scoping guardrail at both checkpoints: reflect the request back before the first scan runs, and flag it plainly before pulling full detail on a large set of matches. If asked what this will cost, say that an exact figure isn't something this skill can calculate, and point to Crossbeam support or the account's Account Manager.
- On a recurring/scheduled run, this fan-out repeats every cycle. If the account or partner relationship the user is tracking stops making sense to run at full scope, the fix is narrowing it (strategic partner tags, a smaller closed-lost source, a longer lookback checked less often) — raise that as an option rather than letting a run grow without anyone noticing.

</instructions>
