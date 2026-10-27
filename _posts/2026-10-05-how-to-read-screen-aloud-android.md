---
layout: blog
title: "How to Make Android Read the Screen Aloud (4 Ways)"
description: "Four ways to have Android read text aloud: TalkBack, Select to Speak, Chrome Read Aloud and Arc. Covers PDFs, background playback and listening later."
date: 2026-10-05
last_modified_at: 2026-10-27
author: Mamata
tags: ["android", "ai", "accessibility", "text-to-speech"]
keywords: "read screen aloud android, android screen reader, read pdf aloud android, select to speak"
og_image: /assets/images/og-post-how-to-read-screen-aloud-android.png
faq:
  - question: "How do I get my Android phone to read text aloud for free?"
    answer: "Three free options ship with Android: Select to Speak (Settings → Accessibility), Chrome Read Aloud (select text → three dots → Read aloud), and TalkBack for a full screen reader. Arc's sidebar is also free to start and covers any app, not just Chrome."
  - question: "How do I read a PDF aloud on Android?"
    answer: "Open the PDF in the viewer you already use. Select to Speak reads the visible text, and on Pixel and Samsung builds it can OCR images too. Arc reads whatever is rendered on screen, so it also works in Drive or Adobe's viewer without converting or uploading the file; Smart Extract cleans up broken PDF columns first."
  - question: "How can I read the screen aloud without Select to Speak's floating button?"
    answer: "In Chrome, select text and choose Read aloud. In any other app, Arc's sidebar Read action reads the on-screen text directly, with no selection needed."
  - question: "Can it read other languages?"
    answer: "Arc detects the language of the content on-device and picks a matching voice, across 100+ languages including Hindi, Spanish, Chinese and Arabic. You can pin a default voice in Speech Settings if you'd rather choose manually."
  - question: "Can it read text inside images or screenshots?"
    answer: "Yes. Select to Speak OCRs images on most recent devices, and Arc reads what is rendered on screen, including scanned PDFs and app interfaces that don't allow copy and paste."
  - question: "Why are my Bluetooth headphones silent during reads?"
    answer: "Audio routes to the connected device. If nothing plays, either your headphones took over the output or media volume is at zero. Raise media volume (not ringer) or disconnect Bluetooth, then replay."
  - question: "Can I save what it read for later?"
    answer: "In Arc, saved items, summaries and extracts land in the built-in library. In the Unread Queue, tap the speaker icon on any saved item to hear it, with playback continuing in the background."
  - question: "Does this work on Mac too?"
    answer: "Arc's Mac app runs the same reading, summarizing and rewriting features behind a Control+Space overlay."
---

There are four realistic ways to make an Android phone read the screen aloud: **Select to Speak**, **Chrome's Read Aloud**, **TalkBack**, and a screen-aware app like **Arc**. Three are built in and free. They solve different problems, so here is which one fits which job and how to set each up in a couple of minutes.

A disclosure up front: I build [Arc](/), so weigh my take on it accordingly. The built-in tools are genuinely good, and for plenty of people they are all you need.

## The three built-in options

Try these before installing anything. They differ in setup effort, which apps they cover, and how much they change the way your phone behaves.

### Select to Speak: tap or drag to hear specific text

Select to Speak reads the parts of the screen you point at, not the whole interface. It works on any Android 9+ phone from Samsung, Pixel, Xiaomi, Motorola and most others.

Setup, once:

1. Open **Settings → Accessibility → Installed apps** (some phones list it directly as **Select to Speak**).
2. Turn it on and allow the shortcut.
3. Accept the permission prompts: screen access so it can read text, plus the floating control.

Use, every time:

- Tap the control, then tap any text to hear that line.
- Drag a box over a paragraph or card to hear the whole block.
- Play, pause and skip controls appear while it reads, and each sentence highlights as it's spoken.

**Good:** no install, works in nearly every app, reads photos and screenshots with OCR on most devices.
**Not so good:** the floating button sits on top of everything, you get the system TTS voice only, and it takes a tap or two every time. Great for occasional use; tiring as a daily habit.

### Chrome Read Aloud: best for web articles

If "the screen" mostly means web pages, Chrome has a listener built in:

1. Long-press text until Chrome highlights it.
2. Tap the **three dots** in the selection menu.
3. Tap **Read aloud**. Chrome reads the page with sentence highlighting and speed controls.

On some versions it's the overflow menu → **Listen** instead. Same reader either way.

This is the cleanest option for articles: no accessibility mode, no floating button. The limit is that it only works in Chrome. News apps, email, PDF viewers and other apps are out of reach.

### TalkBack: full hands-free navigation

TalkBack is Android's complete screen reader, designed for blind and low-vision users:

1. **Settings → Accessibility → TalkBack**, turn it on.
2. Navigation changes immediately: swipe to move between items, double-tap to activate, two fingers to scroll.
3. TalkBack announces whatever is under your finger, and its reading controls jump by heading or paragraph.

Know what you're switching on. TalkBack changes every gesture on the phone while it's active, which is right for deep accessibility needs and frustrating if you only want an article read to you now and then. For occasional listening, use Select to Speak.

### What about Speechify, NaturalReader and ElevenReader?

These import-based readers have excellent voices and work well for books and long documents you plan to listen to. You share a link or upload a PDF into their library, and they read from there. For "the thing I'm looking at right now," the share-wait-switch-find-your-place loop adds friction, and free tiers cap listening time.

## Reading any app aloud with Arc

Arc is a floating sidebar that sits above every app: Chrome, Gmail, WhatsApp, PDF viewers, news apps, in-app browsers. Its Read action takes the text currently on screen, so it works even in apps that don't allow text selection, and you never copy, share or upload anything.

<img src="{{ '/assets/images/screenshots/01_floating_sidebar_expanded_over_chrome.jpg' | relative_url }}" alt="Arc floating sidebar expanded over a Chrome article, with read aloud and summarize actions one tap away" width="800" height="1760" loading="lazy" />

Setup takes about two minutes:

1. **Install Arc** from [Google Play](https://play.google.com/store/apps/details?id=com.rethink.arc) (details on the [Arc for Android](/android/) page).
2. **Grant two permissions.** Screen access lets Arc read text from other apps when you tap; it doesn't watch the screen in the background. Display over other apps puts the sidebar one swipe away.
3. **Open whatever you want to hear**: an article, an email thread, a PDF.
4. **Swipe in the sidebar and tap Read.** Arc captures the visible text, detects its language and starts reading.
5. **Adjust and save.** Speed and voice are in the player; anything worth keeping goes to your library.

<img src="{{ '/assets/images/screenshots/00_home_screen_dashboard.jpg' | relative_url }}" alt="Arc home screen dashboard showing saved summaries, extracted items, and library tools" width="800" height="1760" loading="lazy" />

### Reading a PDF aloud

You don't need to convert or upload a PDF. Open it in Drive, Adobe or any viewer, swipe in the sidebar and tap Read. Arc reads what's rendered on screen, which also covers scanned pages. If the PDF has columns or tables that come out jumbled, run **Smart Extract** first to get clean text, then listen to that.

### Voice, speed and background playback

In **Settings → Speech Settings**, set the rate from 0.5x to 2x, adjust pitch and preview before saving. Auto voice selection is on by default, so a Hindi article gets a Hindi voice and a German contract a German one, across 100+ languages.

Then leave the app. Playback continues in the background, with play, pause and stop in the notification, on the lock screen and on headset buttons. At 1.5x, a 3,000-word article takes about 13 minutes instead of 20.

### Summarize first when time is short

For long or dense text, tap **AI Summary** in the sidebar, then press **Listen** on the summary. You hear a short version in under a minute and can decide whether the full piece is worth it. Summaries stay in the [AI Summary & Reader](/ai-summary-reader/) library for later.

<img src="{{ '/assets/images/screenshots/02_ai_summary_result.jpg' | relative_url }}" alt="Arc AI summary result panel with key points generated from the on-screen article" width="800" height="1760" loading="lazy" />

### A listen-later queue

When you find something you want to hear but not right now:

1. Open the sidebar and tap **Save**. It goes to the Unread Queue on Arc's home screen.
2. Later, tap the speaker icon on any saved item to hear it straight away.
3. Keep browsing the queue while audio plays and line up the next item.

A 20-minute commute at 1.5x clears two or three saved articles.

<img src="{{ '/assets/images/screenshots/00_summary_library_with_items.jpg' | relative_url }}" alt="Saved summary library in Arc with items ready to listen" width="800" height="1760" loading="lazy" />

## Which one should you use?

| Situation | Best tool |
|---|---|
| One paragraph you're pointing at, occasionally | Select to Speak |
| Web articles only | Chrome Read Aloud |
| Full non-visual phone navigation | TalkBack |
| Books or long documents you plan to listen to | Speechify or ElevenReader |
| Articles, emails and PDFs in any app, with summaries and a queue | Arc |

They also combine well: plenty of people keep Select to Speak for quick taps and use Arc for long reads.

## Who benefits most

- **Commuters and walkers** who want their reading in their ears with the phone in a pocket.
- **People with dyslexia, low vision or eye strain**, for whom adjustable speed and natural voices make long text manageable.
- **Language learners and multilingual readers**, since automatic language detection handles mixed-language feeds without touching settings.

If you'd rather rewrite text than read it, the same sidebar has an [AI Writer](/ai-writer/). On a Mac, the same reading features run behind Control+Space; see [Arc for Mac](/macos/).

## FAQ

### How do I get my Android phone to read text aloud for free?

Three free options ship with Android: Select to Speak (Settings → Accessibility), Chrome Read Aloud (select text → three dots → Read aloud), and TalkBack for a full screen reader. Arc's sidebar is also free to start and covers any app, not just Chrome.

### How do I read a PDF aloud on Android?

Open the PDF in the viewer you already use. Select to Speak reads the visible text, and on Pixel and Samsung builds it can OCR images too. Arc reads whatever is rendered on screen, so it also works in Drive or Adobe's viewer without converting or uploading the file; Smart Extract cleans up broken PDF columns first.

### How can I read the screen aloud without Select to Speak's floating button?

In Chrome, select text and choose Read aloud. In any other app, Arc's sidebar Read action reads the on-screen text directly, with no selection needed.

### Can it read other languages?

Arc detects the language of the content on-device and picks a matching voice, across 100+ languages including Hindi, Spanish, Chinese and Arabic. You can pin a default voice in Speech Settings if you'd rather choose manually.

### Can it read text inside images or screenshots?

Yes. Select to Speak OCRs images on most recent devices, and Arc reads what is rendered on screen, including scanned PDFs and app interfaces that don't allow copy and paste.

### Why are my Bluetooth headphones silent during reads?

Audio routes to the connected device. If nothing plays, either your headphones took over the output or media volume is at zero. Raise media volume (not ringer) or disconnect Bluetooth, then replay.

### Can I save what it read for later?

In Arc, saved items, summaries and extracts land in the built-in library. In the Unread Queue, tap the speaker icon on any saved item to hear it, with playback continuing in the background.

### Does this work on Mac too?

Arc's Mac app runs the same reading, summarizing and rewriting features behind a Control+Space overlay. Details on [Arc for Mac](/macos/).

<!-- sources -->
*Further reading: [Android text-to-speech settings](https://support.google.com/accessibility/android/answer/6006983) · [Android's Select to Speak](https://support.google.com/accessibility/android/answer/7349565).*
