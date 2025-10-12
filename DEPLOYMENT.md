# Deployment Guide for Arc Website

This guide will walk you through deploying your Arc landing page and privacy policy to GitHub Pages.

## 📋 Prerequisites

- GitHub account
- Git installed on your computer
- This `arc-privacy-policy` folder

## 🚀 Step-by-Step Deployment

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **+** icon in the top right → **New repository**
3. Configure your repository:
   - **Repository name:** `arc-privacy-policy`
   - **Description:** "Privacy Policy for Arc AI Summary App"
   - **Visibility:** ✅ **Public** (required for free GitHub Pages)
   - ❌ Do NOT initialize with README (we already have one)
4. Click **Create repository**

### Step 2: Initialize Git and Push Files

Open terminal in the `arc-privacy-policy` folder and run:

```bash
# Navigate to the folder
cd /Users/deepakchougule/Projects/Arc/arc-privacy-policy

# Initialize Git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial privacy policy for Arc app"

# Add your GitHub repository as remote
# Replace YOUR-USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR-USERNAME/arc-privacy-policy.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/YOUR-USERNAME/arc-privacy-policy`
2. Click **Settings** (gear icon at the top)
3. In the left sidebar, scroll down and click **Pages**
4. Under "Build and deployment":
   - **Source:** Deploy from a branch
   - **Branch:** Select `main` and `/ (root)`
   - Click **Save**

### Step 4: Wait for Deployment

1. Click the **Actions** tab in your repository
2. You'll see a workflow running called "pages build and deployment"
3. Wait for the green checkmark (usually 1-2 minutes)
4. Once complete, go back to Settings → Pages
5. You'll see: **"Your site is live at https://YOUR-USERNAME.github.io/arc-privacy-policy/"**

### Step 5: Verify Your Website

1. Click the link or visit: `https://YOUR-USERNAME.github.io/arc-privacy-policy/`
2. Your landing page should be displayed with custom styling and the Cayman theme
3. Check the beautiful features:
   - Gradient "Arc" title with glow effect
   - Feature cards that lift on hover
   - Animated buttons and transitions
   - Responsive mobile design
4. Click "View Privacy Policy" to navigate to the privacy policy page
5. Verify all sections are visible and properly formatted on both pages
6. Test on mobile device or resize browser window

## 📝 Your Website URLs

Once deployed, your website will be available at:

**Landing Page:**
```
https://YOUR-USERNAME.github.io/arc-privacy-policy/
```

**Privacy Policy Page:**
```
https://YOUR-USERNAME.github.io/arc-privacy-policy/privacy.html
```

**Save the privacy policy URL** - you'll need it for:
- Google Play Store listing (Data Safety section)
- Android app integration (Settings → Privacy Policy)
- User inquiries

## 🔄 Making Updates

To update your website:

**Updating the landing page:**
```bash
# Edit index.md with your changes
git add index.md
git commit -m "Update landing page - [describe changes]"
git push
```

**Updating the privacy policy:**
```bash
# Edit privacy.md with your changes
git add privacy.md
git commit -m "Update privacy policy - [describe changes]"
git push
```

**Important:** Always update the "Last Updated" date at the top of `privacy.md` when making privacy policy changes.

GitHub Pages will automatically rebuild within 1-2 minutes after you push changes.

## 🎨 Custom Styling

Your Arc website includes beautiful custom HTML and CSS styling:
- Modern gradient effects and animations
- Arc brand colors (Gold #FFB84D)
- Responsive design for all devices
- Feature cards with hover effects
- Professional layout and typography

See [CUSTOM_STYLING_GUIDE.md](CUSTOM_STYLING_GUIDE.md) for customization options.

## ✅ Next Steps

After deployment, you should:

1. ✅ **Test both URLs** - Make sure landing page and privacy policy are accessible
2. ✅ **Test navigation** - Verify links between pages work correctly
3. ✅ **Update Android app** - Add the privacy policy URL (`https://YOUR-USERNAME.github.io/arc-privacy-policy/privacy.html`) to your app configuration
4. ✅ **Update Play Store** - Add privacy policy URL to Google Play Console → Data Safety
5. ✅ **Update README.md** - Replace `[your-username]` with your actual GitHub username
6. ✅ **Bookmark URLs** - Keep both URLs handy for future reference

## 🛠️ Troubleshooting

### "404 Not Found" after deployment

- Wait 5 minutes and try again (initial deployment can be slow)
- Check Settings → Pages to ensure it says "Your site is live"
- Make sure repository is public
- Verify the branch is set to `main` and folder is `/ (root)`

### Theme not showing correctly

- Check that `_config.yml` exists in the repository root
- Verify `theme: jekyll-theme-cayman` is present in `_config.yml`
- Try triggering a rebuild by making a small change and pushing

### Changes not appearing

- Check Actions tab for build errors
- GitHub Pages can take 1-5 minutes to reflect changes
- Hard refresh your browser (Ctrl+F5 or Cmd+Shift+R)

## 📧 Need Help?

If you encounter issues:
1. Check [GitHub Pages documentation](https://docs.github.com/en/pages)
2. Review the Actions tab for error messages
3. Ensure all files are committed and pushed correctly

## 🔒 Security Notes

- Keep the repository **public** (required for free GitHub Pages)
- Do NOT commit sensitive information (API keys, passwords, etc.)
- The privacy policy itself is meant to be public
- This is separate from your main Android app code repository

---

**Estimated Time:** 10-15 minutes for complete deployment

Good luck! 🚀

