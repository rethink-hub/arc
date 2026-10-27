---
layout: blog
title: "Summarize a PDF or Any Text on Mac in One Keystroke"
description: "How to summarize a PDF, article or any text on macOS without uploading it: Apple's built-in options, plus Control+Space over any window."
date: 2026-09-16
author: Mamata
tags: ["mac", "macos", "ai", "productivity"]
og_image: /assets/images/og-post-ai-summarizer-mac.png
keywords: "summarize pdf mac, summarize text mac, pdf summarizer"
last_modified_at: 2026-10-27
---

To **summarize a PDF** on Mac: open it in Preview or any viewer, press Control+Space, and pick AI Summary. Arc reads the document already on screen and returns numbered key points in seconds — no exporting, and no uploading the file to a summarizer website.

The usual way to summarize something on a Mac is copy-and-paste: select the text, switch to a chat tab, paste, type "summarize this," wait, and copy the answer back. That works, but it's slow when you do it several times a day, and it's awkward for PDFs and email threads.

I build Arc, an [AI screen assistant](/) for Android and macOS. This guide shows how to summarize web pages, PDFs, and email threads with Arc, save the useful summaries, and ask follow-up questions — then compares Apple's built-in options and other tools honestly. Arc works in any Mac app because it reads the frontmost window instead of asking you to bring text to it.

## What to Look for in a Mac Summarizer

Whichever tool you pick, it's worth checking four things:

- **System-wide.** It should work in Safari, Chrome, Preview, Mail, Slack, Obsidian, Pages — any window, not just its own. If a tool only summarizes documents you upload to it, you'll stop using it within a week.
- **One keystroke away.** Selecting, copying, and pasting is the tax you're trying to escape. The summarizer should come to your text, not the other way around.
- **Grounded in the actual window.** The summary should be about the content on your screen right now — the real article, the real PDF — not a paraphrase of what you pasted.
- **Fast and quiet.** It should appear, do the job, and get out of the way. No new tab to manage, no window to shuffle.

Apple's Writing Tools meets some of these on newer Macs (see [other ways to summarize](#other-ways-to-summarize-text-on-macos) below). Here's how Arc handles all four.

## Step 1: Install Arc and Grant One Permission

Arc for Mac ships as a notarized DMG from [arcassistant.app/macos/](/macos/), so it installs like any Mac app — no Gatekeeper warnings, no terminal commands:

1. Download the DMG and open it.
2. Drag **Arc** into your Applications folder.
3. Launch it. Onboarding asks for **Accessibility permission** — this is what lets Arc read the text of the window in front of you. It's the same macOS API family that VoiceOver uses, and nothing is read until you actively press the shortcut.
4. That's it. There's no account wall before your first summary.

Arc runs natively on Apple Silicon and Intel, on macOS 14 (Sonoma) or later, and the free tier gives you 7 requests per week. Screen Recording permission is only requested if you use screenshot-based actions — plain text summarization needs Accessibility alone.

## Step 2: Press Control+Space

Press **Control + Space** anywhere in macOS — with Safari in front, with a PDF open in Preview, mid-email in Mail. A slim floating panel slides in over the active window: anchored to the edge, translucent so you can still see the text behind it, with Arc's actions already listed. It works like Spotlight, except it acts on the window behind it instead of launching apps.

Pick **Summarize** from the panel. Arc reads the frontmost window through the accessibility tree — the actual text, not a screenshot OCR guess — and a tight summary appears in the panel in about 3–6 seconds. The default prompt keeps numbers, names, and deadlines rather than washing them into vague prose. Press **Esc** and the panel collapses; your document is exactly where you left it, unscrolled and untouched.

<img src="{{ '/assets/images/screenshots/macos/01_arc_menu_over_chrome.jpg' | relative_url }}" alt="Arc summarizer panel open over a Chrome window on macOS" width="1200" height="715" loading="lazy" />

If you're a mouse person, there's a small icon in the menu bar that opens the same panel over the active window. And if Control+Space is already bound to something on your machine (it's the default input-source switcher on some setups), you can remap the shortcut in Arc's settings — the panel doesn't care which key summons it.

That's the entire interaction model: one keystroke, one window, one result.

## Step 3: Summarize a Web Page in Safari or Chrome

The most common use. Say you're on a 4,000-word product review and you only want the verdict:

1. Open the article in Safari (or Chrome — Arc reads both the same way).
2. Press **Control + Space**.
3. Choose **Summarize**.
4. Read the summary in the panel. If it's a keeper — a reference doc, a recipe, a comparison you'll need next week — tap **Save** and it goes to your Library, where it survives browser restarts and Mac reboots.

Two things worth knowing about how this works. First, Arc summarizes what's rendered on the page, including parts of long articles that load as you scroll — you don't have to scroll to the bottom first. Second, if the summary skips something you care about, just type a follow-up in the panel: *"what did it say about battery life?"* The answer is grounded in the live window, so it answers from the actual article rather than inventing a plausible guess.

<img src="{{ '/assets/images/screenshots/macos/02_ai_summary_result_panel.jpg' | relative_url }}" alt="AI Summary result panel with numbered key points in Arc for Mac" width="1200" height="715" loading="lazy" />

## Step 4: Summarize a PDF in Preview

PDFs are where tab-bound summarizers fall apart — you'd have to export, upload, and wait. Here it's the same three moves:

1. Open the PDF in Preview (or your PDF reader of choice).
2. **Control + Space**, choose **Summarize**.
3. Get a condensed version of 30 pages without leaving the document.

For academic papers and reports, follow-up questions are the most useful part: *"list the methodology in bullets," "what are the limitations the authors admit?," "extract every statistic into a table."* Each answer is anchored to the PDF in front of you rather than to what a chatbot assumes the document says.

## Step 5: Summarize Email Threads in Mail

A nine-reply thread is mostly repetition with one decision buried in it. Open the thread in Mail, press **Control + Space**, hit **Summarize**, and you get the actual state of the conversation: who asked for what, what was agreed, what's still pending.

And because Arc is a full screen assistant and not only a summarizer, you can go one step further — choose **Reply** and the [AI Writer](/ai-writer/) drafts a response in the tone you've set, placed right where you were about to type it.

<img src="{{ '/assets/images/screenshots/macos/03_ai_writer_inserted_into_gmail.jpg' | relative_url }}" alt="AI Writer reply drafted into a Gmail reply field on macOS" width="1200" height="715" loading="lazy" />

## Step 6: Save Summaries to Your Library

Summaries you save land in Arc's **Library** — a searchable list of everything you've condensed, grouped by source. Saving is what makes summaries useful beyond the moment:

- Research for a project accumulates instead of evaporating with each chat session.
- **Custom actions** let you encode your own summary style. If you always want "3 bullet points + one action item," write that prompt once in the custom-action editor, bind it to its own hotkey, and it becomes a permanent button in the panel. The patterns for chaining these into repeatable pipelines live on the [AI Workflow Automation](/ai-workflow-automation/) page.
- **500+ community actions** are one-click installs — including summarizer presets other users have already tuned.
- The Library optionally backs up to Google Drive, so a new Mac doesn't mean a cold start.

<img src="{{ '/assets/images/screenshots/macos/13_saved_items_library_list.jpg' | relative_url }}" alt="Saved Items library list in Arc for Mac" width="1200" height="715" loading="lazy" />

## More Things This Setup Can Do

Summarizing is the headline act, but the same panel does three related jobs that make it stick as a daily tool.

### Ask the window questions instead of just summarizing

A summary tells you what a document says; follow-up questions tell you what *you* need from it. With the panel open, just type: *"Does this contract clause contradict the email above it?"*, *"Which of these 90 comments actually answer the question?"*, *"What am I agreeing to in this terms page?"* Because every answer is grounded in the live window rather than a chatbot's guess, it doubles as a reading assistant — it can quote the exact line you're asking about.

<img src="{{ '/assets/images/screenshots/macos/08_chat_about_screen_panel.jpg' | relative_url }}" alt="Chat Screen panel discussing the current window's content in Arc for Mac" width="1200" height="715" loading="lazy" />

### Smart Extract: structure instead of prose

Sometimes you don't want a paragraph — you want the data. **Smart Extract** pulls dates, names, prices, and action items out of a messy window into a clean list: an event page becomes every date and venue, a job posting becomes a requirements checklist, an invoice becomes line items. One press, from any app.

### Flashcards for students

If the window is study material — lecture notes, a paper, a textbook chapter — Arc can turn it into a **flashcard deck** you cycle through before the exam. It starts from the same flow as a summary.

## Other Ways to Summarize Text on macOS

Arc isn't the only option, and on a recent Mac you may not need it. Here's what else works.

### Apple Intelligence Writing Tools (M1 and later, macOS 15.1+)

If your Mac has an M-series chip and runs macOS 15.1 or newer, this is the built-in option:

1. Select the text — in an article, a document, a draft, anywhere you can highlight.
2. Right-click the selection and choose **Writing Tools**.
3. Click **Summarize**, or **Key Points** for a bulleted digest, or **Table** if the source is structured.

It works well on prose, runs much of its processing on-device, is free, and shows up in most apps with text. The limits are coverage rather than quality: no Intel Mac gets it, availability also depends on region, and it only sees the text you selected — not the whole window, and with no saved history or follow-up chat.

### The old Summarize service

Before Apple Intelligence, macOS had a Summarize service. On some older versions you may still find it under **System Settings → Keyboard → Keyboard Shortcuts → Services → Text**, where enabling it adds a *Summarize* item for selected text in apps like TextEdit, with a slider for length. Apple deprecated it long ago and pulled the Safari entry point; treat it as a curiosity, not a 2026 answer.

### Everything else

- **ChatGPT or Claude** is the better choice for deep work on one long document — you can upload the whole file and have an extended conversation about it. For quick summaries of whatever is on screen, the copy-paste step adds up.
- **QuillBot and web-based summarizer sites** mean uploading your text every time — awkward for PDFs, worse for anything confidential.
- **Safari Reader and read-later extensions** clean up a page, and some add digests, but they live in the browser. The moment your text is in Preview, Mail, or Slack, they're gone.

### Which method fits which job

- **Occasional summaries on an M1 or newer Mac:** Writing Tools is free and good enough — right-click, Summarize, done.
- **Long reports you'll study in depth:** upload the file to ChatGPT or Claude.
- **An Intel Mac, or macOS 14:** Arc is the option that runs system-wide summarization on the machine you already own; an Intel MacBook Pro from 2019 runs it the same as an M3.
- **Text in Preview, Mail, or Slack:** only a window-level tool sees those, without selecting anything first.
- **Summaries you want to keep:** Arc's Library holds every digest; chatbots and Writing Tools forget instantly.

An honest limit: Arc summarizes the window in front of you, not two documents at once — cross-referencing means two invocations. And it needs a connection, since the models run server-side.

## Tips for Better Summaries

- **Summarize, then interrogate.** The summary is the table of contents; the follow-up questions are where the value is.
- **Bind custom summaries to hotkeys.** I keep one called *Executive brief* — "Summarize the screen as ten bullets, bold the deadlines, note every number" — bound to its own key. It took two minutes to write.
- **Save ruthlessly, search later.** Saved summaries are more findable than browser history.
- **Use read-aloud for the backlog.** When you'd rather hear a window than read it, the [AI Summary & Reader](/ai-summary-reader/) toolkit includes natural-voice read-aloud of whatever's on screen.

## FAQ

**How do I summarize text on a MacBook?**
On an M1 or newer MacBook running macOS 15.1+, select text and right-click → Writing Tools → Summarize. On any Mac with macOS 14 or later — Intel included — install Arc, grant Accessibility permission, press **Control+Space** over any window with text, and choose Summarize. The summary appears in a floating panel in a few seconds, with no copy-pasting and no tab-switching.

**Can I summarize a PDF on Mac with AI?**
Yes. Open the PDF in Preview (or any reader), press Control+Space, and pick Summarize. Arc reads the document directly, so there's no uploading or exporting, and you can ask follow-up questions about specific sections of the PDF afterward.

**Is there a free AI summarizer for Mac?**
Apple Intelligence's Writing Tools is free on supported Macs. Arc is free to start, with 7 requests per week — the floating panel, summaries, and follow-up questions work on the free tier. Paid plans add higher limits and extras like Drive backup, and one subscription covers the Mac, Windows and Android apps.

**Do I need a browser extension to summarize web pages on Mac?**
No. Arc is a system-wide app, not an extension — it reads the frontmost window through macOS accessibility APIs, so it works in Safari, Chrome, and every other app without installing anything per-browser and without any extension permissions to audit.

**What happened to the Summarize feature in Safari?**
Apple removed it years ago — the Summarize service behind it was deprecated, and current macOS versions don't rely on it. Apple Intelligence's Writing Tools is the official successor, on M-series Macs only.

**Does Apple Intelligence already do this on Mac?**
Apple Intelligence can summarize text in supported apps on newer Macs, but it's brief, hardware-dependent, and has no library or follow-up chat. If you have a compatible Mac, try both — Arc adds saved summaries, custom prompts, and grounded Q&A about the window in front of you.

---

**Download Arc for Mac free from [arcassistant.app/macos/](/macos/)**, grant one permission, and try Control+Space on whatever tab you've been avoiding. If you live on Android too, [Arc for Android](/android/) is on [Google Play](https://play.google.com/store/apps/details?id=com.rethink.arc) with the same account and subscription.

<!-- sources -->
*Further reading: [Apple's Accessibility framework](https://developer.apple.com/documentation/accessibility) · [Google's Gemini developer docs](https://ai.google.dev/).*
