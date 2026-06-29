# Crossbeam REST API

Use the REST API when **your own code** needs to pull Crossbeam data on demand
into another system (CRM, data warehouse, internal app, dashboard, script), or to
write activity back onto Crossbeam's timeline.

Canonical docs (authoritative, versioned): **https://developers.crossbeam.com/**
Per-endpoint pages list the exact path, parameters, response schema, code samples
in 20+ languages, and the **required scope**. Treat that site as the source of
truth over anything reconstructed from memory.

> Access note: the REST API is positioned for **Enterprise** customers. Confirm
> the user's plan/access before promising it.

---

## 1. Create an application (get credentials)

In the Crossbeam app, go to **https://app.crossbeam.com/integrations** → the
**Custom** section → **Create Integration**:

- **Integration name** — anything identifying your app
- **Integration description** — optional
- **Callback URL** — your OAuth redirect (for Postman testing use
  `https://oauth.pstmn.io/v1/callback`)
- **Allowed Origins** — leave blank unless you need CORS

After creating, click **View** and copy the **Client ID** and **Client Secret**.
(UI walk-through: https://help.crossbeam.com/en/articles/4677142-rest-api)

---

## 2. Authenticate (OAuth 2.0)

The API uses standard OAuth 2.0. Follow your stack's normal OAuth library flow
with these URLs:

- **Authorization URL:** `https://auth.crossbeam.com/authorize?audience=https://api.getcrossbeam.com`
- **Access Token URL:** `https://auth.crossbeam.com/oauth/token`
- **API base / audience:** `https://api.getcrossbeam.com`

A reference (non-production) client implementation lives at
https://gitlab.com/crossbeam-public/crossbeam-simple-oauth2.

### Scopes

Request `openid` at minimum, plus the scope(s) for the endpoints you need. Each
endpoint's doc page states which scope it requires.

| Scope | Grants |
| --- | --- |
| `openid` | Required baseline |
| `read:partnerships` | Read partner data (e.g. `/v1/partners`) |
| `read:reports` | Read report data |
| `read:populations` | Read your populations |
| `write:activity-timeline` | Write activity onto the timeline |
| `offline_access` | Issues a **refresh token** (needed for long-running apps) |

Example scope string for a partners-only integration that stays logged in:
`openid read:partnerships offline_access`

### Token lifetime & refresh

Access tokens are valid for **24 hours**. For anything long-running, request
`offline_access` and exchange the refresh token for a new access token:

```bash
curl --request POST \
  --url 'https://auth.crossbeam.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=refresh_token \
  --data 'client_id=YOUR_CLIENT_ID' \
  --data client_secret=YOUR_CLIENT_SECRET \
  --data refresh_token=YOUR_REFRESH_TOKEN
```

---

## 3. Required headers

Most endpoints require **two** headers:

1. `Authorization: Bearer <access_token>`
2. `Xbeam-Organization: <organization-uuid>` — tells the backend which org's data
   to return. A user can belong to multiple orgs.

Get the org uuid from **`/v0.1/users/me`**, then read the `uuid` field of the
target organization:

```
Xbeam-Organization: 02fde942-c7cd-4f12-9d4e-07ee8a57c8c6
```

Omitting the org header is the most common cause of 4xx errors.

---

## 4. Endpoints by use case

The developer site is authoritative for full paths/params; these are the common
entry points. When unsure of an exact path or field, link the docs rather than
guessing.

| Use case | Endpoint (entry point) | Scope |
| --- | --- | --- |
| List the orgs the token can access / get the org uuid | `GET /v0.1/users/me` | `openid` |
| Read your partners (coverage, partner records) | `GET /v1/partners` | `read:partnerships` |
| Read your populations | populations endpoints | `read:populations` |
| Read report data (overlap/account-mapping results) | reports endpoints | `read:reports` |
| Read signal events (also pushed via webhooks) | `/v1/signals/*` | (see signals docs) |
| Write activity onto the timeline | activity-timeline endpoint | `write:activity-timeline` |

---

## 5. Rate limits

Defined in Crossbeam's security policy and **subject to change at Crossbeam's
discretion** — don't hard-code an assumed number; check current docs. Note that
API reads (and webhook deliveries) count toward **Record Export limits**, so
design for efficiency (filter server-side, avoid redundant polling).

---

## 6. Fastest way to explore: Postman

The docs offer a **"Run in Postman"** button that clones the Crossbeam collection
and environment. Use the **desktop** Postman app (not web). Set the `client_id`
and `client_secret` collection variables, pick the `scope` you need, and you can
hit live endpoints in minutes. A video walk-through is linked from the developer
docs.
