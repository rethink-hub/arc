---
layout: default
title: Privacy Policy - Arc: AI Reader & Summary
---

<div class="privacy-nav">
  <a href="index.html">← Back to Home</a>
</div>

<div class="privacy-header">
  <h1>Privacy Policy for Arc: AI Reader & Summary</h1>
  <p><strong>Effective Date:</strong> October 12, 2025</p>
  <p><strong>Last Updated:</strong> October 12, 2025</p>
</div>

---

## Introduction

Welcome to Arc: AI Reader & Summary. This policy explains how we handle your data with transparency and care. Our goal is to provide powerful features while respecting your privacy at every step.

## Our Core Privacy Promise

Arc is built to be private by design. Our fundamental promise to you is:

* **You Are in Control:** The app only accesses screen content when you explicitly tap an action in the floating sidebar. It never monitors your screen in the background.
* **Content is Processed, Never Stored on Servers:** When we process your on-screen text for summaries, it is handled ephemerally and is **never stored, saved, or logged on our servers.**
* **Your Data Stays Yours:** Any content you explicitly save is stored **securely on your local device only.** Protected by Android's app sandbox, this data is accessible only to Arc and cannot be seen or accessed by us or other apps.

---

## How We Handle Your On-Screen Data (Sidebar Actions)

When you interact with the floating sidebar, here is exactly what happens with your data:

* **For "AI Summary":** The text content from your screen is sent securely through our backend to the Google Gemini API (or a fallback AI) to generate a summary. This data is used only for this purpose and is immediately discarded.

* **For "AI Read":** The text content is processed in the same way as "AI Summary" to generate a summary first. The resulting summary text is then converted to speech **entirely on your device** using Android's built-in Text-to-Speech (TTS) engine. Your data does not leave your device for the TTS function.

* **For "Save Content":**
    1.  **Consent Required:** When you first tap "Save Content", you'll be asked for permission to capture screenshots. You can grant or deny this permission, and change your choice later in Settings.
    2.  **Screenshot Capture (if permitted):** If you grant permission, a screenshot of your current screen is captured and saved **securely to your local device only**. Screenshots are never taken automatically or in the background.
    3.  **Text Processing:** The on-screen text is processed for an AI summary (same as the "AI Summary" action).
    4.  **Local Storage:** Both the screenshot and summary are saved **securely on your device in Android's protected app storage**. They are never uploaded to our servers unless you choose to back them up to Google Drive.
    5.  **Full Control:** You can delete saved content at any time from within the app, and you can change your screenshot permission in Settings.

---

## Screenshot Permissions & Transparency

We want to be completely transparent about how screenshots work in Arc:

### When Are Screenshots Taken?

* **Only with explicit permission:** You must grant screenshot permission when you first tap "Save Content"
* **Only when you tap the button:** Screenshots are never captured automatically or in the background
* **You can deny or revoke permission:** If you deny permission, content is still saved but without screenshots

### What Happens to Screenshots?

* **Stored locally only:** Screenshots are saved securely on your device
* **Never sent to servers:** Screenshots never leave your device unless you explicitly choose Google Drive backup
* **You control deletion:** Delete any saved content (including screenshots) at any time from the app
* **Android 11+ only:** Screenshot capture requires Android 11 or higher. On older versions, content is saved without screenshots.

### Managing Screenshot Permission

* **In-app control:** Go to Settings > General Settings > Screenshot Permission to enable or disable
* **System settings:** You can also revoke the accessibility service permission in your phone's Settings

### Where Are Screenshots Stored?

* **Location:** Stored securely in your device's internal storage (`/data/data/com.rethink.arc/files/screenshots/`)
* **Security:** Protected by Android's app sandbox; only accessible by Arc app
* **Visibility:** Not visible in your Gallery or to other apps
* **Backups:** Only included in Google Drive backups if you explicitly enable that feature
* **Management:** You can view and delete individual screenshots anytime in the app

---

## Information We Handle for Other Features

#### **Optional Account Information (If You Choose to Sign In)**

Arc is fully functional without an account. However, to enable optional features like Google Drive backup and prepare for future premium services, you can choose to create an account using Google Sign-In.

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

* **Google Gemini API & OpenAI (Fallback):** For generating AI summaries. When you use the Summary or Read features, we send the on-screen text to Gemini's servers for processing. **This text is used only to generate your summary and is not stored by us or Google.** ([Google Privacy Policy](https://policies.google.com/privacy), [OpenAI Privacy Policy](https://openai.com/policies/privacy-policy))
* **Amazon Web Services (AWS):** Our backend, which handles AI requests and stores account information, is hosted on AWS in the **us-east-1** region (Virginia, USA). All data transmission uses encrypted connections (HTTPS/TLS). ([AWS Privacy Policy](https://aws.amazon.com/privacy/))
* **Google Services:** For optional Sign-In and Drive Backup features.
* **Google AdMob:** To display banner ads to non-paying users. ([Google Ad Policy](https://policies.google.com/technologies/ads))

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
* **Retention:** On-screen text for summaries is never retained. Your local data remains until you delete it. Your account information is retained as long as your account is active.

---

## Your Rights and Choices

You have full control over your data. You can manage and delete your locally stored content, revoke permissions in your device settings, and request account deletion by contacting us. Using features like Google Sign-In and Google Drive Backup is completely optional.

---

## Data Deletion

### How to Delete Your Data

**Local Data (Saved Summaries & Screenshots):**

To delete all local app data:
1. Go to your device's **Settings**
2. Navigate to **Apps** or **Applications**
3. Find and select **Arc**
4. Tap **Storage**
5. Tap **Clear Storage** or **Clear Data**
6. Confirm deletion

*Note: This will permanently delete all your saved summaries and screenshots from your device.*

**Account Data (Google Sign-In):**

To delete your account and all associated data from our servers:
1. Email us at **everythingrethink@gmail.com** with subject: "Account Deletion Request"
2. Include your registered email address
3. We will delete your account within 7 business days
4. You will receive confirmation once deletion is complete

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
- Backup data: Automatically deleted when Drive access is revoked

---

## Permissions Explained

Arc requests certain permissions to provide its features. Here's why we need them:

| Permission                  | Purpose                                                                                                 |
| :-------------------------- | :------------------------------------------------------------------------------------------------------ |
| **Accessibility Service** | To read on-screen text and capture screenshots when you explicitly request them. Only active when you tap sidebar actions, never in the background. Screenshot capture requires your consent. |
| **Display Over Other Apps** | To show the floating sidebar, our app's main interface.                                                 |
| **Internet / Network State**| To communicate with AI services, our backend, and load ads.                                             |
| **Foreground Service** | To keep the floating sidebar available and responsive while you use other apps.                         |
| **Receive Boot Completed** | To optionally restart the sidebar service when you reboot your device, so you don't have to open the app again. |
| **Wake Lock** | Required by Android's WorkManager for background tasks (automatic backups and version checks) to complete even when your device goes to sleep. |
| **Post Notifications** | To show notifications for the foreground service (required by Android) and backup status updates in your notification tray. |

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
  <p><em>This privacy policy is effective as of October 12, 2025.</em></p>
  <div class="footer-links" style="margin-top: 30px;">
    <a href="index.html">← Back to Home</a>
    <a href="terms.html">📋 Terms of Service</a>
    <a href="mailto:everythingrethink@gmail.com">📧 Contact Us</a>
  </div>
</div>
