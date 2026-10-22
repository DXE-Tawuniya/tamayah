# Content needing approval: Lifeline option

This file lists the items that need sign-off from Tamayah before launch. Each section says what the site does today
until the item is approved. Last updated 2026-10-22.

To see the "pending approval" markers on the page, open it with `?review=1`, for example `en/index.html?review=1`.
Review mode can also be switched on for every visitor with `REVIEW_MODE = True` in `build.py`. Outside review mode the
markers are `display:none`, so screen readers do not announce them; the accessibility tree is checked for this.

## 1. Leadership portraits: not published

The stakeholder supplied four source URLs on 2026-10-22 and approved them for use. Publishing rights are still
unconfirmed. The quality rule is all-or-nothing: every portrait must be at least ~400 px wide, sharp, and show the
correct person, otherwise all four cards keep their monograms.

| Person | Source host | Result |
|---|---|---|
| Mohammed AlSaeed | media.licdn.com | **Download failed.** The session's network proxy refused the host (HTTP 403 on CONNECT). The URL also requests a 200×200 rendition (`shrink_200_200`), which is below the quality bar. |
| Sultan Alkhomashi | assets.maestronewsroom.com | **Download failed.** Proxy refused the host (403). |
| Abdullah Abahussain | forbesme-prestaging-media.s3.us-east-2.amazonaws.com | Downloaded (outside the repo). **Fails the quality bar: 267 × 267 px.** Not upscaled, not used. |
| Eng. Mohammed Hamad Al-Quraishah | encrypted-tbn0.gstatic.com | **Download failed.** Proxy refused the host (403). This is a search-engine thumbnail, which is normally well under 400 px. |

**Current state:** all four cards keep their monograms. No portrait file was committed, and the site references no
third-party image host.

**What's needed:**
- Official Tamayah headshots, at least 800 px wide, with written confirmation that Tamayah may publish each one
  publicly.
- To publish them, add the derivatives under `assets/leadership/` (for example `mohammed-alsaeed-1x.webp`) and switch
  the cards from monogram to portrait. Nothing else on the page changes.

## 2. Photo licensing and approval: unconfirmed

| Photo | Source | Status |
|---|---|---|
| Hero (consultation at a desk) | Recovered from git `94ee53f`, originally `tamayah-light-theme/assets/img/consult-desk.jpg` | Licence and approval unconfirmed |
| "Private by design" (doctor holding a patient's hands) | Recovered from git `94ee53f`, originally `tamayah-light-theme/assets/img/care-understood.jpg` | Licence and approval unconfirmed |

Both are repo assets from the existing light option. Their licence for public use on the Tamayah site needs
confirmation.

## 3. LinkedIn

Tamayah has no verified LinkedIn company page. LinkedIn has been removed from the Partner contact list (EN + AR); X
stays.

**Action:** re-add LinkedIn when the company page exists, as a row in the direct-contact list in `build.py`.

## 4. Legal pages

Privacy Policy, Terms of Use and Accessibility Statement have no approved URLs. They appear as plain text in the footer:
no links, no tab stops. Supply the URLs to turn them into links.

## 5. Arabic spelling of leadership names: unverified

The names are as published in the approved dark-option copy. No official source was found.

Please confirm:
- "Abdullah Abahussain" is one word in English, but "أبا حسين" is two words in Arabic.
- The Arabic CEO name includes "بن" ("م. محمد بن حمد آل قريشة"), but the English name does not
  ("Eng. Mohammed Hamad Al-Quraishah").
- The singular role "Board Member" / "عضو مجلس المديرين" is used because each person has their own card. The approved
  copy uses the plural "Board Members" for the row.

## 6. Arabic numerals

The Tawuniya guidelines do not specify Arabic-Indic vs Western numerals: no Arabic text node in the Figma System Assets
contains digits. The site keeps the Western digits used in the approved Arabic copy.

## 7. Fonts, palette and logo

- **Fonts:** Tawuniya Light and ExtraLight files are not in the repo, so display type uses Regular 400.
  - The Tawuniya 400/500/700 fonts are served as per-script subsets (Latin and Arabic) to cut load time. Please
    confirm the font licence allows subsetting for web use.
- **Palette:** the Tamayah palette PDF has not been received. Hex values come from the brief.
- **Logo:** clear-space rules for the Tamayah logo have not been received.

## 8. Enquiry form

- **Backend:** no approved endpoint exists. Submitting opens the visitor's email app addressed to `info@tamayah.com`,
  and the page says so.
- **Privacy and consent wording:** the privacy line and the consent checkbox text are drafts that need legal approval.
  They are tagged "Wording pending approval" in review mode.

## 9. Social preview image and production domain

- **Social preview image:** none is approved yet, so `og:image` and `og:image:alt` are omitted and the Twitter card is
  `summary`.
- **Production domain:** canonical, `hreflang` and `og:url` use the GitHub Pages URLs. Update `SITE_URL` in `build.py`
  at launch.

## 10. New or changed copy

Please sign off each item. The EN and AR versions are listed together.

**About lead (new 2026-10-22).** This is the approved About sentence:
- EN (verbatim): "From medical authorization management and claims processing to settlement and financial
  reconciliation, our solutions are designed to deliver greater efficiency, accuracy, transparency and speed."
- AR (verbatim, minus the leading "و"): "تشمل حلولنا إدارة الموافقات الطبية، ومعالجة المطالبات، والتسويات المالية،
  والمطابقة والتسوية المحاسبية، بما يسهم في تعزيز الكفاءة والدقة والشفافية وسرعة الإنجاز."

**About pillar 3 (changed 2026-10-22).** "Close partnership" / "شراكة وثيقة". The body is from the approved
Why-Tamayah sentence:
- EN: "We work closely with our partners to understand their operational needs and deliver solutions that support
  their objectives."
- AR: "نعمل بشكل وثيق مع شركائنا لفهم احتياجاتهم التشغيلية وتقديم حلول تدعم أهدافهم."

**About pillars 1, 2 and 4.** These are condensed from approved copy:

| Pillar | EN | AR |
|---|---|---|
| 1 | Advanced technology | التقنيات المتقدمة |
| 2 | Specialized expertise | الخبرات المتخصصة |
| 4 | Compliance | الالتزام |

**Audience explorer.**
- The services listed for each audience.
- The call-to-action labels, for example "Enquire as an insurer" / "استفسر بصفتك شركة تأمين".

**Claims journey.**
- The "role in the process" line for each of the five stages.
- The heading and intro.

**Care comparison.**
- The shared benefit uses Elite's wording, without Concierge's ", and more".
- The labels "Included in both services" / "مشمولة في الخدمتين" and "Distinctive to this service" /
  "ما يميز هذه الخدمة".

**Alt text.**

| Photo | EN | AR |
|---|---|---|
| Hero | "A healthcare professional in a white coat in conversation with a man across a desk" | "أخصائية رعاية صحية بمعطف أبيض تتحدث مع رجل على مكتب" |
| Care (new 2026-10-22) | "A doctor holding an older woman's hands during a consultation" | "طبيبة تمسك بيدي امرأة مسنّة أثناء استشارة" |

**Form.** Every label, hint, error message, the success message and the mailto explanation.

**Footer.** The legal item names: "Privacy Policy", "Terms of Use", "Accessibility Statement" / "سياسة الخصوصية",
"شروط الاستخدام", "بيان إمكانية الوصول".

## 11. Brand items not verifiable from the Tawuniya guidelines

- **Photo frame:** the Tawuniya photo frame or crop is not specified, because every image in the Figma System Assets
  is a flattened poster. Both photos use a plain rounded rectangle at the card radius.
- **Connected shape:** the "Claim closed" badge uses the official Detail vector `26:2398`. It was verified against
  Figma, with a maximum deviation of 0.0001 units.
