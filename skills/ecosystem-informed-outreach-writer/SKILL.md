---
name: outbound-email-writer
description: >
  Drafts rep-quality outbound emails and 1, 3, or 7-email sequences for any sales,
  partnerships, or GTM motion (cold, warm/intent, re-engagement, expansion, event
  follow-up, referral, partner angle, post-meeting follow-up). Fully self-contained:
  no connectors, no data source, no other skills. Drafts from whatever you give it,
  even a company name and a title alone, and never invents facts. Ends every draft
  with a hard de-AI pass: zero em dashes, no machine-written filler.
  Trigger on: "write an email to X", "draft outreach for Y", "improve this email",
  "help me reach out to Z", "write a follow-up", "draft a cold email", "write a
  3-email sequence", "build a 7-touch cadence", or any request whose output is an
  outbound email or sequence. For bulk post-win outreach to partner reps generated
  from your closed-won deals, use partner-alignment-outreach instead.
---

# README: Outbound Email Writer

Write outbound emails that sound like a sharp rep typed them quickly, not like a template. Single email or a full sequence, any motion, no setup required.

## What it does

Takes whatever you know about the person you want to reach (company, name, title, the reason you're writing, any signal or context you can paste in) and drafts a tight, specific, human-sounding email. Ask for a single email, a 3-email sequence, or a 7-email cadence. Every draft runs through a hard de-AI pass before you see it, so it lands free of em dashes and the usual machine-written tells.

## What you need

Nothing to connect. This skill is fully self-contained: no CRM, no email connector, no other skills, no warehouse. It works from the information you provide in the conversation. If a web search tool happens to be available, it can optionally pull recent public context on the company to sharpen the angle, but this is never required.

To get a strong draft, give it as much of this as you have (none of it is required, more is better):
- Who you're emailing: company, person's name, their title or role
- Why you're writing: the goal (book a call, get a reply, re-engage, expand, follow up)
- Any context or signal: something they did, said, announced, a mutual connection, a prior conversation, a relevant trend
- **Your voice (strongly recommended):** the best way to sound like you is a **personal_voice skill** built once from about 50 of your real calls and emails. If you have one, every draft uses it automatically. If you don't, paste 1 to 3 recent emails or describe your style for this conversation. Voice is the single biggest difference between an email that gets a reply and one that reads like AI outreach.

If all you have is a company name and a title, that's enough to start. The draft will lean on persona and a clear point of view instead of invented specifics. Adding your voice on top of that is what makes it land.

## How to run it

> "Write a cold email to the Head of Partnerships at Acme"
> "Draft a re-engagement email to a customer who's gone quiet"
> "Write me a 3-email sequence for [person] at [company] about [reason]"
> "Improve this email: [paste]"
> "Build a 7-touch cadence for [persona]"

You'll be asked one thing up front: single email, 3-email sequence, or 7-email sequence.

## What to expect

- **One question first:** how many emails (1, 3, or 7). After that it drafts.
- **Drafts only:** nothing is sent. You get clean, copy-ready text to paste into your own tool.
- **No invented facts:** it only uses what you provide. It won't fabricate a signal, a metric, a prior conversation, or a detail about the recipient's company.
- **Sequences that stand alone:** in a 3 or 7-email sequence, every email works on its own, with a different subject line and a fresh angle, no "just following up."
- **Your voice if you give it:** paste a couple of your own emails and the draft will match your rhythm, openers, and CTA wording.

## Not sure what to give it?

Just start with the company and the person's title and say what you're trying to do. It will ask for anything else it needs, and it will tell you where it's working from persona alone versus a real signal you provided.

---

# Skill Instructions

A self-contained outbound email writer. No tools, no connectors, no other skills required. It drafts from user-provided context only and never fetches, sends, or invents data. Output: one email or a labeled sequence of 3 or 7 emails, delivered as copy-ready text.

Run the steps in order. Do not skip Step 2 (the count gate) or Step 5 (the de-AI gate). Each step lists exactly what to do and, where input may be missing, the exact question to ask.

---

## Operating rules (read first)

- **Self-contained.** Do not call any connector, CRM, warehouse, email tool, or other functional skill. If a relevant tool happens to be connected, still do not use it unless the user explicitly asks. The default path is tool-free. The one exception is the sender's own **personal_voice skill**: read it for voice when it exists (see the Voice section). It is a voice profile, not a functional dependency, and the skill still runs fully without it.
- **No invented facts.** Use only what the user provides, or what you verify via the optional web search in Step 1f. Never fabricate a signal, behavioral detail, metric, mutual contact, prior conversation, or anything about the recipient's company. If you don't have a specific hook, write from persona and point of view instead. Inventing a detail is a hard failure.
- **Optional web research.** A quick web search for public company context is allowed and useful, but only when a search tool is available and the user wants it (Step 1f). It is never required, and the skill must run fully without it.
- **Generic by design.** This skill mentions no specific product, company, plan name, internal field, or proprietary score. Keep every draft and instruction vendor-neutral unless the user supplies their own product details.
- **Drafts only.** Never claim to send. Deliver text the user copies themselves.
- **Ask in batches, not one at a time.** When something is missing, ask for everything you need in a single message (see the question blocks below). Never send the user through a chain of one-question-at-a-time replies.

---

## Voice: use a personal_voice skill (greatly recommended)

Using the sender's real voice is greatly advised. It is the single biggest lever on whether an email earns a reply or reads as AI spam. Always check for a voice and use it.

### What a voice is

A voice is a profile of how a specific sender writes, so the draft sounds like that person and not like a generic template. It captures:
- **Opener style:** do they start with a fragment, a question, or straight into the point?
- **Sentence length and rhythm:** short and choppy, medium, or longer and flowing.
- **Contractions and connectors they actually use:** "I'm", "you've", and casual joins like "and", "so", "also", "honestly", "look".
- **Recurring phrases:** signature turns of phrase they reach for.
- **CTA wording:** their literal ask, e.g. "worth a quick chat?", "open to 15 minutes?", "should we grab time?".
- **Sign-off habits:** how they close, if at all.

### The best source: a personal_voice skill

The strongest way to carry voice is a **personal_voice skill** that the sender has built once from a large sample of their own writing, ideally around 50 of their real calls, emails, and messages. Built from that much material, it captures how they actually write far more reliably than a couple of pasted examples can.

**If the sender has a personal_voice skill, it is the primary voice source.** Read it and embed its patterns into every draft, exactly as written. It overrides the generic tone guidance in Step 4c. The only thing it can never override is the de-AI gate in Step 5.

A personal_voice skill is the sender's own voice profile, not a functional dependency of this skill. This skill runs fully without it. When one is present, it simply makes the output sound like the sender.

### Why it's greatly advised

A draft in the sender's real voice clears the de-AI pass in Step 5 naturally and feels personal. A generic draft, however clean, still sounds like everyone else's outreach. The content and angle matter, but the voice is what makes the reader believe a specific human wrote it to them.

### How to get a voice (in priority order)

1. **A personal_voice skill (best, and persists across every session).** If one exists, use it. If the sender doesn't have one yet, recommend they build one once from roughly 50 of their own calls and emails, so it applies automatically to every draft from then on. Building it is a separate one-time setup. This skill does not build, edit, or store a personal_voice skill itself.
2. **Pasted samples (this conversation only).** If there's no personal_voice skill, ask for 1 to 3 of the sender's recent emails and extract the patterns above. Suggest they save the result as a personal_voice skill so future drafts use it automatically.
3. **A one-line style description (this conversation only).** If they have no samples handy, ask them to describe their style in a sentence (e.g. "short, blunt, no pleasantries, always ends on a yes/no question") and build a light profile from it.
4. **None.** Fall back to the universal tone rules in Step 4c.

The exact question to ask is in Step 1c. Capturing the patterns happens in Step 1e, and applying them happens in Step 4c.

---

## Step 1: Gather and check the inputs

### 1a. Read what the user already gave you

From the request, pull out and note each of these. Mark each as "have it" or "missing":

1. **Recipient company** (who they work for)
2. **Recipient identity**: a name, or a title/role (either one is enough)
3. **Goal** of the email (book a call, get a reply, re-engage, expand, follow up after a meeting)
4. **Context or signal** (optional): anything specific and true to open with, a mutual connection, a prior conversation, something they did, said, announced, or a relevant trend
5. **Voice** (strongly recommended): first check whether the sender has a **personal_voice skill** (the best source). If not, their own writing samples or a one-line description of their style. See the Voice section above for the full priority order.

### 1b. Decide whether you can proceed

The minimum to draft is item 1 (company) AND item 2 (a name or a title). Everything else is optional.

- If you have the minimum, continue. Do not stall for the optional items.
- If the minimum is missing, ask for it using the question block in 1c. Ask once, in one message.

### 1c. Exact questions to ask when something is missing

Ask only for what's actually missing. Combine into a single message. Use these phrasings:

- **No company:** "Who are you emailing, and where do they work? A name or just a title is fine."
- **Company but no name or title:** "Got [Company]. Who's the email going to? A name, or even just their role (e.g. Head of Partnerships, VP Sales) works."
- **No goal / unclear goal:** "What do you want this email to do? For example: book a call, get a reply, re-engage someone who went quiet, expand an existing account, or follow up after a meeting."
- **No context, to sharpen the hook (optional, ask once):** "Anything specific I can open with? A signal, something they did or announced, a mutual connection, or a prior conversation. If not, I'll write from their role and a clear point of view."
- **Voice (strongly recommended):** First check whether the sender already has a personal_voice skill. If they do, use it and do not ask. If they don't, ask once: "Want this in your voice? It's the biggest thing that makes an email land. The best option is a personal_voice skill built from about 50 of your past calls and emails, then it applies automatically every time. For now, paste 1 to 3 recent emails or describe your style in a sentence and I'll match it for this conversation. Otherwise I'll use a clean, human, rep-to-rep style." (See the Voice section above for the priority order and what to extract.)

If the user ignores an optional question, do not re-ask. Proceed with what you have.

### 1d. Handle an "improve this email" request

If the user pasted an existing email to fix, that draft is your source:
1. Infer the recipient and intent from the draft itself.
2. Confirm the goal only if it's genuinely unclear (use the goal question above).
3. Go straight to Step 2.

### 1e. Lock in the voice source

Resolve the voice using the priority order in the Voice section:
1. **personal_voice skill present** → it is the primary source. Read it in full now and plan to embed its patterns in Step 4c. Do not ask for samples.
2. **No personal_voice skill, samples pasted** → extract the concrete patterns now (opener style, sentence rhythm, contractions and connectors, recurring phrases, CTA wording, sign-off) and apply them in Step 4c. Suggest the user save these as a personal_voice skill for next time.
3. **No personal_voice skill, only a one-line style description** → build a light profile from it.
4. **Nothing** → use the universal tone rules in Step 4c.

If the user has no personal_voice skill and skipped the offer in 1c, nudge once that building one from about 50 of their calls and emails is the biggest single upgrade, then proceed with what you have.

### 1f. Optional: research the company (only if a web search tool is available)

This step is optional and never required. The skill works fully without it. Run it only when both are true: (1) a web search tool is actually available in the session, and (2) the user wants it, or you have no strong hook from their input and they say yes when you offer.

1. **Offer once:** "Want me to run a quick web search on [Company] for recent context (news, funding, leadership changes, product launches) to sharpen the angle? Or I can write from what you've given me."
2. **If yes and search is available:** look for recent, public signals, roughly the last 90 days. Useful hooks: funding rounds, acquisitions, leadership hires, product launches, notable announcements, and the recipient's public role or background.
3. **Use only what you can verify** in the results. Do not over-read a thin or unrelated result, and do not stretch a finding into a hook it doesn't support. If nothing material turns up, say so and write from persona.
4. **This does not break the no-invented-facts rule.** That rule bans making things up, not using verifiable public research. When a hook comes from a search result, note that in the Step 6 handoff so the user can sanity-check it before sending.
5. **If no web search tool is available, skip silently and proceed.** Never block on it, never claim you searched when you didn't.

Feed any solid finding into the hook in Step 3b.

---

## Step 2: Gate, ask how many emails (MANDATORY)

### 2a. Ask the count, unless the user already said it

Ask this every time before drafting. The only exception: the user already named the count (e.g. "write a single email", "a 3-email sequence", "a 7-touch cadence"). If they named it, confirm in one line and move on. Otherwise ask exactly:

> "Single email, a 3-email sequence (Day 1 / 4 / 7), or a 7-email sequence (Day 1 / 3 / 5 / 7 / 10 / 14 / 18)? Default is a single email, just say 3 or 7 for a sequence."

### 2b. Know what each option is for

**Single email.** One shot. Best angle, one CTA. Right when the context is strong enough that one good email should earn a reply.

**3-email sequence:**

| # | Day | Purpose |
|---|-----|---------|
| 1 | 1 | Hook. Strongest angle, earn a reply. |
| 2 | 4 | Different angle. A new pain point or outcome, nothing repeated from email 1. |
| 3 | 7 | Soft close. Three sentences or fewer, lighter ask, give them an easy out. |

**7-email sequence:**

| # | Day | Purpose |
|---|-----|---------|
| 1 | 1 | Hook. Strongest angle, set the tone. |
| 2 | 3 | Deepen. A different facet of the same problem, or a proof point. |
| 3 | 5 | Social proof. A relevant example that mirrors their situation (only if the user supplied one). |
| 4 | 7 | New angle. A completely different entry point. |
| 5 | 10 | Re-engage. Acknowledge the silence, ask a genuine question. |
| 6 | 14 | Value-add. Share an insight or resource, no ask at all. |
| 7 | 18 | Breakup. Three sentences or fewer: "Should I close this out?" |

### 2c. Store the choice

It sets how many emails you draft and the output format in Step 6.

---

## Step 3: Pick the angle

Make one strategic decision before writing: motion, hook, tone. Base it only on what the user provided.

### 3a. Choose the motion

Pick the closest match to the situation the user described:

| Situation | Motion | Goal |
|---|---|---|
| No prior relationship, no signal | Cold / ICP | Earn a reply, start a conversation |
| They did something relevant (researched, engaged, attended) | Warm / intent | Reference it, convert the interest |
| Existing relationship gone quiet | Re-engagement | Reopen, low friction |
| Existing customer, room to grow | Expansion | Reference the specific gap or next step |
| Met at an event | Event follow-up | Reference the specific event or conversation |
| A mutual connection or partner overlaps | Referral / partner angle | Use the warm context as the opener |
| Just had a meeting or call | Post-meeting follow-up | Recap sharply, confirm next steps |

If the motion is unclear from what you have, default to the goal the user stated in Step 1; if that's also unclear, ask the goal question from 1c before drafting.

### 3b. Choose the hook

The hook is the single most specific true thing you can open with, drawn from the user's input or from verified research in Step 1f:
- Something they did or said, an announcement, a mutual connection, an unresolved item from a prior conversation, a role-specific pain point, or a recent public signal you confirmed by web search (funding, a leadership hire, a launch).
- If two or three pieces of context exist, blend them into one recipient-centric opening sentence rather than listing them.
- If there is no specific hook, lead with a sharp persona-level point of view. Never fabricate a detail to manufacture a hook.

### 3c. Choose the tone

Match seniority and relationship:
- Peer-to-peer for most.
- More economical and senior for C-suite.
- Warmer, continuation-style for existing relationships.

---

## Step 4: Draft

Write the email(s). Execute the angle from Step 3. Two worked example patterns are in Appendix A, use them as structural references.

### 4a. Use the core structure

```
Subject: [specific, 8 words or fewer]

Hi [First name],

[Hook: one specific, true observation or point of view]

[1 to 2 sentences: the implication, tied to a real pain or outcome]

[One CTA: an easy yes/no question]
```

### 4b. Respect the hard limits

- Subject line: 8 words or fewer, specific beats clever, and a different subject for every email in a sequence.
- One CTA only. Never two asks (a post-meeting follow-up may have at most two concrete next steps).
- Length: no fixed cap, but most land at 4 to 8 sentences. Longer is fine only if every sentence earns its place.
- No bullet points or bold in the body. One narrow exception: a short two or three item numbered list is fine in a warm intro (e.g. "two quick things: 1... 2...") when it reads naturally. Never in a cold pitch.
- Sign-off: end after the last line of body copy by default, so the user's own signature completes it. If the user wants a sign-off, use a plain one ("Best,") and nothing performative.
- One link maximum, placed inline as the CTA.

### 4c. Apply voice

Use whatever voice source you locked in at Step 1e. Voice is not decoration added at the end, it shapes every sentence from the first draft.

- **personal_voice skill:** re-read it before writing a single word, then embed its patterns directly: openers, sentence rhythm, contractions and connectors, CTA wording, recurring phrases. A reader who knows the sender should recognize the writing as theirs. The personal_voice skill overrides everything in this step except the de-AI gate in Step 5.
- **Pasted samples or a style description:** match the patterns you extracted in Step 1e in the same way. They override the generic guidance below, except the de-AI gate.
- **No voice given:** apply the universal rules below. It must read like a human typed it quickly, never like it was composed.

**What natural looks like:**
- Make it about them specifically. Use the recipient's company name and real details. Never a generic bucket like "companies like yours", "teams like yours", or "businesses your size", it makes the reader feel like a segment, not a person. If you want to invoke peers, name real ones.
- Short sentences. Fragments are fine.
- Contractions always: "I'm", "you've", "they're".
- Plain connectors: "and", "so", "also". Not "furthermore", "additionally", "moreover".
- "Can we find time?" not "Would you be amenable to a brief introductory conversation?"
- Write as "I", not "we".

**Openers that work:**
- A direct reference to the real context the user gave you.
- A sharp persona-level observation.
- Jumping straight into the point with no warm-up.

**Openers that don't work:**
- "I hope this email finds you well."
- "I'm reaching out because..."
- "My name is X and I work at Y" as the first sentence. A one-line intro is fine, but it never leads (see 4e).
- Anything starting with "I" plus "wanted to" / "would love to" / "am excited to".

**CTAs that work:**
- "Worth a quick call?"
- "Open to 15 minutes next week?"
- "Want me to send the details?"

**CTAs that don't work:**
- "Let me know your thoughts."
- "Feel free to book time" as the only CTA.
- Two asks competing in one email.

### 4d. Follow the sequence rules (3 and 7-email only)

- Every email stands alone and would make sense if it were the only one received.
- No "just following up" or "circling back."
- A different subject line each time.
- Never reuse a hook, data point, proof example, or CTA across the sequence.
- Later emails can be slightly warmer, since first contact is done.
- The final email (soft close or breakup) is three sentences or fewer and gives an easy out.
- In a 7-email sequence, email 6 (value-add) has no ask at all.

### 4e. Handle a first touch

When this is a first email to someone with no prior relationship and the user needs to introduce themselves, lead with the hook, then fold a one-sentence intro into the first paragraph. Never open with the intro.

---

## Step 5: De-AI pass (HARD GATE, the last stop before delivery)

Re-read every draft before it goes anywhere. This is a hard stop: no email is delivered until it passes all three checks. If a draft fails, rewrite it and run the gate again.

### 5a. Zero em dashes

Remove every em dash and every dash used like one. Do not just swap the character for a hyphen. Restructure the sentence with a comma, a period, or two sentences. The final text contains no em dashes anywhere.

### 5b. No machine-written tells

Cut or rewrite anything that marks an email as AI-generated:
- Filler openers: "I hope this finds you well", "I wanted to reach out", "just reaching out", "touching base", "circle back", "circling back".
- Buzzwords: "delve", "robust", "seamless", "streamline", "leverage", "unlock", "navigate", "landscape", "game-changer", "synergy", "ecosystem of solutions", "at the end of the day", "win-win".
- Hype verbs: "excited to", "thrilled to", "delighted to".
- The rule-of-three flourish ("faster, smarter, and more aligned").
- Generic compliments that describe the recipient's company back to them.
- **Generic-bucket framing:** "companies like yours", "teams like yours", "businesses your size", "organizations in your space", "folks like you". It makes the reader feel like a segment instead of a person, and it's the fastest way to sound like mass mail. Replace it with the recipient's actual company name, or name a real, specific peer (e.g. "the way [named company] runs this"). Naming concrete peer companies is good. Lumping the recipient into a vague "like yours" group is not.
- Surveillance framing: "I noticed", "I saw that", "I can see you" plus a specific behavior. Reference context the user gave you as something you know, not something you watched them do.

### 5c. The human test

Would a busy person read this and assume a human typed it between meetings? If not, rewrite until yes.

---

## Step 6: Deliver

### 6a. Present the draft(s)

Show clean, copy-ready text (no tool needed to send):
- **Single email:** the subject and body, nothing else competing with it.
- **Sequence:** each email clearly labeled with its day and purpose (e.g. "Email 1 / Day 1 / Hook"), in order, each one self-contained.

### 6b. Offer a light revision loop

Invite the user to change tone, shorten, swap the angle, or match a voice sample. When they ask, revise the specific email(s), rerun the Step 5 gate, and re-present.

### 6c. Never send

Never send and never claim to have sent. The user copies and sends from their own tool.

---

## Rules

- Self-contained: no connectors, no CRM, no email tool, no warehouse, no other functional skills. The sender's own personal_voice skill is the only thing read in, and only for voice.
- Voice priority: personal_voice skill (best, persists across sessions) > pasted samples > one-line style description > universal tone. A personal_voice skill is built once from about 50 of the sender's calls and emails; this skill does not build or store it.
- Use only user-provided information, or facts verified via the optional Step 1f web search. Never invent a signal, fact, metric, contact, or prior conversation.
- Web research (Step 1f) is optional and tool-gated: offer it only when a search tool is available, never require it, and skip silently when it isn't there.
- When input is missing, ask the exact questions in Step 1c, batched into one message.
- The 1 / 3 / 7 gate (Step 2) is mandatory unless the user already stated the count.
- The de-AI gate (Step 5) is mandatory and is a hard stop: zero em dashes, no machine-written filler, every time.
- Generic and vendor-neutral: no product names, plan names, internal fields, or proprietary scores unless the user supplies them.
- Drafts only. Never send.
- One CTA per email. Different subject line per email in a sequence. Every email stands alone.

---

## Appendix A: Worked example patterns

Two real, high-performing outbound patterns, genericized. Use them as structural references, not fill-in-the-blank scripts. Both end without a typed sign-off so the sender's own signature can complete the email. (Typing the sign-off by hand is also how you get the classic broken-signature glitch, where "Best," splits across a line as "B ... est,". Ending after the body avoids it.)

### Example 1: You use their product, peer curiosity (warm cold)

**Motion:** cold or near-cold, opened from a real relationship (you already use the recipient's product). **Why it works:** leads with credibility and genuine curiosity, names relevant peers, and asks one real question instead of pitching.

**Pattern:** disclosure (you use their product) → an opportunity you see from a different angle → the category-level problem → two named peers doing it well → one genuine question → light CTA.

```
Subject: [specific, 8 words or fewer]

Hi [First name],

Full disclosure: our [team] here at [Your company] relies on [their product] for [use case]. We're big fans.

Looking at it through a [different] lens, though, I noticed an opportunity for your [team].

[Category] companies often hit the same wall: [specific problem]. When that goes unsolved, [the concrete cost].

It's why companies like [Peer 1] and [Peer 2] use [Your company]. They [the specific thing they do differently].

Since we already use [their product], I'm curious, how is your team handling [the specific thing] today?

Worth a 20 minute chat next week?
```

### Example 2: Intro and offer to help (warm / onboarding)

**Motion:** warm outreach to a new or active user. **Why it works:** generous, low-pressure, references real activity, and makes the next step effortless.

**Pattern:** quick self-intro → offer yourself as a resource → reference the specific activity you saw → offer a walkthrough or to answer questions → easy calendar option → warm close.

```
Subject: [specific, 8 words or fewer]

Hi [First name],

[Your name] from [Your company]'s [team] here. Two quick things:
1. A proper intro, good to meet you.
2. I want to be a resource for you and the [Company] team.

I saw you've spent some time in [product or area] lately. Want me to answer any questions, or would a quick walkthrough be useful?

I'm around whenever, just reach out. Or grab time here: [calendar link].

Looking forward to working together.
```

Both examples obey the rules in Steps 4 and 5: no em dashes, one CTA, a specific subject, and no machine-written filler. Adapt the placeholders to the real situation, and never invent the peer names, the use case, or the activity, use only what the user gave you or what you verified in Step 1f.
