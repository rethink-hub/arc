---
layout: blog
title: "Arc for Mac Is Here — Your AI Screen Assistant, Now on macOS"
description: "Arc for Mac is out. Press Control + Space anywhere in macOS to summarize, read aloud, chat, or rewrite whatever is on your screen. Free to start, notarized by Apple, and it syncs with Arc on Android."
date: 2026-09-06
author: Rethink
tags: ["macos", "arc-for-mac", "release", "ai-assistant", "productivity"]
og_image: /assets/images/og-macos.png
---

Arc started on Android as a floating sidebar that could read whatever was on your screen and do something useful with it. The most common piece of feedback I got, over and over, was some version of the same sentence: *"I want this on my Mac."*

It's here. **Arc for Mac is available today**, and you can [download it now]({{ '/macos/' | relative_url }}).

## What It Actually Does

Press **⌃ Space** — Control and Space — anywhere in macOS. A Spotlight-style panel appears over whatever you're working on, with your actions in it. Pick one. Arc reads the window you were just in, does the thing, and gets out of your way. Press **Esc** to dismiss.

That's the whole interaction model. No tab switching, no copy-paste, no "paste your text here" box.

What you can run on that screen:

- **AI Summary** — a long Safari page, a PDF open in Preview, a thread in Mail, a wall of Slack messages. Summarized without leaving the app.
- **AI Text Reader** — listen to any article or document with macOS's natural text-to-speech voices.
- **AI Chat** — ask follow-up questions about the window in front of you.
- **AI Writer** — rewrite, reply, translate, or polish text directly inside whatever app you're typing in. It puts the result back in the field you were editing.
- **Smart Extract** — pull dates, contacts, key points, and action items out of a screen and drop them somewhere useful.
- **Custom Actions** — write your own prompt once, bind it to a global hotkey, and stop retyping the same instruction every day.
- **500+ Community Actions** — ready-made actions shared by other Arc users, installable in a click.

There's also a real app window, not just a menu bar popup. It holds your Library of saved summaries, your custom actions, the Info Vault of personal snippets that AI Writer can reference, and settings.

## Why I Built It This Way

Nearly every AI tool on the desktop makes you *bring the text to the AI*. You select, you copy, you switch to a browser tab or a chat window, you paste, you ask, you copy the answer, you switch back, you paste again.

Six steps for something that should be one.

Arc inverts it. The AI comes to the screen you're already looking at. On macOS that's built on the system accessibility APIs — the same ones VoiceOver uses — which is what lets Arc read the content of the frontmost window in any app, whether or not that app has an AI feature of its own.

Crucially: **only when you invoke an action.** Arc doesn't read your screen in the background, doesn't watch you type, and isn't a keylogger. It wakes up when you press the hotkey and goes back to sleep when it's done. Password managers are skipped automatically.

## It Talks to the Android App

If you already use Arc on Android, sign in on the Mac and your saved content, your custom actions, and your subscription carry across. One account, both devices. Write a custom action on your laptop, use it on your phone.

Google Drive backup is there too, optionally, if you want to move your library to another Mac.

## Free to Start

Same model as Android: **7 free requests per week** on the basic features, no account required, no ads, no trial that quietly expires. If you only reach for Arc occasionally, you may never need to pay for it.

Premium unlocks unlimited use, and if you're already subscribed on Android, you're already subscribed here. It's the same subscription, not a second one.

## Notarized, and Not on the Mac App Store

Arc for Mac is signed with an Apple Developer ID and notarized by Apple, so it installs without the "unidentified developer" warning. It updates itself through a cryptographically signed update feed — you'll get new versions automatically without hunting for a download link.

It is not on the Mac App Store, and it can't be. App Store apps must run inside Apple's App Sandbox, and the sandbox specifically forbids the accessibility APIs that let one app read another app's window. Those APIs *are* Arc. Shipping through the App Store would mean shipping an app that can't do the one thing it exists to do.

So it's distributed straight from this site instead — with Apple's notarization and a signed auto-updater doing the same job the App Store's review would, minus the restriction that breaks the product.

## Getting Started

1. [Download the DMG]({{ '/macos/' | relative_url }}) and drag **Arc** into your Applications folder.
2. Launch it. Onboarding will ask for **Accessibility** permission, which is how Arc reads the active window. Screen Recording is optional and only needed for screenshot-based actions.
3. Press **⌃ Space** and try it on whatever's already open.

You can change the shortcut in Settings if Control + Space is spoken for on your machine.

## What It Runs On

macOS 14 (Sonoma) or later. It's a universal binary, so it runs natively on both Apple Silicon and Intel Macs — no Rosetta, no separate download to pick between.

It ships in 10 languages: English, Spanish, German, Portuguese (Brazil and Portugal), French, Korean, Indonesian, Japanese, and Arabic.

## Still Just Me

Arc is built by one person. Every Swift file in the Mac app, every Kotlin file in the Android app, every reply to a support email — same guy.

That means the Mac version will get better in the direction users actually push it. If something is broken, awkward, or missing, tell me and it lands in the next build rather than in a backlog three quarters deep.

[Get Arc for Mac →]({{ '/macos/' | relative_url }})

---

*Arc is also available on [Android]({{ '/android/' | relative_url }}). [iOS]({{ '/ios/' | relative_url }}) and [Windows]({{ '/windows/' | relative_url }}) are on the way.*
