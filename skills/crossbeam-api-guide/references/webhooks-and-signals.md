# Crossbeam Webhooks & Signals

Use webhooks when the requirement is **"tell me the moment something happens in a
partner's data"** rather than "let me pull data when I ask." Crossbeam pushes
**Signal** events to an endpoint you control in near-real-time, so you can trigger
alerts and workflows (Slack, HubSpot, a custom internal tool, an AI agent) without
polling.

> Access note: **Webhooks are an Enterprise-only feature.** Only **Admins** can
> create them, but the workflows they trigger benefit anyone in the org.

UI setup walk-through:
https://help.crossbeam.com/en/articles/12732223-getting-started-with-signals-how-to-access-real-time-partner-data-via-api-and-webhooks
Technical reference: https://developers.crossbeam.com/ (see `/v1/signals/*` and the
Webhooks section).

---

## Two ways to consume signals

1. **Webhook (push)** — Crossbeam calls your endpoint when a signal fires. Best
   for real-time activation.
2. **Enriched-APIs / signals endpoint (pull)** — your CRM or analytics platform
   calls Crossbeam to fetch, say, all new *Opportunity Closed Won* signals from
   the past 24 hours. Best for batch syncs or recovering a missed webhook.

Both count toward **Record Export limits**.

## Signal event types

Currently surfaced signals include **partner deal opened** (*Opportunity Created*)
and **partner deal closed won** (*Opportunity Closed Won*). Expanded signals can
include contact-level detail (which partner-shared contacts are tied to the deal
and their role). Check the docs for the current, full list before claiming
coverage.

---

## Setting up a webhook (UI)

1. **Data → Integrations → Create Integration → Webhook.**
2. Provide your receiving endpoint URL. Use a **random, hard-to-guess path**.
3. **Test** the webhook — filters can't be added until a successful test.
4. Add **filters**: choose which partners/Populations to receive signals for. The
   webhook only fires on overlaps between *your* selected Populations and the
   *partner's* selected Populations.
5. **Save Settings.** Manage later under **Data → Integrations → Settings** on the
   webhook.

---

## Securing your receiver

The receiving endpoint is public, so verify every request actually came from
Crossbeam:

1. **Validate the HMAC signature.** Crossbeam gives you a secret key at setup.
   Each request carries `X-Crossbeam-Signature-256` (base64). Recompute it:
   HMAC-SHA256 over `body + timestamp` using your secret, base64-encode, and
   compare with a constant-time check.
2. **Validate the timestamp.** `X-Crossbeam-Timestamp` must be **within the last
   300 seconds** to prevent replay.
3. **Use an unguessable endpoint path** as defense in depth.

### Minimal verified receiver (Flask)

```python
from flask import Flask, request, abort
import hmac, hashlib, time, base64

app = Flask(__name__)
WEBHOOK_SECRET = b"111122223333secret"   # from the Crossbeam UI
MAX_TIMESTAMP_AGE = 300                   # seconds

def verify(request):
    sig = request.headers.get("X-Crossbeam-Signature-256")
    ts  = request.headers.get("X-Crossbeam-Timestamp")
    if not sig or not ts:
        return False
    try:
        ts = int(ts)
    except ValueError:
        return False
    if abs(int(time.time()) - ts) > MAX_TIMESTAMP_AGE:
        return False
    signed = f"{request.data.decode()}{ts}".encode()
    expected = base64.b64encode(
        hmac.new(WEBHOOK_SECRET, signed, hashlib.sha256).digest()
    ).decode()
    return hmac.compare_digest(sig, expected)

@app.route("/webhook/<random-unguessable-path>", methods=["POST"])
def webhook():
    if not verify(request):
        abort(403)
    payload = request.get_json()
    # Trusted: process the signal (alert, enrich CRM, trigger agent, ...)
    return {}, 200
```

---

## Delivery semantics

- **Respond fast with a 2xx** (200 or 201). No body required.
- **Retries:** Crossbeam retries on `408`, `429`, `500`, `502`, `503`, `504`.
  After retries are exhausted, fetch the missed message via the signals REST
  endpoint — so build the pull path as a backstop, not just the push path.
- Make your handler **idempotent**; retries mean a signal can arrive more than
  once.
