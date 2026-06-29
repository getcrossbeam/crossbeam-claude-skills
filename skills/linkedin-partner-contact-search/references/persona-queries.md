# Persona query recipes

Ready-made title sets and query patterns for the personas ecosystem-led GTM
teams search most. Partnerships/alliances/ecosystem leads first — they're the
core ELG persona you recruit, co-sell, and account-map with. Titles are
inconsistent across companies, so each persona lists the real-world variants to
expand into. Run one query per cluster and merge the results.

Reminder on mechanics:
- Always prefix with `site:linkedin.com/in`.
- Wrap multi-word titles in quotes so they match as phrases.
- Pass `blocked_domains` to suppress job boards: `builtin.com`, `themuse.com`,
  `indeed.com`, `glassdoor.com`, `ziprecruiter.com`, `web3.career`,
  `wikipedia.org`, `greenhouse.io`, `jobs.lever.co`.
- Keep only URLs containing `linkedin.com/in/`.

---

## Partnerships / Alliances / Ecosystem

The core persona for partner-side outreach and co-sell.

Title variants:
- `"VP Partnerships"`, `"VP of Partnerships"`
- `"Head of Partnerships"`
- `"Director of Partnerships"`, `"Director, Strategic Partnerships"`
- `"Strategic Alliances"`, `"VP Alliances"`, `"Head of Alliances"`
- `"Partnerships Lead"`, `"Partner Manager"`, `"Partnership Manager"`
- `"Ecosystem"` (e.g. `"Head of Ecosystem"`, `"VP Ecosystem"`)
- `"Channel"` (e.g. `"Channel Partnerships"`, `"VP Channel"`)
- `"Business Development"` (broad; filter hard — overlaps with sales)

PARTNER mode (named company):
```
site:linkedin.com/in "Head of Partnerships" "Acme Corp"
site:linkedin.com/in "VP Partnerships" "Acme Corp"
site:linkedin.com/in "Strategic Alliances" "Acme Corp"
```

PROSPECT mode (ICP):
```
site:linkedin.com/in "Head of Partnerships" SaaS "United States"
site:linkedin.com/in "VP Alliances" fintech
```

---

## RevOps / Revenue Operations

Title variants:
- `"Revenue Operations"`, `"RevOps"`
- `"VP Revenue Operations"`, `"Head of Revenue Operations"`
- `"Director of Revenue Operations"`, `"Director, RevOps"`
- `"Sales Operations"`, `"VP Sales Operations"`
- `"GTM Operations"`, `"Go-to-Market Operations"`

```
site:linkedin.com/in "Revenue Operations" "Acme Corp"
site:linkedin.com/in "Director of Revenue Operations" SaaS "New York"
```

---

## Sales leadership

Title variants:
- `"VP Sales"`, `"VP of Sales"`, `"SVP Sales"`
- `"Chief Revenue Officer"`, `"CRO"`
- `"Head of Sales"`, `"Director of Sales"`
- `"Regional Sales Director"`, `"Sales Director"`

```
site:linkedin.com/in "Chief Revenue Officer" "Acme Corp"
site:linkedin.com/in "VP Sales" "Series B" SaaS
```

---

## Founders / executives

Title variants:
- `"Founder"`, `"Co-Founder"`, `"CEO"`
- `"Chief Executive Officer"`
- `"President"`, `"COO"`, `"Chief Operating Officer"`

```
site:linkedin.com/in "Co-Founder" "Acme Corp"
site:linkedin.com/in "CEO" "vertical SaaS" "Austin"
```

---

## Tips for sharpening results

- **Too few results**: drop the geography term, broaden the title (e.g. add
  `"Business Development"`), or try the bare company name without a title to see
  who surfaces.
- **Too much noise**: add a second distinguishing keyword (industry, product,
  city), tighten to the exact title phrase, or add more job-board domains to
  `blocked_domains`.
- **Same-name company decoys** (PARTNER mode): confirm the company string
  appears in the snippet; a profile that only matches the title isn't a hit.
- **International targets**: results surface under country subdomains
  (`uk.linkedin.com/in`, `ca.linkedin.com/in`, `de.linkedin.com/in`). These are
  valid — don't filter them out.
