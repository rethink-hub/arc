---
layout: default
title: "AI Assistant for iPhone — Works in Any App | Arc"
description: "An AI assistant for iPhone that works on the screen you're already on — summarize, listen, rewrite, automate. In development; Android ships today."
keywords: "ai assistant for iphone, iphone ai assistant, ai assistant ios, ios ai screen assistant, iphone ai summary app, iphone text to speech ai"
platform: ios
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
    answer: "Not yet as a native app. Arc ships on Android and macOS today. If you use a Mac alongside your iPhone, the Mac app covers reading and writing on the desktop while the iPhone version is in development."
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

Arc is an AI assistant that runs on the content you are already looking at. Open an article, a message thread, a PDF or a contract, invoke Arc, and it summarizes that screen, reads it aloud in a natural voice, rewrites your draft reply, or pulls out the dates and contacts buried in it.

The iPhone version is in development and has no release date yet. The honest reason is below: iOS does not allow the floating overlay that makes the Android app work, so the iPhone build is being designed around the entry points Apple does provide. In the meantime [Arc for Android](/android/) is live on Google Play and [Arc for Mac](/macos/) is available to download.

</div>

<!-- Screenshots (captured on Android; iOS will mirror these flows) -->
<div class="section-header">
  <span class="section-tag">What it looks like</span>
  <h2>The app, running today on Android.</h2>
  <p>These are real screenshots from the shipping Android app — the same features the iPhone version is being built around. The iOS interface will follow native iPhone patterns, so expect these flows rather than these exact pixels.</p>
</div>

<div class="shot-gallery shot-gallery--phone">
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img src="{{ '/assets/images/screenshots/01_floating_sidebar_expanded_over_chrome.jpg' | relative_url }}" alt="Arc floating sidebar expanded over a Chrome browser window on Android" width="800" height="1760" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>Invoke from any app.</strong> On Android this is a floating sidebar; on iPhone it will be the Share Sheet, Shortcuts and the Action Button.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img src="{{ '/assets/images/screenshots/02_ai_summary_result.jpg' | relative_url }}" alt="Arc AI summary result showing numbered key points from an article" width="800" height="1760" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>AI Summary.</strong> Numbered key points from the screen, with listen, save and share on the result. See <a href="{{ '/ai-summary-reader/' | relative_url }}">AI summary &amp; reader</a>.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img src="{{ '/assets/images/screenshots/02_ai_summary_chat_input.jpg' | relative_url }}" alt="Arc chat input asking a follow-up question about a summarized screen" width="800" height="1760" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>Ask follow-ups.</strong> Keep questioning the same screen without re-explaining what you're looking at.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img src="{{ '/assets/images/screenshots/03_ai_writer_reply_mode.jpg' | relative_url }}" alt="Arc AI Writer in reply mode generating a message response" width="800" height="1760" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>AI Writer.</strong> Replies, rewrites and grammar fixes in the app you're typing in. See <a href="{{ '/ai-writer/' | relative_url }}">AI writer</a>.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img src="{{ '/assets/images/screenshots/10_smart_extract_results.jpg' | relative_url }}" alt="Arc Smart Extract results listing dates, contacts and action items from a screen" width="800" height="1760" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>Smart Extract.</strong> Dates, contacts, codes and tasks pulled out with a button that acts on each. See <a href="{{ '/smart-extract/' | relative_url }}">Smart Extract</a>.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img src="{{ '/assets/images/screenshots/06_custom_actions_list_with_active_actions.jpg' | relative_url }}" alt="List of custom AI actions configured in Arc for Android" width="800" height="1760" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>Custom actions.</strong> Your own prompts, saved as one-tap commands. See <a href="{{ '/ai-workflow-automation/' | relative_url }}">AI workflow automation</a>.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img src="{{ '/assets/images/screenshots/07_community_actions_browse_with_filter.jpg' | relative_url }}" alt="Browsing community-shared AI actions in Arc with a category filter" width="800" height="1760" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>Community actions.</strong> 500+ ready-made actions from other Arc users, installable in a tap.</figcaption>
  </figure>
  <figure class="shot">
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-screen">
        <img src="{{ '/assets/images/screenshots/09_flashcards_viewer_question.jpg' | relative_url }}" alt="Arc flashcard viewer showing a generated study question" width="800" height="1760" loading="lazy">
        <div class="iphone-reflection"></div>
      </div>
    </div>
    <figcaption><strong>Flashcards.</strong> Any page of study material becomes a reviewable deck. See <a href="{{ '/flashcards/' | relative_url }}">AI flashcards</a>.</figcaption>
  </figure>
</div>

---

<!-- Feature teaser -->
<div class="section-header">
  <span class="section-tag">Planned for iPhone</span>
  <h2>What will ship on iOS.</h2>
  <p>Same feature set, reached through the entry points iOS actually allows.</p>
</div>

<div class="coming-soon-features">
  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-icon icon-summary" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L14 9L21 12L14 15L12 22L10 15L3 12L10 9L12 2Z"/></svg>
      </div>
      <h3>Summarize on Tap</h3>
      <p>Condense long articles, messages and web pages from the Share Sheet in Safari or any app.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-reader" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5L6 9H2V15H6L11 19V5Z"/><path class="wave-1" d="M15.54 8.46C16.48 9.4 17 10.62 17 12C17 13.38 16.48 14.6 15.54 15.54"/><path class="wave-2" d="M19.07 4.93C20.95 6.81 22 9.28 22 12C22 14.72 20.95 17.19 19.07 19.07"/></svg>
      </div>
      <h3>Listen Anywhere</h3>
      <p>Natural iOS voices read text aloud in any language while you multitask. See <a href="{{ '/text-to-speech/' | relative_url }}">AI text to speech</a>.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-writer" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20H21"/><path d="M16.5 3.5C16.8978 3.10217 17.4374 2.87868 18 2.87868C18.5626 2.87868 19.1022 3.10217 19.5 3.5C19.8978 3.89782 20.1213 4.43739 20.1213 5C20.1213 5.56261 19.8978 6.10217 19.5 6.5L7 19L3 20L4 16L16.5 3.5Z"/></svg>
      </div>
      <h3>Write in Any App</h3>
      <p>A custom keyboard rewrites replies and fixes grammar in place, wherever you're typing.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-actions" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14H12L11 22L21 10H12L13 2Z"/></svg>
      </div>
      <h3>One-Tap Actions</h3>
      <p>Run custom AI commands from the Action Button, a Shortcuts automation, or a Home Screen widget.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-chat" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5C21.0034 12.82 20.6951 13.12 20.12 14.3C19.3875 15.82 18.2056 17.05 16.72 17.83C15.2344 18.61 13.5465 18.9 11.88 18.66C11.48 18.6 11.09 18.53 10.7 18.43C9.6333 18.86 8.44083 19.08 7.22 19.08C6.87 19.08 6.53 18.93 6.29 18.68C6.04 18.44 5.9 18.1 5.9 17.74V15.6C4.76 14.36 4.08 12.79 4.08 11.08C4.08 8.35 6.27 5.99 9.01 5.61C9.49 2.61 12.13 0.25 15.34 0.25C18.91 0.25 21.8 3.14 21.8 6.71C21.8 8.37 21.1 9.87 19.97 10.97"/></svg>
      </div>
      <h3>Chat About Content</h3>
      <p>Ask follow-up questions about the page or document you just shared into Arc.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-privacy" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
      </div>
      <h3>Smart Extract</h3>
      <p>Pull dates, contacts, codes and action items from any screen, each with a button that uses it.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-community" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21V19C17 17.9391 16.5786 16.9217 15.8284 16.1716C15.0783 15.4214 14.0609 15 13 15H5C3.93913 15 2.92172 15.4214 2.17157 16.1716C1.42143 16.9217 1 17.9391 1 19V21"/><circle cx="9" cy="7" r="4"/><path d="M23 21V19C23 18.22 22.81 17.48 22.46 16.82C22.11 16.16 21.64 15.58 21.06 15.13"/><path d="M16 3.13C16.64 3.58 17.11 4.16 17.46 4.82C17.81 5.48 18 6.22 18 7C18 7.78 17.81 8.52 17.46 9.18C17.11 9.84 16.64 10.42 16 10.87"/></svg>
      </div>
      <h3>500+ Community Actions</h3>
      <p>The same shared action catalog Android and Mac users already draw from.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-summary" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L14 9L21 12L14 15L12 22L10 15L3 12L10 9L12 2Z"/></svg>
      </div>
      <h3>Flashcards</h3>
      <p>Turn study material into decks you can review on the phone you already carry.</p>
    </div>
  </div>
</div>

---

<!-- Cross platform CTA -->
<div class="coming-soon-section">
  <h2>Available now on Android and Mac</h2>
  <p>Arc for iPhone is in development. The same app is shipping on two platforms today.</p>
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

On Android, Arc draws a floating sidebar over other apps and reads their content through the accessibility service. That is a capability Android grants and iOS deliberately does not. An iPhone app cannot draw over another app, and it cannot read another app's content in the background. No amount of engineering gets around that — it is a platform decision by Apple, and it is the reason there is no true screen-reading AI assistant on iOS from anyone.

So Arc for iPhone is being built around the openings Apple does provide:

- **Share Sheet** — send the current page, PDF, image or selection into Arc from any app, which covers Safari, Mail, Files, Messages and most third-party apps.
- **Shortcuts and the Action Button** — bind a custom Arc action to the side button on iPhone 15 Pro and later, or to any Shortcuts automation.
- **A custom keyboard** — rewrite, reply and fix grammar in place, in whatever field you're typing in.
- **Widgets and App Intents** — surface the Saved Items library and one-tap actions without opening the app.

That is a genuinely different interaction model from Android's sidebar. It reaches the same features with one extra tap, and it's the version that can actually ship on the App Store.

### What you get on iPhone today

Nothing native yet. Two things do work now if you're in the Apple ecosystem: [Arc for Mac](/macos/) handles reading, summarizing and rewriting on the desktop with a Control+Space hotkey, and saved items sync so anything you capture on the Mac is there when the iPhone app arrives. If you also carry an Android device, [Arc for Android](/android/) is the complete product.

For a sense of what the reading and listening side feels like, the [AI summary and reader](/ai-summary-reader/) page covers it in detail, and [private AI assistant](/private-ai-assistant/) explains how content is handled.

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

Not yet as a native app. Arc ships on Android and macOS today. If you use a Mac alongside your iPhone, the Mac app covers reading and writing on the desktop while the iPhone version is in development.

</div>

{% include referral-handoff.html %}
