# Audit: Tawuniya-aligned light option ("Lifeline")

Audit date: 2026-10-21. Baseline: `main` at `dd09483`. This note was written before the redesign and is kept as the record of
what was found. The results after the redesign are in [the final section](#after-the-redesign).

## 1. Current-state issues (baseline)

I captured EN and AR at 1440, 834 and 390 px with reduced motion enabled.

**Layout and hierarchy**
- The page is long and text-heavy: about 11,600 px on desktop, 13,700 on tablet and 16,500 on mobile (EN).
- The regulatory statement appears three times: in the hero chips, the ledger box and the footer.
- "More than processing transactions" appears twice: in the audience intro and in the Why Tamayah paragraphs.
- The About and Why Tamayah sections are long paragraphs with no scannable structure.
- The Who we serve cards are static, and every one links to the same few anchors.
- Concierge Medicine and Elite & VIP are two long stacked lists that repeat four identical benefits.
- Leadership is a plain list of rows. There is no real enquiry path, only mailto and tel buttons.

**Brand fidelity**
- A visible 6-column background grid is drawn in the hero and the services section. In the Tawuniya file this grid is
  documentation only.
- The connecting "neck" between pills is a hand-drawn 28 px mask, and the hourglass and vision-band shapes were drawn
  from memory. None of them match the official construction (section 2).
- Display type uses negative letter-spacing (−0.035em), but the guidelines use 0% throughout.
- Cards and boxes have drop shadows, but the guideline material is flat.

**Responsive**
- At 834 px the hero becomes one column, with a very large photo before the trust chips.
- The services rail and the journey turn into long vertical stacks.

**Accessibility**
- axe-core reports 0 violations. The remaining gaps are behavioural:
  - The mobile drawer uses `inert` but does not trap focus while open.
  - There is no form, so there is no validation or live-region feedback.
  - The journey animates automatically. It has a pause button, but it is still autoplay.

**RTL**
- Mirroring works, using logical properties throughout.
- The language switch only keeps the section if the URL already has a hash.

**Performance**
- The hero JPG is 167 KB and is the LCP element on mobile. The header logo is a 2400×784 PNG of 165 KB, used at about
  148 px wide.
- There is no `srcset`, and `hreflang` uses relative URLs.

**Motion**
- Reveals move 26 px, more than the 16 px maximum.
- The auto-cycling journey loops while the section is visible.
- Hover zoom on the photo is decorative.

**Baseline Lighthouse 12.8.2** (mobile, local http-server, headless Chromium 1194):

| Page | Performance | Accessibility | Best Practices | SEO | LCP | CLS |
|---|---|---|---|---|---|---|
| EN | 82 | 100 | 100 | 91 | 4.2 s | 0 |
| AR | 88 | 100 | 100 | 91 | 3.9 s | 0 |

SEO fails on `hreflang` because the URLs are relative. Performance is held back by LCP from the hero image.

## 2. Verified Tawuniya design rules

Source: Figma `Brand-Assets---Guidelines`, page "Assets", section "System Assets" (`68:3`). I read it through the Figma
API, including raw vector paths and text properties.

| Area | Verified rule | Evidence |
|---|---|---|
| Typeface | "Tawuniya" family, in ExtraLight, Light, Regular, Medium and Bold | Text nodes in `68:3` |
| Tracking | Letter-spacing 0% on every text node; line height Auto | Every text node in `68:3` |
| Display type | Large statements and labels in Light; big numerals in ExtraLight, with the unit in Regular at about ⅓ size ("86 %") | Grid example "86%" |
| Labels | Uppercase labels at 0% tracking ("DOWNLOAD FULL REPORT", "MARGINS") | Same |
| Background | Warm white `#F7F6F2` / `#F8F6F1` (identical to Tamayah Warm White), with white `#FFFFFF` surfaces | Fill census |
| Elevation | No drop shadows in the system assets: flat colour planes only | No effects found |
| Connected shape: Crop | Vector `26:2520`, 3160.48 × 639.84: three lobes joined by sculpted bridges. Bridge thickness = 26.64 = **4.16 %** of shape height. The lobe ends sweep inward over about ½ the height into small fillets (≈ 38 × 33). | Raw path data |
| Connected shape: Detail | Vector `26:2398`, 410.48 × 78.8: two pills, bridge 3.28 = **4.16 %** of height, the same construction rule | Raw path data |
| Box | Rounded boxes whose corner radius is ≈ 4 % of box width (40.3 on 1013.8; 51.8 on 690). Boxes attach to their tab with the same filleted bridge. | `26:2861`, `26:2812` |
| Shapes / buttons | Pills (stadiums) for labels, and the "اتصل الآن" call-to-action with an arrow in a circle | Grid example |
| Imagery | Photography or illustration placed inside lifeline crops, never as a full-bleed decorative overlay | Behaviour 01–04 |
| Grid | 6×6 / 6×12 layout grids with margins and gutters. **They are documentation aids, not visible on final artwork.** | "Lifeline Grid" `26:4066` |

How these rules are applied:
- **Connected shape:** the website uses only the two official paths above, verbatim, scaled uniformly. They are never
  redrawn or stretched non-uniformly, and no generic connector is used.
- **Grid:** no grid lines appear anywhere in the site.

## 3. Unverified items and open questions

1. **Light and ExtraLight weights.** The guidelines use Tawuniya Light and ExtraLight for display type and numerals, but
   only 400/500/700 files exist in the repo. Display type therefore uses Regular 400. I did **not** substitute another
   font.
2. **Web type scale, spacing scale, breakpoints and icon set.** These are not specified in the Figma file, which only
   holds poster-scale examples. The site's values are derived and labelled as such in `assets/style.css`.
3. **Card radius token.** I derived it from the Box ratio (≈ 4 % of width). An exact web token was not available.
4. **Tamayah palette PDF and approved logo file.** Both are on the requester's machine (`~/Downloads`) and could not be
   read from this cloud session. Hex values come from the brief; the logo is the repo copy
   `Tamayah_Logo_POS.png` (2400×784). Clear-space rules for the Tamayah logo are unverified.
5. **Derived tints.** The site uses mixes of approved colours (for example teal 10 % on warm white). The palette may
   define official tints.
6. **Arabic numerals.** The guidelines do not specify Arabic-Indic vs Western digits. The existing approved Arabic copy
   uses Western digits, so I kept them.
7. **LinkedIn URL** is still the search URL inherited from the dark option. The official company page is unverified:
   a web search on 2026-10-21 found no Tamayah company page, so the link is left unchanged.
8. **Privacy, Terms and Accessibility pages** have no approved URLs, so the footer shows labelled placeholders.
9. **Enquiry form.** There is no approved backend endpoint, and the privacy and consent copy needs legal approval.
10. **Leadership portraits** have not been approved, so the leadership cards use monograms.
11. **Audience-to-service mapping and stage "role" lines** are condensed from existing approved copy. They need content
    owner sign-off.
12. **Shared care benefit wording.** Concierge's "Proactive check-ups" adds ", and more"; the shared line uses Elite's
    wording.
13. **Brand motion principles.** The Figma file has no motion specification, so the motion follows the brief.

14. **Singular leadership role.** Each person now has their own card, so the approved plural row label "Board Members"
    is shown as "Board Member" / "عضو مجلس المديرين".
15. **Error colour.** The Tamayah palette has no error or alert colour. Errors therefore use Dark Blue with an icon and
    explicit text, so colour is never the only signal.

## After the redesign

Full results are in `README.md` → "Validation results".

| Issue | Resolution |
|---|---|
| Visible background grid | Removed everywhere |
| Hand-drawn connector, hourglass and vision shapes | Replaced by the official paths `26:2520` and `26:2398`, used in only two places |
| Regulatory statement ×3 | Now appears only in the hero trust strip and the footer |
| "More than processing transactions" ×2 | Now appears once, in the audience intro |
| Long About and Why paragraphs | Replaced by a lead statement plus 4 pillars, and a lead statement plus 5 values |
| Static audience cards | Replaced by an accessible tabbed audience explorer with deep links and a preselecting CTA |
| Autoplay journey | Replaced by a user-driven journey explorer with a completion state. Nothing moves automatically. |
| Repeated care benefits | Shared benefits shown once, with differences per service |
| No enquiry path | Validated `mailto` enquiry form with live regions; honest copy about what submission does |
| Drawer without a focus trap | Focus trap, `inert` page, and Esc that returns focus |
| Relative `hreflang` | Absolute URLs plus `x-default` and canonical (SEO 91 → 100) |
| Stock-photo LCP | Abstract claim-status visual; mobile Performance 82 → 92–93 |
| 26 px reveal movement | 16 px, 600 ms, 70 ms stagger |
| Mobile page height | Page height (EN): 11,634 → 9,705 px on desktop and 16,550 → 14,086 px on mobile |

## Connector geometry verification (2026-10-21)

On 2026-10-21 I re-read both official vectors from Figma and compared them with the constants in `build.py`:

| Figma node | Shipped constant | SVG commands | Numbers compared | Max deviation |
|---|---|---|---|---|
| `26:2520` Crop, 3160.48 × 639.84 | `CROP_PATH` | identical (174 tokens) | 142 | 0.0001 units (2-dp rounding) |
| `26:2398` Detail, 410.48 × 78.8 | `DETAIL_PATH` | identical (106 tokens) | 86 | 0.0000 units |

A side-by-side render of Figma node `26:2519` and the site's `.status__shape` shows the same construction.

These two official paths are the only connected shapes in the site. There are 0 occurrences of `.gridlines`, `.neck`,
`--neck-h`, `--neck-v`, CSS masks or `repeating-linear-gradient` in the HTML, CSS, JS and generator.
