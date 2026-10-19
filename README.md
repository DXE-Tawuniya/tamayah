# Tamayah website (EN / AR)

Static site, no build tooling needed to view it.

    python3 -m http.server 8000     # then open http://localhost:8000/
    python3 build.py                # regenerate pages after editing copy

- `build.py` – all copy (EN + AR) and the section components; outputs `en/*.html`, `ar/*.html`, `index.html` (language redirect).
- `assets/style.css`, `assets/site.js` – design system and progressive-enhancement motion. Fonts are self-hosted.
- Pages: index, about, solutions, why, leadership, contact.

To confirm before launch: `LINKEDIN_URL` (official company page link) and the email `info@tamayah.com`
(the source docx splits it as "I" + "nfo@tamayah.com").
