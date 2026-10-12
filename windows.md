---
layout: default
title: "AI Assistant for Windows — Free on Microsoft Store | Arc"
description: "Arc is an AI assistant for Windows that reads any window. Press Ctrl+Space to summarize, listen, rewrite and automate in any app. Free on the Microsoft Store."
keywords: "ai assistant for windows, ai assistant microsoft store, download ai assistant windows, windows ai assistant, ai assistant for pc, ai screen assistant windows, windows ai summary app, windows text to speech ai"
platform: windows
og_image: /assets/images/og-windows.png
product_page: true
faq:
  - question: "Is there an AI assistant for Windows that works in every app?"
    answer: "Arc does. It reads the frontmost window through the Windows UI Automation APIs, so it works in Edge, Chrome, Word, Outlook, Slack, Teams, PDF readers and legacy Win32 apps without copy-pasting anything into a chatbot. It is a free download from the Microsoft Store."
  - question: "Where can I download Arc for Windows?"
    answer: "From the Microsoft Store. It installs and updates like any Store app, runs on Windows 10 (version 1809 or later) and Windows 11, and supports both Intel/AMD and Arm PCs."
  - question: "How much does Arc for Windows cost?"
    answer: "Arc is freemium. The free tier gives you 7 requests per week on basic features, and a premium subscription unlocks unlimited summaries, text-to-speech, AI chat and workflow automation. Pricing is identical on every platform — there is no Windows-specific upsell."
  - question: "How is Arc different from Copilot in Windows?"
    answer: "Copilot answers questions in its own panel, so you paste content into it. Arc runs on whatever window is already in front of you — press Ctrl+Space and it reads that window directly. You can also bind your own prompts to global hotkeys, which Copilot does not offer."
  - question: "Does Arc for Windows need an internet connection?"
    answer: "Yes. AI summaries, chat and rewriting are processed by a hosted model, so Arc needs a connection for those. Your saved items, custom actions and Info Vault entries are stored locally on your PC."
last_modified_at: 2026-10-04
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
      <img class="demo-mobile-fallback" src="{{ '/assets/images/screenshots/macos/01_arc_menu_over_chrome.jpg' | relative_url }}" alt="The Arc panel open over a browser window, listing AI actions" width="1200" height="715" loading="lazy" decoding="async">
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

<!-- Screenshots (captured on macOS; identical UI on Windows) -->
<div class="section-header">
  <span class="section-tag">What it looks like</span>
  <h2>The same app on Windows and Mac.</h2>
  <p>Captured on macOS — Arc for Windows is the same codebase and interface, with <strong>Ctrl</strong> in place of <strong>⌃</strong>.</p>
</div>

<div class="shot-gallery">
  <figure class="shot">
    <img width="1200" height="715" src="{{ '/assets/images/screenshots/macos/01_arc_menu_over_chrome.jpg' | relative_url }}" alt="Arc menu panel floating over a Chrome browser window, listing AI actions" loading="lazy">
    <figcaption><strong>The Arc menu.</strong> Ctrl+Space opens it over whatever app you're in.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="710" src="{{ '/assets/images/screenshots/macos/02_ai_summary_result_panel.jpg' | relative_url }}" alt="Arc AI Summary result panel showing numbered key points from a web article" loading="lazy">
    <figcaption><strong>AI Summary.</strong> Numbered key points from the window Arc just read. Prefer listening? See <a href="{{ '/text-to-speech/' | relative_url }}">AI text to speech</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="710" src="{{ '/assets/images/screenshots/macos/08_chat_about_screen_panel.jpg' | relative_url }}" alt="Arc chat panel answering a question about the content on screen" loading="lazy">
    <figcaption><strong>Chat about your screen.</strong> Follow-ups on the page in front of you.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1058" height="984" src="{{ '/assets/images/screenshots/macos/03_ai_writer_gmail_before_invoke.jpg' | relative_url }}" alt="Arc AI Writer ready to rewrite text in a Gmail reply field" loading="lazy">
    <figcaption><strong>AI Writer.</strong> Rewrite, reply or fix grammar, and Arc writes the result back into the field. See <a href="{{ '/ai-writer/' | relative_url }}">AI writer</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="912" src="{{ '/assets/images/screenshots/macos/12_shortcut_assigned_ai_writer.jpg' | relative_url }}" alt="Custom global keyboard shortcut assigned to the AI Writer action in Arc settings" loading="lazy">
    <figcaption><strong>Global hotkeys.</strong> Bind any action to a system-wide keystroke. See <a href="{{ '/ai-shortcuts/' | relative_url }}">AI shortcuts</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="780" src="{{ '/assets/images/screenshots/macos/06_arc_actions_create_form_empty.jpg' | relative_url }}" alt="Arc custom action creation form with a prompt template field" loading="lazy">
    <figcaption><strong>Your own actions.</strong> A prompt with a <code>{screen_text}</code> placeholder becomes a one-key command, or install one of 500+ community actions. More on <a href="{{ '/ai-workflow-automation/' | relative_url }}">AI workflow automation</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="780" src="{{ '/assets/images/screenshots/macos/13_saved_items_library_list.jpg' | relative_url }}" alt="Arc saved items library listing captured screens with titles and categories" loading="lazy">
    <figcaption><strong>Saved items.</strong> A searchable local library of every summary, with source app and URL.</figcaption>
  </figure>
  <figure class="shot">
    <img width="1200" height="780" src="{{ '/assets/images/screenshots/macos/11_info_vault_with_entries.jpg' | relative_url }}" alt="Arc Info Vault storing reusable personal details for AI writing" loading="lazy">
    <figcaption><strong>Info Vault.</strong> Reusable details for AI writing, stored on your PC. Pull dates and contacts with <a href="{{ '/smart-extract/' | relative_url }}">Smart Extract</a> or build <a href="{{ '/flashcards/' | relative_url }}">flashcards</a> too.</figcaption>
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

For sensitive work, see the [private AI assistant](/private-ai-assistant/) setup.

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

### Is there an AI assistant for Windows that works in every app?

Arc does. It reads the frontmost window through the Windows UI Automation APIs, so it works in Edge, Chrome, Word, Outlook, Slack, Teams, PDF readers and legacy Win32 apps without copy-pasting anything into a chatbot. It is a free download from the Microsoft Store.

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
