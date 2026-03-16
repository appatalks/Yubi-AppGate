# Yubi AppGate — Website

This repository hosts the **GitHub Pages** website for **Yubi AppGate**, an Android app that locks apps behind YubiKey HMAC-SHA1 challenge-response authentication.

🔗 **Live site:** [https://appatalks.github.io/Yubi-AppGate/](https://appatalks.github.io/Yubi-AppGate/)

## Pages

| Page | File | Purpose |
|------|------|---------|
| Home | `index.html` | App overview, features, pricing, download link |
| Features | `features.html` | Detailed feature descriptions |
| How It Works | `how-it-works.html` | Step-by-step setup and usage guide |
| Support | `support.html` | FAQ, troubleshooting, contact |
| Privacy Policy | `privacy.html` | Privacy policy (required for Google Play) |
| Security | `security.html` | Authentication architecture explanation |

## Structure

```
/
├── index.html
├── features.html
├── how-it-works.html
├── support.html
├── privacy.html
├── security.html
├── css/
│   └── styles.css
├── js/
│   └── script.js
├── assets/
│   └── images/          ← screenshot and image assets
└── README.md
```

## Deploy to GitHub Pages

1. **Push this repo** to `https://github.com/appatalks/Yubi-AppGate`.

2. Go to **Settings → Pages** in the GitHub repository.

3. Under **Source**, select:
   - **Branch:** `main`
   - **Folder:** `/ (root)`

4. Click **Save**. The site will be live at:
   ```
   https://appatalks.github.io/Yubi-AppGate/
   ```

5. *(Optional)* To use a custom domain, add a `CNAME` file to the repo root containing your domain, and configure DNS accordingly.

## Replace Screenshot Placeholders

The home page includes placeholder cards for app screenshots. To replace them with real images:

1. Take screenshots on your Android device (setup screen, app selection, lock screen).

2. Save them in `assets/images/` — for example:
   ```
   assets/images/screenshot-setup.png
   assets/images/screenshot-apps.png
   assets/images/screenshot-lock.png
   ```

3. Open `index.html` and find the `<!-- Screenshots -->` section. Replace each placeholder `<div>` with an `<img>` tag:

   ```html
   <!-- Before -->
   <div class="screenshot-placeholder">
     <span class="placeholder-icon">📱</span>
     <span>Setup Screen</span>
   </div>

   <!-- After -->
   <img src="assets/images/screenshot-setup.png"
        alt="Yubi AppGate setup screen"
        style="border-radius:20px;width:100%;">
   ```

4. Commit and push. The screenshots will appear on the live site.

## Customization

- **Google Play link** — Update the `play.google.com` URLs in all pages once the app is published.
- **Contact email** — The support email is set to `appatalks@closetemail.com`. Change it in `support.html`, `privacy.html`, and `security.html` if needed.
- **Pricing** — The Free/Pro pricing cards are on `index.html` and `features.html`. Update pricing details as needed.
- **Colors** — Edit the CSS custom properties at the top of `css/styles.css` to change the color scheme.

## Tech Stack

- Static HTML, CSS, JavaScript only
- No frameworks, no build step, no dependencies
- Mobile responsive
- Dark theme with neon accents
- Accessible color contrast and keyboard navigation

## License

This website content is proprietary. The Yubi AppGate source code is maintained in a separate private repository.
