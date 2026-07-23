#!/usr/bin/env python3
"""Generate 1200x630 Open Graph images for Arc pages."""

from PIL import Image, ImageDraw, ImageFont
import os

ASSETS = "assets/images"
SCREENSHOTS = os.path.join(ASSETS, "screenshots")
OUTDIR = ASSETS

BRAND_PURPLE = (108, 49, 255)
DARK_BG = (11, 11, 15)
DARK_BG_2 = (26, 26, 46)
TEXT_WHITE = (255, 255, 255)
TEXT_MUTED = (170, 170, 190)

# Try to load a nice font; fall back to default if unavailable.
def load_font(size):
    candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/ArialHB.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

pages = [
    ("og-arc.png", "Arc: AI Screen Assistant", "Understand any screen, instantly", None),
    ("og-android.png", "Arc for Android", "Free AI screen assistant on Google Play", "02_ai_summary_result.jpg"),
    ("og-ai-summary-reader.png", "AI Summary & Reader", "Summarize & listen on any Android screen", "02_ai_summary_result.jpg"),
    ("og-ai-writer.png", "AI Writer for Android", "Rewrite, reply & polish text anywhere", "03_ai_writer_rewrite_result.jpg"),
    ("og-ai-workflow-automation.png", "AI Workflow Automation", "Build custom AI actions for Android", "06_custom_actions_list_with_active_actions.jpg"),
    ("og-macos.png", "Arc for Mac", "AI screen assistant coming to macOS", None),
    ("og-ios.png", "Arc for iOS", "AI screen assistant coming to iPhone", None),
    ("og-windows.png", "Arc for Windows", "AI screen assistant coming to PC", None),
    ("og-blog.png", "Arc Blog", "AI tips, Android guides & productivity", None),
    ("og-blog-gemini.png", "Gemini Intelligence vs AI Assistants", "What actually helps day-to-day", "06_custom_actions_list_with_active_actions.jpg"),
    ("og-blog-mod-apk.png", "No Arc Mod APK Needed", "Why the real app costs less than you think", None),
]

def make_base():
    img = Image.new("RGB", (1200, 630), DARK_BG)
    draw = ImageDraw.Draw(img)
    # diagonal gradient
    for y in range(630):
        ratio = y / 630
        r = int(DARK_BG[0] + (DARK_BG_2[0] - DARK_BG[0]) * ratio)
        g = int(DARK_BG[1] + (DARK_BG_2[1] - DARK_BG[1]) * ratio)
        b = int(DARK_BG[2] + (DARK_BG_2[2] - DARK_BG[2]) * ratio)
        draw.line([(0, y), (1200, y)], fill=(r, g, b))

    # brand accent glow
    for i in range(200, 0, -2):
        alpha = int(20 * (i / 200))
        draw.ellipse([900 - i, 300 - i, 1200 + i, 630 + i], fill=(BRAND_PURPLE[0], BRAND_PURPLE[1], BRAND_PURPLE[2], alpha))

    # top brand bar
    draw.rectangle([0, 0, 1200, 8], fill=BRAND_PURPLE)
    return img

def add_logo(img):
    logo_path = os.path.join(ASSETS, "arc-logo.png")
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo_size = 80
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        img.paste(logo, (80, 80), logo)

def add_screenshot(img, filename):
    path = os.path.join(SCREENSHOTS, filename)
    if not os.path.exists(path):
        return
    shot = Image.open(path).convert("RGB")
    # target height around 420px, keep aspect ratio
    target_h = 420
    ratio = target_h / shot.height
    target_w = int(shot.width * ratio)
    shot = shot.resize((target_w, target_h), Image.Resampling.LANCZOS)
    # rounded corners mask
    x = 1200 - target_w - 80
    y = (630 - target_h) // 2 + 20
    # drop shadow
    shadow = Image.new("RGBA", (target_w + 20, target_h + 20), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle([10, 10, target_w + 10, target_h + 10], radius=28, fill=(0, 0, 0, 80))
    img = img.convert("RGBA")
    img.alpha_composite(shadow, (x - 10, y - 10))
    # rounded screenshot
    mask = Image.new("L", (target_w, target_h), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle([0, 0, target_w, target_h], radius=24, fill=255)
    img.paste(shot, (x, y), mask)
    return img.convert("RGB")

def generate(filename, title, subtitle, screenshot):
    img = make_base()
    add_logo(img)
    draw = ImageDraw.Draw(img)

    title_font = load_font(56)
    subtitle_font = load_font(30)
    brand_font = load_font(24)

    # brand name
    draw.text((180, 100), "Arc AI", font=brand_font, fill=TEXT_WHITE)

    # wrap title to fit left column
    max_width = 620
    words = title.split()
    lines = []
    current = ""
    for word in words:
        test = current + (" " if current else "") + word
        bbox = draw.textbbox((0, 0), test, font=title_font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)

    y = 210
    for line in lines:
        draw.text((80, y), line, font=title_font, fill=TEXT_WHITE)
        y += 70

    # subtitle
    draw.text((80, y + 20), subtitle, font=subtitle_font, fill=TEXT_MUTED)

    # site url at bottom
    url_font = load_font(20)
    draw.text((80, 560), "arcassistant.app", font=url_font, fill=TEXT_MUTED)

    if screenshot:
        img = add_screenshot(img, screenshot)
        if img is None:
            img = make_base()
            add_logo(img)

    out_path = os.path.join(OUTDIR, filename)
    img.save(out_path, "PNG", optimize=True)
    print(f"Saved {out_path}")

def main():
    for filename, title, subtitle, screenshot in pages:
        generate(filename, title, subtitle, screenshot)

if __name__ == "__main__":
    main()
