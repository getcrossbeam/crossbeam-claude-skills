---
name: linkedin-partner-contact-search
description: >-
  Find the right people on LinkedIn through an ecosystem-led-growth (ELG) lens —
  net-new prospects matching an ICP, or partner-side contacts (Partnerships,
  alliances, channel, ecosystem, RevOps) to recruit, co-sell, or account-map
  with. Works entirely on its own using public web search over linkedin.com/in
  profiles; no other skill or paid data tool required. Returns a ranked,
  deduplicated list with name, title, company, location, profile URL, and an
  ecosystem angle per person (why they matter and how a partner could warm the
  intro). Use whenever someone wants to find people, contacts, prospects, or
  leads on LinkedIn, asks "who runs partnerships at [company]", "find the
  alliances/ecosystem lead at [account]", "find me [title]s at [type of
  company]", "build a list of [persona] in [geography]", "who should I reach out
  to at [company] about co-selling", or any request to discover individuals by
  title, company, industry, or location. Self-contained: it searches, filters,
  ranks, and presents on its own.
---

# LinkedIn Search (ecosystem-led)

Find specific people on LinkedIn and rank them for an ecosystem-led-growth play.
This skill turns a loose ask ("who runs partnerships at Gong?", "find me 10
RevOps leaders at mid-market fintechs") into a clean, ranked list of real
individuals with their LinkedIn profile URLs and, for each, the *ecosystem
angle*: why they matter and how a shared partner could warm the introduction.

It is fully self-contained. It needs no other skill and no paid data provider —
just a web search tool. Everything below (search, noise-filtering, scoring,
output) happens inside this skill.

## The ecosystem-led lens

Ecosystem-led growth means using your partner network to find, win, and grow
customers — instead of cold-touching everyone. That lens changes *who* you look
for and *why* a given person matters, so apply it throughout:

- **Partner-side leaders are first-class targets, not an afterthought.** The
  people who run Partnerships, alliances, channel, and ecosystem are the ones you
  recruit, co-sell, and account-map with. Surface them deliberately.
- **For every person, ask "who could warm this intro?"** The strongest ELG path
  to a prospect is often through a partner you already share, not a cold email.
  Even without overlap data, name the *type* of partner most likely to know them
  (e.g. "a shared SI", "their CRM/data-platform partner") so the user knows where
  to look for a warm path.
- **Prefer multi-threading over a single contact.** Ecosystem motions land when
  several people inside an account are engaged. When useful, surface a primary
  contact plus a secondary to multi-thread.

This lens is a general GTM methodology — keep it vendor-neutral. Do not assume
any specific overlap tool, CRM, or product is present; if the user has one, they
can layer it on top of this list themselves.

## How this actually works (and its limits)

There is no open LinkedIn search API. What works reliably is **web search over
public LinkedIn profile pages** (`site:linkedin.com/in`). Search engines index
the public version of most profiles, and the result snippet carries the payload
that matters: name, current title, company, and often location.

What you get: name, title, company, location, profile URL — enough to build a
prioritised, ecosystem-aware outreach list.

What you do NOT get: anything behind LinkedIn's login wall. Do not try to fetch a
`linkedin.com/in/...` URL expecting the full profile — it returns a login gate,
not the page. Work from the search-result snippets. If the user needs deeper
detail (mutual connections, full history, verified email), say so plainly and
treat it as a manual follow-up; never fabricate it.

Always be honest that results come from public search indexing, may be slightly
stale, and are worth a quick eyeball before outreach.

**If no web search tool is available:** say so directly, and fall back to what
you *can* do without one — explain the exact `site:linkedin.com/in` queries the
user can run themselves, and offer to rank/clean any list of names or a company
employee export they paste in. The skill still adds value with zero tools; it
just can't do the discovery step itself.

## Two modes — detect which one the request needs

**PARTNER mode** — find the right contact(s) at a *named* company. The company is
known; the job is to surface the person who owns a function — usually
Partnerships / alliances / channel / ecosystem (the core ELG persona), but it can
be any role. Triggers: "who runs partnerships at HubSpot", "find the alliances
lead at Snowflake", "who should I talk to at Okta about co-selling". This is the
heart of ecosystem-led discovery.

**PROSPECT mode** — net-new discovery by ICP. The user describes a *type* of
person (title + company profile + geography) and wants a list of candidates.
Triggers: "find me VPs of Sales at Series B fintechs", "build a list of RevOps
directors at mid-market SaaS". Apply the ecosystem lens here too: flag which
prospects are themselves partnership personas and, for each, the partner type
most likely to open a warm door.

If the request blends both (e.g. "find partnerships leads at these 5 accounts"),
run PARTNER mode once per company.

When the request is ambiguous about title, seniority, geography, or how many
people are wanted, ask one tight clarifying question before searching — a vague
search wastes turns and returns noise.

## The search workflow

1. **Translate the ask into target attributes**: title(s), seniority,
   company(ies) or company profile, industry, geography, and target count.

2. **Build title variations.** Job titles are inconsistent, so one canonical
   title misses most matches. Expand into the real-world variants. For a
   partnerships leader: `"VP Partnerships"`, `"Head of Partnerships"`,
   `"Director of Partnerships"`, `"Strategic Alliances"`, `"Partnerships Lead"`,
   `"Head of Ecosystem"`, `"Channel"`, `"Business Development"`. See
   `references/persona-queries.md` for ready-made title sets per persona.

3. **Run several `site:linkedin.com/in` queries in parallel**, one per
   title-variant cluster, rather than a single broad one. Recall comes from
   breadth of phrasing, not one perfect query. Issue them in the same turn so
   they return together.

   - PARTNER query shape:
     `site:linkedin.com/in "<title variant>" "<Company Name>"`
   - PROSPECT query shape:
     `site:linkedin.com/in "<title variant>" <industry/keyword> "<geography>"`
   - Profiles surface under country subdomains too (`ca.linkedin.com/in`,
     `uk.linkedin.com/in`, `de.linkedin.com/in`) — these are valid, don't reject
     them for not being `www`.

4. **Filter the noise at the source.** `site:linkedin.com/in` still pulls in job
   boards and aggregators. If your search tool supports domain blocking, suppress
   the usual offenders: `builtin.com`, `themuse.com`, `web3.career`,
   `wikipedia.org`, `indeed.com`, `glassdoor.com`, `ziprecruiter.com`,
   `greenhouse.io`, `jobs.lever.co`, `startup.jobs`. Then keep only results whose
   URL actually contains `linkedin.com/in/`.

5. **Parse each kept result** into: name, title, company, location (when
   present), profile URL. The title and company usually live in the result
   title/snippet as "Name - Title at Company" or "Name - Title | Company".

6. **Deduplicate** across query variants by profile URL and by name+company.

7. **Score, add the ecosystem angle, and rank** (see below), then present.

## Scoring and the ecosystem angle

Rank candidates so the user works the best-fit people first. Score each on:

- **Title fit** — how closely the actual title matches the target role and
  seniority. An exact senior match beats an adjacent or junior one.
- **Company fit** — in PROSPECT mode, how well the company matches the ICP
  (industry, size, type). In PARTNER mode, whether it's actually the named
  company (watch for same-name decoys).
- **Geography fit** — matches the requested region, if one was given.
- **Ecosystem relevance** — is this person a partnerships/alliances/ecosystem
  persona (highest ELG value), and is there a plausible warm path to them through
  a shared partner type? Weight ecosystem-relevant contacts up.
- **Confidence** — how complete and unambiguous the snippet is.

Produce a simple High / Medium / Low fit tier (or 1-5 if the user prefers
numbers). Don't over-engineer the math — the goal is a sensible ordering.

For the top few, write a one-line **ecosystem angle**: why they matter for an
ecosystem-led play and, where you can, the *type* of partner most likely to warm
the intro. Keep it grounded — name a partner *type*, not a specific overlap you
can't verify.

## Output format

Default to a **ranked table in chat**:

```
| # | Name | Title | Company | Location | Fit | LinkedIn |
|---|------|-------|---------|----------|-----|----------|
```

After the table:
- An **ecosystem angle** line for the top few — why they're a strong ELG target
  and how a partner could open the door (multi-thread suggestions go here too).
- A short **notes** line: how many profiles were scanned, any gaps, and a
  reminder that snippets are public-index data worth a quick manual check before
  outreach.

If the user explicitly wants a spreadsheet or a CRM push, still deliver the
ranked list in chat first — that is this skill's complete output. Producing a
file or writing to a CRM is a separate step the user can take with whatever
tools they have; this skill does not depend on them.

## Quality bar

- Never invent a person, title, company, or URL. If search returns thin results,
  say so and suggest tighter or alternate queries rather than padding the list.
- Don't return the same person twice under different query variants.
- Don't include job postings, company pages, or articles — only individual
  `/in/` profiles.
- If a name appears without a confidently-readable title or company, mark it Low
  confidence rather than guessing.
- Keep the ecosystem angle honest: name partner *types* and plausible warm paths,
  never a specific overlap or relationship you haven't verified.
- Respect the user's count. If they asked for 10, don't dump 40; if you can only
  confidently find 6, return 6 and explain why.

See `references/persona-queries.md` for title sets and query recipes for the
personas ecosystem-led teams search most (Partnerships/alliances, RevOps, Sales
leadership, founders/execs).
