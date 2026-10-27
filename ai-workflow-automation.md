---
layout: default
title: "AI Shortcuts & Custom AI Actions for Android and Mac | Arc"
description: "Save any prompt as a one-tap AI action and run it on whatever is on screen — from the Android sidebar or a keyboard shortcut on Mac and Windows. Free."
keywords: "ai shortcuts, custom ai actions, ai workflow automation"
og_image: /assets/images/og-ai-workflow-automation.png
product_page: true
faq:
  - question: "Can I share my custom actions?"
    answer: "Yes. Publish them to the Community Actions library with a Google sign-in, and other Arc users can find and add them."
  - question: "Are there limits on custom actions?"
    answer: "No limit on how many. You can create unlimited custom actions, and each prompt can run to 40,000 characters, so multi-step instructions fit in one action."
  - question: "How accurate is the AI fact checker?"
    answer: "A fact-check action with web search enabled checks each claim against outside sources and links one. Treat it as a fast first pass and verify anything critical against an authoritative source."
  - question: "Can actions work without internet?"
    answer: "No. Running an action needs a connection because the models are cloud-side. Your action configurations are stored on the device and sync to Google Drive if you turn on backup, so a new phone gets your sidebar back."
  - question: "Is Arc a Tasker alternative?"
    answer: "Different jobs. Tasker, MacroDroid and Automate trigger on device events — time, location, battery, notifications — and are still the right tools for toggling Wi-Fi or scheduling an SMS. Acting on the content inside an app means brittle simulated taps that break on the next app update. Arc's actions do the language work instead — replies, translation, fact checks, extraction — on whatever is on screen, with you present. Many power users run both."
  - question: "How do I open Arc with a shortcut?"
    answer: "Android: swipe from the screen edge. macOS: press ⌃Space in any window. Windows: press Ctrl+Space. Esc dismisses the menu. On iPhone, you'll be able to bind Arc to the Action Button or a double-tap-on-back gesture."
  - question: "Can I change the ⌃Space shortcut?"
    answer: "Yes. Open Settings → Activation, press Record, and choose any combination. Arc detects conflicts with its own action shortcuts and names the action that already owns a key."
  - question: "Is it free?"
    answer: "Yes — Arc, custom actions, and Community Actions are free, with 7 AI requests per week. An optional Pro subscription removes the limits across Android, macOS, and Windows on one account."
last_modified_at: 2026-10-27
---

<!-- Hero: copy left, the same feature on Mac and Android right -->
<section class="fhero">
  <div class="fhero-copy">
      <span class="fhero-badge">Android &amp; Mac</span>
      <h1>AI Shortcuts and Custom AI Actions</h1>
      <p class="fhero-sub">Turn any prompt you repeat into a one-tap <strong>AI action</strong>: translate, fact-check, simplify, extract data, or anything else you can describe. Run it from the Arc sidebar on Android, or bind it to a key on Mac and Windows — it works on whatever is on screen, in any app.</p>
      <div class="home-hero-ctas fhero-ctas">
      <a href="https://play.google.com/store/apps/details?id=com.rethink.arc" class="btn btn-primary btn-lg" data-cta="android" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.523 15.3414c-.566 0-1.027-.478-1.027-1.068 0-.591.461-1.069 1.027-1.069.567 0 1.028.478 1.028 1.069 0 .59-.461 1.068-1.028 1.068zm-11.046 0c-.567 0-1.028-.478-1.028-1.068 0-.591.461-1.069 1.028-1.069.566 0 1.027.478 1.027 1.069 0 .59-.461 1.068-1.027 1.068zm11.4-6.12l1.997-3.459a.433.433 0 00-.158-.591.438.438 0 00-.593.156l-2.022 3.502c-1.515-.69-3.205-1.078-4.984-1.078-1.75 0-3.414.374-4.908 1.043L5.355 5.155a.437.437 0 00-.593-.156.433.433 0 00-.158.591l2.006 3.46C2.95 11.479.5 15.096.5 19.245h23c0-4.149-2.45-7.766-5.623-10.024z"/></svg>Get it on Google Play</a>
      <a href="{{ '/macos/' | relative_url }}" class="btn btn-secondary btn-lg" data-cta="mac"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.21-1.96 1.07-3.11-1.05.05-2.31.7-3.06 1.57-.67.78-1.25 2.04-1.09 3.27 1.17.09 2.37-.7 3.08-1.73z"/></svg>Download for Mac</a>
      </div>
  </div>
  <div class="tab-media fhero-media">
    <img width="1200" height="780" class="shot-mac" src="{{ '/assets/images/screenshots/macos/06_arc_actions_create_form_empty.jpg' | relative_url }}" alt="Creating a custom AI action in Arc for Mac" loading="eager" decoding="async">
    <div class="phone-mini"><img width="800" height="1760" src="{{ '/assets/images/screenshots/06_custom_actions_list_with_active_actions.jpg' | relative_url }}" alt="Custom AI actions listed in the Arc sidebar on Android" loading="eager" decoding="async"></div>
  </div>
</section>

<div class="video-embed-section">
  <h2>See it in action</h2>
  <div class="video-embed"><iframe loading="lazy" src="https://www.youtube.com/embed/qk6gu5Owaas?si=yFJd1TiF16FNph2C" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>
</div>


---

## How custom actions work

A custom action is a saved prompt that runs on the content of your current screen. Instead of copying text into a chatbot and retyping the same instruction, you tap the action and get the result in 2–3 seconds.

<div class="steps-container">
  <div class="step">
    <div class="step-number">1</div>
    <div class="step-title">Write the Prompt</div>
    <p class="step-description">Settings → Custom Actions → Create New Action. Describe what you want done, e.g. "Extract all dates"</p>
  </div>

  <div class="step">
    <div class="step-number">2</div>
    <div class="step-title">Choose the Toggles</div>
    <p class="step-description">Turn on screenshot capture or web search only if the action needs them</p>
  </div>

  <div class="step">
    <div class="step-number">3</div>
    <div class="step-title">Run It Anywhere</div>
    <p class="step-description">The action appears in your floating sidebar or Arc menu — tap it over any app, or press its shortcut, to run it on what's on screen</p>
  </div>
</div>

On desktop the form is the same: a **Name**, a **Prompt**, an icon, the optional *Capture a screenshot region* and *Enable web search* toggles, and a keyboard shortcut. Use `{screen_text}` to control where the screen content lands in your prompt:

<pre><code>You are a senior editor. Rewrite the following in plain English, max 120 words:

{screen_text}

Then list any claims that need a citation.</code></pre>

Omit the placeholder and the screen content is simply appended as context. Screenshot actions start with a region selector (the first capture asks for consent).

---

## Open Arc with one gesture or keystroke

<div class="coming-soon-features">
  <div class="features-grid">
    <div class="feature-card">
      <h3>📱 Android: swipe from the edge</h3>
      <p>The floating sidebar slides out over any app. One swipe, every action — and it plays nicely alongside Samsung Edge Panel, OnePlus Shelf, and OPPO Smart Sidebar.</p>
    </div>
    <div class="feature-card">
      <h3>💻 macOS: ⌃ Space anywhere</h3>
      <p>A Spotlight-style panel appears over any window, reads what's on screen, runs the action, and disappears. Esc dismisses it. It never steals focus from the app underneath.</p>
    </div>
    <div class="feature-card">
      <h3>🪟 Windows: Ctrl + Space</h3>
      <p>The same Arc Menu, keyboard-first, over every app on Windows. Press Ctrl+Space in any window; Esc dismisses it. Get it from the <a href="{{ site.windows_app.store }}" target="_blank" rel="noopener">Microsoft Store</a>.</p>
    </div>
    <div class="feature-card">
      <h3>📱 iPhone: Action Button & back-tap</h3>
      <p>Coming soon — bind Arc to the Action Button or a double-tap-on-back gesture and it opens over any app you're in.</p>
    </div>
  </div>
</div>

<img class="inline-shot" width="1200" height="715" src="/assets/images/screenshots/macos/01_arc_menu_over_chrome.jpg" alt="Arc menu floating over Google Chrome on macOS, listing built-in and custom AI actions" loading="lazy" decoding="async">

### It never steals your focus

The desktop Arc menu is a **non-activating panel**. When you press ⌃ Space it fades in over your current window, but your app keeps focus and your text cursor stays exactly where it was — macOS doesn't flip you to another Space. That's what lets the [AI Writer]({{ '/ai-writer/' | relative_url }}) read the field you're typing in and write the result back into that same field.

Close the main window and Arc keeps running — a menu-bar item on macOS, a tray icon on Windows — with the hotkey alive from any app. If ⌃ Space already belongs to Spotlight or your input method, open Settings → Activation, press Record, and pick a different combination.

### Keyboard-first, from summon to result

The search field is focused the moment the menu opens, with the first action selected. Type to filter, ↑ / ↓ to move, Return to run, Esc to bail out.

- **Search filters by name and description.** Typing "summarize" finds AI Summary even though that word only appears in its subtitle. Custom actions filter in the same pass.
- **The search box doubles as a prompt box.** Type a question no action matches — "what are the risks listed here?" — and press Return. Arc reads the current screen, attaches it as context, and opens a chat with your question already asked.
- **Any action can skip the menu entirely.** Each row carries a keyboard icon. Click it, press a combination — ⌥ S, say — and from then on that key runs the action headlessly: no menu, no panel, just the result. Arc rejects a combination that's already bound and tells you which action owns it.

### Built-in actions you can bind

Seven actions ship with the app. Each can be enabled, disabled, drag-reordered, or bound to its own key — and your custom actions sit in the same list.

| Action | What it does |
| --- | --- |
| **AI Summary** | Summarize the current screen |
| **AI Writer** | Rewrite or reply from the focused text field |
| **Save Content** | Save the on-screen text |
| **AI Read** | Read the current screen aloud |
| **Chat Screen** | Ask questions about the current screen |
| **Flashcards** | Generate flashcards |
| **Smart Extract** | Extract structured data — events, contacts, meeting links, OTP codes, and more, each with a one-click action |

---

## Three actions worth copying

The feature is only as good as the prompts you put in it. These three are the ones that earn their place on the sidebar — copy the prompt text straight into **Settings → Custom Actions → Create New Action**.

**1. Meeting-to-tasks**

> Read the screen and list only the action items, one per line. For each, write who owns it and the deadline if one was stated. If no owner or deadline was given, write "unassigned" rather than guessing. Ignore discussion that produced no action.

Run it on a meeting-notes doc, a long Slack thread, or an email chain. The "rather than guessing" clause is what keeps it from inventing owners — without it, models fill the blank.

**2. Vocabulary capture (language learners)**

> Find every word or phrase on this screen that a B1-level learner of this language would not know. For each: the word, a one-line meaning, and the sentence it appeared in, copied exactly.

Turn on **screenshot capture** for this one so it reads text inside images and subtitles. Pair it with [flashcards]({{ '/flashcards/' | relative_url }}) and the output becomes a study deck.

**3. Claim check**

> List each factual claim on this screen as a separate line. For each, search the web and mark it supported, disputed, or unverifiable, with one source link. Do not mark a claim supported on the strength of the page it came from.

This one needs **web search** enabled or it will only tell you what the page already says.

## What makes an action prompt work

Four things separate an action you keep from one you delete after a week:

- **Name the output shape.** "One per line," "a table with three columns," "at most 40 words." Actions run on wildly different screens; the shape is the only thing holding the result steady.
- **Say what to do with missing information.** Models fill gaps by default. "Write unassigned rather than guessing" costs you six words and removes the most common failure.
- **Use the two toggles deliberately.** *Screenshot capture* lets the action see text inside images, video subtitles, and apps that block text extraction — useful for learning and receipts, unnecessary for a web article. You drag a selection box over the region first, so frame just the chart or menu rather than the whole screen. *Web search* lets it check the screen against something other than itself, which is the whole point of a fact-check action and pure latency everywhere else — it roughly doubles the wait.
- **Narrow beats clever.** Two sharp actions beat one that tries to branch. "Extract dates" and "extract contacts" both work; "extract the important stuff" does not.

## 500+ ready-made community actions

Before writing your own, check the built-in system actions in the Community Actions browser: **Fact Check** (verdict, reasoning, source links), **Smart Reply**, **ELI5**, **Math Solver**, **Find Calories**, **Find Cheaper Alternatives**, **Conflict Cooler** and more, available in 10 languages. A camera badge marks actions that capture a screenshot and a globe badge those that search the web. One tap adds any of them to your sidebar, and drag-to-reorder keeps your top three at the top.

Actions written by other people are browsable in the same place, and you can publish your own with a Google sign-in. The useful ones are rarely general-purpose: a kanji-breakdown action written by someone in Japan is now used by thousands of learners — the kind of thing that never survives a product roadmap but does fine when whoever needed it just built it.

Every card shows the **actual prompt**, a **Verified** badge where reviewed, upvotes, and **Screenshot** / **Web** capability tags. Added actions are fully editable and bindable like your own.

| Community action | What it does |
| --- | --- |
| **Fact Check** | Checks the claims on your screen, with web search for sources |
| **Find Calories** | Estimates calories and protein from a meal on screen |
| **Gluten Allergy Scan** | Flags gluten risks in ingredients and menus |
| **Describe Image** | Screenshot-backed descriptions of charts, photos, and designs |
| **Link extractor** | Pulls every link out of the current page, ready to copy |

---

## Frequently asked questions

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Can I share my custom actions?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">Yes. Publish them to the Community Actions library with a Google sign-in, and other Arc users can find and add them.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Are there limits on custom actions?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">No limit on how many. You can create unlimited custom actions, and each prompt can run to 40,000 characters, so multi-step instructions fit in one action.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">How accurate is the AI fact checker?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">A fact-check action with web search enabled checks each claim against outside sources and links one. Treat it as a fast first pass and verify anything critical against an authoritative source.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Can actions work without internet?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">No. Running an action needs a connection because the models are cloud-side. Your action configurations are stored on the device and sync to Google Drive if you turn on backup, so a new phone gets your sidebar back.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Is Arc a Tasker alternative?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">Different jobs. Tasker, MacroDroid and Automate trigger on device events — time, location, battery, notifications — and are still the right tools for toggling Wi-Fi or scheduling an SMS. Acting on the content inside an app means brittle simulated taps that break on the next app update. Arc's actions do the language work instead — replies, translation, fact checks, extraction — on whatever is on screen, with you present. Many power users run both.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">How do I open Arc with a shortcut?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">Android: swipe from the screen edge. macOS: press ⌃Space in any window. Windows: press Ctrl+Space. Esc dismisses the menu. On iPhone, you'll be able to bind Arc to the Action Button or a double-tap-on-back gesture.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Can I change the ⌃Space shortcut?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">Yes. Open Settings → Activation, press Record, and choose any combination. Arc detects conflicts with its own action shortcuts and names the action that already owns a key.</p>
</details>

<details style="margin: 20px auto; max-width: 800px; text-align: left;">
  <summary style="font-weight: 600; cursor: pointer; padding: 10px; color: var(--brand);">Is it free?</summary>
  <p style="padding: 10px 20px; color: var(--text-2);">Yes — Arc, custom actions, and Community Actions are free, with 7 AI requests per week. An optional Pro subscription removes the limits across Android, macOS, and Windows on one account.</p>
</details>

---

<div class="download-section">
  <h2>Build your first action free</h2>
  <p style="font-size: 1.1em; color: var(--text-2); margin-bottom: 30px;">
    Free download. Build your first custom action in under a minute.
  </p>
  <a href="https://play.google.com/store/apps/details?id=com.rethink.arc" target="_blank" rel="noopener">
    <img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" alt="Get Arc on Google Play" width="250" height="83" loading="lazy">
  </a>
</div>

---

## Related features

- **[AI Summary &amp; Reader]({{ '/ai-summary-reader/' | relative_url }})** - Automatic text summarization and text-to-speech
- **[AI Writer]({{ '/ai-writer/' | relative_url }})** - Rewrite, reply, and polish text in any app
- **[Smart Extract]({{ '/ai-summary-reader/' | relative_url }}#extract)** - Built-in extraction of dates, contacts and codes
- **[Flashcards]({{ '/flashcards/' | relative_url }})** - Turn captured vocabulary into a study deck

## Available platforms

- **[Arc for Android]({{ '/android/' | relative_url }})** - Download now from Google Play
- **[Arc for iOS]({{ '/ios/' | relative_url }})** - In development
- **[Arc for Mac]({{ '/macos/' | relative_url }})** - Available now, free download
- **[Arc for Windows]({{ '/windows/' | relative_url }})** - Free on the Microsoft Store

<!-- related-posts: generated, see scratchpad linkplan -->
<div class="related-links">
  <h2>More on this</h2>
  <p>Guides that go further on what's above:</p>
  <ul>
    <li><a href="{{ '/2026/10/10/ai-automation-mac/' | relative_url }}">AI Automation on Mac: Run Real AI Actions in Any App</a></li>
    <li><a href="{{ '/2026/09/17/ai-assistant-for-mac/' | relative_url }}">Best AI App for Mac: What Arc Does Beyond ChatGPT</a></li>
  </ul>
</div>
<!-- /related-posts -->
