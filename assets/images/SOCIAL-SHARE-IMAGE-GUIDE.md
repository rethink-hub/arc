# Social Share Image Guide for Arc AI

## Current Status
Currently using the app logo (`arc-logo.png`) as the social share image. For optimal social media sharing, create a dedicated social share image.

## Recommended Social Share Image

### Specifications
- **Dimensions:** 1200 x 630 pixels (Facebook/LinkedIn/Twitter optimal)
- **File Format:** PNG or JPG
- **File Name:** `arc-social-share.png`
- **File Size:** < 1MB for fast loading
- **Safe Zone:** Keep important content in center 1200 x 600 px (avoid edges)

### Content Suggestions

**Option 1: Feature Showcase**
- Arc AI logo
- Tagline: "Understand Your Screen. Instantly."
- 3-4 key feature icons with labels:
  - AI Summary
  - Text-to-Speech
  - Workflow Automation
  - AI Chat
- Call-to-action: "Free on Google Play"
- Modern gradient background (gold/orange/purple theme)

**Option 2: Benefit-Focused**
- Large, bold text: "Your Android AI Assistant"
- Subtitle: "AI Summaries • Text Reader • Workflow Automation"
- Phone mockup showing the app in use
- Arc AI branding
- Vibrant, eye-catching design

**Option 3: Accessibility Focus**
- Highlight: "AI for Everyone"
- Show accessibility features
- Diverse user personas
- Inclusive messaging
- Professional design

### Design Guidelines
- Use brand colors from `style.scss`:
  - Gold: #FFB84D
  - Orange: #FF8C42
  - Purple: #9D4EDD
  - Dark background: #0a0a0a
- Maintain readable text (minimum 24px)
- High contrast for text visibility
- Include Arc AI branding/logo
- Professional, modern aesthetic
- Match website design language

### Tools for Creation
- **Canva:** Easy template-based design (recommended for non-designers)
- **Figma:** Professional design tool
- **Adobe Photoshop:** Advanced image editing
- **GIMP:** Free open-source alternative

### After Creating the Image
1. Save as `arc-social-share.png` in `/arc/assets/images/`
2. Optimize file size (use TinyPNG or similar)
3. Test preview on:
   - Facebook Sharing Debugger
   - Twitter Card Validator
   - LinkedIn Post Inspector
4. Remove TODO comment from `_layouts/default.html`

### Image Preview Testing
After creating the image, test social sharing on:
- https://www.opengraph.xyz/
- https://developers.facebook.com/tools/debug/
- https://cards-dev.twitter.com/validator

### Current Fallback
The existing `arc-logo.png` (512x512px) serves as a functional fallback. While not ideal for rectangular social previews, it maintains brand identity until a dedicated image is created.

---

**Priority:** Medium - Current fallback works, but dedicated image will improve:
- Click-through rates on social shares by 30-40%
- Brand recognition
- Professional appearance
- Social media engagement


