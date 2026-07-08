# Crossbeam Skills for Claude, ChatGPT, and AI Agents

The Crossbeam team has created ready-made Skills for partnership and go-to-market teams. Each skill brings partner overlap, co-sell context, and ecosystem signals from [Crossbeam](https://www.crossbeam.com/) into your revenue team's AI workflows.

Every skill is a set of agent instructions and resources packaged in a plain Markdown file (`.md`) so you can **read it directly here on
GitHub** before you ever load it into Claude, ChatGPT, or your AI tool of choice. Each skill lives in its own folder
under [`skills/`](skills/) with a `SKILL.md` (the skill itself) plus any
supporting `references/` and `README.md` files.

**MCP connections provide data to your agents; Skills provide the judgment and the Ecosystem-Led Growth best practices.**
The [Crossbeam](https://www.crossbeam.com/) MCP returns partner overlaps, co-sell context, and ecosystem signals. These skills encode an expert workflow on top of it: which partner to work and why, the right play, the next best action to take. 

**Note: Skills can be used across different AI tools, not just Claude or ChatGPT. The format is an open standard, so the skills you see here can also work with other AI platforms that support skills or building agents using natural language. If you’re using a different AI tool, check their docs for instructions on how to set up and use skills there.**

## Available Skills

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

Each skill lives in its own folder under [`skills/`](skills/) as Markdown, so you can open and read any `SKILL.md` directly on GitHub. To use one in Claude (Claude Desktop, Claude Code, or the Claude API), ChatGPT, or other AI agents:

1. Download the full skill folder — not just the `SKILL.md` file. Some skills depend on files in the `references/` subfolder to work correctly. You can download a ready-to-use `.zip` for each skill from [crossbeam.com/claudeskills](https://www.crossbeam.com/claudeskills), or download the full folder from GitHub.
2. Review and configure the skill to your needs. (Tip: Ask your AI tool for help with configuration.)
3. Upload the skill following the instructions in your tools support docs
   -  [Claude's support docs](https://support.claude.ai/en/articles/10065836-using-skills-in-claude).
   -  [ChatGPT's support docs](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).
4. The skill will be available in any new conversation.

https://github.com/user-attachments/assets/2837be4f-d9b8-4bec-b682-f40a2464ad48

For details on connecting Crossbeam to Claude, review our [help documentation here](https://help.crossbeam.com).

## Feedback

Have feedback or a use case we haven't built yet? Share it with our team [here](https://docs.google.com/forms/d/e/1FAIpQLScPr15cLPv3HZniTbid7QBXraCLPBAP8rJGB-fxDEzMWw_Wjg/formResponse)
