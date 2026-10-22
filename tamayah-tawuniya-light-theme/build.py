#!/usr/bin/env python3
"""Tamayah — Tawuniya-aligned light option ("Lifeline") generator.

Approved copy, information architecture and contact facts are imported from the
dark option's generator (../tamayah-dark-theme/build.py). This file owns the
layout, the components and a small set of UI strings (UI below). Every new
string in UI is either interface wording or a condensation of approved copy,
and is listed for sign-off in AUDIT.md.

Run:  python3 build.py        -> writes en/index.html, ar/index.html, index.html
"""
import os, re, sys, html, importlib.util

sys.dont_write_bytecode = True  # never leave a __pycache__ inside the dark option's folder
ROOT = os.path.dirname(os.path.abspath(__file__))
DARK_BUILD = os.path.join(ROOT, "..", "tamayah-dark-theme", "build.py")
SITE_URL = "https://dxe-tawuniya.github.io/tamayah/tamayah-tawuniya-light-theme/"  # change at the production domain
# Review mode shows "pending approval" helper text. It is also switched on per visit with ?review=1 (site.js).
REVIEW_MODE = False

_spec = importlib.util.spec_from_file_location("tamayah_dark_build", DARK_BUILD)
dark = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dark)

CONTENT, NAV_ITEMS = dark.CONTENT, dark.NAV_ITEMS
EMAIL, PHONE, X_HANDLE, LINKEDIN_URL = dark.EMAIL, dark.PHONE, dark.X_HANDLE, dark.LINKEDIN_URL

# ---------------------------------------------------------------- Official Tawuniya geometry
# Read verbatim from the Tawuniya brand file (Figma "System Assets").
# Never redraw it or scale it non-uniformly.
# Detail behaviour, vector 26:2398 — two pills joined by the same bridge construction (4.16 % of height).
DETAIL_W, DETAIL_H = 410.48, 78.8
DETAIL_PATH = ("M99.8 78.8C119.64 78.8 136 64.16 138.8 45.12C139.12 42.8 141.12 41.04 143.48 41.04L156.6 41.04"
               "C158.96 41.04 160.92 42.76 161.28 45.12C164.04 64.16 180.44 78.8 200.28 78.8L371.08 78.8"
               "C392.84 78.8 410.48 61.16 410.48 39.4C410.48 17.64 392.84 0 371.08 0L200.28 0"
               "C180.44 0 164.08 14.64 161.28 33.68C160.96 36 158.96 37.76 156.6 37.76L143.48 37.76"
               "C141.12 37.76 139.16 36.04 138.8 33.68C136.04 14.64 119.64 0 99.8 0L39.4 0"
               "C17.64 0 0 17.64 0 39.4C0 61.16 17.64 78.8 39.4 78.8L99.8 78.8Z")

# ---------------------------------------------------------------- UI strings (see AUDIT.md §3 for sign-off)
UI = {
"en": {
  "trust_h": "Regulatory standing",
  "hero_alt": "A healthcare professional in a white coat in conversation with a man across a desk",
  "pillars_h": "What we bring together",
  "pillars": [
    ("Advanced technology", "Intelligent digital solutions that simplify and streamline the medical claims lifecycle."),
    ("Specialized expertise", "Experienced operational teams that help partners optimize claims operations and service quality."),
    ("End-to-end lifecycle", "From medical authorizations and claims processing to settlement and financial reconciliation."),
    ("Compliance", "Maintaining compliance with applicable regulatory and professional standards.")],
  "aud_tabs": "Choose your organization type",
  "aud_services": "Relevant Tamayah services",
  "aud_cta": {"insurers": "Enquire as an insurer", "employers": "Enquire as a self-funded employer",
              "systems": "Enquire as a health system", "providers": "Enquire as a healthcare provider",
              "beneficiaries": "Contact our service team"},
  "jx_h": "The claims journey",
  "jx_intro": "Select a stage to see what happens and which Tamayah capability supports it.",
  "jx_tabs": "Claims journey stages",
  "jx_stage": "Stage", "jx_of": "of",
  "jx_what": "What happens", "jx_role": "Role in the process", "jx_cap": "Related capability",
  "jx_prev": "Previous stage", "jx_next": "Next stage",
  "roles": ["Requests are reviewed for alignment with coverage benefits, policy terms and conditions, and regulatory requirements.",
            "Claims are received, reviewed, validated and processed through technology-enabled systems.",
            "Settlement is managed through structured processes with clear handling.",
            "Financial reconciliation identifies and addresses discrepancies.",
            "Claims are closed accurately and transparently."],
  "svc_h": "Our services",
  "care_shared": "Included in both services",
  "care_plans": "Compare services",
  "care_distinct": "Distinctive to this service",
  "board_member": "Board Member",
  "form_h": "Send an enquiry",
  "form_intro": "Tell us about your organization and we will prepare an email to our team.",
  "f_name": "Full name", "f_org": "Organization", "f_role": "I am a…", "f_role_ph": "Select one",
  "f_other": "Other", "f_email": "Work email", "f_phone": "Phone", "f_msg": "How can we help?", "f_opt": "optional",
  "f_email_hint": "For example name@company.com",
  "f_consent": "I agree that Tamayah may use these details to respond to my enquiry.",
  "f_privacy": "Your details are used only to respond to your enquiry.",
  "f_pending": "Wording pending approval",
  "f_submit": "Send enquiry by email",
  "f_how": "Submitting opens your email app with your enquiry addressed to info@tamayah.com. Nothing is sent until you press send there.",
  "e_name": "Enter your full name.", "e_org": "Enter your organization's name.", "e_role": "Choose the option that best describes you.",
  "e_email": "Enter your work email.", "e_email_fmt": "Enter an email address in the format name@company.com.",
  "e_phone": "Enter a phone number using digits only, for example 920011978.",
  "e_msg": "Tell us briefly how we can help.", "e_consent": "Confirm that we may use these details to respond.",
  "e_summary": "Please correct {n} fields before sending.", "e_summary1": "Please correct 1 field before sending.",
  "ok": "Your email app should now open with your enquiry. If it doesn't, email us at info@tamayah.com.",
  "direct_h": "Or contact us directly",
  "legal_h": "Legal", "legal": ["Privacy Policy", "Terms of Use", "Accessibility Statement"], "legal_pending": "link pending approval",
  "about_lead": "Tamayah is a specialized provider of medical claims management and settlement solutions.",
  "mail_subject": "Enquiry from the Tamayah website",
  "mail_labels": {"name": "Name", "org": "Organization", "role": "I am a", "email": "Work email", "phone": "Phone", "msg": "Message"},
},
"ar": {
  "trust_h": "الوضع التنظيمي",
  "hero_alt": "أخصائية رعاية صحية بمعطف أبيض تتحدث مع رجل على مكتب",
  "pillars_h": "ما نجمع بينه",
  "pillars": [
    ("التقنيات المتقدمة", "حلول رقمية ذكية تبسّط دورة المطالبات الطبية وتديرها بكفاءة أعلى."),
    ("الخبرات المتخصصة", "فرق تشغيلية ذات خبرة تساعد على تحسين عمليات إدارة المطالبات والارتقاء بجودة الخدمات."),
    ("دورة متكاملة", "من إدارة الموافقات الطبية ومعالجة المطالبات إلى التسويات المالية والمطابقة."),
    ("الالتزام", "ضمان الالتزام بالمعايير التنظيمية والمهنية المعمول بها.")],
  "aud_tabs": "اختر نوع جهتك",
  "aud_services": "خدمات تماية ذات الصلة",
  "aud_cta": {"insurers": "استفسر بصفتك شركة تأمين", "employers": "استفسر بصفتك صاحب عمل يموّل برنامجه ذاتيًا",
              "systems": "استفسر بصفتك منشأة صحية", "providers": "استفسر بصفتك مقدم خدمة صحية",
              "beneficiaries": "تواصل مع فريق الخدمة"},
  "jx_h": "رحلة المطالبة",
  "jx_intro": "اختر مرحلة لمعرفة ما يحدث فيها وما القدرة التي تدعمها تماية.",
  "jx_tabs": "مراحل رحلة المطالبة",
  "jx_stage": "المرحلة", "jx_of": "من",
  "jx_what": "ما يحدث", "jx_role": "الدور في العملية", "jx_cap": "القدرة ذات الصلة",
  "jx_prev": "المرحلة السابقة", "jx_next": "المرحلة التالية",
  "roles": ["تُراجع الطلبات للتأكد من توافقها مع منافع التغطية وشروط الوثيقة وأحكامها والمتطلبات التنظيمية.",
            "تُستقبل المطالبات وتُراجع ويُتحقق منها وتُعالج عبر أنظمة مدعومة بالتقنية.",
            "تُدار التسوية بإجراءات منظمة وآليات واضحة.",
            "تُحدَّد الفروقات في المطابقة المالية وتُعالَج.",
            "تُغلق المطالبات بدقة وشفافية."],
  "svc_h": "خدماتنا",
  "care_shared": "مشمولة في الخدمتين",
  "care_plans": "قارن بين الخدمتين",
  "care_distinct": "ما يميز هذه الخدمة",
  "board_member": "عضو مجلس المديرين",
  "form_h": "أرسل استفسارك",
  "form_intro": "أخبرنا عن جهتك وسنجهّز رسالة بريد إلكتروني إلى فريقنا.",
  "f_name": "الاسم الكامل", "f_org": "الجهة", "f_role": "أنا…", "f_role_ph": "اختر",
  "f_other": "أخرى", "f_email": "البريد الإلكتروني للعمل", "f_phone": "رقم الهاتف", "f_msg": "كيف يمكننا مساعدتك؟", "f_opt": "اختياري",
  "f_email_hint": "مثال: name@company.com",
  "f_consent": "أوافق على أن تستخدم تماية هذه البيانات للرد على استفساري.",
  "f_privacy": "تُستخدم بياناتك فقط للرد على استفسارك.",
  "f_pending": "الصياغة بانتظار الاعتماد",
  "f_submit": "إرسال الاستفسار عبر البريد",
  "f_how": "عند الإرسال يُفتح تطبيق البريد لديك وفيه استفسارك موجّهًا إلى info@tamayah.com. لا يُرسل شيء حتى تضغط إرسال هناك.",
  "e_name": "أدخل اسمك الكامل.", "e_org": "أدخل اسم جهتك.", "e_role": "اختر الخيار الأنسب لك.",
  "e_email": "أدخل بريدك الإلكتروني للعمل.", "e_email_fmt": "أدخل بريدًا إلكترونيًا بصيغة name@company.com.",
  "e_phone": "أدخل رقم الهاتف بالأرقام فقط، مثل 920011978.",
  "e_msg": "أخبرنا باختصار كيف يمكننا مساعدتك.", "e_consent": "أكّد موافقتك على استخدام هذه البيانات للرد.",
  "e_summary": "يرجى تصحيح {n} حقول قبل الإرسال.", "e_summary1": "يرجى تصحيح حقل واحد قبل الإرسال.",
  "ok": "يُفترض أن يُفتح تطبيق البريد الآن وفيه استفسارك. إن لم يُفتح، راسلنا على info@tamayah.com.",
  "direct_h": "أو تواصل معنا مباشرة",
  "legal_h": "قانوني", "legal": ["سياسة الخصوصية", "شروط الاستخدام", "بيان إمكانية الوصول"], "legal_pending": "الرابط بانتظار الاعتماد",
  "about_lead": "تماية هي شركة متخصصة في تقديم حلول إدارة وتسوية المطالبات الطبية.",
  "mail_subject": "استفسار من موقع تماية",
  "mail_labels": {"name": "الاسم", "org": "الجهة", "role": "أنا", "email": "البريد الإلكتروني", "phone": "الهاتف", "msg": "الرسالة"},
}}

# Audience keys in the order of CONTENT[lang]["aud"]["items"], with the services relevant to each
# (condensed from approved copy; listed for sign-off in AUDIT.md).
AUDIENCES = [("insurers", ["auth", "claims", "settle", "phm", "call"]),
             ("employers", ["claims", "settle", "phm"]),
             ("systems", ["claims", "settle", "phm"]),
             ("providers", ["auth", "claims", "settle", "call"]),
             ("beneficiaries", ["call", "concierge", "elite"])]
STAGE_CAPABILITY = ["auth", "claims", "settle", "settle", "settle"]
SHARED_PERKS = 4  # the last four perks of each care service are identical (see AUDIT.md §3.12)

# ---------------------------------------------------------------- Icons (1.6px line icons, currentColor)
def icon(name, cls="ico"):
    p = {
      "arrow": '<path d="M4 12h15M13 6l6 6-6 6"/>',
      "back": '<path d="M20 12H5M11 6l-6 6 6 6"/>',
      "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
      "shield": '<path d="M12 3l7 3v5.5c0 4.4-3 8.2-7 9.5-4-1.3-7-5.1-7-9.5V6z"/><path d="M9 12l2 2 4-4"/>',
      "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1.2 1.2"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1.2-1.2"/>',
      "network": '<circle cx="12" cy="5" r="2.2"/><circle cx="5" cy="18" r="2.2"/><circle cx="19" cy="18" r="2.2"/><path d="M12 7.2v4.3M12 11.5l-5.6 4.8M12 11.5l5.6 4.8"/>',
      "chip": '<rect x="6" y="6" width="12" height="12" rx="2.5"/><path d="M9.5 2.5v3M14.5 2.5v3M9.5 18.5v3M14.5 18.5v3M2.5 9.5h3M2.5 14.5h3M18.5 9.5h3M18.5 14.5h3"/>',
      "people": '<circle cx="9" cy="8" r="3"/><path d="M3.5 19c.6-3.1 2.9-5 5.5-5s4.9 1.9 5.5 5"/><circle cx="17" cy="9" r="2.3"/><path d="M16 14.2c2.4.2 4.1 1.9 4.5 4.8"/>',
      "cycle": '<path d="M20 12a8 8 0 0 1-13.7 5.6M4 12a8 8 0 0 1 13.7-5.6"/><path d="M18 3v3.8h-3.8M6 21v-3.8h3.8"/>',
      "scale": '<path d="M12 4v16M7 20h10M5 8h14"/><path d="M5 8l-2.5 6a2.8 2.8 0 0 0 5 0zM19 8l-2.5 6a2.8 2.8 0 0 0 5 0z"/>',
      "at": '<circle cx="12" cy="12" r="3.6"/><path d="M15.6 12v1.4a2.6 2.6 0 0 0 5.2 0V12a8.8 8.8 0 1 0-3.5 7"/>',
      "mail": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M4 7l8 6 8-6"/>',
      "phone": '<path d="M5 4h3.5l1.8 4.5-2.3 1.5a11 11 0 0 0 6 6l1.5-2.3L20 15.5V19a1.5 1.5 0 0 1-1.6 1.5A16 16 0 0 1 3.5 5.6 1.5 1.5 0 0 1 5 4z"/>',
    }[name]
    flip = " flip" if name in ("arrow", "back") else ""
    return f'<svg class="{cls}{flip}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{p}</svg>'


def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")


def monogram(name, lang):
    """Initials of the first and family name, skipping titles and the Al-/ال article."""
    words = [w for w in strip(name).replace("Eng.", "").replace("م.", "").split() if w not in ("بن", "آل")]
    def initial(w):
        if lang == "ar":
            return w[2] if w.startswith("ال") and len(w) > 2 else w[0]
        w = re.sub(r"^Al-?(?=[A-Z])", "", w)
        return w[0]
    letters = [initial(words[0]), initial(words[-1])] if len(words) > 1 else [initial(words[0])]
    return (" " if lang == "ar" else "").join(letters)


def href(page):
    return dict(NAV_ITEMS)[page]


def logo(cls, eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<picture class="{cls}"><source type="image/webp" srcset="../assets/logo-320.webp 320w, ../assets/logo-640.webp 640w" sizes="160px">'
            f'<img src="../assets/logo-320.png" srcset="../assets/logo-320.png 320w, ../assets/logo-640.png 640w" sizes="160px" width="320" height="105" alt="{{alt}}" {load}></picture>')


def services(c):
    e, s = c["eco"], c["suite"]
    return {"auth": e["core"][0][0], "claims": e["core"][1][0], "settle": e["core"][2][0],
            "phm": e["layers"][0][1], "call": e["layers"][1][1],
            "concierge": s["concierge"]["t"], "elite": s["elite"]["t"]}


def svc_target(k):
    return {"auth": "#svc-auth", "claims": "#svc-claims", "settle": "#svc-settle", "phm": "#svc-phm",
            "call": "#svc-call", "concierge": "#suite", "elite": "#suite"}[k]


def shead(eyebrow, h2, lede="", hid=""):
    ld = f'<p class="lede rv" style="--d:2">{lede}</p>' if lede else ""
    idattr = f' id="{hid}"' if hid else ""
    return f'''<div class="shead"><p class="eyebrow rv">{eyebrow}</p><h2 class="h2 rv" style="--d:1"{idattr}>{h2}</h2>{ld}</div>'''


# ---------------------------------------------------------------- Components
def header(c):
    nav = "".join(f'<li><a href="{href(p)}" data-nav-link>{c["nav"][p]}</a></li>' for p, _ in NAV_ITEMS)
    drawer = "".join(f'<li><a href="{href(p)}"><span>{c["nav"][p]}</span>{icon("arrow")}</a></li>' for p, _ in NAV_ITEMS)
    en_cur = "true" if c["lang"] == "en" else "false"
    ar_cur = "true" if c["lang"] == "ar" else "false"
    lang = (f'<div class="lang" role="group" aria-label="{c["lang_label"]}">'
            f'<a href="../en/index.html" hreflang="en" lang="en" aria-current="{en_cur}">EN</a>'
            f'<a href="../ar/index.html" hreflang="ar" lang="ar" aria-current="{ar_cur}">عربي</a></div>')
    return f'''<header class="header"><div class="wrap header__in">
  <a class="brand" href="#top">{logo("brand__logo", eager=True).replace("{alt}", c["name"])}</a>
  <nav class="nav" aria-label="Primary"><ul>{nav}</ul></nav>
  <div class="header__tools">{lang}
    <a class="btn btn--sm header__cta" href="#partner">{c["cta"]}{icon("arrow")}</a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="drawer"><span class="sr-only">{c["menu"]}</span><span class="burger__bar" aria-hidden="true"></span><span class="burger__bar" aria-hidden="true"></span></button>
  </div>
</div>
<div class="drawer" id="drawer"><nav aria-label="Mobile"><ul>{drawer}</ul></nav>
  <a class="btn" href="#partner">{c["cta"]}{icon("arrow")}</a></div></header>'''


def hero(c):
    h, r, u = c["hero"], c["reg"], UI[c["lang"]]
    lines = "".join(f'<span class="line"><span style="--i:{i}">{t}</span></span>' for i, t in enumerate(h["lines"]))
    chips = [("shield", h["meta"][0]), ("link", h["meta"][1])]
    trust = "".join(f'<li class="trust__item">{icon(ic)}<span>{t}</span></li>' for ic, t in chips)
    img = ('<picture><source type="image/webp" srcset="../assets/img/hero-640.webp 640w, ../assets/img/hero-960.webp 960w, ../assets/img/hero-1280.webp 1280w" sizes="(min-width:1024px) 40vw, (min-width:720px) 88vw, 100vw">'
           '<img src="../assets/img/hero-960.jpg" srcset="../assets/img/hero-640.jpg 640w, ../assets/img/hero-960.jpg 960w, ../assets/img/hero-1280.jpg 1280w" '
           f'sizes="(min-width:1024px) 40vw, (min-width:720px) 88vw, 100vw" width="1280" height="960" alt="{u["hero_alt"]}" fetchpriority="high" decoding="async"></picture>')
    return f'''<section class="hero" id="top" aria-labelledby="hero-h">
  <div class="wrap">
    <div class="hero__grid">
      <div class="hero__copy">
        <p class="eyebrow fade-up">{h["eyebrow"]}</p>
        <h1 class="h1" id="hero-h">{lines}</h1>
        <p class="lede fade-up" style="--d:2">{h["lede"]}</p>
        <div class="hero__actions fade-up" style="--d:3">
          <a class="btn" href="#partner">{h["primary"]}{icon("arrow")}</a>
          <a class="btn btn--ghost" href="#services">{h["secondary"]}</a>
        </div>
      </div>
      <figure class="hero__media fade-up" style="--d:4">{img}</figure>
    </div>
    <div class="trust fade-up" style="--d:5">
      <h2 class="sr-only">{u["trust_h"]}</h2>
      <div class="trust__stat"><span class="stat"><span class="stat__n" data-count="{r["count"]}">{r["count"]:,}</span><span class="stat__u">+</span></span><span class="stat__l">{r["count_label"]}</span></div>
      <ul class="trust__list">{trust}</ul>
      <p class="trust__reg">{r["text"]}</p>
    </div>
  </div>
</section>'''


def about(c):
    a, v, u = c["about"], c["vmc"], UI[c["lang"]]
    icons = ["chip", "people", "cycle", "scale"]
    pillars = "".join(f'<li class="pillar rv" style="--d:{i}">{icon(icons[i])}<h4 class="h4">{t}</h4><p>{d}</p></li>'
                      for i, (t, d) in enumerate(u["pillars"]))
    return f'''<section class="section about" id="about" aria-labelledby="about-h"><div class="wrap">
  <div class="split">
    {shead(a["eyebrow"], a["h1"], u["about_lead"], "about-h")}
    <div><h3 class="label rv">{u["pillars_h"]}</h3><ul class="pillars">{pillars}</ul></div>
  </div>
  <div class="vision rv">
    <div class="vision__main"><h3 class="label">{v["vision_h"]}</h3><p class="statement">{v["vision"]}</p></div>
    <div class="vision__col"><h3 class="label">{v["mission_h"]}</h3><p>{v["mission"]}</p></div>
    <div class="vision__col"><h3 class="label">{v["commit_h"]}</h3><p>{v["commit"][0]}</p></div>
  </div>
</div></section>'''


def audiences(c):
    a, u, svc = c["aud"], UI[c["lang"]], services(c)
    tabs, panels = "", ""
    for i, ((key, keys), (t, d, _)) in enumerate(zip(AUDIENCES, a["items"])):
        sel = "true" if i == 0 else "false"
        tabs += f'<button class="seg__tab" type="button" role="tab" id="tab-{key}" aria-controls="audience-{key}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">{t}</button>'
        items = "".join(f'<li><a href="{svc_target(k)}">{icon("check")}<span>{svc[k]}</span></a></li>' for k in keys)
        panels += f'''<div class="aud__panel" id="audience-{key}" role="tabpanel" aria-labelledby="tab-{key}" tabindex="0">
  <div class="aud__main"><span class="aud__n" aria-hidden="true">0{i+1}</span><h3 class="h3">{t}</h3><p class="aud__vp">{d}</p>
    <a class="btn" href="#partner" data-audience="{key}">{u["aud_cta"][key]}{icon("arrow")}</a></div>
  <div class="aud__svc"><h4 class="label">{u["aud_services"]}</h4><ul class="svc-list">{items}</ul></div>
</div>'''
    return f'''<section class="section aud" id="audiences" aria-labelledby="aud-h"><div class="wrap">
  {shead(a["eyebrow"], a["h2"], a["lede"], "aud-h")}
  <div class="aud__x rv" data-tabs data-hash="audience-">
    <div class="seg seg--scroll" role="tablist" aria-label="{u["aud_tabs"]}">{tabs}</div>
    <div class="aud__panels">{panels}</div>
  </div>
</div></section>'''


def journey(c):
    u, svc = UI[c["lang"]], services(c)
    n = len(c["states"])
    tabs, panels = "", ""
    for i, (t, s) in enumerate(c["states"]):
        sel = "true" if i == 0 else "false"
        tabs += f'''<button class="jx__tab" type="button" role="tab" id="stage-tab-{i+1}" aria-controls="stage-{i+1}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}"><span class="jx__dot" aria-hidden="true">0{i+1}</span><span class="jx__t">{t}</span></button>'''
        cap = STAGE_CAPABILITY[i]
        done = ""
        if i == n - 1:
            done = f'''<div class="closed" aria-hidden="true"><svg viewBox="0 0 {DETAIL_W} {DETAIL_H}" focusable="false"><path d="{DETAIL_PATH}"/></svg>
  <span class="closed__ico">{icon("check")}</span><span class="closed__t">{t}</span></div>'''
        prev = f'<button class="btn btn--ghost btn--sm" type="button" data-step="-1">{icon("back")}{u["jx_prev"]}</button>' if i else ""
        nxt = f'<button class="btn btn--sm" type="button" data-step="1">{u["jx_next"]}{icon("arrow")}</button>' if i < n - 1 else ""
        panels += f'''<div class="jx__panel" id="stage-{i+1}" role="tabpanel" aria-labelledby="stage-tab-{i+1}" tabindex="0">
  <p class="jx__count">{u["jx_stage"]} {i+1} {u["jx_of"]} {n}</p>
  <h4 class="h3">{t}</h4>{done}
  <dl class="jx__dl">
    <div><dt>{u["jx_what"]}</dt><dd>{s}</dd></div>
    <div><dt>{u["jx_role"]}</dt><dd>{u["roles"][i]}</dd></div>
    <div><dt>{u["jx_cap"]}</dt><dd><a class="link" href="{svc_target(cap)}">{svc[cap]}{icon("arrow")}</a></dd></div>
  </dl>
  <div class="jx__nav">{prev}{nxt}</div>
</div>'''
    return f'''<div class="jx rv" data-tabs data-hash="stage-">
  <div class="jx__head"><h3 class="h3">{u["jx_h"]}</h3><p>{u["jx_intro"]}</p></div>
  <div class="jx__rail"><span class="jx__track" aria-hidden="true"><span class="jx__fill"></span></span>
    <div class="jx__tabs" role="tablist" aria-label="{u["jx_tabs"]}">{tabs}</div></div>
  <div class="jx__panels">{panels}</div>
</div>'''


def eco(c):
    e, u = c["eco"], UI[c["lang"]]
    ids = ["svc-auth", "svc-claims", "svc-settle"]
    core = "".join(f'<li class="svc rv" id="{ids[i]}" style="--d:{i}"><span class="svc__n">0{i+1}</span><h4 class="h3">{t}</h4><p>{d}</p></li>'
                   for i, (t, d) in enumerate(e["core"]))
    lids = ["svc-phm", "svc-call"]
    layers = "".join(f'<li class="svc svc--layer rv" id="{lids[i]}" style="--d:{i}"><p class="label">{tag}</p><h4 class="h3">{t}</h4><p>{d}</p></li>'
                     for i, (tag, t, d) in enumerate(e["layers"]))
    return f'''<section class="section eco" id="services" aria-labelledby="eco-h"><div class="wrap">
  {shead(e["eyebrow"], e["h2"], e["lede"], "eco-h")}
  {journey(c)}
  <h3 class="label svc__h rv">{u["svc_h"]}</h3>
  <ul class="svcs">{core}{layers}</ul>
</div></section>'''


def suite(c):
    s, u = c["suite"], UI[c["lang"]]
    shared = s["elite"]["perks"][-SHARED_PERKS:]
    shared_html = "".join(f'<li>{icon("check")}<span><b>{a}</b>{b}</span></li>' for a, b in shared)
    plans, tabs = "", ""
    for i, k in enumerate(("concierge", "elite")):
        d = s[k]
        own = d["perks"][:len(d["perks"]) - SHARED_PERKS]
        own_html = "".join(f'<li>{icon("check")}<span><b>{a}</b>{b}</span></li>' for a, b in own)
        sel = "true" if i == 0 else "false"
        tabs += f'<button class="seg__tab" type="button" role="tab" id="plan-tab-{k}" aria-controls="plan-{k}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">{d["t"]}</button>'
        plans += f'''<div class="plan plan--{k}" id="plan-{k}" role="tabpanel" aria-labelledby="plan-tab-{k}">
  <h3 class="h3">{d["t"]}</h3><p>{d["intro"]}</p><p class="plan__hours">{d["hours"]}</p>
  <h4 class="label">{u["care_distinct"]}</h4><ul class="perks">{own_html}</ul></div>'''
    return f'''<section class="section suite" id="suite" aria-labelledby="suite-h"><div class="wrap">
  {shead(s["eyebrow"], s["h2"], s["lede"], "suite-h")}
  <div class="care rv" data-tabs data-mobile-only>
    <div class="seg care__seg" role="tablist" aria-label="{u["care_plans"]}">{tabs}</div>
    <div class="care__plans">{plans}</div>
    <div class="care__shared"><h3 class="label">{u["care_shared"]}</h3><ul class="perks perks--shared">{shared_html}</ul></div>
  </div>
</div></section>'''


def why(c):
    w = c["why"]
    vals = "".join(f'<li class="val rv" style="--d:{i}"><span class="val__n">0{i+1}</span><h4 class="h4">{t}</h4><p>{d}</p></li>'
                   for i, (t, d) in enumerate(w["values"]))
    return f'''<section class="section why" id="why" aria-labelledby="why-h"><div class="wrap">
  <div class="why__lead"><p class="eyebrow rv">{w["eyebrow"]}</p><h2 class="statement rv" style="--d:1" id="why-h">{w["quote"]}</h2></div>
  <h3 class="label rv">{w["values_h"]}</h3>
  <ul class="values">{vals}</ul>
</div></section>'''


def leadership(c):
    l, u = c["lead"], UI[c["lang"]]
    cards = ""
    i = 0
    for role, names in l["rows"]:
        if len(names) > 1:  # one card per person, so a plural row label becomes singular
            role = u["board_member"]
        for n in names:
            cards += f'''<li class="person rv" style="--d:{i}"><span class="person__mono" aria-hidden="true">{monogram(n, c["lang"])}</span>
  <h3 class="person__name">{n}</h3><p class="person__role">{role}</p></li>'''
            i += 1
    return f'''<section class="section lead" id="leadership" aria-labelledby="lead-h"><div class="wrap">
  {shead(l["eyebrow"], l["h2"], "", "lead-h")}
  <ul class="people">{cards}</ul>
</div></section>'''


def field(fid, label, u, kind="text", req=True, auto="", extra="", hint=""):
    opt = "" if req else f' <span class="field__opt">({u["f_opt"]})</span>'
    reqa = ' required aria-required="true"' if req else ""
    hint_html = f'<p class="field__hint" id="{fid}-hint">{hint}</p>' if hint else ""
    desc = f"{fid}-err" + (f" {fid}-hint" if hint else "")
    ac = f' autocomplete="{auto}"' if auto else ""
    if kind == "textarea":
        ctl = f'<textarea id="{fid}" name="{fid}" rows="5"{reqa} aria-describedby="{desc}"{extra}></textarea>'
    else:
        ctl = f'<input id="{fid}" name="{fid}" type="{kind}"{ac}{reqa} aria-describedby="{desc}"{extra}>'
    return f'''<div class="field"><label for="{fid}">{label}{opt}</label>{ctl}{hint_html}<p class="field__err" id="{fid}-err" hidden></p></div>'''


def contact(c):
    b, k, u, r = c["cta_block"], c["contact"], UI[c["lang"]], c["contact"]["rows"]
    opts = "".join(f'<option value="{key}">{strip(t)}</option>' for (key, _), (t, _d, _l) in zip(AUDIENCES, c["aud"]["items"]))
    opts += f'<option value="other">{u["f_other"]}</option>'
    errs = {k2: v for k2, v in u.items() if k2.startswith("e_") or k2 == "ok"}
    data = " ".join(f'data-{k2.replace("_", "-")}="{html.escape(v)}"' for k2, v in errs.items())
    labels = " ".join(f'data-l-{k2}="{html.escape(v)}"' for k2, v in u["mail_labels"].items())
    form = f'''<form class="form" id="enquiry" action="mailto:{EMAIL}" method="post" enctype="text/plain" novalidate
  data-email="{EMAIL}" data-subject="{html.escape(u["mail_subject"])}" {data} {labels}>
  <div class="form__summary" role="alert" tabindex="-1" hidden></div>
  <div class="form__grid">
    {field("name", u["f_name"], u, auto="name")}
    {field("org", u["f_org"], u, auto="organization")}
    <div class="field"><label for="role">{u["f_role"]}</label>
      <select id="role" name="role" required aria-required="true" aria-describedby="role-err"><option value="">{u["f_role_ph"]}</option>{opts}</select>
      <p class="field__err" id="role-err" hidden></p></div>
    {field("email", u["f_email"], u, kind="email", auto="email", hint=u["f_email_hint"], extra=' inputmode="email" spellcheck="false" dir="ltr"')}
    {field("phone", u["f_phone"], u, kind="tel", req=False, auto="tel", extra=' inputmode="tel" dir="ltr"')}
  </div>
  {field("msg", u["f_msg"], u, kind="textarea")}
  <div class="consent">
    <p class="pending"><span class="pending__tag review-only">{u["f_pending"]}</span> {u["f_privacy"]}</p>
    <div class="check"><input id="consent" name="consent" type="checkbox" required aria-required="true" aria-describedby="consent-err">
      <label for="consent">{u["f_consent"]}</label></div>
    <p class="field__err" id="consent-err" hidden></p>
  </div>
  <div class="form__foot"><button class="btn" type="submit">{u["f_submit"]}{icon("arrow")}</button><p class="form__how">{u["f_how"]}</p></div>
  <p class="form__ok" role="status" aria-live="polite"></p>
</form>'''
    return f'''<section class="section contact" id="contact" aria-labelledby="partner-h"><div class="wrap">
  <div class="contact__grid">
    <div class="contact__intro" id="partner">
      <p class="eyebrow rv">{b["eyebrow"]}</p>
      <h2 class="h2 rv" style="--d:1" id="partner-h">{b["h2"]}</h2>
      <p class="lede rv" style="--d:2">{b["text"]}</p><p class="rv" style="--d:2">{b["text2"]}</p>
      <h3 class="label direct__h">{u["direct_h"]}</h3>
      <ul class="direct">
        <li>{icon("mail")}<span><span class="direct__l">{r["email"]}</span><a class="ltr" href="mailto:{EMAIL}">{EMAIL}</a></span></li>
        <li>{icon("phone")}<span><span class="direct__l">{r["phone"]}</span><a class="ltr" href="tel:{PHONE}">{PHONE}</a></span></li>
        <li>{icon("link")}<span><span class="direct__l">{r["linkedin"]}</span><a class="ltr" href="{LINKEDIN_URL}" target="_blank" rel="noopener">{k["linkedin_text"]}</a></span></li>
        <li>{icon("at")}<span><span class="direct__l">{r["x"]}</span><a class="ltr" href="https://x.com/{X_HANDLE}" target="_blank" rel="noopener">@{X_HANDLE}</a></span></li>
      </ul>
    </div>
    <div class="contact__form rv"><h3 class="h3">{u["form_h"]}</h3><p class="form__intro">{u["form_intro"]}</p>{form}</div>
  </div>
</div></section>'''


def footer(c):
    """Compact footer: logo, formal regulatory statement, legal items, copyright.

    Legal destinations are not approved yet, so they render as plain text (not links). The
    "pending approval" helper only appears in review mode (?review=1 or REVIEW_MODE).
    """
    f, u = c["footer"], UI[c["lang"]]
    legal = "".join(f'<li><span>{t}</span><span class="review-only legal__pending"> ({u["legal_pending"]})</span></li>' for t in u["legal"])
    return f'''<footer class="footer"><div class="wrap footer__in">
  <a class="brand footer__logo" href="#top">{logo("brand__logo").replace("{alt}", c["name"])}</a>
  <p class="footer__reg">{f["reg"]}</p>
  <ul class="legal" aria-label="{u["legal_h"]}">{legal}</ul>
  <p class="footer__copy">{f["rights"]}</p>
</div></footer>'''


def render(lang):
    c = CONTENT[lang]
    body = hero(c) + about(c) + audiences(c) + eco(c) + suite(c) + why(c) + leadership(c) + contact(c)
    page = f'''<!DOCTYPE html>
<html lang="{lang}" dir="{c["dir"]}" class="no-js"{" data-review" if REVIEW_MODE else ""}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(c["titles"]["index"], quote=False)}</title>
<meta name="description" content="{html.escape(c["desc"])}">
<meta name="theme-color" content="#F7F6F2">
<link rel="canonical" href="{SITE_URL}{lang}/index.html">
<link rel="alternate" hreflang="en" href="{SITE_URL}en/index.html">
<link rel="alternate" hreflang="ar" href="{SITE_URL}ar/index.html">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}">
<link rel="icon" type="image/png" href="../assets/mark.png">
<link rel="preload" href="../assets/fonts/tawuniya-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/style.css">
<script>document.documentElement.classList.replace('no-js','js')</script>
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
    return re.sub(r"&(?![a-zA-Z]+;|#[0-9]+;|#x[0-9a-fA-F]+;)", "&amp;", page)  # escape bare & from shared copy


ROOT_INDEX = '''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tamayah | تماية</title><meta name="theme-color" content="#F7F6F2">
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#F7F6F2;color:#132028;font-family:system-ui,sans-serif;text-align:center}
a{color:#326B73;margin:0 12px;font-size:1.2rem}img{width:220px;height:auto;margin:0 auto 28px}</style>
<script>
(function(){var l;try{l=localStorage.getItem('tamayah-lang')}catch(e){}
if(!l){l=(navigator.language||'en').toLowerCase().indexOf('ar')===0?'ar':'en'}
location.replace(l+'/index.html'+location.hash)})();
</script></head>
<body><div><img src="assets/logo-640.png" width="640" height="209" alt="Tamayah تماية"><br><a href="en/index.html">English</a><a href="ar/index.html" lang="ar">العربية</a></div></body></html>
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
