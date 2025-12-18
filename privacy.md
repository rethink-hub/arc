---
layout: default
title: "Privacy Policy - Arc AI: Android AI Assistant"
description: "Arc AI privacy policy for our Android AI assistant app. Learn how we protect your data, handle AI summaries, and ensure privacy in our AI productivity tool."
keywords: "Arc AI privacy, Android AI app privacy, AI assistant privacy policy"
---

<div class="privacy-nav">
  <a href="index.html">← Back to Home</a>
</div>

<div class="privacy-header">
  <h1>Privacy Policy for Arc: AI Screen Assistant</h1>
  <p><strong>Effective Date:</strong> December 7, 2025</p>
  <p><strong>Last Updated:</strong> December 7, 2025</p>
</div>

---

## Introduction

Welcome to Arc: AI Screen Assistant. This policy explains how we handle your data with transparency and care. Our goal is to provide powerful features while respecting your privacy at every step.

## Our Core Privacy Promise

Arc is built to be private by design. Our fundamental promise to you is:

* **You Are in Control:** The app only accesses screen content when you explicitly tap an action in the floating sidebar. It never monitors your screen in the background.
* **Content is Processed, Never Stored on Servers:** When we process your on-screen text for summaries, it is handled ephemerally and is **never stored, saved, or logged on our servers.**
* **Your Data Stays Yours:** Any content you explicitly save is stored **securely on your local device only.** Protected by Android's app sandbox, this data is accessible only to Arc and cannot be seen or accessed by us or other apps.

---

## How We Handle Your On-Screen Data (Sidebar Actions)

When you interact with the floating sidebar, here is exactly what happens with your data:

* **For "AI Summary":** The text content from your screen is sent securely through our backend to the Google Gemini API to generate a summary. This data is used only for this purpose and is immediately discarded.

* **For "AI Read":** The text content is processed in the same way as "AI Summary" to generate a summary first. The resulting summary text is then converted to speech **entirely on your device** using Android's built-in Text-to-Speech (TTS) engine. Your data does not leave your device for the TTS function.

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

## Third-Party Services & Data Sharing

We use reputable third-party services and only share the minimum data necessary:

* **Google Gemini API:** Primary AI service for generating summaries, processing custom actions, and chat conversations. When you use these features, we send the relevant text to Google's servers for processing. **This text is used only to generate your response and is not stored by us.** ([Google Privacy Policy](https://policies.google.com/privacy))

* **Google Search Grounding:** When web search is enabled for custom actions, your content may be sent to Google Search through the Gemini API to access real-time information. ([Google Privacy Policy](https://policies.google.com/privacy))

* **OpenAI (Fallback):** Available as a fallback AI provider if Gemini is unavailable. Same data handling principles apply. ([OpenAI Privacy Policy](https://openai.com/policies/privacy-policy))

* **Amazon Web Services (AWS):** Our backend, which handles AI requests and stores account information, is hosted on AWS in the **us-east-1** region (Virginia, USA). All data transmission uses encrypted connections (HTTPS/TLS). ([AWS Privacy Policy](https://aws.amazon.com/privacy/))

* **Google Services:** For optional Sign-In and Drive Backup features.

* **ML Kit Language ID:** On-device language detection. No data is sent to external servers.

* **Google Play In-App Review:** We use Google's In-App Review API to occasionally prompt for app reviews. This is handled entirely by Google Play and we do not collect any data about your review.

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
  - Published community actions: Server-stored until you unpublish
  - Your local data: Remains until you delete it
  - Your account information: Retained as long as your account is active

---

## Your Rights and Choices

You have full control over your data. You can manage and delete your locally stored content, revoke permissions in your device settings, and request account deletion by contacting us. Using features like Google Sign-In and Google Drive Backup is completely optional.

---

## Data Deletion

### How to Delete Your Data

**Local Data (Saved Summaries, Screenshots, Chat History, Custom Actions):**

To delete all local app data:
1. Go to your device's **Settings**
2. Navigate to **Apps** or **Applications**
3. Find and select **Arc**
4. Tap **Storage**
5. Tap **Clear Storage** or **Clear Data**
6. Confirm deletion

*Note: This will permanently delete all your saved summaries, screenshots, chat history, and custom actions from your device.*

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

## Permissions Explained

Arc requests certain permissions to provide its features. Here's why we need them:

| Permission                  | Purpose                                                                                                 |
| :-------------------------- | :------------------------------------------------------------------------------------------------------ |
| **Accessibility Service** | To read on-screen text and capture screenshots when you explicitly request them. Only active when you tap sidebar actions, never in the background. Screenshot capture requires your consent. |
| **Display Over Other Apps** | To show the floating sidebar, our app's main interface.                                                 |
| **Internet / Network State**| To communicate with AI services and our backend.                                                        |
| **Foreground Service** | To keep the floating sidebar available and responsive while you use other apps.                         |
| **Receive Boot Completed** | To optionally restart the sidebar service when you reboot your device, so you don't have to open the app again. |
| **Wake Lock** | Required by Android's WorkManager for background tasks (automatic backups and version checks) to complete even when your device goes to sleep. |
| **Post Notifications** | To show notifications for the foreground service (required by Android) and backup status updates in your notification tray. |
| **Query All Packages** | To display a list of installed apps in App Management settings, allowing you to enable/disable Arc for specific apps. This data never leaves your device. |

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
  <p><em>This privacy policy is effective as of December 7, 2025.</em></p>
  <div class="footer-links" style="margin-top: 30px;">
    <a href="index.html">← Back to Home</a>
    <a href="terms.html">📋 Terms of Service</a>
    <a href="mailto:everythingrethink@gmail.com">📧 Contact Us</a>
  </div>
</div>
