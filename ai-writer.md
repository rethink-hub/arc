---
layout: default
title: "AI Writer & Reply Generator for Android and Mac | Arc"
description: "Rewrite, fix grammar, translate and draft replies inside WhatsApp, Gmail, Slack or any app on Android and Mac. No copy-paste. 7 free requests a week."
keywords: "ai writer, ai reply generator, rewrite text ai"
og_image: /assets/images/og-ai-writer.png
product_page: true
faq:
  - question: "Does it work in every app?"
    answer: "Yes. The AI Writer works across all Android apps with text fields, including email clients, messaging apps, social media, browsers, notes apps, and more."
  - question: "What languages are supported?"
    answer: "Arc's app interface and AI features support 9 languages: English, Spanish, German, French, Portuguese (Brazil & Portugal), Korean, Japanese, and Indonesian. Translation and writing assistance work across many additional languages."
  - question: "Can I choose the tone of the rewrite?"
    answer: "Yes. Pick Rephrase, Professional, Polite, Shorten or Elaborate, or type a Custom instruction for any other tone — casual, persuasive, apologetic."
  - question: "Does the AI Writer store my text?"
    answer: "No. Text is processed for AI responses but never stored on our servers. Your content stays private and is not used to train models."
  - question: "Can it make AI-generated text sound human?"
    answer: "Yes. If a chatbot draft reads robotic, run it through Rewrite with Rephrase or a Custom instruction like \"casual and plain\" and the stiff phrasing gets reworked. If you only want errors repaired, Fix Grammar keeps the wording as is."
  - question: "Can it rewrite text I can't select or copy?"
    answer: "Usually. Arc reads the visible screen rather than the clipboard, so text that's awkward to select on Android — a preview pane, a PDF viewer, part of a web page — is still workable. For very long documents, capture the relevant section or condense it first with AI Summary."
  - question: "Does the reply generator read my whole conversation?"
    answer: "It reads the visible thread on your screen so the reply fits the context — who asked what, and how the conversation has gone. The expandable context preview shows exactly what was captured, and nothing is generated until you tap to generate."
  - question: "Can I fix grammar without opening the panel?"
    answer: "On desktop, yes — bind Fix Grammar (or Rephrase) to a global shortcut like Control+R. Cursor in the field, press the key, the text is corrected in place."
last_modified_at: 2026-10-27
---

<!-- Hero: copy left, the same feature on Mac and Android right -->
<section class="fhero">
  <div class="fhero-copy">
      <span class="fhero-badge">Android &amp; Mac</span>
      <h1>AI Writer and Reply Generator</h1>
      <p class="fhero-sub">Rewrite a draft, fix its grammar, translate it, or answer the message in front of you — inside WhatsApp, Gmail, Slack or any other text field, on Android and Mac. Arc writes the result back where your cursor was, so there's nothing to copy or paste.</p>
      <div class="home-hero-ctas fhero-ctas">
      <a href="https://play.google.com/store/apps/details?id=com.rethink.arc" class="btn btn-primary btn-lg" data-cta="android" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.523 15.3414c-.566 0-1.027-.478-1.027-1.068 0-.591.461-1.069 1.027-1.069.567 0 1.028.478 1.028 1.069 0 .59-.461 1.068-1.028 1.068zm-11.046 0c-.567 0-1.028-.478-1.028-1.068 0-.591.461-1.069 1.028-1.069.566 0 1.027.478 1.027 1.069 0 .59-.461 1.068-1.027 1.068zm11.4-6.12l1.997-3.459a.433.433 0 00-.158-.591.438.438 0 00-.593.156l-2.022 3.502c-1.515-.69-3.205-1.078-4.984-1.078-1.75 0-3.414.374-4.908 1.043L5.355 5.155a.437.437 0 00-.593-.156.433.433 0 00-.158.591l2.006 3.46C2.95 11.479.5 15.096.5 19.245h23c0-4.149-2.45-7.766-5.623-10.024z"/></svg>Get it on Google Play</a>
      <a href="{{ '/macos/' | relative_url }}" class="btn btn-secondary btn-lg" data-cta="mac"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.21-1.96 1.07-3.11-1.05.05-2.31.7-3.06 1.57-.67.78-1.25 2.04-1.09 3.27 1.17.09 2.37-.7 3.08-1.73z"/></svg>Download for Mac</a>
      </div>
  </div>
  <div class="tab-media fhero-media">
    <img width="1200" height="637" class="shot-mac" src="{{ '/assets/images/screenshots/macos/03_ai_writer_rewrite_generated.jpg' | relative_url }}" alt="Arc AI Writer on Mac rewriting a Gmail draft" loading="eager" decoding="async">
    <div class="phone-mini"><video src="{{ '/assets/videos/ai-writer.mp4' | relative_url }}" autoplay loop muted playsinline preload="metadata" poster="{{ '/assets/images/screenshots/03_ai_writer_rewrite_result.jpg' | relative_url }}" width="800" height="1760" aria-label="Arc AI Writer on Android rewriting a message"></video></div>
  </div>
</section>


---

## How the AI Writer works

Arc AI Writer lives in the floating sidebar on Android and behind **Control+Space** on Mac. It reads the text in the field you're in, rewrites it, and writes it back — no copy-paste into another app. Here is the real flow on a rough Gmail draft:

<div class="content-section">
  <h3>1. Invoke Arc over the draft</h3>
  <p>Your draft: <em>"Hi, This is a test mail that i am writing to test AI Writer in Arc App on MacOS/Windows."</em> Press <strong>Control+Space</strong> (Mac) or swipe the edge (Android) and pick <strong>AI Writer</strong>. Arc auto-fetches the focused field's text into the <strong>SELECTED TEXT</strong> box without stealing focus.</p>
  <img class="inline-shot" width="1058" height="984" src="/assets/images/screenshots/macos/03_ai_writer_gmail_before_invoke.jpg" alt="Gmail compose window with a rough draft email before invoking Arc" loading="lazy" decoding="async">

  <h3>2. Pick a tone and generate</h3>
  <p>Choose <strong>Rewrite</strong>, then a tone: <strong>Rephrase</strong> (fresh wording), <strong>Professional</strong>, <strong>Polite</strong> (softens a blunt message), <strong>Shorten</strong>, <strong>Elaborate</strong> (two lines into a full message), or <strong>Custom</strong> — any instruction, like "make it apologetic". Not right? Tap <strong>Regenerate</strong> or step back through the generation history.</p>
  <img class="inline-shot" width="1200" height="637" src="/assets/images/screenshots/macos/03_ai_writer_rewrite_generated.jpg" alt="Arc AI Writer showing the rewritten, polished email draft" loading="lazy" decoding="async">

  <h3>3. Insert</h3>
  <p>Tap <strong>Insert</strong> and the polished text replaces your draft exactly where the cursor was. Hit send.</p>
</div>

## What each mode returns

Each mode is tuned for a different job, and the difference shows up in what comes back:

| Mode | You start with | You get back |
| --- | --- | --- |
| **Rewrite** | "hey so i cant make the 3pm, something came up, sorry" | The same message in the tone you picked, with the meaning and the facts unchanged |
| **Grammar fix** | A paragraph with typos and comma splices | The same paragraph, same voice, with the mistakes corrected and nothing else touched |
| **Reply** | A message thread on screen | A draft answer that reads the thread first — see [replies](#replies) below |
| **Translate** | Text in any of the supported languages | The translation with tone preserved — a casual message stays casual |
| **Create post** | A rough idea or a link | A short-form post shaped for the platform, with variations to pick from |

Rewrite keeps your facts: it will turn "can't make 3pm" into "I'm unable to attend at 3:00 PM," but it will not invent a reason you didn't give it.

### Save the rewrites you run every day

The built-in tones cover most fixes, but daily users end up with a few instructions they repeat — "shorten to one line for a status update", "rewrite as a three-bullet update, lead with the outcome", "confident but not aggressive". Save each once as a [custom action]({{ '/ai-workflow-automation/' | relative_url }}) and it becomes a one-tap button, instead of a Custom instruction you retype.

<h2 id="replies">Replies: five intentions, one tap each</h2>

Open the message in WhatsApp, Gmail or Slack, invoke Arc (edge swipe on Android, **Control+Space** on Mac), choose **AI Writer → Reply**, and tap an intention. Arc reads the message on screen, drafts the response, and **Insert** writes it into the reply field.

| Intention | When to use it | What Arc writes |
| --- | --- | --- |
| Yes / Agree | Confirming a plan, accepting an invite | A warm confirmation with the details echoed back |
| No / Decline | Turning something down politely | A clear, courteous no |
| Thank | Someone helped, sent, or hosted | A genuine thank-you with a specific callback |
| Ask for details | The message is vague or missing info | A focused question asking exactly what's missing |
| Acknowledge | Just let them know you saw it | A brief "got it, will circle back" — no over-promising |

A draft that needs a different register can go straight through one of the rewrite tones above.

<img class="inline-phone" width="800" height="1760" src="/assets/images/screenshots/03_ai_writer_reply_mode.jpg" alt="Arc AI Writer reply mode on Android with five reply intentions" loading="lazy" decoding="async">

### It knows which side of the thread you're on

Paste-the-message tools reply to one message with no memory of what came before, and often from the wrong side of the conversation. Arc reads the visible thread and works out who said what: in WhatsApp and Telegram by bubble alignment (left is them, right is you), in Gmail from the flow of the conversation. It copes with quoted email threads, nested comments and right-to-left scripts like Arabic, Hebrew, Urdu and Persian. A context preview shows exactly what was captured before you generate. If your cursor is already in the reply box, anything you'd started typing is pulled in too.

In practice: a WhatsApp thread ending in *"Want to grab coffee at 3pm today?"*, one tap on Agree, and two to three seconds later — *"Yes, perfect! I'll be there at 3pm. See you then!"*

### Replies that sound like you

<img class="inline-shot" width="1200" height="780" src="/assets/images/screenshots/macos/11_info_vault_with_entries.jpg" alt="Arc Info Vault with saved personal context entries" loading="lazy" decoding="async">

The **My Info Vault** stores your name and title, company, tone preferences and sign-offs once; they appear as optional chips in every reply — include them for a full signature, skip them for one-liners. Entries are stored locally on your device and only leave it if you opt in to Drive backup; with two devices, backups merge instead of overwriting.

### Keyboard-speed fixes on desktop

On Mac and Windows, bind any sub-action to a global shortcut — **Control+R** for Rephrase by default — and fix a text field without opening the Arc panel. It even works in terminals and Electron apps. More on that in [AI shortcuts and custom actions]({{ '/ai-workflow-automation/' | relative_url }}).

| Works inside | Android | macOS / Windows |
| --- | --- | --- |
| WhatsApp / WhatsApp Web | ✅ | ✅ |
| Gmail / Outlook | ✅ | ✅ |
| Slack / Teams | ✅ | ✅ |
| Any text field, any app | ✅ | ✅ |
| Write back into the field | ✅ Insert | ✅ Insert |
| Per-action keyboard shortcut | — | ✅ ⌃R style |

## How it compares to what's already on your phone

- **Gboard's built-in proofread** is free and instant — the right tool for a typo. It fixes; it does not rewrite, reply, or translate with tone.
- **The Grammarly keyboard** is strong on grammar and style, but as a keyboard it acts on what you type, not on what's on screen around it.
- **QuillBot and browser rewriters** are good for long documents on a desktop. On a phone they mean leaving the app, pasting, copying and pasting back — five or six steps for a two-line fix.
- **Pasting into ChatGPT or Gemini** gives you the most capable model for long-form work, at the cost of an app switch and two pastes every time.
- **Arc's AI Writer** reads the screen, so it can answer a message it can see and return you to the app you were in. It is not a live as-you-type grammar engine, and for a 2,000-word draft you want a full chat interface.

## Setup and pricing

Setup is two permissions — accessibility, so Arc can read screen text, and display-over-other-apps, so the sidebar can float — granted from onboarding in about two minutes. Arc disables itself automatically in around 400 sensitive apps, including banking, crypto and password managers, and you can add your own exclusions.

The free tier is 7 requests per week. Premium removes the cap and covers [Android]({{ '/android/' | relative_url }}), [Mac]({{ '/macos/' | relative_url }}) and [Windows]({{ '/windows/' | relative_url }}) on one subscription. No ad tier, no expiring trial.

---

## Frequently asked questions

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Does it work in every app?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">Yes. The AI Writer works across all Android apps with text fields, including email clients, messaging apps, social media, browsers, notes apps, and more.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">What languages are supported?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">Arc's app interface and AI features support 9 languages: English, Spanish, German, French, Portuguese (Brazil & Portugal), Korean, Japanese, and Indonesian. Translation and writing assistance work across many additional languages.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Can I choose the tone of the rewrite?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">Yes. Pick Rephrase, Professional, Polite, Shorten or Elaborate, or type a Custom instruction for any other tone — casual, persuasive, apologetic.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Does the AI Writer store my text?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">No. Text is processed for AI responses but never stored on our servers. Your content stays private and is not used to train models.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Can it make AI-generated text sound human?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">Yes. If a chatbot draft reads robotic, run it through Rewrite with Rephrase or a Custom instruction like "casual and plain" and the stiff phrasing gets reworked. If you only want errors repaired, Fix Grammar keeps the wording as is.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Can it rewrite text I can't select or copy?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">Usually. Arc reads the visible screen rather than the clipboard, so text that's awkward to select on Android — a preview pane, a PDF viewer, part of a web page — is still workable. For very long documents, capture the relevant section or condense it first with <a href="{{ '/ai-summary-reader/' | relative_url }}">AI Summary</a>.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Does the reply generator read my whole conversation?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">It reads the visible thread on your screen so the reply fits the context — who asked what, and how the conversation has gone. The expandable context preview shows exactly what was captured, and nothing is generated until you tap to generate.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Can I fix grammar without opening the panel?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">On desktop, yes — bind Fix Grammar (or Rephrase) to a global shortcut like Control+R. Cursor in the field, press the key, the text is corrected in place.</p>
</details>

---

<div class="download-section">
  <h2>Try the AI Writer free</h2>
  <p style="font-size: 1.1em; color: var(--text-2); margin-bottom: 30px;">
    Rewrite, reply, and polish text in any app on Android and Mac
  </p>
  <a href="https://play.google.com/store/apps/details?id=com.rethink.arc" target="_blank" rel="noopener">
    <img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" alt="Get Arc AI Writer App on Google Play" width="250" height="83" loading="lazy">
  </a>
</div>

---

## Related features

- **[AI Summary &amp; Reader]({{ '/ai-summary-reader/' | relative_url }})** - Summarize and listen to any content
- **[AI Shortcuts &amp; Custom Actions]({{ '/ai-workflow-automation/' | relative_url }})** - Save your own prompts as one-tap actions
- **[Private AI Assistant]({{ '/private-ai-assistant/' | relative_url }})** - Exactly what text goes where

## Available platforms

- **[Arc for Android]({{ '/android/' | relative_url }})** - Download now from Google Play
- **[Arc for iOS]({{ '/ios/' | relative_url }})** - In development
- **[Arc for Mac]({{ '/macos/' | relative_url }})** - Available now, free download
- **[Arc for Windows]({{ '/windows/' | relative_url }})** - Free on the Microsoft Store

---

<!-- related-posts: generated, see scratchpad linkplan -->
<div class="related-links">
  <h2>More on this</h2>
  <p>Guides that go further on what's above:</p>
  <ul>
    <li><a href="{{ '/2026/09/20/ai-writer-mac/' | relative_url }}">AI Writing Assistant for Mac: Rewrite in Any App</a></li>
  </ul>
</div>
<!-- /related-posts -->
