# Tamayah — Tawuniya-aligned light option ("Lifeline")

This is a light design direction that sits next to the existing options and does not change them. Before the redesign
I wrote an audit, which is in [`AUDIT.md`](AUDIT.md). It covers the baseline, the verified Tawuniya rules and the open
questions.

- Light option 3: `../tamayah-light-theme/option-3.html`
- Dark option: `../tamayah-dark-theme/`
- **This option:** `./` (redirects to `en/` or `ar/` and keeps any `#hash`)

The site is static and needs no build tools to view.

    python3 -m http.server 8000     # from the repo root, then open http://localhost:8000/tamayah-tawuniya-light-theme/
    python3 build.py                # regenerate en/index.html, ar/index.html and index.html

## Where things live

- `build.py` holds the layout and components. Approved copy is **imported** from `../tamayah-dark-theme/build.py`, so
  the two options never drift apart. The `UI` dictionary holds the only new strings: interface labels plus
  condensations of approved copy. All of them are listed for sign-off in `AUDIT.md` §3.
- `assets/style.css` is the design system, in three layers:
  1. Tawuniya foundation, verified in Figma (`--tw-*`)
  2. Tamayah palette (`--tm-*`)
  3. Derived web tokens, which the guidelines don't specify

  It uses logical properties only, so Arabic RTL works without extra rules.
- `assets/site.js` is vanilla progressive enhancement (about 10 KB, no libraries). Without it every panel is visible and
  the form posts via `mailto:`.
- Fonts: the Tawuniya typeface (400/500/700, WOFF2). Only the 400 weight is preloaded.
- Logo: `logo-320/640.{webp,png}` are resized renditions of `Tamayah_Logo_POS.png`. They are never recoloured, and the
  aspect ratio is preserved.

## The connected shape (official geometry only)

The site uses Tawuniya's connected-shape motif in exactly two places. Both use the **official vector paths** read from
the brand file, scaled uniformly:

| Use | Source | Where |
|---|---|---|
| Hero claim-status visual | Crop behaviour, vector `26:2520` (three lobes) | `CROP_PATH` in `build.py` |
| "Claim closed" completion badge | Detail behaviour, vector `26:2398` (two lobes) | `DETAIL_PATH` in `build.py` |

Elsewhere the site uses separate rounded forms. There are no background grids, construction lines or hand-drawn
connectors anywhere. In RTL the shapes are mirrored with `scaleX(-1)`, which is a transform, not a redraw.

## Interactive components

| Component | Pattern | Keyboard | Deep link |
|---|---|---|---|
| Audience explorer | ARIA tabs | ←/→ (mirrored in RTL), ↑/↓, Home, End | `#audience-insurers` … `#audience-beneficiaries` |
| Claims journey explorer | ARIA tabs + Previous/Next; progress rail | Same as above | `#stage-1` … `#stage-5` |
| Care-service comparison | Side by side on desktop; segmented tabs below 900 px | Same as above | `#suite` |
| Mobile menu | Disclosure with focus trap; the page behind it is `inert` | Esc closes and returns focus to the button | — |
| Enquiry form | Inline validation, error summary (`role=alert`), success message (`role=status`) | Native | `#partner` |

**Enquiry form:** there is no approved backend, so submitting opens the visitor's email app with a pre-filled message to
`info@tamayah.com`. The page says this before submission. No data leaves the browser until the visitor presses Send in
their mail client. To use a real endpoint, change the form's `action` and replace the `mailto` branch in `site.js`.

## Validation results (2026-10-21)

| Check | Result |
|---|---|
| axe-core 4.10.2 (WCAG 2.0/2.1/2.2 A+AA + best practices), EN and AR at 1440 / 834 / 390 px | **0 violations** on all 6 |
| Behaviour suite (Playwright): keyboard, RTL arrows, deep links, focus trap, form, no-JS, reduced motion, target size ≥24 px, heading order, sticky CTA, language switch | **61 / 61 pass** |
| Horizontal overflow, EN and AR at 390 / 834 / 1440 | None |
| html-validate 9.4.1 (recommended; inline-style rule off for the `--d` stagger variables) | 0 problems |
| ESLint 10.1.0 | Clean |
| Contrast of all token pairs used for text (§ below) | ≥ 4.86:1 |

Lighthouse 12.8.2, run on a local http-server with headless Chromium:

| | Performance | Accessibility | Best Practices | SEO | LCP | CLS |
|---|---|---|---|---|---|---|
| Before, mobile EN | 82 | 100 | 100 | 91 | 4.2 s | 0 |
| After, mobile EN | 92–93 | 100 | 100 | 100 | 2.9–3.0 s | 0 |
| After, mobile AR | 92–93 | 100 | 100 | 100 | 2.9–3.0 s | 0 |
| After, desktop EN / AR | 100 | 100 | 100 | 100 | 0.6 s | ≤ 0.007 |

**Text contrast:**

| Text on background | Ratio |
|---|---|
| Dark Blue on Warm White | 15.35 |
| Teal on Warm White | 5.57 |
| Teal on teal-10 tint | 4.86 |
| White on Teal | 6.02 |
| Dark Blue on Neon | 11.38 |
| Warm White on Dark Blue | 15.35 |

**Non-text contrast:**

| Element | Ratio |
|---|---|
| Field border (Smart Gray on white) | 3.27 |
| Segmented-control border | 3.03 |
| Focus ring | ≥ 15.35 |

Smart Gray, Nature Green and Neon fail as text colours on light backgrounds, so they are never used for text.

## Still to confirm

See `AUDIT.md` §3 for the full list. The short version:
- Tawuniya Light/ExtraLight font files
- The Tamayah palette PDF and logo clear-space rules
- The official LinkedIn URL
- Privacy, Terms and Accessibility URLs
- The form backend and its privacy/consent copy
- Leadership portraits
- Sign-off on the condensed copy
