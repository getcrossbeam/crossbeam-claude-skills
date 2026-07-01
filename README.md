# Crossbeam Claude Skills

Ready-made [Claude](https://www.claude.com/) Skills for partnership and
go-to-market teams. Each skill brings partner overlap, co-sell context, and
ecosystem signals from [Crossbeam](https://www.crossbeam.com/) into your
revenue team's AI workflows.

Every skill is plain Markdown (`.md`) so you can **read it directly here on
GitHub** before you ever load it into Claude. Each skill lives in its own folder
under [`skills/`](skills/) with a `SKILL.md` (the skill itself) plus any
supporting `references/` and `README.md` files.

**The MCP gives the data; the skill gives the judgment and the ELG method.**
The [Crossbeam](https://www.crossbeam.com/) MCP returns partner overlaps,
co-sell context, and ecosystem signals — but the raw data still leaves the hard
calls to you. These skills encode the expert workflow on top of it: which
partner to work and why, the right play, the safe next step. The same expert
workflow for every rep, every run.

## What are Skills?

A Claude Skill is a saved, reusable package of instructions Claude fires
automatically when it recognizes the task. A prompt is a one-time instruction —
next time you want to complete that same task, you start over.

A skill is the next step. You identify a recurring task or workflow, create a
skill for it, and load it into Claude once. From there, Claude reads what you're
asking, decides which skill applies, and executes. You describe the task in
plain language and the saved playbook (the skill) fires.

## Skills

### Co-sell & prospecting

| Skill | What it does |
|---|---|
| [Co-Sell Copilot](skills/crossbeam-co-sell-copilot/SKILL.md) | Name an account or a stuck deal; it finds the best-positioned partner, picks the play (intro / intel / reference / voucher / co-sell), and drafts the rep-to-rep ask — with something to give back. |
| [Ecosystem Prospecting (EQL Finder)](skills/crossbeam-ecosystem-prospecting/SKILL.md) | Turns the ecosystem into a ranked prospect list: who to work, why (which partner, customer vs deal), the angle, and the warm path in. |

### Account intelligence & prioritization

| Skill | What it does |
|---|---|
| [Ecosystem-Informed Account Brief](skills/ecosystem-informed-account-brief/SKILL.md) | Produces a structured account brief enriched with Crossbeam ecosystem intelligence — partner overlap, ecosystem relationships, and recent partner activity signals. |
| [Ecosystem-Powered Pipeline Prioritization](skills/ecosystem-powered-pipeline-prioritization/SKILL.md) | Scans a list of accounts for partner signals — deal activity, overlap populations, recent partner movement — then ranks them and surfaces the ones worth acting on. |

### Outreach

| Skill | What it does |
|---|---|
| [Ecosystem-Informed Outreach Writer](skills/ecosystem-informed-outreach-writer/SKILL.md) | Drafts rep-quality outbound emails and 1, 3, or 7-touch sequences for any sales, partnerships, or GTM motion — with a hard de-AI pass on every draft. |
| [Partner Alignment Outreach](skills/partner-alignment-outreach/SKILL.md) | Turns recent closed-won deals into partner-alignment outreach — finds which partners overlap each won account and drafts a short alignment email to each partner rep. |
| [LinkedIn Partner Contact Search](skills/linkedin-partner-contact-search/SKILL.md) | Finds the right people on LinkedIn through an ELG lens — net-new prospects or partner-side contacts to recruit, co-sell, or account-map with. |

### Strategy & enablement

| Skill | What it does |
|---|---|
| [ELG Advisor](skills/elg-advisor/SKILL.md) | Gives actionable ecosystem-led growth (ELG) and partner strategy recommendations, built on frameworks developed at Crossbeam. No account required. |
| [Partner Pitch Builder](skills/partner-pitch-builder/SKILL.md) | Extracts and organizes your "why partner with us" value into a structured inventory, mapped to partner types, partner-side personas, and recruitment channels. |

### Developer & integration

| Skill | What it does |
|---|---|
| [Crossbeam API Guide](skills/crossbeam-api-guide/SKILL.md) | Routes any "how do I get Crossbeam data into X" question to the right access method — REST API, Webhooks/Signals, the MCP server, or in-app AI Chat — with the exact docs, scopes, and endpoints. |

## Using a skill

Each skill lives in its own folder under [`skills/`](skills/) as Markdown, so
you can open and read any `SKILL.md` directly on GitHub. To use one in Claude
(Claude Desktop, Claude Code, or the Claude API):

1. Download the skill's **whole folder** from [`skills/`](skills/) — not just
   `SKILL.md`. Several skills rely on their `references/` files to work
   correctly, so keep the folder intact. GitHub has no per-folder download
   button, so use one of these approaches (replace the example skill name with
   the one you want):

   - **`degit`** (fastest, no git history):
     ```bash
     npx degit getcrossbeam/crossbeam-claude-skills/skills/ecosystem-powered-pipeline-prioritization my-folder
     ```
   - **Folder-to-ZIP trick** — paste the folder's GitHub URL into
     [download-directory.github.io](https://download-directory.github.io) and it
     zips just that folder, e.g.:
     ```
     https://download-directory.github.io/?url=https://github.com/getcrossbeam/crossbeam-claude-skills/tree/main/skills/ecosystem-powered-pipeline-prioritization
     ```
   - **Sparse checkout** — a real git clone, useful if you'll pull updates later:
     ```bash
     git clone --filter=blob:none --sparse https://github.com/getcrossbeam/crossbeam-claude-skills
     cd crossbeam-claude-skills
     git sparse-checkout set skills/ecosystem-powered-pipeline-prioritization
     ```
   - Or just download the full repo as a ZIP (green **Code** button →
     **Download ZIP**) and pull out the folder you want.
2. Review and configure the skill to your needs (tip: ask Claude for support
   here).
3. Package the skill folder as a ZIP file (keep `SKILL.md` and any
   `references/` files inside it), then upload it to Claude via
   **Customize → Skills → + → Create skill → Upload a skill**. See Claude's
   support docs for details
   ([Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)).
4. The skill will be available in any new conversation.

For details on connecting Crossbeam to Claude, review our
[help documentation](https://help.crossbeam.com/en/articles/12601327-crossbeam-mcp-server-limited-availability).

## Feedback

Have a use case we haven't built yet, or feedback on an existing skill? Let the
Crossbeam team know using
[this form](https://docs.google.com/forms/d/e/1FAIpQLScPr15cLPv3HZniTbid7QBXraCLPBAP8rJGB-fxDEzMWw_Wjg/viewform).
