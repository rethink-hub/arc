---
layout: default
title: "AI Assistant for iPhone — Works in Any App | Arc"
description: "An AI assistant for iPhone that works on the screen you're already on — summarize, listen, rewrite, automate. In development; Android ships today."
keywords: "ai assistant for iphone, iphone ai assistant, ai assistant ios, ios ai screen assistant, iphone ai summary app, iphone text to speech ai"
platform: ios
robots: noindex, follow
og_image: /assets/images/og-ios.png
faq:
  - question: "Is there an AI assistant for iPhone that works inside other apps?"
    answer: "Arc is building one. It summarizes, reads aloud, rewrites and extracts from the screen you're already on, rather than making you paste text into a chatbot. The iPhone version is in development; the same app ships on Android today and on macOS."
  - question: "When will Arc for iOS be available?"
    answer: "Arc for iOS is in development with no announced date. iOS restricts background screen access far more tightly than Android, so the iPhone version is being built around Share Sheet, Shortcuts and keyboard extensions instead of a floating overlay. Join the waitlist to be emailed when the beta opens."
  - question: "Why can't Arc for iPhone use a floating sidebar like Android?"
    answer: "iOS does not permit apps to draw over other apps or read their content in the background — that is an Android capability Apple deliberately does not expose. Arc for iPhone will use the system entry points Apple does provide: the Share Sheet, the Shortcuts app, an Action Button binding, and a custom keyboard for in-place rewriting."
  - question: "How much will Arc for iOS cost?"
    answer: "The same as every other platform: free for 7 requests per week on basic features, with a premium subscription for unlimited summaries, text-to-speech, AI chat and automation. No ads, no expiring trial."
  - question: "Can I use Arc on iPhone right now?"
    answer: "Not yet as a native app. Arc ships on Android, macOS and Windows today. If you use a Mac alongside your iPhone, the Mac app covers reading and writing on the desktop while the iPhone version is in development."
  - question: "Which is the best AI assistant for iPhone?"
    answer: "It depends on the job. ChatGPT and Claude are strong standalone chat apps, and Apple Intelligence covers system-level writing tools in the places Apple wires them in. The gap is an assistant that works on the screen you're already on — summarizing, reading aloud and rewriting inside the app you're using. That's the role Arc is building for."
  - question: "Which iPhone models will be supported?"
    answer: "The plan is recent iOS versions, including Action Button models. Exact hardware requirements will be confirmed at beta, and waitlist members hear first."
last_modified_at: 2026-09-19
---

<!-- Hero -->
<div class="coming-soon-hero">
  <div class="coming-soon-badge">Coming soon — in development</div>
  <div class="coming-soon-icon icon-ios" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.21-1.96 1.07-3.11-1.05.05-2.31.7-3.06 1.57-.67.78-1.25 2.04-1.09 3.27 1.17.09 2.37-.7 3.08-1.73z"/></svg>
  </div>
  <h1>AI Assistant for iPhone</h1>
  <p class="hero-subtitle">Summarize, listen to, rewrite and extract from whatever is on your screen — without pasting it into a chatbot first. In development for iPhone; shipping on Android today.</p>
  <form class="notify-form" action="mailto:everythingrethink@gmail.com?subject=Notify%20me%20when%20Arc%20for%20iOS%20is%20ready" method="post" enctype="text/plain">
    <input type="email" name="email" placeholder="Enter your email" aria-label="Email for Arc for iOS updates" required>
    <button type="submit" class="cta-button">Join the waitlist</button>
  </form>
</div>

---

<div class="content-section" markdown="1">

## What Arc for iPhone Will Be

Arc is an AI assistant that runs on the content you are already looking at. Open an article, a message thread, a PDF or a contract, invoke Arc, and it summarizes that screen, [reads it aloud](/text-to-speech/) in a natural voice, rewrites your draft reply, or pulls out the dates and contacts buried in it.

The iPhone version is in development, built around the entry points iOS allows (below). Meanwhile [Arc for Android](/android/) is live on Google Play and [Arc for Mac](/macos/) is available to download.

</div>

<!-- Screenshots (captured on Android; iOS will mirror these flows) -->
<div class="section-header">
  <span class="section-tag">What it looks like</span>
  <h2>The app, running today on Android.</h2>
  <p>Screenshots from the shipping Android app. The iPhone version will follow these flows with native iOS patterns.</p>
</div>

<div class="shot-gallery shot-gallery--phone">
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img width="800" height="1760" src="{{ '/assets/images/screenshots/01_floating_sidebar_expanded_over_chrome.jpg' | relative_url }}" alt="Arc floating sidebar expanded over a Chrome browser window on Android" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>Invoke from any app.</strong> On Android this is a floating sidebar; on iPhone it will be the Share Sheet, Shortcuts and the Action Button.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img width="800" height="1760" src="{{ '/assets/images/screenshots/02_ai_summary_result.jpg' | relative_url }}" alt="Arc AI summary result showing numbered key points from an article" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>AI Summary.</strong> Numbered key points from the screen. See <a href="{{ '/ai-summary-reader/' | relative_url }}">AI summary &amp; reader</a>.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img width="800" height="1760" src="{{ '/assets/images/screenshots/03_ai_writer_reply_mode.jpg' | relative_url }}" alt="Arc AI Writer in reply mode generating a message response" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>AI Writer.</strong> Replies, rewrites and grammar fixes in the app you're typing in. See <a href="{{ '/ai-writer/' | relative_url }}">AI writer</a>.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img width="800" height="1760" src="{{ '/assets/images/screenshots/10_smart_extract_results.jpg' | relative_url }}" alt="Arc Smart Extract results listing dates, contacts and action items from a screen" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>Smart Extract.</strong> Dates, contacts, codes and tasks pulled out with a button that acts on each. See <a href="{{ '/ai-summary-reader/' | relative_url }}">AI summary and extract</a>.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img width="800" height="1760" src="{{ '/assets/images/screenshots/06_custom_actions_list_with_active_actions.jpg' | relative_url }}" alt="List of custom AI actions configured in Arc for Android" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>Custom actions.</strong> Your own prompts as one-tap commands, plus 500+ community actions. See AI workflow automation.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img width="800" height="1760" src="{{ '/assets/images/screenshots/09_flashcards_viewer_question.jpg' | relative_url }}" alt="Arc flashcard viewer showing a generated study question" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>Flashcards.</strong> Any page of study material becomes a reviewable deck. See AI flashcards.</figcaption>
  </figure>
</div>

---

<!-- Cross platform CTA -->
<div class="coming-soon-section">
  <h2>Available now on Android, Mac and Windows</h2>
  <p>Arc for iPhone is in development. The same app is shipping on three platforms today.</p>
  <div class="platform-links">
    <a href="{{ '/android/' | relative_url }}">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.523 15.3414c-.566 0-1.027-.478-1.027-1.068 0-.591.461-1.069 1.027-1.069.567 0 1.028.478 1.028 1.069 0 .59-.461 1.068-1.028 1.068zm-11.046 0c-.567 0-1.028-.478-1.028-1.068 0-.591.461-1.069 1.028-1.069.566 0 1.027.478 1.027 1.069 0 .59-.461 1.068-1.027 1.068zm11.4-6.12l1.997-3.459a.433.433 0 00-.158-.591.438.438 0 00-.593.156l-2.022 3.502c-1.515-.69-3.205-1.078-4.984-1.078-1.75 0-3.414.374-4.908 1.043L5.355 5.155a.437.437 0 00-.593-.156.433.433 0 00-.158.591l2.006 3.46C2.95 11.479.5 15.096.5 19.245h23c0-4.149-2.45-7.766-5.623-10.024z"/></svg>
      Get Arc for Android
    </a>
    <a href="{{ '/macos/' | relative_url }}">Arc for Mac</a>
    <a href="{{ '/windows/' | relative_url }}">Arc for Windows</a>
  </div>
</div>

<div class="content-section" markdown="1">

## Why iOS Is Harder Than Android

An iPhone app cannot draw over another app or read its content in the background — a platform decision by Apple, and the reason no true screen-reading AI assistant exists on iOS from anyone. So Arc for iPhone is being built around the openings Apple does provide:

- **Share Sheet** — send the current page, PDF, image or selection into Arc from any app, which covers Safari, Mail, Files, Messages and most third-party apps.
- **Shortcuts, Back Tap and the Action Button** — bind a custom Arc action to the side button on iPhone 15 Pro and later, to a double Back Tap, or to any Shortcuts automation.
- **A custom keyboard** — rewrite, reply and fix grammar in place, in whatever field you're typing in.
- **Widgets and App Intents** — surface the Saved Items library and one-tap actions without opening the app.

It reaches the same features with one extra tap, and it can actually ship on the App Store. Saved items sync, so anything you capture with [Arc for Mac](/macos/) now will be there when the iPhone app arrives. For how content is handled, see private AI assistant.

### What day one should look like

1. Reading a 4,000-word report in Safari: tap Share → Arc and get a summary in about twenty seconds, with the option to listen to it on your commute.
2. A client email needs a reply between meetings: select the thread, invoke Arc, and pick from three drafted replies in different tones.
3. An address, price or recipe on screen: one action saves it to your Info Vault, so it's findable later without a screenshot.
4. Double Back Tap: Arc summarizes whatever you were just reading — the closest iOS allows to Android's always-there sidebar.

## Arc for iOS FAQ

### Is there an AI assistant for iPhone that works inside other apps?

Arc is building one. It summarizes, reads aloud, rewrites and extracts from the screen you're already on, rather than making you paste text into a chatbot. The iPhone version is in development; the same app ships on Android today and on macOS.

### When will Arc for iOS be available?

Arc for iOS is in development with no announced date. iOS restricts background screen access far more tightly than Android, so the iPhone version is being built around Share Sheet, Shortcuts and keyboard extensions instead of a floating overlay. Join the waitlist to be emailed when the beta opens.

### Why can't Arc for iPhone use a floating sidebar like Android?

iOS does not permit apps to draw over other apps or read their content in the background — that is an Android capability Apple deliberately does not expose. Arc for iPhone will use the system entry points Apple does provide: the Share Sheet, the Shortcuts app, an Action Button binding, and a custom keyboard for in-place rewriting.

### How much will Arc for iOS cost?

The same as every other platform: free for 7 requests per week on basic features, with a premium subscription for unlimited summaries, text-to-speech, AI chat and automation. No ads, no expiring trial.

### Can I use Arc on iPhone right now?

Not yet as a native app. Arc ships on Android, macOS and Windows today. If you use a Mac alongside your iPhone, the Mac app covers reading and writing on the desktop while the iPhone version is in development.

### Which is the best AI assistant for iPhone?

It depends on the job. ChatGPT and Claude are strong standalone chat apps, and Apple Intelligence covers system-level writing tools in the places Apple wires them in. The gap is an assistant that works on the screen you're already on — summarizing, reading aloud and rewriting inside the app you're using. That's the role Arc is building for.

### Which iPhone models will be supported?

The plan is recent iOS versions, including Action Button models. Exact hardware requirements will be confirmed at beta, and waitlist members hear first.

</div>

{% include referral-handoff.html %}
