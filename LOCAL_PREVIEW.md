# Preview Privacy Policy Locally (Optional)

If you want to preview your privacy policy on your local machine before pushing to GitHub, follow these steps.

## Prerequisites

- Ruby installed (version 2.7 or higher)
- Bundler gem installed

## Setup

```bash
# Install Ruby (if not already installed)
# On macOS with Homebrew:
brew install ruby

# Install Bundler
gem install bundler

# Navigate to the privacy policy folder
cd /Users/deepakchougule/Projects/Arc/arc-privacy-policy

# Install dependencies
bundle install
```

## Run Local Server

```bash
# Start Jekyll server
bundle exec jekyll serve

# Or with live reload:
bundle exec jekyll serve --livereload
```

Your privacy policy will be available at:
```
http://localhost:4000/arc-privacy-policy/
```

## Making Changes

1. Edit `index.md`
2. Save the file
3. If using `--livereload`, your browser will automatically refresh
4. Otherwise, manually refresh the browser

## Stop Server

Press `Ctrl+C` in the terminal to stop the server.

## Notes

- Local preview is **optional** - you can deploy directly to GitHub Pages without testing locally
- The local preview may look slightly different from GitHub Pages
- GitHub Pages automatically builds and deploys when you push changes

## Troubleshooting

### "Command not found: bundle"

Install Bundler:
```bash
gem install bundler
```

### Ruby version errors

Update Ruby:
```bash
# On macOS:
brew upgrade ruby

# Or use rbenv/rvm for version management
```

### Port already in use

Use a different port:
```bash
bundle exec jekyll serve --port 4001
```

---

**This is optional** - you can skip local preview and deploy directly to GitHub Pages!

