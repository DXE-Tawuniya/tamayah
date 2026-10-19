#!/usr/bin/env python3
"""Tamayah — Tawuniya-aligned light option ("Lifeline") generator.

Copy, information architecture and contact facts are imported from the dark
option's generator (../tamayah-dark-theme/build.py), so both options always
speak with the same words. Only layout, components and a handful of UI labels
live here.

Run:  python3 build.py        -> writes en/index.html, ar/index.html, index.html
"""
import os, sys, html, importlib.util

sys.dont_write_bytecode = True  # never leave a __pycache__ inside the dark option's folder
ROOT = os.path.dirname(os.path.abspath(__file__))
DARK_BUILD = os.path.join(ROOT, "..", "tamayah-dark-theme", "build.py")

_spec = importlib.util.spec_from_file_location("tamayah_dark_build", DARK_BUILD)
dark = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dark)

CONTENT, NAV_ITEMS = dark.CONTENT, dark.NAV_ITEMS
EMAIL, PHONE, X_HANDLE, LINKEDIN_URL = dark.EMAIL, dark.PHONE, dark.X_HANDLE, dark.LINKEDIN_URL

# UI labels that only this layout needs (everything else comes from CONTENT).
UI = {
  "en": {"journey_eyebrow": "The claim lifeline", "journey_h": "Every claim, one connected journey.",
         "pause": "Pause animation", "play": "Play animation", "step": "Step",
         "next": "Next step"},
  "ar": {"journey_eyebrow": "مسار المطالبة", "journey_h": "كل مطالبة، رحلة واحدة مترابطة.",
         "pause": "إيقاف الحركة", "play": "تشغيل الحركة", "step": "الخطوة",
         "next": "الخطوة التالية"},
}

# ---------------------------------------------------------------- SVG pieces
ARROW = '<svg class="ico flip" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
TICK = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
PAUSE = '<svg class="ico ico--pause" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><rect x="6" y="5" width="4" height="14" rx="1.5"/><rect x="14" y="5" width="4" height="14" rx="1.5"/></svg><svg class="ico ico--play" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10-6.5a1 1 0 0 0 0-1.72l-10-6.5A1 1 0 0 0 8 5.5z"/></svg>'

# The Tawuniya "Crop" behaviour: two lobes joined by a lifeline neck.
HOURGLASS = '''<svg class="hourglass" viewBox="0 0 200 400" aria-hidden="true" focusable="false">
  <path d="M0 0H200V80A100 100 0 0 1 100 180A100 100 0 0 1 0 80Z"/>
  <path d="M80 178C90 180 94 184 94 192V208C94 216 90 220 80 222H120C110 220 106 216 106 208V192C106 184 110 180 120 178Z"/>
  <path d="M0 400H200V320A100 100 0 0 0 100 220A100 100 0 0 0 0 320Z"/>
</svg>'''

NECK = '<span class="neck" aria-hidden="true"></span>'


def href(page, ext=""):
    return f"{dict(NAV_ITEMS)[page]}{ext}"


def target(link):
    if "#" in link:
        return "#" + link.split("#", 1)[1]
    return href(link)


def head(eyebrow, h2, lede="", num=None, cls=""):
    n = f'<span class="tag__n">{num}</span>' if num else ""
    ld = f'<p class="lede rv" style="--d:2">{lede}</p>' if lede else ""
    return f'''<div class="shead {cls}"><span class="tag rv">{n}{eyebrow}</span>
    <h2 class="h2 rv" style="--d:1">{h2}</h2>{ld}</div>'''


# ---------------------------------------------------------------- Components
def header(c):
    nav = "".join(f'<li><a href="{href(p)}" data-nav-link>{c["nav"][p]}</a></li>' for p, _ in NAV_ITEMS)
    drawer = "".join(f'<li><a href="{href(p)}"><span>{c["nav"][p]}</span><small>0{i+1}</small></a></li>'
                     for i, (p, _) in enumerate(NAV_ITEMS))
    en_cur = "true" if c["lang"] == "en" else "false"
    ar_cur = "true" if c["lang"] == "ar" else "false"
    lang = (f'<div class="lang" role="group" aria-label="{c["lang_label"]}">'
            f'<a href="../en/index.html" hreflang="en" lang="en" aria-current="{en_cur}">EN</a>'
            f'<a href="../ar/index.html" hreflang="ar" lang="ar" aria-current="{ar_cur}">عربي</a></div>')
    return f'''<header class="header"><div class="wrap header__in">
  <a class="brand" href="#top" aria-label="{c["name"]}"><img src="../assets/Tamayah_Logo_POS.png" width="2400" height="784" alt="{c["name"]}"></a>
  <nav class="nav" aria-label="Primary"><ul>{nav}</ul></nav>
  <div class="header__tools">{lang}
    <a class="btn btn--sm header__cta" href="#partner">{c["cta"]}{ARROW}</a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="drawer" aria-label="{c["menu"]}"><span></span><span></span></button>
  </div>
</div></header>
<div class="drawer" id="drawer"><nav aria-label="Mobile"><ul>{drawer}</ul></nav>
  <a class="btn" href="#partner">{c["cta"]}{ARROW}</a></div>'''


def hero(c):
    h = c["hero"]
    lines = "".join(f'<span class="line"><span style="--i:{i}">{t}</span></span>' for i, t in enumerate(h["lines"]))
    meta = NECK.join(f'<span class="cap cap--chip">{m}</span>' for m in h["meta"])
    last_t, last_s = c["states"][-1]
    return f'''<section class="hero" id="top">
  <div class="gridlines" aria-hidden="true"></div>
  <div class="wrap hero__in">
    <div class="hero__copy">
      <span class="tag fade-up">{h["eyebrow"]}</span>
      <h1 class="h1">{lines}</h1>
      <p class="lede fade-up" style="--d:3">{h["lede"]}</p>
      <div class="hero__actions fade-up" style="--d:4">
        <a class="btn" href="#partner">{h["primary"]}{ARROW}</a>
        <a class="btn btn--outline" href="#services">{h["secondary"]}</a>
      </div>
    </div>
    <div class="hero__art fade-up" style="--d:2" aria-hidden="true">
      <div class="ll ll--v">
        <figure class="cap cap--photo"><img src="../assets/img/consult-desk.jpg" width="1400" height="1050" alt=""></figure>
        {NECK}
        <div class="ll">
          <div class="cap cap--mint"><span class="cap__tick">{TICK}</span><span><b>{last_t}</b><small>{last_s}</small></span></div>
        </div>
      </div>
    </div>
  </div>
  <div class="wrap"><div class="ll ll--meta fade-up" style="--d:5">{meta}</div></div>
</section>'''


def journey(c):
    u = UI[c["lang"]]
    steps = ""
    for i, (t, s) in enumerate(c["states"]):
        steps += f'''<li class="step" data-step="{i}"><div class="step__pill"><span class="step__n"><span class="sr-only">{u["step"]} </span>0{i+1}</span><span class="step__t">{t}</span><span class="step__tick">{TICK}</span></div><p class="step__d">{s}</p></li>'''
    return f'''<section class="section journey" aria-labelledby="journey-h"><div class="wrap">
  <div class="journey__top">
    <div class="shead"><span class="tag rv">{u["journey_eyebrow"]}</span><h2 class="h2 rv" id="journey-h" style="--d:1">{u["journey_h"]}</h2></div>
    <button class="pp rv" type="button" aria-pressed="false" data-label-pause="{u["pause"]}" data-label-play="{u["play"]}" hidden>{PAUSE}<span class="sr-only">{u["pause"]}</span></button>
  </div>
  <ol class="steps rv" style="--d:2" aria-label="{c["stack_aria"]}">{steps}</ol>
</div></section>'''


def ledger(c):
    r = c["reg"]
    return f'''<section class="section ledger" aria-label="{r["tag"]}"><div class="wrap">
  <div class="ledger__box rv">
    <div class="ledger__num"><span class="count"><span data-count="{r["count"]}">{r["count"]:,}</span><sup>+</sup></span><span class="ledger__lbl">{r["count_label"]}</span></div>
    <div class="ledger__txt"><span class="tag">{r["tag"]}</span><p>{r["text"]}</p></div>
  </div>
</div></section>'''


def about(c):
    a = c["about"]
    paras = "".join(f"<p>{p}</p>" for p in a["paras"])
    return f'''<section class="section about" id="about"><div class="wrap split">
  <div class="shead"><span class="tag rv"><span class="tag__n">01</span>{a["eyebrow"]}</span><h2 class="h2 rv" style="--d:1">{a["h1"]}</h2><p class="lede rv" style="--d:2">{a["lede"]}</p></div>
  <div class="prose rv" style="--d:2">{paras}</div></div></section>'''


def audiences(c):
    a = c["aud"]
    items = "".join(
        f'''<li class="aud__i rv" style="--d:{i}"><a class="aud__a" href="{target(link)}"><span class="aud__n">0{i+1}</span><h3 class="h3">{t}</h3><p>{d}</p><span class="aud__go">{ARROW}</span></a></li>'''
        for i, (t, d, link) in enumerate(a["items"]))
    return f'''<section class="section aud"><div class="wrap">
  {head(a["eyebrow"], a["h2"], a["lede"], "02")}
  <ul class="aud__grid">{items}</ul></div></section>'''


def eco(c):
    e = c["eco"]
    svcs = "".join(
        f'''<li class="svc rv" style="--d:{i}"><span class="svc__n">0{i+1}</span><h3 class="h3">{t}</h3><p>{d}</p></li>'''
        for i, (t, d) in enumerate(e["core"]))
    layers = "".join(
        f'''<div class="layer rv" style="--d:{i}"><span class="tag tag--chip">{tag}</span><h3 class="h3">{t}</h3><p>{d}</p></div>'''
        for i, (tag, t, d) in enumerate(e["layers"]))
    return f'''<section class="section eco" id="services">
  <div class="gridlines" aria-hidden="true"></div>
  <div class="wrap">
  {head(e["eyebrow"], e["h2"], e["lede"], "03")}
  <ol class="svcs">{svcs}</ol>
  <div class="layers">{layers}</div>
  <p class="rv eco__more"><a class="link" href="#suite">{e["more"]}{ARROW}</a></p>
</div></section>'''


def suite(c):
    s = c["suite"]

    def col(k, mod):
        d = s[k]
        perks = "".join(f'<li>{TICK}<span><b>{a}</b>{b}</span></li>' for a, b in d["perks"])
        return f'''<article class="tier tier--{mod} rv"><h3 class="h3">{d["t"]}</h3><p class="tier__intro">{d["intro"]}</p><span class="tier__hours">{d["hours"]}</span><ul class="perks">{perks}</ul></article>'''

    return f'''<section class="section suite" id="suite"><div class="wrap">
  <div class="ll ll--suite rv">
    <figure class="cap cap--photo"><img src="../assets/img/care-understood.jpg" width="1400" height="933" alt="" loading="lazy"></figure>
    {NECK}
    <div class="cap cap--teal"><span class="tag tag--on-teal">{s["eyebrow"]}</span><h2 class="h2">{s["h2"]}</h2><p>{s["lede"]}</p></div>
  </div>
  <div class="tiers">{col("concierge", "a")}{col("elite", "b")}</div>
</div></section>'''


def why(c):
    w = c["why"]
    paras = "".join(f"<p>{p}</p>" for p in w["paras"])
    vals = "".join(
        f'<li class="val rv" style="--d:{i}"><span class="val__n">0{i+1}</span><h4 class="h3">{t}</h4><p>{d}</p></li>'
        for i, (t, d) in enumerate(w["values"]))
    return f'''<section class="section why" id="why"><div class="wrap">
  <div class="why__top">
    <div><span class="tag rv"><span class="tag__n">04</span>{w["eyebrow"]}</span>
    <h2 class="quote rv" style="--d:1">{w["quote"]}</h2></div>
    {HOURGLASS}
  </div>
  <div class="prose prose--cols rv">{paras}</div>
  <h3 class="tag rv values__h">{w["values_h"]}</h3>
  <ul class="values">{vals}</ul>
</div></section>'''


def vmc(c):
    v = c["vmc"]
    commit = "".join(f"<p>{p}</p>" for p in v["commit"])
    return f'''<section class="section vmc"><div class="wrap">
  <svg class="vmc__ll" viewBox="0 0 600 200" aria-hidden="true" focusable="false"><rect x="0" y="40" width="250" height="120" rx="60"/><path d="M244 86C256 86 260 96 268 96H332C340 96 344 86 356 86V114C344 114 340 104 332 104H268C260 104 256 114 244 114Z"/><rect x="350" y="0" width="250" height="200" rx="100"/></svg>
  <div class="vmc__vision rv"><span class="tag tag--on-teal">{v["vision_h"]}</span><p class="quote">{v["vision"]}</p></div>
  <div class="vmc__cols">
    <div class="rv"><h3 class="h3">{v["mission_h"]}</h3><p>{v["mission"]}</p></div>
    <div class="rv" style="--d:2"><h3 class="h3">{v["commit_h"]}</h3>{commit}</div>
  </div>
</div></section>'''


def leadership(c):
    l = c["lead"]
    rows = "".join(
        f'''<div class="lead__row rv" style="--d:{i}"><span class="lead__role">{r}</span><ul class="ll ll--names">{NECK.join(f'<li class="cap cap--name">{n}</li>' for n in names)}</ul></div>'''
        for i, (r, names) in enumerate(l["rows"]))
    return f'''<section class="section lead" id="leadership"><div class="wrap">
  <div class="shead"><span class="tag rv"><span class="tag__n">05</span>{l["eyebrow"]}</span><h2 class="h2 rv" style="--d:1">{l["h2"]}</h2></div>
  <div class="lead__rows">{rows}</div></div></section>'''


def cta(c):
    b = c["cta_block"]
    return f'''<section class="section cta" id="partner"><div class="wrap">
  <div class="cta__panel rv">
    <div class="cta__copy">
      <span class="tag">{b["eyebrow"]}</span>
      <h2 class="h1 cta__h">{b["h2"]}</h2>
      <p class="lede">{b["text"]}</p><p>{b["text2"]}</p>
      <div class="cta__actions"><a class="btn" href="mailto:{EMAIL}">{b["email"]}{ARROW}</a><a class="btn btn--outline" href="tel:{PHONE}">{b["call"]}</a></div>
    </div>
    {HOURGLASS}
  </div>
</div></section>'''


def contact(c):
    k = c["contact"]; r = k["rows"]
    return f'''<section class="section contact" id="contact"><div class="wrap split">
  <div class="shead"><span class="tag rv"><span class="tag__n">06</span>{k["eyebrow"]}</span><h2 class="h2 rv" style="--d:1">{k["h2"]}</h2><p class="lede rv" style="--d:2">{k["lede"]}</p>
    <img class="contact__logo rv" style="--d:3" src="../assets/Tamayah_Logo_POS.png" width="2400" height="784" alt="{c["name"]}" loading="lazy"></div>
  <dl class="contact__list rv">
    <div><dt>{r["email"]}</dt><dd><a class="ltr" href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
    <div><dt>{r["phone"]}</dt><dd><a class="ltr" href="tel:{PHONE}">{PHONE}</a></dd></div>
    <div><dt>{r["linkedin"]}</dt><dd><a class="ltr" href="{LINKEDIN_URL}" target="_blank" rel="noopener">{k["linkedin_text"]}</a></dd></div>
    <div><dt>{r["x"]}</dt><dd><a class="ltr" href="https://x.com/{X_HANDLE}" target="_blank" rel="noopener">@{X_HANDLE}</a></dd></div>
  </dl></div></section>'''


def footer(c):
    f = c["footer"]
    nav = "".join(f'<li><a href="{href(p)}">{c["nav"][p]}</a></li>' for p, _ in NAV_ITEMS)
    return f'''<footer class="footer"><div class="wrap">
  <div class="footer__top">
    <div><a class="brand" href="#top" aria-label="{c["name"]}"><img src="../assets/Tamayah_Logo_POS.png" width="2400" height="784" alt="{c["name"]}" loading="lazy"></a><p class="footer__reg">{f["reg"]}</p></div>
    <div><h2 class="footer__h">{f["explore"]}</h2><ul>{nav}</ul></div>
    <div><h2 class="footer__h">{f["contact"]}</h2><ul>
      <li><a class="ltr" href="tel:{PHONE}">{PHONE}</a></li>
      <li><a class="ltr" href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a class="ltr" href="{LINKEDIN_URL}" target="_blank" rel="noopener">LinkedIn · Tamayah</a></li>
      <li><a class="ltr" href="https://x.com/{X_HANDLE}" target="_blank" rel="noopener">X · @{X_HANDLE}</a></li></ul></div>
  </div>
  <div class="footer__bot"><span>{f["rights"]}</span></div>
</div></footer>'''


def render(lang):
    c = CONTENT[lang]
    body = (hero(c) + journey(c) + ledger(c) + about(c) + audiences(c) + eco(c) + suite(c)
            + why(c) + vmc(c) + leadership(c) + cta(c) + contact(c))
    return f'''<!doctype html>
<html lang="{lang}" dir="{c["dir"]}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(c["titles"]["index"], quote=False)}</title>
<meta name="description" content="{html.escape(c["desc"])}">
<meta name="theme-color" content="#F7F6F2">
<link rel="alternate" hreflang="en" href="../en/index.html">
<link rel="alternate" hreflang="ar" href="../ar/index.html">
<link rel="icon" type="image/png" href="../assets/mark.png">
<link rel="preload" href="../assets/fonts/tawuniya-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<a class="skip" href="#main">{c["skip"]}</a>
{header(c)}
<main id="main">
{body}
</main>
{footer(c)}
<script src="../assets/site.js" defer></script>
</body>
</html>
'''


ROOT_INDEX = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tamayah | تماية</title><meta name="theme-color" content="#F7F6F2">
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#F7F6F2;color:#132028;font-family:system-ui,sans-serif;text-align:center}
a{color:#326B73;margin:0 12px;font-size:1.2rem}img{width:220px;height:auto;margin-bottom:28px}</style>
<script>
(function(){var l;try{l=localStorage.getItem('tamayah-lang')}catch(e){}
if(!l){l=(navigator.language||'en').toLowerCase().indexOf('ar')===0?'ar':'en'}
location.replace(l+'/index.html')})();
</script></head>
<body><div><img src="assets/Tamayah_Logo_POS.png" width="2400" height="784" alt="Tamayah تماية"><br><a href="en/index.html">English</a><a href="ar/index.html" lang="ar">العربية</a></div></body></html>
'''


def main():
    for lang in ("en", "ar"):
        os.makedirs(os.path.join(ROOT, lang), exist_ok=True)
        with open(os.path.join(ROOT, lang, "index.html"), "w", encoding="utf-8") as f:
            f.write(render(lang))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(ROOT_INDEX)
    print("built 2 one-page language variants (Tawuniya-aligned light option)")


if __name__ == "__main__":
    main()
