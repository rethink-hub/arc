# Assets Directory

This directory contains custom assets for the Arc GitHub Pages website.

## Directory Structure

```
assets/
└── css/
    └── style.scss    # Custom CSS styling for Arc website
```

## Custom CSS (style.scss)

This SCSS file extends the Cayman theme with custom styling:

### Features
- **Brand Colors:** Arc's signature gold (#FFB84D) and dark theme
- **Gradient Effects:** Animated text and button gradients
- **Card Layouts:** Feature cards with hover effects
- **Responsive Design:** Mobile-first approach
- **Animations:** Smooth transitions and effects
- **Typography:** Optimized readability

### How It Works
Jekyll automatically processes this SCSS file and includes it in your pages. The file:
1. Imports the base Cayman theme
2. Adds custom variables and styles
3. Is compiled to CSS by GitHub Pages

## Adding More Assets

You can add more assets to enhance your site:

### Images
Create an `images/` folder:
```
assets/
├── css/
└── images/
    ├── logo.png
    ├── screenshot1.png
    └── app-icon.png
```

Use in markdown:
```markdown
![Arc Logo](assets/images/logo.png)
```

### JavaScript
Create a `js/` folder:
```
assets/
├── css/
└── js/
    └── custom.js
```

Include in your layout or page:
```html
<script src="{{ '/assets/js/custom.js' | relative_url }}"></script>
```

### Fonts
Download and add custom fonts:
```
assets/
├── css/
└── fonts/
    ├── CustomFont-Regular.woff2
    └── CustomFont-Bold.woff2
```

## Performance Tips

1. **Optimize images** - Use compressed PNG/JPG or WebP
2. **Minimize CSS** - Jekyll does this automatically
3. **Use SVG for icons** - Better than raster images
4. **Lazy load images** - For better initial page load

## Customization

To customize the colors, edit the CSS variables in `style.scss`:

```scss
:root {
  --accent-gold: #FFB84D;        /* Your primary color */
  --background-dark: #1a1a1a;    /* Background */
  --text-primary: #FFFFFF;       /* Main text */
  --text-secondary: #B0B0B0;     /* Secondary text */
}
```

---

See [CUSTOM_STYLING_GUIDE.md](../CUSTOM_STYLING_GUIDE.md) for complete styling documentation.

