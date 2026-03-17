# Copilot Instructions — Yubi AppGate Website

## Project Overview

This repository hosts the **GitHub Pages** website for **Yubi AppGate**, an Android app that locks apps behind YubiKey HMAC-SHA1 challenge-response authentication.

- **Live site:** https://appatalks.github.io/Yubi-AppGate/
- **Deployment:** GitHub Pages from `main` branch root (`/`)

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
│   └── styles.css          ← all styling, dark theme, CSS custom properties
├── js/
│   └── script.js           ← nav toggle, FAQ accordion, lightbox, scroll effects
├── assets/
│   └── images/             ← screenshots, SVG logos, Play Store assets
├── .github/
│   └── copilot-instructions.md
└── README.md
```

## Tech Stack

- Static HTML, CSS, JavaScript only — no frameworks, no build step, no dependencies
- Dark theme with neon accents (CSS custom properties in `:root` of `styles.css`)
- Cache-busted via `?v=2` query params on CSS/JS references
- Mobile responsive with breakpoints at 768px and 480px

## Key Conventions

- **Colors:** `--bg-primary: #06060c`, `--accent-cyan: #00d4ff`, `--accent-green: #00ff88`, `--accent-purple: #9b59ff`
- **SVG assets:** `logo-horizontal.svg` (site logo), `app-icon-512.svg` (nav icon + Play Store), `feature-graphic-1024x500.svg` (Play Store)
- **Screenshots:** 5 PNGs in `assets/images/`, displayed in a 5-column grid with lightbox on click
- **Contact links:** All contact references point to GitHub Issues (`https://github.com/appatalks/Yubi-AppGate/issues`)
- **Copy tone:** Natural, conversational. Avoid em-dashes. Use colons for definition lists.

## Customization Notes

- **Google Play link** — Update `play.google.com` URLs across all pages when the app listing changes.
- **Pricing** — Free/Pro pricing cards are on `index.html` and `features.html`.
- **Adding screenshots** — Place PNGs in `assets/images/`, reference them in the screenshots grid in `index.html`.
- **Generating PNGs from SVGs** — Use `rsvg-convert` (e.g. `rsvg-convert -w 512 -h 512 app-icon-512.svg -o app-icon-512.png`).
