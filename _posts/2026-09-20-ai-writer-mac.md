---
layout: blog
title: "AI Writing Assistant for Mac: Rewrite in Any App"
description: "An AI writing assistant for Mac that works inside the app you're typing in. Rewrite, reply, fix grammar — and Arc inserts the result back in place."
date: 2026-09-20
author: Mamata
tags: ["mac", "macos", "ai", "writing"]
keywords: "ai writing assistant mac, ai rewrite tool mac, ai reply generator"
last_modified_at: 2026-10-27
og_image: /assets/images/og-post-ai-writer-mac.png
faq:
  - question: "Does Arc's AI Writer work in any Mac app?"
    answer: "Anywhere macOS exposes a text field: native mail clients, browsers (Gmail, Outlook Web, WhatsApp Web, LinkedIn), Electron apps like Slack and VS Code, terminals, and note apps. Apps that expose no text field fall back to a clipboard-based capture path."
  - question: "How is Arc different from Apple Intelligence Writing Tools?"
    answer: "Writing Tools is free on M-series Macs with macOS 15.1+, and it proofreads and rewrites selected text in most apps. Arc also runs on Intel Macs and macOS 14, adds thread-aware replies with set intentions, Info Vault context about you, and one-key shortcuts for each rewrite tone. If Writing Tools covers what you need, you may not need Arc."
  - question: "Is iA Writer an AI writer?"
    answer: "No. iA Writer is a well-regarded markdown editor for focused drafting; it doesn't rewrite text inside other apps. Arc works over other apps: it captures the draft from the field you're typing in, rewrites or replies, and inserts the result back."
  - question: "Can I use Arc's AI Writer on Mac for free?"
    answer: "Yes. Arc downloads free from arcassistant.app/macos/ and the AI Writer is included in the free tier's weekly requests."
  - question: "Does it work in Gmail, Slack, and WhatsApp Web?"
    answer: "Yes. The Reply mode is particularly useful in Slack and WhatsApp Web, where Arc extracts the message thread from the screen so the reply is written from your side of the conversation."
---

An **AI writing assistant** is only useful if it works where you actually write. Arc runs inside the app you're already typing in on Mac — Mail, Slack, a browser text box — so you press one key, it rewrites or replies, and the result goes straight back into the field you were in.

The common alternative is copy-and-paste: select your draft, switch to a ChatGPT tab, paste, wait, copy the result, switch back, paste over the draft. It works, but formatting breaks and you lose your place, especially across a dozen emails a day.

This guide walks through Arc's AI Writer on Mac — install, first rewrite, replies, grammar fixes, personalization, and one-key shortcuts — and compares it fairly with Apple's Writing Tools and other options.

Arc is an [AI screen assistant](/) — it sees the frontmost window on your Mac, which is what makes in-place writing possible. The full feature rundown lives on the [AI Writer](/ai-writer/) page; here I'll show you the actual day-to-day workflow.

## What a Mac Writing Assistant Should Do

"AI writer" means very different things across the App Store. A useful one should:

- **Work system-wide.** Mail, Gmail in Chrome, Slack, WhatsApp Web, Outlook, a CRM form — your writing lives everywhere, so the writer has to live there too. A tool that only works inside its own editor fails immediately.
- **Grab the draft itself.** If you have to select, copy, and paste before the AI even sees your text, the tool has added friction to the exact problem it was supposed to remove.
- **Write the result back.** The round trip only counts as done when the polished text lands back in the original field, in the original app.
- **Handle more than rewrites.** Fixing grammar, replying to a thread, and composing a post from scratch are different jobs that need different controls.
- **Sound like you.** Generic AI output is easy to spot. The writer should know your role, your projects, and your tone.

Arc's AI Writer is built around those five. It's the same engine that ships in [Arc for Android](/android/), adapted for the desktop with keyboard-first controls. Here's the setup, start to finish.

## Step 1: Install Arc

Download Arc free from [arcassistant.app/macos/](/macos/) and drag it into Applications. On first launch, macOS asks for **Accessibility** permission, which lets Arc read the text in the frontmost window and write the rewritten text back into it. **Screen Recording** is only needed if you use screenshot or region capture. Grant them in System Settings when prompted — it takes under a minute.

No account is required to start. Open any app with a text field and you're ready for step two.

## Step 2: Rewrite a Draft in Place

This is the flow you'll use most often. Say you've got a rough email draft in Gmail:

1. Leave your cursor in the text field — don't select anything, don't copy anything.
2. Press **Control+Space**, Arc's global shortcut, from anywhere.
3. Arc's menu appears over the app. Select **AI Writer** and press Return.
4. The AI Writer panel opens over your draft — and the draft is already in it. Arc auto-fetches whatever was in the focused field into the Selected Text box.

<img src="{{ '/assets/images/screenshots/macos/03_ai_writer_gmail_before_invoke.jpg' | relative_url }}" alt="Rough Gmail draft on Mac before AI Writer is invoked" width="1200" height="715" loading="lazy" />

5. Pick a mode and a tone. For rewrites there are six: **Rephrase, Professional, Polite, Shorten, Elaborate, Custom**. Writing to a client who's annoyed with you? Polite. Turned three paragraphs into nine? Shorten.
6. Click **Generate**. The rewritten version appears in the output pane in a few seconds.

<img src="{{ '/assets/images/screenshots/macos/03_ai_writer_rewrite_captured_text.jpg' | relative_url }}" alt="AI Writer panel over Gmail with the draft auto-captured and rewrite mode selected" width="1200" height="715" loading="lazy" />

7. Not happy with the take? Click **Regenerate** — every generation is kept, so you can step back and forth through the versions and pick the one that reads best.
8. Click **Insert**. The panel closes and Arc writes the final text into the original field, replacing the rough draft. Gmail reacts as if you'd typed it yourself — "Draft saved" appears at the bottom, exactly like a normal edit.

<img src="{{ '/assets/images/screenshots/macos/03_ai_writer_rewrite_generated.jpg' | relative_url }}" alt="AI Writer rewrite result generated on Mac, ready to insert back into the app" width="1200" height="715" loading="lazy" />

That's the whole loop: read the field, generate, write it back. Because the panel is non-activating, your cursor and scroll position never move while it's open.

### Fix Grammar Without Rewording

Sometimes you don't want a rewrite — you want the same message with the typos gone. The **Fix Grammar** mode is built for exactly that: it corrects spelling, agreement errors, and punctuation while keeping your voice and phrasing intact. Invoke the panel the same way, switch to the Fix Grammar tab, Generate, Insert.

### Reply to a Thread With One Tap

Replying is a different job than rewriting, so it has its own mode. Open the thread — email, Slack, a support ticket — then summon **AI Writer** and switch to the **Reply** tab. Arc extracts the conversation from the screen and classifies who said what, so the reply is written from your side of the exchange. If it mislabels a message, you can flip the attribution.

Then pick from five one-tap intentions: **Yes/Agree**, **No/Decline**, **Thank**, **Ask for details**, **Acknowledge**. Generate, review, Insert. Because Arc reads the thread, the reply refers to what was actually said. Always review it before sending.

### Create a Post or Review From Scratch

The fourth mode, **Create Post**, writes from nothing. Choose Post or Review, then pick the target platform — Reddit gets conversational paragraphs, X gets something concise with hashtags, LinkedIn gets thought-leadership framing, and store reviews get the right tone for Google Play or the App Store. Describe what the post should say, Generate, then Insert or Copy. Same panel, zero tab-switching.

## Step 3: Make the Output Sound Like You

Generic output is the biggest complaint about AI writing tools. Arc's answer is **Info Vault** — a place to store entries about your role, projects, and preferences. In the AI Writer panel, the "Use from my Info Vault" row shows a chip for each entry. Tap one or two — say, `#My Job` and `#Arc Project` — and their contents travel with the generation request as context.

The difference shows up quickly: instead of "I'm happy to help with the project," you get "Happy to take the API migration next sprint" — because the vault entry said your team calls it the API migration and you own that sprint.

## Step 4: Skip the Panel Entirely With Shortcuts

Once you know which fix you always want, bind it. AI Writer has **twelve bindable sub-actions** — Fix Grammar, each of the five rewrite tones, each of the five reply intentions, and Create Post. Open Arc's shortcut settings, assign a combination like **Control+R** to Rephrase, and from then on the flow collapses to one keystroke: select text anywhere, press Control+R, and the panel never opens. Arc reads the field, rephrases, and writes the result straight back.

One caveat from the design: the **Custom** tone isn't bindable, because it needs free-text instructions that a headless shortcut can't supply. Everything else can be bound.

## How Arc Compares With Other Options

The options look similar but suit different people:

- **Apple Intelligence Writing Tools.** Free on M-series Macs running macOS 15.1+, works in most text fields, and handles proofreading and rewrites well. If you have a supported Mac and mainly need tone rewrites, try it first. Arc adds Intel and macOS 14 support, thread-aware replies, Info Vault context, and one-key shortcuts per tone.
- **ChatGPT or Claude.** The better choice for long drafts, brainstorming, and back-and-forth editing of a big document. For quick fixes inside other apps, the copy-paste cycle is the cost.
- **Grammarly.** Strong for ongoing grammar and clarity suggestions as you type, including in its desktop app. It's less suited to generating a full reply to a thread.
- **iA Writer — not what it sounds like.** If you searched for an AI writer on Mac, half the results are for *iA* Writer, a well-regarded markdown editor with no AI generation at all. Different product, different problem: it's for focused drafting, not for rewriting text inside other apps.

Arc fits best if you want one shortcut that rewrites or replies in whatever app you're in and inserts the result back. If you also want the reading side — summaries and text-to-speech over any window — that's covered in the [AI Summary & Reader](/ai-summary-reader/) guide, and both features ship in the same app.

## FAQ

### Does Arc's AI Writer work in any Mac app?

Yes — anywhere macOS exposes a text field. That covers native mail clients, browsers (Gmail, Outlook Web, WhatsApp Web, LinkedIn), Electron apps like Slack and VS Code, terminals, and note apps. Apps that expose no text field fall back to a clipboard-based capture path, so there's almost always a way in.

### How is Arc different from Apple Intelligence Writing Tools?

Writing Tools is free on M-series Macs with macOS 15.1+, and it proofreads and rewrites selected text in most apps. Arc also runs on Intel Macs and macOS 14, adds thread-aware replies with set intentions, Info Vault context about you, and one-key shortcuts for each rewrite tone. If Writing Tools covers what you need, you may not need Arc.

### Is iA Writer an AI writer?

No. iA Writer is a markdown editor for focused drafting — excellent at it, but it doesn't rewrite text inside other apps. Arc works over *other* apps: it captures the draft from whatever field you're typing in, rewrites or replies, and inserts the result back. If you want a place to write, use iA Writer. If you want the writing fixed everywhere you already write, use Arc.

### Can I use Arc's AI Writer on Mac for free?

Yes. Arc downloads free from [arcassistant.app/macos/](/macos/) and the AI Writer is included — install it, grant the two permissions, and you can run the first rewrite within two minutes of opening the DMG.

### Does it work in Gmail, Slack, and WhatsApp Web?

Yes. The Reply mode is particularly useful in Slack and WhatsApp Web, where Arc extracts the message thread from the screen so the generated reply answers the right person from the right side of the conversation.

### Can I run a rewrite without opening the Arc panel?

Yes — bind any of the twelve sub-actions to a global shortcut (Fix Grammar, Rephrase, Shorten, Thank, and so on). Then it's one combination from any app: Arc rewrites the focused field headlessly and writes the text back, no panel, no clicking.

## Try Arc's AI Writer on Your Mac

The core loop takes two minutes to set up and about ten seconds per use after that: Control+Space, AI Writer, Generate, Insert. Download Arc for Mac free from [arcassistant.app/macos/](/macos/), grant the two permissions, and put ⌃Space to work on the next draft you'd rather not polish by hand. Android users get the same AI Writer in [Arc for Android](/android/) — grab it free on [Google Play](https://play.google.com/store/apps/details?id=com.rethink.arc).

<!-- sources -->
*Further reading: [Apple's Accessibility framework](https://developer.apple.com/documentation/accessibility) · [Google's Gemini developer docs](https://ai.google.dev/).*
