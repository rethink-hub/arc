---
layout: default
title: "Privacy Policy - Arc AI: Android & macOS AI Assistant"
description: "Arc AI privacy policy for our Android and macOS AI assistant. Learn how we protect your data, handle AI summaries, and ensure privacy."
keywords: "Arc AI privacy, Android AI app privacy, Mac AI app privacy, AI assistant privacy policy"
og_image: /assets/images/og-arc.png
robots: noindex, follow
redirect_from:
  - /privacy
---

<div class="privacy-nav">
  <a href="{{ '/' | relative_url }}">← Back to Home</a>
</div>

<div class="privacy-header">
  <h1>Privacy Policy for Arc: AI Screen Assistant</h1>
  <p><strong>Effective Date:</strong> December 7, 2025</p>
  <p><strong>Last Updated:</strong> September 6, 2026</p>
</div>

---

## Introduction

Welcome to Arc: AI Screen Assistant. This policy explains how we handle your data with transparency and care. Our goal is to provide powerful features while respecting your privacy at every step.

**Which apps this policy covers.** This policy applies to Arc on **Android** and Arc for **macOS**. The two apps share the same backend, the same AI processing, and the same core privacy promise, but they run on different platforms and therefore use different system permissions, a different payment processor, and a different update mechanism. Wherever behaviour differs, the platform is named explicitly. Sections that mention Google Play, Android permissions, or Firebase Cloud Messaging apply to the **Android app only**; see [macOS Permissions Explained](#macos-permissions-explained) and [Subscription & Billing Information](#subscription--billing-information) for the macOS equivalents.

## Our Core Privacy Promise

Arc is built to be private by design. Our fundamental promise to you is:

* **You Are in Control:** The app only accesses screen content when you explicitly tap an action in the floating sidebar. It never monitors your screen in the background.
* **Content is Processed, Never Stored on Servers:** When we process your on-screen text for summaries, it is handled ephemerally and is **never stored, saved, or logged on our servers.**
* **Your Data Stays Yours:** Any content you explicitly save is stored **securely on your local device only.** On Android this is protected by the app sandbox; on macOS it is stored in Arc's own Application Support container under your user account. In both cases the data is accessible only to Arc and cannot be seen or accessed by us.

---

## How We Handle Your On-Screen Data (Sidebar Actions)

When you interact with the floating sidebar, here is exactly what happens with your data:

* **For "AI Summary":** The text content from your screen is sent securely through our backend to the Google Gemini API to generate a summary. This data is used only for this purpose and is immediately discarded.

* **For "AI Read":** The text content is processed in the same way as "AI Summary" to generate a summary first. The resulting summary text is then converted to speech **entirely on your device** using Android's built-in Text-to-Speech (TTS) engine. Your data does not leave your device for the TTS function.

* **For "AI Writer":** When you tap the AI Writer button, Arc extracts text from your currently focused input field (if any) and captures surrounding conversation context from the screen. This text is sent securely to our AI service to generate rewritten text, grammar fixes, replies, or posts. The processed text is **used only to generate your response and is immediately discarded.** Generated responses are stored **locally on your device only** so you can access previous responses. If you use My Info Vault, your vault content is included in the AI prompt to personalize responses — vault data is stored locally and only sent as part of AI Writer prompts when you explicitly activate the feature.

* **For "Flashcards":** The text content from your screen is sent securely to the Google Gemini API to generate study flashcards (question/hint/answer format). This data is used only for this purpose and is immediately discarded. Generated flashcards are stored **locally on your device only** in your flashcard library.

* **For "Smart Extract":** The text content from your screen is sent securely to the Google Gemini API to identify actionable items (events, reminders, contacts, meeting links, verification codes, phone numbers, email addresses, etc.). This data is used only for extraction and is immediately discarded. Extracted items are displayed for you to act on (e.g., add to calendar, save contact) — they are **not stored on our servers**.

* **For "Save Content":**
    1.  **Consent Required:** When you first tap "Save Content", you'll be asked for permission to capture screenshots. You can grant or deny this permission, and change your choice later in Settings.
    2.  **Screenshot Capture (if permitted):** If you grant permission, a screenshot of your current screen is captured and saved **securely to your local device only**. Screenshots are never taken automatically or in the background.
    3.  **Text Processing:** The on-screen text is processed for an AI summary (same as the "AI Summary" action).
    4.  **Local Storage:** Both the screenshot and summary are saved **securely on your device in Android's protected app storage**. They are never uploaded to our servers unless you choose to back them up to Google Drive.
    5.  **Full Control:** You can delete saved content at any time from within the app, and you can change your screenshot permission in Settings.

---

## Chat with AI Feature

Arc allows you to have conversations about content on your screen through our Chat with AI feature.

### How Chat Data is Handled

* **Chat History:** All chat conversations are stored **locally on your device only**. We do not store your chat history on our servers.
* **Message Processing:** When you send a message, it is sent to our AI service (Google Gemini) along with the relevant context (screen content or summary) to generate a response. This data is processed ephemerally and not stored.
* **Screenshot Attachments:** You can optionally attach screenshots to chat messages by tapping the screenshot button. These screenshots are:
    - Captured only when you explicitly tap the button
    - Stored locally on your device with the chat message
    - Sent securely through our backend to Google Gemini API for that specific message to provide visual context
    - Processed ephemerally and **never stored** on our servers

### Chat Session Types

* **Screen Chat:** Discusses content currently on your screen
* **Summary Chat:** Asks follow-up questions about generated summaries
* **Custom Action Chat:** Discusses results from custom AI actions

---

## AI Call Insights

Arc can analyze your call recordings to provide transcriptions, summaries, action items, and key insights. It offers two modes of operation:

### Two Modes of Operation

1. **Manual Upload:** You can manually select and upload individual audio files for analysis at any time. This mode requires no background setup — you simply pick a file and Arc processes it.

2. **Auto Analysis:** You can optionally set up automatic monitoring of specific folders for new call recordings. **This mode only works when you explicitly set it up** in Call Insight Settings. Arc can **only read files from folders you grant access to** via Android's document picker — it cannot access files outside those folders. This uses Android's scoped storage permissions, meaning Arc has no ability to browse or read any files beyond what you explicitly authorize.

### How Call Insight Data is Handled

* **Audio File Access:** Arc uses the `READ_MEDIA_AUDIO` permission (Android 13+) or `READ_EXTERNAL_STORAGE` (Android 12 and below) to access call recording audio files. For Auto Analysis, access is further restricted to **only the specific folders you explicitly configure** via Android's document picker.
* **Audio Processing:** Audio content is sent securely through our backend to the Google Gemini API for transcription and analysis. This audio data is **processed ephemerally and never stored on our servers.**
* **Local Storage:** Call transcripts, summaries, and extracted insights are stored **locally on your device only**.
* **Background Monitoring (Auto Analysis only):** When Auto Analysis is enabled, Arc uses Android's WorkManager to periodically check your configured folders for new recordings. This monitoring only reads file metadata (name, date, size) to detect new files — it does not access audio content until processing. It cannot access any folders or files beyond what you have explicitly authorized.
* **User Control:** You can enable/disable Auto Analysis, choose which folders to monitor, set file size limits, and switch to Manual Upload only at any time in Call Insight Settings. You can delete any call insight from the app at any time.

---

## My Info Vault

Arc includes a secure local vault where you can store personal or professional information to personalize AI Writer responses.

### How Info Vault Data is Handled

* **Local Storage Only:** All Info Vault entries (title and content) are stored **securely on your device in Android's protected app storage**. They are never uploaded to our servers independently.
* **AI Writer Context:** When you activate AI Writer with Info Vault enabled, your selected vault items are included as context in the AI prompt to generate personalized responses. This data is sent to the AI service **only when you explicitly use AI Writer** and is processed ephemerally.
* **User Control:** You control what information you store in the vault, and you can add, edit, or delete entries at any time.

---

## Custom Actions

Arc allows you to create personalized AI actions with custom prompts.

### Local Custom Actions

* **Storage:** Your custom actions (name, icon, prompt, settings) are stored **locally on your device only**.
* **Screenshot Option:** Each custom action can optionally capture screenshots when executed. This requires your initial screenshot consent.
* **Web Search Option:** Custom actions can optionally use Google Search grounding to access real-time information. When enabled, your query and screen content may be sent to Google Search through the Gemini API.

### How Custom Actions Process Data

When you execute a custom action:
1. Screen text is captured (only when you tap the action)
2. Optional screenshot is captured (if enabled for that action)
3. Your custom prompt and screen content are sent to the AI
4. Results are displayed and can be saved locally
5. Nothing is stored on our servers

---

## Community Actions

Arc features a community where users can share and discover AI actions created by others.

### Publishing Actions

When you choose to **publish** a custom action to the community:

* **What Becomes Public:** Your action's name, icon, and prompt template become publicly visible to all Arc users.
* **Your Identity:** Your email address is displayed as the creator of the action.
* **AI Content Review:** When you publish an action, it is reviewed by our AI service (Google Gemini) to assess whether it is meaningful and appropriate. Actions that are clearly harmful or nonsensical may be rejected. Actions where the assessment is uncertain are added with a pending approval status. Your action's name and prompt are sent to the AI for this review.
* **Server Storage:** Published actions are stored on our servers (AWS DynamoDB) to make them available to the community.
* **Upvotes:** Other users can upvote your actions. Upvote counts are tracked on our servers.

### Your Control Over Published Actions

* **Voluntary:** Publishing is completely optional. You can use custom actions without ever publishing.
* **Unpublish Anytime:** You can remove (unpublish) your actions from the community at any time through the app.
* **Independence:** Deleting a local custom action does not affect its published version, and vice versa.

### Using Community Actions

* **Adding Actions:** When you add a community action to your sidebar, a copy is stored locally on your device.
* **No Tracking:** We do not track which community actions you add or use.

---

## App Management & Installed Apps

Arc includes an App Management feature that lets you control which apps Arc can work with.

### How We Use Installed App Information

* **Permission:** Arc uses the `QUERY_ALL_PACKAGES` permission to display a list of apps installed on your device.
* **Purpose:** This allows you to enable or disable Arc's sidebar for specific apps (e.g., disable Arc in banking apps for privacy).
* **Local Only:** The list of installed apps and your preferences are stored **locally on your device only**. This information is **never sent to our servers** or shared with anyone.
* **Default Protection:** Arc automatically disables itself for nearly 400 sensitive apps by default, including:
    - Banking and financial apps (200+ verified worldwide)
    - Password managers
    - Cryptocurrency wallets and exchanges
    - Government and identity apps

---

## Screenshot Permissions & Transparency

We want to be completely transparent about how screenshots work in Arc:

### When Are Screenshots Taken?

* **Only with explicit permission:** You must grant screenshot permission when you first use a feature that requires it
* **Only when you tap the button:** Screenshots are never captured automatically or in the background
* **You can deny or revoke permission:** If you deny permission, content is still saved but without screenshots

### Screenshot Region Selection

When capturing screenshots for Custom Actions or Smart Extract, you can optionally select a specific region of the screen to capture instead of the full screen. This uses a draggable rectangle overlay. The selected region preference can be remembered for future use. Region selection data stays entirely on your device.

### Screenshot Consent Levels

Arc uses a tiered consent approach:

1. **Save Content:** Full consent dialog (Allow/Deny) because screenshot is automatic
2. **Custom Actions:** Info dialog when you enable screenshot toggle (you chose to enable it)
3. **Screen Chat:** Info dialog when you tap screenshot button (you explicitly requested it)

### What Happens to Screenshots?

* **Stored locally:** Screenshots are saved securely on your device for local viewing and history
* **Sent for AI processing:** When you use features that analyze screenshots (Custom Actions with screenshot enabled, Chat with screenshot attachment), the screenshot is sent securely through our backend to Google Gemini API for visual analysis. These screenshots are **processed ephemerally and never stored** on our servers.
* **Never stored on our servers:** While screenshots may be transmitted for AI processing, they are never saved, logged, or retained on our backend
* **You control deletion:** Delete any saved content (including screenshots) at any time from the app
* **Android 11+ only:** Screenshot capture requires Android 11 or higher. On older versions, content is saved without screenshots.

### Where Are Screenshots Stored?

* **Location:** Stored securely in your device's internal storage (`/data/data/com.rethink.arc/files/screenshots/`)
* **Security:** Protected by Android's app sandbox; only accessible by Arc app
* **Visibility:** Not visible in your Gallery or to other apps
* **Backups:** Only included in Google Drive backups if you explicitly enable that feature
* **Management:** You can view and delete individual screenshots anytime in the app

---

## On-Device Language Detection

Arc uses ML Kit Language Identification to automatically detect the language of content for text-to-speech.

* **Entirely On-Device:** Language detection runs completely on your device using Google's ML Kit.
* **No Data Sent:** No text is sent to external servers for language detection.
* **Purpose:** Enables automatic voice selection to match the content's language for natural pronunciation.
* **User Control:** You can disable auto-voice selection in Speech Settings to use a fixed voice.

---

## Information We Handle for Other Features

#### **Optional Account Information (If You Choose to Sign In)**

Arc is fully functional without an account. However, to enable optional features like Google Drive backup and Community Actions, you can choose to create an account using Google Sign-In.

* **What We Collect:** If you sign in, we collect only your **Google ID** and **Email Address**. This minimal data is stored securely on our backend servers (hosted on AWS) to identify your account.

* **What We DON'T Collect:** We explicitly do NOT collect or store:
  - Your full name
  - Profile picture
  - Any other profile information
  - Friends list or contacts
  - Files from your Google Drive

---

## Subscription & Billing Information

Arc operates on a **freemium** model with optional subscription. The payment processor depends on the platform you use.

**On Android**, subscription billing is handled entirely through **Google Play Billing**.

* **What We Collect:** We do not collect or store your payment card information. Billing, payment processing, and subscription management are all handled by Google Play.
* **Subscription Status:** We may receive notification from Google Play about your subscription status (active, cancelled, expired) to manage your access to premium features.
* **No Payment Data:** All financial information is processed by Google Play and is subject to [Google's Privacy Policy](https://policies.google.com/privacy). We never see or store your credit card details, bank accounts, or other payment instruments.
* **Promo Coupons:** If you use a promotional coupon or discount code, the transaction is processed through Google Play. We do not store any coupon-related payment information.

**On macOS**, Arc is distributed directly from our website rather than the Mac App Store, so subscription billing is handled by **[Dodo Payments](https://dodopayments.com/)**, our merchant of record.

* **How Checkout Works:** When you start a purchase, Arc opens Dodo's secure hosted checkout page in your default web browser. You enter your payment details on Dodo's page — **never inside the Arc app**. Arc receives only the resulting subscription identifier and status.
* **What We Collect:** We do not collect, see, or store your card number, CVC, bank account, or billing address. Those are handled entirely by Dodo Payments as merchant of record and are subject to the [Dodo Payments Privacy Policy](https://dodopayments.com/privacy-policy).
* **Subscription Status:** Our backend receives webhook notifications from Dodo about your subscription lifecycle (created, active, cancelled, expired, payment failed) so we can manage your access to premium features. We store the subscription ID, plan, status, and expiry date against your account — not payment instrument data.
* **Taxes & Invoices:** As merchant of record, Dodo Payments calculates applicable sales tax/VAT/GST and issues your invoice or receipt. Any billing correspondence you receive comes from Dodo.
* **Managing Your Subscription:** You can manage or cancel a macOS subscription from Settings inside Arc, which opens the Dodo customer portal in your browser.

Your subscription entitlement is tied to your Arc account, so a subscription purchased on one platform is recognised when you sign in on the other. Billing itself, however, is always managed by the processor you originally purchased through.

---

## Analytics & Crash Reporting

To improve Arc and fix issues, we use the following services.

**On Android:**

* **Google Analytics for Firebase:** We collect **anonymous usage data** to understand how features are used and improve the app. This includes:
  - Which features you use (e.g., AI Summary, AI Read, Save Content)
  - Screen navigation patterns
  - Settings preferences (without the actual values)
  - App performance metrics
  
  **What we DON'T collect:** Your screen content, personal information, or any text you process.

* **Firebase Crashlytics:** We collect **anonymous crash reports** to identify and fix bugs. This includes:
  - Crash stack traces and error logs
  - Device model and OS version
  - App version and build information
  
  **What we DON'T collect:** Your screen content or personal data. Crash reports contain only technical diagnostic information.

**On macOS:**

* **Google Analytics 4 (Measurement Protocol):** The macOS app cannot embed the Firebase SDK, so it reports the same kind of **anonymous usage events** directly to Google Analytics over HTTPS. This includes which features you use, navigation patterns, and app performance metrics — the same categories listed above for Android.

  Events are tagged with a **randomly generated per-installation identifier** (not your name, device serial, or advertising ID) and, if you are signed in, your Arc account ID so that usage can be reconciled across your devices. Events are queued locally and may be sent when the app next has network access.

  **What we DON'T collect:** Your screen content, the text you process, your AI prompts, or the results Arc generates. Analytics events carry feature names and counts only — never the content itself.

* **Crash Reporting:** The macOS app does **not** include a third-party crash reporting SDK (Crashlytics cannot be built into it). Instead Arc records its own crash reports. If Arc for Mac stops unexpectedly, it writes a report **to your Mac** containing:
  - the error or signal type (for example `SIGSEGV`, or an exception name such as `NSInvalidArgumentException`) and its message
  - the call stack at the moment of the crash
  - the app version, macOS version, and processor architecture
  - a short trail of recent in-app actions and diagnostic flags — feature names and states only

  The report stays on your Mac until the next time you open Arc. At that point Arc sends a **summary** of it — the error type, a truncated message, and the single most relevant line of the call stack — as a `app_exception` analytics event, and then **deletes the local report**. The full stack never leaves your Mac.

  **What we DON'T collect:** your screen content, the text you process, your prompts, or Arc's generated output. Crash reports carry technical diagnostic information only.

  Separately, macOS itself may offer to send a diagnostic report to Apple under your standard Analytics & Improvements settings (**System Settings → Privacy & Security → Analytics & Improvements**). Those go to Apple, not to us.

**Turning macOS collection off.** Both of the above are controlled by a single switch in Arc for Mac: **Settings → Privacy → "Share usage data & crash reports."** It is on by default (matching the Android app). Turning it off stops all analytics and crash reporting immediately, discards anything still queued on your device, and deletes any crash reports waiting to be sent. Nothing further is transmitted unless you turn it back on.

These services collect data anonymously and do not identify you personally. You can review Google's data practices at [Google Privacy Policy](https://policies.google.com/privacy).

---

## Push Notifications

**This section applies to the Android app only.** Arc for macOS does not use Firebase Cloud Messaging and sends no push notifications.

Arc uses Firebase Cloud Messaging (FCM) to send optional push notifications about new features and app updates.

### Purpose of Notifications

* **Feature Announcements:** Learn about new Arc features and improvements
* **Tips & Updates:** Occasional tips for using Arc more effectively
* **Important Updates:** Critical app announcements (rare)

### Opt-In Model

* **Android 13+:** Notification permission is requested during onboarding. You can skip this if you prefer not to receive notifications.
* **Pre-Android 13:** Notifications are enabled by default (no runtime permission required), but you can disable them in your device's notification settings.
* **Your Choice:** You can enable or disable notifications at any time via Android Settings > Apps > Arc > Notifications.

### How Notifications Work

* **Topic-Based:** All users who grant permission are subscribed to an "announcements" topic.
* **Broadcast Only:** The same notification is sent to all subscribers. We do not target individual users.
* **No Personal Data:** Notifications contain only general announcement content - no personal information.
* **Frequency:** We send notifications occasionally (not daily or weekly) - only when there's something meaningful to share.

### Unread Nudge Notifications (Local Reminders)

Arc can send local reminder notifications to encourage you to revisit unread saved content (summaries, flashcards, and call insights).

* **Entirely Local:** These notifications are scheduled and triggered **entirely on your device** using Android's WorkManager. No data is sent to our servers.
* **Throttled:** Nudge notifications are limited to a maximum of 2 per week with at least a 3-day gap between notifications.
* **Conditions:** Notifications are sent only when your reading streak is at risk (3+ days inactive) or when you have unread content piling up (3+ items older than 2 days).
* **User Control:** You can disable these notifications via Android Settings > Apps > Arc > Notifications.

### Data Handling

* **Anonymous Analytics:** We track notification types received (e.g., "feature_announcement") for analytics purposes only.
* **No Content Tracking:** We do not track or store the specific notifications you view or interact with.
* **FCM Token:** A device token is generated by Firebase for delivery purposes. This token is not linked to your personal identity.

---

## Third-Party Services & Data Sharing

We use reputable third-party services and only share the minimum data necessary:

* **Google Gemini API:** Primary AI service for generating summaries, processing custom actions, and chat conversations. When you use these features, we send the relevant text to Google's servers for processing. **This text is used only to generate your response and is not stored by us.** ([Google Privacy Policy](https://policies.google.com/privacy))

* **Google Search Grounding:** When web search is enabled for custom actions, your content may be sent to Google Search through the Gemini API to access real-time information. ([Google Privacy Policy](https://policies.google.com/privacy))

* **OpenAI (Fallback):** Available as a fallback AI provider if Gemini is unavailable. Same data handling principles apply. ([OpenAI Privacy Policy](https://openai.com/policies/privacy-policy))

* **Amazon Web Services (AWS):** Our backend, which handles AI requests and stores account information, is hosted on AWS in the **us-east-1** region (Virginia, USA). All data transmission uses encrypted connections (HTTPS/TLS). ([AWS Privacy Policy](https://aws.amazon.com/privacy/))

* **Google Services:** For optional Sign-In and Drive Backup features.

* **ML Kit Language ID:** On-device language detection. No data is sent to external servers.

* **Google Play In-App Review:** We use Google's In-App Review API to occasionally prompt for app reviews. This is handled entirely by Google Play and we do not collect any data about your review.

* **Google Analytics for Firebase** *(Android)*: Anonymous usage analytics to improve the app experience. ([Firebase Privacy](https://firebase.google.com/support/privacy))

* **Firebase Crashlytics** *(Android)*: Anonymous crash reporting to identify and fix bugs. ([Firebase Privacy](https://firebase.google.com/support/privacy))

* **Firebase Cloud Messaging (FCM)** *(Android)*: Push notification delivery for feature announcements and updates. Only anonymous device tokens are used for delivery. ([Firebase Privacy](https://firebase.google.com/support/privacy))

* **Google Analytics 4 Measurement Protocol** *(macOS)*: Anonymous usage analytics and crash summaries sent directly over HTTPS, as described above. Controlled by Settings → Privacy → "Share usage data & crash reports". ([Google Privacy Policy](https://policies.google.com/privacy))

* **Dodo Payments** *(macOS)*: Merchant of record for macOS subscriptions. Handles checkout, card processing, tax calculation, invoicing, and the subscription customer portal. We never receive your payment instrument details. ([Dodo Payments Privacy Policy](https://dodopayments.com/privacy-policy))

* **Sparkle Updater** *(macOS)*: Arc for Mac checks for new versions by fetching an update feed from `arcassistant.app`. This request is made to our own servers and carries only what an ordinary web request carries (such as your IP address and the app version being checked). No account information is attached, and updates are cryptographically signed so a tampered download is rejected. Arc asks for your permission before enabling automatic update checks, and you can also check for updates manually from Arc's settings.

**We will never sell your personal information.**

---

## Google OAuth Scopes

We use Google Sign-In for two separate, optional features:

**1. Account Authentication (Optional):**
- **Scopes:** `openid`, `email`
- **Purpose:** Create and authenticate your account
- **Access:** Email address only (no profile, no Drive access)

**2. Google Drive Backup (Optional - Requires Separate Consent):**
- **Scope:** `https://www.googleapis.com/auth/drive.appdata`
- **Purpose:** Backup and restore your saved summaries
- **Access:** ONLY the app-specific hidden folder (appDataFolder)
- **Limitation:** Cannot access any other files in your Drive or other apps' data

Both features are completely optional and can be used independently or not at all.

---

## Data Security & Retention

* **Security Measures:** 
  - **Data in Transit:** All network communications use HTTPS/TLS encryption to protect data while it travels between your device and our servers.
  - **Local Device Storage:** Data saved on your device is protected by Android's app sandbox security model, which isolates your app data and makes it accessible only to Arc (not to us, other apps, or other users of your device).
  - **Server Storage:** Account information stored on our AWS servers is protected by AWS security measures and access controls.

* **Retention:** 
  - On-screen text for summaries: Never retained
  - Chat conversations: Local only, until you delete them
  - Custom actions: Local only, until you delete them
  - Flashcards: Local only, until you delete them
  - Call insights and transcripts: Local only, until you delete them
  - Info Vault entries: Local only, until you delete them
  - AI Writer previous responses: Local only, until you delete them
  - Published community actions: Server-stored until you unpublish
  - Your local data: Remains until you delete it
  - Your account information: Retained as long as your account is active

---

## Your Rights and Choices

You have full control over your data. You can manage and delete your locally stored content, revoke permissions in your device settings, and request account deletion by contacting us. Using features like Google Sign-In and Google Drive Backup is completely optional.

---

## Data Deletion

### How to Delete Your Data

**Local Data (Saved Summaries, Screenshots, Chat History, Custom Actions, Flashcards, Call Insights, Info Vault, AI Writer Responses):**

To delete all local app data:
1. Go to your device's **Settings**
2. Navigate to **Apps** or **Applications**
3. Find and select **Arc**
4. Tap **Storage**
5. Tap **Clear Storage** or **Clear Data**
6. Confirm deletion

*Note: This will permanently delete all your saved summaries, screenshots, chat history, custom actions, flashcards, call insights, Info Vault entries, and AI Writer responses from your device.*

**Account Data (Google Sign-In):**

To delete your account and all associated data from our servers:
1. Email us at **everythingrethink@gmail.com** with subject: "Account Deletion Request"
2. Include your registered email address
3. We will delete your account within 7 business days
4. You will receive confirmation once deletion is complete

**Published Community Actions:**

To remove actions you've published:
1. Go to **Custom Actions** in the app
2. Find your published action
3. Tap to edit and select **Unpublish**
4. The action will be removed from the community immediately

**Google Drive Backups:**

To delete backups stored in Google Drive:
1. Go to your **Google Account settings**
2. Navigate to "Manage your data & privacy"
3. Under "Apps with account access", find **Arc**
4. Click "Remove access" to revoke permissions
5. Backups in Drive AppData will be automatically deleted when access is revoked

**Data Deletion Timeline:**
- Local data: Immediate upon deletion via device settings
- Account data: Within 7 business days of request
- Published actions: Immediate upon unpublishing
- Backup data: Automatically deleted when Drive access is revoked

---

## Android Permissions Explained

Arc for Android requests certain permissions to provide its features. Here's why we need them:

| Permission                  | Purpose                                                                                                 |
| :-------------------------- | :------------------------------------------------------------------------------------------------------ |
| **Accessibility Service** | To read on-screen text and capture screenshots when you explicitly request them. Only active when you tap sidebar actions, never in the background. Screenshot capture requires your consent. |
| **Display Over Other Apps** | To show the floating sidebar, our app's main interface.                                                 |
| **Internet / Network State**| To communicate with AI services and our backend.                                                        |
| **Foreground Service** | To keep the floating sidebar available and responsive while you use other apps.                         |
| **Receive Boot Completed** | To optionally restart the sidebar service when you reboot your device, so you don't have to open the app again. |
| **Wake Lock** | Required by Android's WorkManager for background tasks (automatic backups and version checks) to complete even when your device goes to sleep. |
| **Post Notifications** | To show notifications for the foreground service (required by Android), backup status updates, and optional push notifications about new features and updates. On Android 13+, you can skip this permission during onboarding. |
| **Query All Packages** | To display a list of installed apps in App Management settings, allowing you to enable/disable Arc for specific apps. This data never leaves your device. |
| **Read Media Audio (Android 13+)** | To access call recording audio files for AI Call Insights (Manual Upload and Auto Analysis). For Auto Analysis, only reads files from folders you explicitly grant access to via Android's document picker — cannot access files outside those folders. Audio content is processed for transcription and insights via AI and never stored on our servers. On Android 12 and below, Read External Storage is used instead. |
| **Request Ignore Battery Optimizations** | To request that Android exempts Arc from aggressive battery optimization, preventing the floating sidebar service from being killed on devices with aggressive OEM battery management. This permission is only shown on devices where it is needed and does not access any personal data. |

---

<h2 id="macos-permissions-explained">macOS Permissions Explained</h2>

Arc for macOS is a notarized app distributed directly from our website. It is **not sandboxed**, because the macOS Accessibility APIs it depends on are unavailable to sandboxed apps — this is also why Arc for Mac is not distributed through the Mac App Store. macOS still gates every sensitive capability behind a system permission prompt that only you can grant, and you can revoke any of them at any time in **System Settings → Privacy & Security**.

| macOS Permission | Why Arc Needs It | When It Is Used |
| :--------------- | :--------------- | :-------------- |
| **Accessibility** | To read the text of the window you are currently working in, and to insert text back into an editor or input field when you use AI Writer. This is the core capability that lets Arc work on whatever is already on your screen instead of making you copy and paste. | **Only when you invoke an action** — pressing the Arc hotkey or choosing an action from the Arc menu. Arc does **not** read your screen in the background, does not log keystrokes, and does not monitor apps you are not acting on. Arc additionally skips known password managers. |
| **Screen Recording** | To capture a screenshot of the current screen or a region you select, for actions that need visual context (for example a custom action with screenshots enabled, or Save Content). macOS classifies any screen capture under this permission name. | **Only when you run an action that requires an image.** Screenshots are sent for AI processing and are **not stored on our servers**. Arc does not record video and does not capture your screen continuously. |
| **Calendar** | To create calendar events from details Arc extracts with Smart Extract (for example a meeting or a deadline). | **Only when you tap the "Add to Calendar" action** on an extracted item. Arc writes the event you approve; it does not read, upload, or scan your existing calendar. |
| **Reminders** | To create reminders from tasks and follow-ups Arc extracts with Smart Extract. | **Only when you tap the "Add Reminder" action** on an extracted item. Arc does not read or upload your existing reminders. |
| **Apple Events / Automation** | To paste generated text into the app you are working in when direct insertion is not supported, and to ask a supported browser for the URL of the page you are acting on (so summaries can cite their source). | **Only during an action you invoked.** macOS prompts you separately for each app Arc needs to talk to. |
| **Network Access** | To communicate with our backend and the AI services that generate your results, and to check for app updates. | Whenever you run an action that needs AI processing, and for periodic update checks. |
| **Launch at Login** *(optional)* | To start Arc automatically when you log in, so the global hotkey is available without opening the app first. | Only if you enable it during onboarding or in Settings. Accesses no personal data. |

**What Arc for Mac never does:** it does not run a keylogger, does not read your screen when you have not invoked an action, does not take screenshots without an explicit action, does not upload files from your Mac, and does not transmit the contents of your Keychain, Photos, Contacts, or Messages.

If you deny or later revoke Accessibility or Screen Recording, the features that depend on them stop working, but the rest of the app continues to function. Revoking permission in System Settings takes effect immediately.

---

## Children's Privacy (COPPA Compliance)

Arc is **not intended for and does not knowingly collect information from children under 13 years of age**.

* We do not market to children
* We do not knowingly collect personal information from children under 13
* If we discover we have collected data from a child under 13, we will delete it immediately
* Parents who believe their child has provided us with information should contact us immediately at **everythingrethink@gmail.com**

---

## Contact Us

If you have any questions about this policy, please contact us at: **everythingrethink@gmail.com**

**Response Time:** We aim to respond to all inquiries within 7 business days.

---

<div class="footer-section">
  <p><em>This privacy policy is effective as of December 7, 2025. Last updated September 6, 2026.</em></p>
  <div class="footer-links" style="margin-top: 30px;">
    <a href="{{ '/' | relative_url }}">← Back to Home</a>
    <a href="/terms/">📋 Terms of Service</a>
    <a href="mailto:everythingrethink@gmail.com">📧 Contact Us</a>
  </div>
</div>
