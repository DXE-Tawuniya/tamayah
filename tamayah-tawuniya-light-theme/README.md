# Tamayah — Tawuniya-aligned light option ("Lifeline")

A new light design direction that sits next to the existing options. It does not change them.

- Light option 3: `../tamayah-light-theme/option-3.html`
- Dark option: `../tamayah-dark-theme/`
- **This option:** `./` (redirects to `en/` or `ar/`)

The site is static and needs no build tools to view.

    python3 -m http.server 8000     # from the repo root, then open http://localhost:8000/tamayah-tawuniya-light-theme/
    python3 build.py                # regenerate en/index.html, ar/index.html and index.html

## Where things live

- `build.py` holds the layout and components. **Copy is not duplicated here.** The generator imports `CONTENT`,
  `NAV_ITEMS` and the contact facts from `../tamayah-dark-theme/build.py`, because stakeholders preferred the dark
  option's content, sections and information architecture. If you edit copy there, run `python3 build.py` here too.
  The only extra strings are a few UI labels (the claim-journey heading and the pause/play button), kept in `UI`.
- `assets/style.css` is the design system. It uses logical properties only, so Arabic RTL works without extra rules.
- `assets/site.js` is progressive enhancement. The page is fully usable without it.
- Fonts: the Tawuniya typeface (400/500/700), converted to WOFF2 from `../tamayah-light-theme/assets/fonts/`.
- Images: `consult-desk.jpg` and `care-understood.jpg`, resized from `../tamayah-light-theme/assets/img/`.
- Logo: `Tamayah_Logo_POS.png` (2400×784). It is always rendered with its intrinsic width and height and `height:auto`,
  so its proportions never distort.

## Design system in brief

**Foundation (Tawuniya brand guidelines, Figma "System Assets").** The Lifeline system: stadium and pill shapes joined
by a thin neck with soft fillets ("Complete" and "Crop" behaviours), a visible 6-column lifeline grid on a warm paper
background, large numerals inside rounded crops ("Box"), the Tawuniya typeface, and pill buttons.

**Identity (Tamayah palette and logo).**

| Token | Hex | Use |
|---|---|---|
| `--ink` | `#132028` | Text, secondary CTA on mint, active nav |
| `--teal` | `#326B73` | Primary CTA, tags, the vision band, completed claim steps |
| `--mint` | `#80EABA` | Highlight moments: the hero word pill, the active claim step, the partner panel |
| `--green` / `--gray` | `#7EAC8A` / `#809197` | Reserved for decoration (not used for text, since contrast is too low) |
| `--paper` | `#F7F6F2` | Page background |

Tints such as `--teal-tint`, `--mint-tint` and `--teal-deep` are derived from these colours.

**Accessibility.** Every text pair meets WCAG AA (axe-core reports no violations in EN or AR). There is a visible 3px
focus ring, a skip link, a mobile drawer that is `inert` when closed and closes with Esc, and a pause control for the
auto-advancing claim journey (WCAG 2.2.2). `prefers-reduced-motion` turns all motion off.

To confirm before launch (inherited from the dark option): `LINKEDIN_URL` and the email address `info@tamayah.com`.
