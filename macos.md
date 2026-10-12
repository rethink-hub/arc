---
layout: default
title: "AI Assistant for Mac — Free Download | Arc"
description: "Arc is an AI assistant for Mac that reads any window. Press Control+Space to summarize, listen, rewrite and automate in any app. Free download, macOS 14+."
keywords: "ai assistant for mac, mac ai assistant, macos ai assistant, ai screen assistant mac, mac ai summary app, mac text to speech ai, download ai assistant mac"
platform: macos
og_image: /assets/images/og-macos.png
product_page: true
faq:
  - question: "Is there an AI assistant for Mac that works in every app?"
    answer: "Arc does. Press Control+Space in any macOS app and Arc reads that window through the system accessibility APIs, then summarizes it, reads it aloud, rewrites your text or runs a prompt you wrote. It works in Safari, Chrome, Preview, Mail, Slack, Obsidian and anything else that puts text on screen."
  - question: "Is Arc for Mac free?"
    answer: "Yes. Arc is free with 7 requests per week on basic features, and a premium subscription unlocks unlimited summaries, text-to-speech, AI chat and workflow automation. One subscription covers Mac, Windows and Android."
  - question: "What are the system requirements for Arc on Mac?"
    answer: "macOS 14 (Sonoma) or later. Arc is a universal binary that runs natively on both Apple Silicon and Intel Macs, and it is code-signed with an Apple Developer ID and notarized by Apple, so it installs without security warnings."
  - question: "Why isn't Arc on the Mac App Store?"
    answer: "Arc reads on-screen content through the macOS accessibility APIs, which Apple's App Sandbox prohibits. Sandboxing is mandatory for Mac App Store apps, so Arc is distributed directly from this site — still notarized by Apple, and updated through a signed Sparkle update feed."
  - question: "Does Arc read my screen in the background?"
    answer: "No. Arc reads the frontmost window only when you invoke an action yourself. It is not a keylogger and it does not monitor continuously. Screenshots are captured only for actions that explicitly need one, and password managers are skipped automatically."
last_modified_at: 2026-09-19
---

<!-- Hero: text left, live interactive demo right (mirrors the Android homepage) -->
<div class="hero-section hero-with-live-demo">
  <div class="hero-content-row macos-hero-row">
    <div class="hero-text-col">
      <div class="coming-soon-badge status-live">Now available for macOS</div>
      <h1>Arc for Mac</h1>
      <p class="hero-subtitle">Your AI screen assistant, built for macOS. Summarize, read aloud, chat, and automate any window with a single shortcut.</p>
      <div class="hero-cta-group">
        <a href="{{ site.mac_app.dmg | relative_url }}" class="cta-button" download>
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.27 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.94 1.21-1.96 1.07-3.11-1.11.05-2.31.7-3.06 1.57-.67.78-1.25 2.04-1.09 3.27 1.17.09 2.37-.7 3.08-1.73z"/></svg>
          Download for Mac
        </a>
      </div>
      <ul class="hero-meta">
        <li>Free · v{{ site.mac_app.version }}</li>
        <li>macOS {{ site.mac_app.min_macos }}+</li>
        <li>Apple Silicon &amp; Intel</li>
        <li>Notarized by Apple</li>
      </ul>
      <a class="hero-alt-link" href="https://play.google.com/store/apps/details?id=com.rethink.arc" target="_blank" rel="noopener">Also on Android →</a>
    </div>
    <div class="hero-demo-col hero-demo-col--arc">
      {% include arc-interactive-demo.html %}
      <img class="demo-mobile-fallback" src="{{ '/assets/images/screenshots/macos/01_arc_menu_over_chrome.jpg' | relative_url }}" alt="Arc menu panel over Chrome on macOS, listing AI actions" width="1200" height="715" loading="lazy" decoding="async">
    </div>
  </div>
</div>

---

<div class="content-section" markdown="1">

## What Arc for Mac Is

Arc is an AI assistant for Mac that works on the window you're already in. Press **Control + Space**, a Spotlight-style panel appears over your current app, and every action runs against the text in that window — summarize it, read it aloud, rewrite your draft, chat about it, or pull the dates and contacts out of it.

Arc lives in the menu bar. Nothing is copied or pasted, and the panel is non-activating, so your cursor and focus stay where they were. The interface is available in 10 languages.

</div>

<div class="section-header">
  <span class="section-tag">What it looks like</span>
  <h2>Arc, running on a Mac.</h2>
</div>

<div class="shot-gallery">
  <figure class="shot">
    <img width="1200" height="715" src="{{ '/assets/images/screenshots/macos/01_arc_menu_over_chrome.jpg' | relative_url }}" alt="Arc menu panel floating over a Chrome window on macOS, listing AI actions" loading="lazy">
    <figcaption><strong>The Arc menu.</strong> Control+Space opens it over any app; the search field doubles as a prompt box.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="710" src="{{ '/assets/images/screenshots/macos/02_ai_summary_result_panel.jpg' | relative_url }}" alt="Arc AI Summary result panel with numbered key points from a web article on macOS" loading="lazy">
    <figcaption><strong>AI Summary.</strong> Numbered key points with title, category and source URL. See <a href="{{ '/ai-summary-reader/' | relative_url }}">AI summary &amp; reader</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="710" src="{{ '/assets/images/screenshots/macos/08_chat_about_screen_panel.jpg' | relative_url }}" alt="Arc chat panel answering a question about the content on screen on macOS" loading="lazy">
    <figcaption><strong>Chat about your screen.</strong> Follow-up questions on the document in front of you.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="637" src="{{ '/assets/images/screenshots/macos/03_ai_writer_rewrite_generated.jpg' | relative_url }}" alt="Arc AI Writer showing rewritten text ready to insert back into the field" loading="lazy">
    <figcaption><strong>AI Writer.</strong> Rewrite, reply or fix grammar, then Insert writes it back into the field. See <a href="{{ '/ai-writer/' | relative_url }}">AI writer</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="914" src="{{ '/assets/images/screenshots/macos/12_shortcut_recorder_listening.jpg' | relative_url }}" alt="Arc shortcut recorder waiting for a global hotkey to be pressed" loading="lazy">
    <figcaption><strong>Global hotkeys.</strong> Bind any action to a system-wide keystroke. See <a href="{{ '/ai-shortcuts/' | relative_url }}">AI shortcuts</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="780" src="{{ '/assets/images/screenshots/macos/06_arc_actions_create_form_empty.jpg' | relative_url }}" alt="Arc custom action creation form with a prompt template field on macOS" loading="lazy">
    <figcaption><strong>Your own actions.</strong> A prompt with a <code>{screen_text}</code> placeholder becomes a permanent command, or install one of 500+ community actions. See <a href="{{ '/ai-workflow-automation/' | relative_url }}">AI workflow automation</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="780" src="{{ '/assets/images/screenshots/macos/09_flashcards_decks_library.jpg' | relative_url }}" alt="Arc flashcard decks library on macOS" loading="lazy">
    <figcaption><strong>Flashcards.</strong> Turn a page of study material into a deck. See <a href="{{ '/flashcards/' | relative_url }}">AI flashcards</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="780" src="{{ '/assets/images/screenshots/macos/11_info_vault_with_entries.jpg' | relative_url }}" alt="Arc Info Vault storing reusable personal details for AI writing on macOS" loading="lazy">
    <figcaption><strong>Info Vault.</strong> Reusable details Arc drops into what it writes, stored locally. See <a href="{{ '/private-ai-assistant/' | relative_url }}">private AI assistant</a>.</figcaption>
  </figure>
</div>

---

<!-- Install steps -->
<div class="section-header">
  <span class="section-tag">Getting started</span>
  <h2>Up and running in a minute.</h2>
</div>

<div class="steps-container">
  <div class="step">
    <div class="step-number">1</div>
    <div class="step-title">Download &amp; Install</div>
    <p class="step-description">Open the <code>.dmg</code>, drag <strong>Arc</strong> into Applications, and launch it.</p>
  </div>

  <div class="step">
    <div class="step-number">2</div>
    <div class="step-title">Grant Accessibility</div>
    <p class="step-description">Lets Arc read the window you're working in. Screen Recording is only needed for screenshot-based actions.</p>
  </div>

  <div class="step">
    <div class="step-number">3</div>
    <div class="step-title">Press ⌃ Space</div>
    <p class="step-description">Open the Arc menu anywhere in macOS. You can change the shortcut in Settings.</p>
  </div>
</div>

---

<!-- Cross platform CTA -->
<div class="coming-soon-section">
  <h2>Also available on Android</h2>
  <p>One account: saved summaries, custom actions and your subscription carry across, with optional Google Drive backup.</p>
  <div class="platform-links">
    <a href="{{ '/android/' | relative_url }}">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.523 15.3414c-.566 0-1.027-.478-1.027-1.068 0-.591.461-1.069 1.027-1.069.567 0 1.028.478 1.028 1.069 0 .59-.461 1.068-1.028 1.068zm-11.046 0c-.567 0-1.028-.478-1.028-1.068 0-.591.461-1.069 1.028-1.069.566 0 1.027.478 1.027 1.069 0 .59-.461 1.068-1.027 1.068zm11.4-6.12l1.997-3.459a.433.433 0 00-.158-.591.438.438 0 00-.593.156l-2.022 3.502c-1.515-.69-3.205-1.078-4.984-1.078-1.75 0-3.414.374-4.908 1.043L5.355 5.155a.437.437 0 00-.593-.156.433.433 0 00-.158.591l2.006 3.46C2.95 11.479.5 15.096.5 19.245h23c0-4.149-2.45-7.766-5.623-10.024z"/></svg>
      Get Arc for Android
    </a>
    <a href="{{ '/ios/' | relative_url }}">Arc for iOS</a>
    <a href="{{ '/windows/' | relative_url }}">Arc for Windows</a>
  </div>
</div>

---

<div class="content-section" markdown="1">

## Arc for Mac FAQ

### Is there an AI assistant for Mac that works in every app?

Arc does. Press Control+Space in any macOS app and Arc reads that window through the system accessibility APIs, then summarizes it, reads it aloud, rewrites your text or runs a prompt you wrote. It works in Safari, Chrome, Preview, Mail, Slack, Obsidian and anything else that puts text on screen.

### Is Arc for Mac free?

Yes. Arc is free with 7 requests per week on basic features, and a premium subscription unlocks unlimited summaries, text-to-speech, AI chat and workflow automation. One subscription covers Mac, Windows and Android.

### What are the system requirements for Arc on Mac?

macOS 14 (Sonoma) or later. Arc is a universal binary that runs natively on both Apple Silicon and Intel Macs, and it is code-signed with an Apple Developer ID and notarized by Apple, so it installs without security warnings.

### Why isn't Arc on the Mac App Store?

Arc reads on-screen content through the macOS accessibility APIs, which Apple's App Sandbox prohibits. Sandboxing is mandatory for Mac App Store apps, so Arc is distributed directly from this site — still notarized by Apple, and updated through a signed Sparkle update feed.

### Does Arc read my screen in the background?

No. Arc reads the frontmost window only when you invoke an action yourself. It is not a keylogger and it does not monitor continuously. Screenshots are captured only for actions that explicitly need one, and password managers are skipped automatically.

The [Privacy Policy]({{ '/privacy/' | relative_url }}#macos-permissions-explained) lists every macOS permission and exactly when each is used.

</div>

{% include referral-handoff.html %}

<!-- related-posts: generated, see scratchpad linkplan -->
<div class="related-links">
  <h2>More on this</h2>
  <p>Guides that go further on what's above:</p>
  <ul>
    <li><a href="{{ '/2026/09/14/ai-screen-assistant-mac/' | relative_url }}">AI Screen Assistant Mac: One Shortcut for Every Window</a></li>
    <li><a href="{{ '/2026/10/07/read-screen-aloud-mac/' | relative_url }}">AI Screen Reader for macOS: Read Any Window</a></li>
    <li><a href="{{ '/2026/09/20/ai-writer-mac/' | relative_url }}">AI Writing Assistant for Mac: Rewrite in Any App</a></li>
    <li><a href="{{ '/2026/09/16/ai-summarizer-mac/' | relative_url }}">Summarize a PDF on Mac in One Keystroke</a></li>
  </ul>
</div>
<!-- /related-posts -->
