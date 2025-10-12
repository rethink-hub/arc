---
layout: default
title: Privacy Policy - Arc: AI Reader & Summary
---

<div class="privacy-nav">
  <a href="index.html">← Back to Home</a>
</div>

<div class="privacy-header">
  <h1>Privacy Policy for Arc: AI Reader & Summary</h1>
  <p><strong>Effective Date:</strong> October 7, 2025</p>
</div>

---

## Introduction

Welcome to Arc: AI Reader & Summary. This policy explains how we handle your data with transparency and care. Our goal is to provide powerful features while respecting your privacy at every step.

## Our Core Privacy Promise

Arc is built to be private by design. Our fundamental promise to you is:

* **You Are in Control:** The app only accesses screen content when you explicitly tap an action in the floating sidebar. It never monitors your screen in the background.
* **Content is Processed, Never Stored on Servers:** When we process your on-screen text for summaries, it is handled ephemerally and is **never stored, saved, or logged on our servers.**
* **Your Data Stays Yours:** Any content you explicitly save is stored **encrypted only on your local device.** We cannot see or access this data.

---

## How We Handle Your On-Screen Data (Sidebar Actions)

When you interact with the floating sidebar, here is exactly what happens with your data:

* **For "AI Summary":** The text content from your screen is sent securely through our backend to the Google Gemini API (or a fallback AI) to generate a summary. This data is used only for this purpose and is immediately discarded.

* **For "AI Read":** The text content is processed in the same way as "AI Summary" to generate a summary first. The resulting summary text is then converted to speech **entirely on your device** using Android's built-in Text-to-Speech (TTS) engine. Your data does not leave your device for the TTS function.

* **For "Save Content":**
    1.  **Consent Required:** When you first tap "Save Content", you'll be asked for permission to capture screenshots. You can grant or deny this permission, and change your choice later in Settings.
    2.  **Screenshot Capture (if permitted):** If you grant permission, a screenshot of your current screen is captured and saved **encrypted to your local device only**. Screenshots are never taken automatically or in the background.
    3.  **Text Processing:** The on-screen text is processed for an AI summary (same as the "AI Summary" action).
    4.  **Local Storage:** Both the screenshot and summary are saved **encrypted only on your device**. They are never uploaded to our servers unless you choose to back them up to Google Drive.
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

---

## Information We Handle for Other Features

#### **Optional Account Information (If You Choose to Sign In)**

Arc is fully functional without an account. However, to enable optional features like Google Drive backup and prepare for future premium services, you can choose to create an account using Google Sign-In.

* **Google Account Information:** If you sign in, we collect your **Google ID** and **Email Address**. This is stored securely on our backend servers (hosted on AWS) to identify your account. We **do not** collect your full name or profile picture.

#### **Anonymous Technical Data**

To fix bugs and improve the app, we collect anonymous, non-personal data like device model, OS version, and crash logs. This data is not linked to your identity.

---

## Third-Party Services & Data Sharing

We use reputable third-party services and only share the minimum data necessary:

* **Google Gemini API & OpenAI (Fallback):** For generating AI summaries. ([Google Privacy Policy](https://policies.google.com/privacy), [OpenAI Privacy Policy](https://openai.com/policies/privacy-policy))
* **Amazon Web Services (AWS):** Our backend, which handles AI requests and stores account information, is hosted on AWS. ([AWS Privacy Policy](https://aws.amazon.com/privacy/))
* **Google Services:** For optional Sign-In and Drive Backup features.
* **Google AdMob:** To display banner ads to non-paying users. ([Google Ad Policy](https://policies.google.com/technologies/ads))

**We will never sell your personal information.**

---

## Data Security & Retention

* **Encryption:** All data is encrypted in transit using HTTPS/TLS. All data you save on your device and any account information on our servers are encrypted at rest.
* **Retention:** On-screen text for summaries is never retained. Your local data remains until you delete it. Your account information is retained as long as your account is active.

---

## Your Rights and Choices

You have full control over your data. You can manage and delete your locally stored content, revoke permissions in your device settings, and request account deletion by contacting us. Using features like Google Sign-In and Google Drive Backup is completely optional.

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

---

## Contact Us

If you have any questions about this policy, please contact us at: **everythingrethink@gmail.com**

---

<div class="footer-section">
  <p><em>This privacy policy is effective as of October 7, 2025.</em></p>
  <div class="footer-links" style="margin-top: 30px;">
    <a href="index.html">← Back to Home</a>
    <a href="terms.html">📋 Terms of Service</a>
    <a href="mailto:everythingrethink@gmail.com">📧 Contact Us</a>
  </div>
</div>
