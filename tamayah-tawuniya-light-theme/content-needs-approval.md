# Content needing approval: Lifeline option

This file lists the items that need sign-off from Tamayah before launch. Each section says what the site does today
until the item is approved. Last updated 2026-10-22.

To see the "pending approval" markers on the page, open it with `?review=1`, for example `en/index.html?review=1`.
Review mode can also be switched on for every visitor with `REVIEW_MODE = True` in `build.py`.

## 1. Leadership portraits: rights not confirmed

| Person (EN) | Person (AR, as published) | Portrait source supplied | Publication approval | Shown now |
|---|---|---|---|---|
| Mohammed AlSaeed | محمد السعيد | No | No | Monogram |
| Sultan Alkhomashi | سلطان الخمشي | No | No | Monogram |
| Abdullah Abahussain | عبدالله أبا حسين | No | No | Monogram |
| Eng. Mohammed Hamad Al-Quraishah | م. محمد بن حمد آل قريشة | No | No | Monogram |

The request on 2026-10-22 contained template placeholders (`[URL or local path] | approved: [yes/no]`) rather than
sources or approvals, so no image was fetched or published.

**What's needed:** official Tamayah-approved headshots, with written confirmation that Tamayah may publish each one
publicly.

**Requirements for each headshot:**
- At least 800 px wide. Anything under 400 px wide will not be used.
- One consistent background and lighting.
- Shoulders up.

**What happens on approval:**
- The site publishes only optimized 4:5 WebP and JPEG derivatives at 1x and 2x, with explicit width and height and
  `loading="lazy"`.
- Every card gets the same crop, face scale and eye line.
- Alt text will read "Portrait of [name], [role]."
- Source originals are never committed, and images are never hotlinked.

## 2. Arabic spelling of leadership names: unverified

The Arabic names are the ones in the approved dark-option copy. I could not verify them against an official Tamayah or
regulatory source: a web search on 2026-10-22 returned no matching record.

Please confirm the following inconsistencies between EN and AR:
- "Abdullah Abahussain" is one word in English, but "أبا حسين" is two words in Arabic.
- The Arabic CEO name includes "بن" ("م. محمد بن حمد آل قريشة"), but the English name does not
  ("Eng. Mohammed Hamad Al-Quraishah").

## 3. Role titles

The approved copy uses the plural label "Board Members" for one row. Each person now has their own card, so the label
reads "Board Member" / "عضو مجلس المديرين". Please confirm.

## 4. Legal pages

Privacy Policy, Terms of Use and Accessibility Statement have no approved URLs. They appear as plain text (not links)
in the footer. Supply the URLs and they become real links.

## 5. Enquiry form

- **Backend:** no approved endpoint exists. Submitting opens the visitor's email app addressed to `info@tamayah.com`,
  and the page explains this before submission.
- **Privacy and consent wording:** the privacy line and the consent checkbox text are drafts that need legal
  approval. They are tagged "Wording pending approval" in review mode.

## 6. LinkedIn

The link is still the search-results URL inherited from the dark option. No official company page could be verified,
so it is unchanged. Supply the official URL.

## 7. New wording condensed from approved copy

Please sign off:
- The four About pillars.
- The audience-to-service mapping in the audience explorer.
- The one-line "role in the process" for each journey stage.
- The shared care benefit, which uses Elite's wording without Concierge's ", and more".
- The hero image alt text:
  - EN: "A healthcare professional in a white coat in conversation with a man across a desk"
  - AR: "أخصائية رعاية صحية بمعطف أبيض تتحدث مع رجل على مكتب"

## 8. Brand items not verifiable from the Tawuniya guidelines

- **Photo frame:** the Tawuniya photo frame or crop is not specified as a reusable shape, because every image in the
  Figma System Assets is a flattened poster. The hero photo uses a plain rounded rectangle at the card radius.
- **Numerals:** Arabic-Indic vs Western numerals are not specified. No Arabic text node in the guidelines contains
  digits. The site keeps the Western digits used in the approved Arabic copy.
- **Fonts and palette:** the Tawuniya Light and ExtraLight font files are missing, and the Tamayah palette PDF and
  logo clear-space rules have not been received.

## 9. SEO

- **Social preview image:** none is approved yet, so `og:image` and `og:image:alt` are omitted and the Twitter card is
  `summary`.
- **Production domain:** canonical, `hreflang` and `og:url` use the GitHub Pages URLs. Update `SITE_URL` in `build.py`
  when the production domain is known.
