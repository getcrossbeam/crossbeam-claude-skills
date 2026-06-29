# Crossbeam MCP Server & In-App AI Chat

These are the **AI-native** ways into Crossbeam data. Reach for them when the user
wants to *ask questions and act* rather than write integration code.

- **In-app AI Chat** — a natural-language assistant **inside the Crossbeam app**.
  Zero setup, no code, no connector. Best when the user just wants answers while
  working in Crossbeam.
- **MCP Server** — a remote Model Context Protocol server that gives **external AI
  tools and agents** (Claude, ChatGPT, or homegrown agents) secure, structured,
  permission-governed access to ecosystem data. Best when the user wants partner
  context and actions inside the AI tool they already use.

Privacy stance (accurate for both): **Crossbeam does not train LLMs on customer
data.** Data passes through models for real-time processing only — not long-term
storage or training.

Docs:
- MCP: https://help.crossbeam.com/en/articles/12601327-crossbeam-mcp-server-limited-availability
- Claude connector listing: https://claude.com/connectors/crossbeam
- Crossbeam AI product page: https://www.crossbeam.com/what-is-crossbeam/crossbeam-ai
- Academy course: https://academy.crossbeam.com/

---

## In-app AI Chat

Crossbeam **AI Chat** is the in-app assistant for partner data — ask questions in
plain language and get answers, prioritization, and next-best actions without
leaving Crossbeam. It has a dedicated navigation entry in the app (alongside
Search and Pipeline Generation). Recommend this first to non-technical users who
"just want to ask Crossbeam something." No API keys, OAuth, or connector setup.

---

## MCP Server

> Access note: the Crossbeam MCP Server is in **Limited Availability** for
> **Supernode and Enterprise** customers, with access approved by company domain.
> SAML SSO is not yet supported as an auth option, and functionality is evolving.
> To request access: the user's Crossbeam contact or **product@crossbeam.com**.

### What it's good for

- Bring partner context into internal copilots / CRM assistants (partners to
  leverage, next steps, account highlights).
- Layer ecosystem data onto existing account prioritization.
- Trigger actions on ecosystem signals (e.g. surface partners to engage when a
  deal hits a stage).

### Supported tools

The MCP server exposes these tools; their power comes from **combining** them
(e.g. find top partners, then check who's engaged on a specific account):

| Tool | Returns |
| --- | --- |
| `find_partners` | All your Crossbeam partners — assess coverage and impact |
| `get_partner_tags` | Partner tags your org created, for filtering/segmentation |
| `get_partner_suggestions` | Suggested / potential new partners |
| `get_partner_leaderboard` | Historical partner performance across recently closed deals |
| `get_own_populations` | Your org's defined Populations |
| `get_partner_populations` | Partner Populations visible to you |
| `get_account_overlap_info` | Partner overlaps for a specific account by ID |
| `get_own_account_info` | Search your accounts by domain, CRM record ID, or name (fuzzy) |
| `get_record_signals` | Signal events for accounts/leads (e.g. partner deal opened / closed won), newest first |
| `search_help_center` | Product info from the Crossbeam Help Center |
| `search_blog_site` | Context/tactics/stories from Crossbeam Insider |
| `search_elg_book` | Use cases from the Ecosystem-Led Growth book |

### Example prompts

- "Which of our partners have the highest win rate right now?"
- "Which partner can help me move this deal forward?"
- "Which partners also have this account in their pipeline?"
- "What's the average deal size and win rate when I work with [Partner X]?"
- "Suggest new partners we should invite based on our ecosystem data."
- "Who are our most active partners in the past quarter?"

### Connecting to Claude

Crossbeam has a **native connector in the Claude.ai marketplace**; you authenticate
with your Crossbeam login. Requires a Claude plan that allows remote MCP
connectors.

- **Team/Enterprise admins (Workspace/Primary Owners):** Organization Settings →
  Connectors → **+** → search **Crossbeam** → add. It then appears for members
  under Customize → Connectors.
- **Individual users:** Customize → Connectors → **+** → search **Crossbeam** →
  **Connect** → sign in with Crossbeam credentials → review/accept permissions.
- Toggle individual tools under Customize → Connectors → Crossbeam, or per-chat via
  the Search-and-tools menu. Claude only accesses data you're permitted to see.
- Once connected on Claude web, the same connector works on Claude for iOS/Android.

### Connecting to ChatGPT

Crossbeam has a **native connector in the ChatGPT Apps directory**; authenticate
with your Crossbeam login.

- Any **paid** ChatGPT user can connect it from the Apps Directory (not available
  on Free).
- Enterprise/Education workspaces have connectors **disabled by default** — an
  admin must enable them first. ChatGPT Apps are in beta and availability varies by
  region (may not be in UK/EU yet).
- Settings → Apps → Explore apps → find **Crossbeam**. In a chat, invoke it with
  `@Crossbeam` or the **+** menu → More → Crossbeam.

### Connecting other AI tools / custom agents

The MCP server is a standard remote MCP endpoint, so any MCP-capable client or
homegrown agent can connect. Request the server URL and access credentials from
your Crossbeam contact or **product@crossbeam.com**, then follow your client's
remote-MCP connection steps.

### Troubleshooting

During Limited Availability, transient auth issues can occur — **retry first**. If
it still fails, confirm your domain has been approved for access (contact your
Crossbeam rep or **product@crossbeam.com**).
