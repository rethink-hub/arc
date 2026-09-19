---
layout: default
title: "AI Assistant for Windows — Works on Any App | Arc"
description: "An AI assistant for Windows that reads the window you're already in — summarize, listen, rewrite, automate with Ctrl+Space. In beta; join the waitlist."
keywords: "ai assistant for windows, windows ai assistant, ai assistant for pc, ai screen assistant windows, windows ai summary app, windows text to speech ai"
platform: windows
og_image: /assets/images/og-windows.png
faq:
  - question: "Is there an AI assistant for Windows that works in every app?"
    answer: "Arc does. It reads the frontmost window through the Windows UI Automation APIs, so it works in Edge, Chrome, Word, Outlook, Slack, Teams, PDF readers and legacy Win32 apps without copy-pasting anything into a chatbot. Arc for Windows is in beta — the Mac build, which is the same application, is available today."
  - question: "When will Arc for Windows be released?"
    answer: "Arc for Windows is in beta. macOS and Windows are the same codebase and the same feature set, so the Windows build ships once hotkey registration and capture permissions are verified across Windows 10 and 11. Join the waitlist on this page and you'll be emailed when the beta opens."
  - question: "How much does Arc for Windows cost?"
    answer: "Arc is freemium. The free tier gives you 7 requests per week on basic features, and a premium subscription unlocks unlimited summaries, text-to-speech, AI chat and workflow automation. Pricing is identical on every platform — there is no Windows-specific upsell."
  - question: "How is Arc different from Copilot in Windows?"
    answer: "Copilot answers questions in its own panel, so you paste content into it. Arc runs on whatever window is already in front of you — press Ctrl+Space and it reads that window directly. You can also bind your own prompts to global hotkeys, which Copilot does not offer."
  - question: "Does Arc for Windows need an internet connection?"
    answer: "Yes. AI summaries, chat and rewriting are processed by a hosted model, so Arc needs a connection for those. Your saved items, custom actions and Info Vault entries are stored locally on your PC."
---

<!-- Hero: text left, live interactive demo right (mirrors the macOS page) -->
<div class="hero-section hero-with-live-demo">
  <div class="hero-content-row macos-hero-row">
    <div class="hero-text-col">
      <div class="coming-soon-badge">Coming soon — in beta</div>
      <h1>AI Assistant for Windows</h1>
      <p class="hero-subtitle">Press Ctrl+Space in any Windows app and Arc reads that window — summarizes it, reads it aloud, rewrites your text, or runs a prompt you wrote yourself.</p>
      <form class="notify-form" action="mailto:everythingrethink@gmail.com?subject=Notify%20me%20when%20Arc%20for%20Windows%20is%20ready" method="post" enctype="text/plain">
        <input type="email" name="email" placeholder="Enter your email" aria-label="Email for Arc for Windows updates" required>
        <button type="submit" class="cta-button">Join the waitlist</button>
      </form>
    </div>
    <div class="hero-demo-col hero-demo-col--arc">
      {% include arc-interactive-demo.html platform="windows" cta_label="Join the Windows waitlist →" cta_href="#about-arc-for-windows" %}
    </div>
  </div>
</div>

---

<div class="content-section" markdown="1">

## What Arc for Windows Is

Arc is an AI assistant for Windows that works on the window you are already looking at. You press **Ctrl + Space**, a search panel appears over your current app, and every action — summarize, read aloud, rewrite, chat, extract — runs against the text in that window. Nothing is copied, nothing is pasted, and you never switch to a separate chatbot tab.

It is in beta on Windows today. The same application already ships on macOS, so everything below is the real product rather than a mockup — [Arc for Mac](/macos/) is available to download now.

</div>

<!-- Screenshots (captured on macOS; identical UI on Windows) -->
<div class="section-header">
  <span class="section-tag">What it looks like</span>
  <h2>The same app you'll run on Windows.</h2>
  <p>Arc for Windows and Arc for Mac are one codebase with one interface. These screenshots were captured on macOS — on Windows the panel, actions and results are identical, with <strong>Ctrl</strong> in place of <strong>⌃</strong>.</p>
</div>

<div class="shot-gallery">
  <figure class="shot">
    <img src="{{ '/assets/images/screenshots/macos/01_arc_menu_over_chrome.jpg' | relative_url }}" alt="Arc menu panel floating over a Chrome browser window, listing AI actions" width="1200" height="715" loading="lazy">
    <figcaption><strong>The Arc menu.</strong> Ctrl+Space opens it over whatever app you're in. Your cursor and focus stay put underneath.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/images/screenshots/macos/02_ai_summary_result_panel.jpg' | relative_url }}" alt="Arc AI Summary result panel showing numbered key points from a web article" width="1200" height="715" loading="lazy">
    <figcaption><strong>AI Summary.</strong> Numbered key points from the window Arc just read, with listen, copy, save and share on the result.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/images/screenshots/macos/08_chat_about_screen_panel.jpg' | relative_url }}" alt="Arc chat panel answering a question about the content on screen" width="1200" height="710" loading="lazy">
    <figcaption><strong>Chat about your screen.</strong> Ask follow-up questions about the document or page in front of you.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/images/screenshots/macos/03_ai_writer_gmail_before_invoke.jpg' | relative_url }}" alt="Arc AI Writer ready to rewrite text in a Gmail reply field" width="1200" height="715" loading="lazy">
    <figcaption><strong>AI Writer.</strong> Arc grabs the focused text field, rewrites it, and writes the result straight back in — here in a browser mail compose box.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/images/screenshots/macos/12_shortcut_assigned_ai_writer.jpg' | relative_url }}" alt="Custom global keyboard shortcut assigned to the AI Writer action in Arc settings" width="1200" height="715" loading="lazy">
    <figcaption><strong>Global hotkeys.</strong> Bind any action — built-in or your own — to a keystroke that works system-wide. See <a href="{{ '/ai-shortcuts/' | relative_url }}">AI shortcuts</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/images/screenshots/macos/06_arc_actions_create_form_empty.jpg' | relative_url }}" alt="Arc custom action creation form with a prompt template field" width="1200" height="715" loading="lazy">
    <figcaption><strong>Your own actions.</strong> Write a prompt once with a <code>{screen_text}</code> placeholder and it becomes a one-key command. More on <a href="{{ '/ai-workflow-automation/' | relative_url }}">AI workflow automation</a>.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/images/screenshots/macos/13_saved_items_library_list.jpg' | relative_url }}" alt="Arc saved items library listing captured screens with titles and categories" width="1200" height="715" loading="lazy">
    <figcaption><strong>Saved items.</strong> Every summary and capture lands in a searchable local library with its source app and URL.</figcaption>
  </figure>
  <figure class="shot">
    <img src="{{ '/assets/images/screenshots/macos/11_info_vault_with_entries.jpg' | relative_url }}" alt="Arc Info Vault storing reusable personal details for AI writing" width="1200" height="715" loading="lazy">
    <figcaption><strong>Info Vault.</strong> Reusable details Arc can drop into what it writes for you, stored on your own machine.</figcaption>
  </figure>
</div>

---

<!-- Feature teaser -->
<div class="section-header">
  <span class="section-tag">Features</span>
  <h2>What you can do with it.</h2>
  <p>Every action below runs on the window in front of you, not on text you pasted somewhere.</p>
</div>

<div class="coming-soon-features">
  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-icon icon-summary" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L14 9L21 12L14 15L12 22L10 15L3 12L10 9L12 2Z"/></svg>
      </div>
      <h3>Summarize Any Window</h3>
      <p>Turn long browser tabs, Word documents, and Teams threads into numbered key points instantly.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-reader" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5L6 9H2V15H6L11 19V5Z"/><path class="wave-1" d="M15.54 8.46C16.48 9.4 17 10.62 17 12C17 13.38 16.48 14.6 15.54 15.54"/><path class="wave-2" d="M19.07 4.93C20.95 6.81 22 9.28 22 12C22 14.72 20.95 17.19 19.07 19.07"/></svg>
      </div>
      <h3>Read Aloud</h3>
      <p>Windows natural voices read any text while you work on something else, with language auto-detected. See <a href="{{ '/text-to-speech/' | relative_url }}">AI text to speech</a>.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-chat" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5C21.0034 12.82 20.6951 13.12 20.12 14.3C19.3875 15.82 18.2056 17.05 16.72 17.83C15.2344 18.61 13.5465 18.9 11.88 18.66C11.48 18.6 11.09 18.53 10.7 18.43C9.6333 18.86 8.44083 19.08 7.22 19.08C6.87 19.08 6.53 18.93 6.29 18.68C6.04 18.44 5.9 18.1 5.9 17.74V15.6C4.76 14.36 4.08 12.79 4.08 11.08C4.08 8.35 6.27 5.99 9.01 5.61C9.49 2.61 12.13 0.25 15.34 0.25C18.91 0.25 21.8 3.14 21.8 6.71C21.8 8.37 21.1 9.87 19.97 10.97"/></svg>
      </div>
      <h3>Chat About Your Screen</h3>
      <p>Ask questions about what you see in any app and get contextual answers without re-explaining it.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-writer" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20H21"/><path d="M16.5 3.5C16.8978 3.10217 17.4374 2.87868 18 2.87868C18.5626 2.87868 19.1022 3.10217 19.5 3.5C19.8978 3.89782 20.1213 4.43739 20.1213 5C20.1213 5.56261 19.8978 6.10217 19.5 6.5L7 19L3 20L4 16L16.5 3.5Z"/></svg>
      </div>
      <h3>AI Writer</h3>
      <p>Rewrite, reply, translate or fix grammar in any Windows app — Arc writes the result back into the field. See <a href="{{ '/ai-writer/' | relative_url }}">AI writer</a>.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-actions" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14H12L11 22L21 10H12L13 2Z"/></svg>
      </div>
      <h3>Custom AI Actions</h3>
      <p>Write a prompt once, assign it a global hotkey, and run it on any screen for the rest of your life.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-community" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21V19C17 17.9391 16.5786 16.9217 15.8284 16.1716C15.0783 15.4214 14.0609 15 13 15H5C3.93913 15 2.92172 15.4214 2.17157 16.1716C1.42143 16.9217 1 17.9391 1 19V21"/><circle cx="9" cy="7" r="4"/><path d="M23 21V19C23 18.22 22.81 17.48 22.46 16.82C22.11 16.16 21.64 15.58 21.06 15.13"/><path d="M16 3.13C16.64 3.58 17.11 4.16 17.46 4.82C17.81 5.48 18 6.22 18 7C18 7.78 17.81 8.52 17.46 9.18C17.11 9.84 16.64 10.42 16 10.87"/></svg>
      </div>
      <h3>500+ Community Actions</h3>
      <p>Browse and install ready-made AI actions shared by other Arc users for work, study and productivity.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-privacy" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
      </div>
      <h3>Smart Extract</h3>
      <p>Pull dates, contacts, codes and action items out of any screen, each with a button that uses it. See <a href="{{ '/smart-extract/' | relative_url }}">Smart Extract</a>.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon icon-summary" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L14 9L21 12L14 15L12 22L10 15L3 12L10 9L12 2Z"/></svg>
      </div>
      <h3>Flashcards</h3>
      <p>Turn any page of study material into a reviewable deck without retyping it. See <a href="{{ '/flashcards/' | relative_url }}">AI flashcards</a>.</p>
    </div>
  </div>
</div>

---

<div class="content-section" id="about-arc-for-windows" markdown="1">

## How Arc Works on Windows

Most AI tools on Windows ask you to bring the content to them: select text, copy it, switch to a browser tab or a chat panel, paste, then carry the answer back. Arc inverts that. It reads the frontmost window through the **Windows UI Automation** framework — the same accessibility layer screen readers use — so the content is already there when the panel opens.

That covers the whole desktop: modern UWP apps, legacy Win32 software, Edge and Chrome windows, Office documents, PDF viewers and Electron apps like Slack and Teams. Arc runs from the system tray, registers global hotkeys, and the panel is non-activating, so the app underneath keeps focus and your cursor never moves.

### Windows vs. Mac: what actually differs

macOS and Windows run the same Arc codebase with the same feature set. Three things differ, and all three are the operating system's doing rather than ours:

| | macOS | Windows |
|---|---|---|
| Summon hotkey | ⌃ Space | Ctrl + Space |
| Screen reading | Accessibility API | UI Automation |
| Permissions | Accessibility + Screen Recording prompts | No equivalent prompt; capture is granted at install |
| Background home | Menu bar | System tray |

Everything else — the actions, the result panel, the Saved Items library, the Info Vault, custom actions, community actions — is identical.

### Why Arc instead of Copilot

Copilot in Windows is a chat panel: it is excellent at answering questions you type into it, and it has no idea what is in the window behind it unless you tell it. Arc's whole premise is the opposite one. It never asks what you are looking at, because it just read it.

The second difference is programmability. In Arc you write a prompt once — "extract every action item and who owns it from `{screen_text}`" — give it a hotkey, and it becomes a permanent command you run on any screen. That is closer to a scripting layer for AI than a chatbot. If that's the part you care about, [AI workflow automation](/ai-workflow-automation/) covers it in depth, and the same ideas apply to the [private AI assistant](/private-ai-assistant/) setup for sensitive work.

### When is the Windows release?

Arc for Windows is in beta. Because it is the same codebase as the shipping Mac app, the remaining work is platform plumbing rather than features: hotkey registration across Windows 10 and 11, capture permissions, and installer signing. Join the waitlist above and you'll get an email when the beta opens — no other mail.

If you don't want to wait, [Arc for Mac](/macos/) is available today and [Arc for Android](/android/) is on Google Play.

</div>

---

<!-- Cross platform CTA -->
<div class="coming-soon-section">
  <h2>Available now on Mac and Android</h2>
  <p>Arc for Windows is in beta. The same app is shipping on two platforms today.</p>
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

Arc does. It reads the frontmost window through the Windows UI Automation APIs, so it works in Edge, Chrome, Word, Outlook, Slack, Teams, PDF readers and legacy Win32 apps without copy-pasting anything into a chatbot. Arc for Windows is in beta — the Mac build, which is the same application, is available today.

### When will Arc for Windows be released?

Arc for Windows is in beta. macOS and Windows are the same codebase and the same feature set, so the Windows build ships once hotkey registration and capture permissions are verified across Windows 10 and 11. Join the waitlist on this page and you'll be emailed when the beta opens.

### How much does Arc for Windows cost?

Arc is freemium. The free tier gives you 7 requests per week on basic features, and a premium subscription unlocks unlimited summaries, text-to-speech, AI chat and workflow automation. Pricing is identical on every platform — there is no Windows-specific upsell.

### How is Arc different from Copilot in Windows?

Copilot answers questions in its own panel, so you paste content into it. Arc runs on whatever window is already in front of you — press Ctrl+Space and it reads that window directly. You can also bind your own prompts to global hotkeys, which Copilot does not offer.

### Does Arc for Windows need an internet connection?

Yes. AI summaries, chat and rewriting are processed by a hosted model, so Arc needs a connection for those. Your saved items, custom actions and Info Vault entries are stored locally on your PC.

</div>

{% include referral-handoff.html %}
