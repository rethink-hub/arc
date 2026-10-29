---
layout: default
title: "AI Assistant for Windows — Free on Microsoft Store | Arc"
description: "Get Arc free from the Microsoft Store for Windows 10 and 11. Press Ctrl+Space in Word, Outlook, Edge or Teams to summarize, read aloud or rewrite."
keywords: "ai assistant for windows, ai assistant microsoft store, download ai assistant windows, windows ai assistant, ai assistant for pc, ai screen assistant windows, windows ai summary app, windows text to speech ai"
platform: windows
og_image: /assets/images/og-windows.png
product_page: true
faq:
  - question: "Does Arc for Windows need administrator rights?"
    answer: "No. The Microsoft Store installs Arc per user, so it works on PCs where you can't install software as an administrator, as long as the Store is allowed."
  - question: "What if Ctrl+Space is already taken on my PC?"
    answer: "Some input methods use Ctrl+Space to switch languages. Open Arc's Settings, record a different key combination for the Arc menu, and the new shortcut takes over system-wide."
  - question: "Where can I download Arc for Windows?"
    answer: "From the Microsoft Store. It installs and updates like any Store app, runs on Windows 10 (version 1809 or later) and Windows 11, and supports both Intel/AMD and Arm PCs."
  - question: "How much does Arc for Windows cost?"
    answer: "Arc is freemium. The free tier gives you 7 requests per week on basic features, and a premium subscription unlocks unlimited summaries, text-to-speech, AI chat and workflow automation. Pricing is identical on every platform — there is no Windows-specific upsell."
  - question: "How is Arc different from Copilot in Windows?"
    answer: "Copilot answers questions in its own panel, so you paste content into it. Arc runs on whatever window is already in front of you — press Ctrl+Space and it reads that window directly. You can also bind your own prompts to global hotkeys, which Copilot does not offer."
  - question: "Does Arc for Windows need an internet connection?"
    answer: "Yes. AI summaries, chat and rewriting are processed by a hosted model, so Arc needs a connection for those. Your saved items, custom actions and Info Vault entries are stored locally on your PC."
last_modified_at: 2026-10-29
---

<!-- Hero: text left, live interactive demo right (mirrors the macOS page) -->
<div class="hero-section hero-with-live-demo">
  <div class="hero-content-row macos-hero-row">
    <div class="hero-text-col">
      <div class="coming-soon-badge status-live">Now available for Windows</div>
      <h1>AI Assistant for Windows</h1>
      <p class="hero-subtitle">Press Ctrl+Space in any Windows app and Arc reads that window — summarizes it, reads it aloud, rewrites your text, or runs a prompt you wrote yourself.</p>
      <div class="hero-cta-group">
        <a href="{{ site.windows_app.store }}" class="cta-button" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M0 3.449L9.75 2.1v9.451H0m10.949-9.602L24 0v11.4H10.949M0 12.6h9.75v9.451L0 20.699M10.949 12.6H24V24l-12.9-1.801"/></svg>
          Get it from Microsoft
        </a>
      </div>
      <ul class="hero-meta">
        <li>Free</li>
        <li>Windows 10 &amp; 11</li>
        <li>x64 &amp; Arm</li>
        <li>Microsoft Store</li>
      </ul>
      <a class="hero-alt-link" href="{{ '/macos/' | relative_url }}">Also on Mac →</a>
    </div>
    <div class="hero-demo-col hero-demo-col--arc">
      {% include arc-interactive-demo.html platform="windows" cta_label="Get Arc for Windows →" cta_href=site.windows_app.store %}
      <img class="demo-mobile-fallback" src="{{ '/assets/images/screenshots/windows/01_arc_menu_over_edge.jpg' | relative_url }}" alt="The Arc menu open over Microsoft Edge on Windows 11, listing AI actions" width="1600" height="845" loading="lazy" decoding="async">
    </div>
  </div>
</div>

---

<div class="content-section" markdown="1">

## What Arc for Windows Is

Arc is an AI assistant for Windows that works on the window you are already looking at. You press **Ctrl + Space**, a search panel appears over your current app, and every action — summarize, read aloud, rewrite, chat, extract — runs against the text in that window. Nothing is copied, nothing is pasted, and you never switch to a separate chatbot tab.

It's a free download from the [Microsoft Store]({{ site.windows_app.store }}) for Windows 10 and 11.

### What's in the Ctrl+Space menu

The panel lists seven built-in actions — **AI Summary, AI Writer, Save Content, AI Read, Chat Screen, Flashcards, Smart Extract** — and the search field doubles as a free-text prompt box. Each action can be reordered, disabled or bound to its own global shortcut. Esc dismisses the panel with no residue.

- **AI Summary** returns an AI-generated title, numbered key points and a source chip in a couple of seconds, with Listen, Copy, Share, Save and Ask questions underneath.
- **AI Read** opens no window at all: Arc detects the on-screen language, picks the best installed voice and starts reading. Lists are spoken as separate points with pauses, and invoking it again stops playback.
- **AI Writer** pulls the draft from whatever field your cursor is in and offers four modes: Rewrite (Rephrase, Professional, Polite, Shorten, Elaborate, Custom), Fix Grammar, Reply (Agree, Decline, Thank, Ask for details, Acknowledge) and Create Post for Reddit, X, LinkedIn and store reviews. **Insert** writes the result back into the original field.
- **Arc Actions** are your own prompts with a `{screen_text}` placeholder — "extract every action item and deadline from this thread", "turn this error message into a bug report" — bound to a hotkey and run headless against the current window. The community catalog is filterable by language.

</div>

<!-- Install steps -->
<div class="section-header">
  <span class="section-tag">Getting started</span>
  <h2>Install from the Microsoft Store.</h2>
</div>

<div class="steps-container">
  <div class="step">
    <div class="step-number">1</div>
    <div class="step-title">Get it from Microsoft</div>
    <p class="step-description">Open the <a href="{{ site.windows_app.store }}" target="_blank" rel="noopener">Store listing</a> and click Get. No installer to download and no admin prompt.</p>
  </div>
  <div class="step">
    <div class="step-number">2</div>
    <div class="step-title">Launch from Start</div>
    <p class="step-description">Arc settles into the system tray. Turn on "start with Windows" if you want it ready after every reboot.</p>
  </div>
  <div class="step">
    <div class="step-number">3</div>
    <div class="step-title">Press Ctrl + Space</div>
    <p class="step-description">Open Word, Outlook, Edge or a PDF and press Ctrl+Space. The panel reads that window straight away.</p>
  </div>
</div>

<!-- Screenshots (captured on macOS; identical UI on Windows) -->
<div class="section-header">
  <span class="section-tag">What it looks like</span>
  <h2>The panel, the summary, the rewrite.</h2>
  <p>These were captured on a Mac. The Windows build uses the same interface, with <strong>Ctrl</strong> in place of <strong>⌃</strong>.</p>
</div>

<div class="shot-gallery">
  <figure class="shot">
    <img width="1600" height="845" src="{{ '/assets/images/screenshots/windows/01_arc_menu_over_edge.jpg' | relative_url }}" alt="The Arc menu open over Microsoft Edge on Windows 11, listing its built-in AI actions" loading="lazy">
    <figcaption><strong>The panel.</strong> Seven built-in actions plus a prompt box, over whatever window has focus.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1600" height="845" src="{{ '/assets/images/screenshots/windows/02_ai_summary_over_edge.jpg' | relative_url }}" alt="An Arc summary on Windows with numbered key points from a Wikipedia article in Edge" loading="lazy">
    <figcaption><strong>A summary.</strong> Key points from a long Edge article or Outlook thread, with a play button to listen. More on <a href="{{ '/text-to-speech/' | relative_url }}">reading it aloud</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1600" height="845" src="{{ '/assets/images/screenshots/windows/03_ai_writer_rewrite_mail.jpg' | relative_url }}" alt="Arc AI Writer on Windows rewriting a rough email draft in a professional tone" loading="lazy">
    <figcaption><strong>A rewrite.</strong> Insert puts the new text back into the mail, Word or Outlook field you were typing in. See <a href="{{ '/ai-writer/' | relative_url }}">AI writer</a>.</figcaption>
  </figure>
</div>

---

<div class="content-section" id="about-arc-for-windows" markdown="1">

## How Arc Works on Windows

Arc reads the frontmost window through the **Windows UI Automation** framework — the same accessibility layer screen readers use — so the content is already there when the panel opens.

That covers UWP apps, legacy Win32 software, browsers, Office, PDF viewers and Electron apps like Slack and Teams. The panel is non-activating, so the app underneath keeps focus. The Store installs Arc per user with no administrator rights and keeps it updated; it runs from the system tray and can start with Windows.

### Windows vs. Mac: what actually differs

Same codebase, same features. Only these differ:

| | macOS | Windows |
|---|---|---|
| Summon hotkey | ⌃ Space | Ctrl + Space |
| Screen reading | Accessibility API | UI Automation |
| Permissions | Accessibility + Screen Recording prompts | No equivalent prompt; works as installed from the Store |
| Background home | Menu bar | System tray |

Your own prompts with hotkeys are covered on AI workflow automation; for sensitive work, see the private AI assistant setup.

</div>

---

<!-- Cross platform CTA -->
<div class="coming-soon-section">
  <h2>Also on Mac and Android</h2>
  <p>The same Arc, with one subscription across every platform you use.</p>
  <div class="platform-links">
    <a href="{{ '/macos/' | relative_url }}">Arc for Mac</a>
    <a href="{{ '/android/' | relative_url }}">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.523 15.3414c-.566 0-1.027-.478-1.027-1.068 0-.591.461-1.069 1.027-1.069.567 0 1.028.478 1.028 1.069 0 .59-.461 1.068-1.028 1.068zm-11.046 0c-.567 0-1.028-.478-1.028-1.068 0-.591.461-1.069 1.028-1.069.566 0 1.027.478 1.027 1.069 0 .59-.461 1.068-1.027 1.068zm11.4-6.12l1.997-3.459a.433.433 0 00-.158-.591.438.438 0 00-.593.156l-2.022 3.502c-1.515-.69-3.205-1.078-4.984-1.078-1.75 0-3.414.374-4.908 1.043L5.355 5.155a.437.437 0 00-.593-.156.433.433 0 00-.158.591l2.006 3.46C2.95 11.479.5 15.096.5 19.245h23c0-4.149-2.45-7.766-5.623-10.024z"/></svg>
      Get Arc for Android
    </a>
    <a href="{{ '/ios/' | relative_url }}">Arc for iOS</a>
  </div>
</div>

<div class="content-section" markdown="1">

## Arc for Windows FAQ

### Does Arc for Windows need administrator rights?

No. The Microsoft Store installs Arc per user, so it works on PCs where you can't install software as an administrator, as long as the Store is allowed.

### What if Ctrl+Space is already taken on my PC?

Some input methods use Ctrl+Space to switch languages. Open Arc's Settings, record a different key combination for the Arc menu, and the new shortcut takes over system-wide.

### Where can I download Arc for Windows?

From the [Microsoft Store]({{ site.windows_app.store }}). It installs and updates like any Store app, runs on Windows 10 (version 1809 or later) and Windows 11, and supports both Intel/AMD and Arm PCs.

### How much does Arc for Windows cost?

Arc is freemium. The free tier gives you 7 requests per week on basic features, and a premium subscription unlocks unlimited summaries, text-to-speech, AI chat and workflow automation. Pricing is identical on every platform — there is no Windows-specific upsell.

### How is Arc different from Copilot in Windows?

Copilot answers questions in its own panel, so you paste content into it. Arc runs on whatever window is already in front of you — press Ctrl+Space and it reads that window directly. You can also bind your own prompts to global hotkeys, which Copilot does not offer.

### Does Arc for Windows need an internet connection?

Yes. AI summaries, chat and rewriting are processed by a hosted model, so Arc needs a connection for those. Your saved items, custom actions and Info Vault entries are stored locally on your PC.

</div>

{% include referral-handoff.html %}
