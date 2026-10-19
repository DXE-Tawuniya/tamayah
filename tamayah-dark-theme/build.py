#!/usr/bin/env python3
"""Tamayah site generator.

All copy lives in CONTENT (en / ar). Components below render the same markup for
both languages; direction is handled by <html dir> + CSS logical properties.

Run:  python3 build.py        -> writes en/index.html, ar/index.html, index.html
"""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---- Confirmed / pending contact facts (see README) -------------------------
EMAIL = "info@tamayah.com"   # source docx: run split across "I" + "nfo@tamayah.com"
PHONE = "920011978"
X_HANDLE = "Tamayah_sa"
LINKEDIN_URL = "https://www.linkedin.com/search/results/companies/?keywords=Tamayah"  # TODO: replace with the official company URL

# The public site is deliberately a single long-form page in each language.
# These entries power the in-page navigation and map every menu item to its section.
NAV_ITEMS = [
    ("index", "#top"),
    ("about", "#about"),
    ("solutions", "#services"),
    ("why", "#why"),
    ("leadership", "#leadership"),
    ("contact", "#contact"),
]

CONTENT = {
"en": {
  "lang": "en", "dir": "ltr", "name": "Tamayah",
  "other": "ar", "other_label": "العربية", "this_label": "EN",
  "skip": "Skip to content", "menu": "Menu", "lang_label": "Language",
  "nav": {"index": "Home", "about": "About", "solutions": "What We Do", "why": "Why Tamayah", "leadership": "Leadership", "contact": "Contact"},
  "cta": "Partner with us",
  "titles": {
    "index": "Tamayah | Medical claims management & settlement solutions",
    "about": "About Tamayah | Who we are",
    "solutions": "What We Do | Tamayah",
    "why": "Why Tamayah",
    "leadership": "Leadership | Tamayah",
    "contact": "Contact | Partner with Tamayah"},
  "desc": "Tamayah is a specialized provider of medical claims management and settlement solutions in Saudi Arabia, operating under the supervision and oversight of the Insurance Authority.",
  "hero": {
    "eyebrow": "Medical claims management & settlement",
    "lines": ["Healthcare claims", "&amp; benefits, made", "<em>clear.</em>"],
    "lede": "Tamayah is a specialized provider of medical claims management and settlement solutions. We bring technology, specialized expertise and operational excellence together to make claims and benefits administration efficient, transparent and reliable.",
    "primary": "Partner with Tamayah", "secondary": "Explore what we do",
    "meta": ["<b>Insurance Authority</b> supervised", "Authorized via <b>Nphies</b>", "<b>1,700+</b> healthcare providers"]},
  "stack_aria": "Illustrative claim journey: authorization, claim validation, settlement, reconciliation, closure",
  "states": [
    ("Medical authorization", "Reviewed against benefits &amp; policy terms"),
    ("Claim validation", "Received, reviewed, validated"),
    ("Settlement", "Processed with clear handling"),
    ("Reconciliation", "Discrepancies identified &amp; addressed"),
    ("Claim closed", "Accurate and transparent closure")],
  "reg": {"tag": "Regulatory standing",
          "text": "Tamayah operates under the supervision and oversight of the Insurance Authority and is authorized to conduct transactions through the Nphies platform.",
          "count": 1700, "count_label": "healthcare providers supported"},
  "aud": {
    "eyebrow": "Who we serve", "h2": "Built for every party in the claims journey.",
    "lede": "Effective claims management is more than processing transactions. It is creating an efficient, transparent and reliable experience for all stakeholders.",
    "items": [
      ("Insurers", "The technology, network and expertise to run health programs efficiently, transparently and at scale.", "solutions"),
      ("Self-funded employers", "Structured processes and clear handling of claims and settlement activity for the programs you fund.", "solutions"),
      ("Health systems", "Accurate processing and timely resolution across the claims lifecycle, with transparent settlement.", "why"),
      ("Healthcare providers", "Timely processing and responsive operations that help you reach faster, more efficient claim resolution.", "solutions"),
      ("Beneficiaries", "A smoother experience through our call center and customer service, with concierge and elite services.", "solutions#suite")]},
  "eco": {
    "eyebrow": "What we do", "h2": "One connected claims-and-benefits ecosystem.",
    "lede": "At Tamayah, we manage the healthcare claims and benefits administration journey through an integrated approach that combines technology, expertise and operational discipline. Our services support partners throughout the claims lifecycle, enabling efficient processing, accurate decision-making and transparent settlement.",
    "core": [
      ("Medical Authorizations", "We manage and review medical authorization requests efficiently and accurately, ensuring alignment with applicable coverage benefits, policy terms and conditions, and regulatory requirements."),
      ("Medical Claims Management", "We receive, review, validate and process medical claims through advanced technology-enabled systems, helping ensure accuracy, efficiency and timely resolution throughout the claims lifecycle."),
      ("Claims Settlement &amp; Reconciliation", "We manage claims settlement and financial reconciliation processes, identify and address discrepancies, and facilitate accurate and transparent claim closure.")],
    "layers": [
      ("Health outcomes", "Population Health Management", "PHM programs that prevent complications, improve outcomes and reduce avoidable utilization, raising care quality and the efficiency of health spending."),
      ("Service experience", "Call Center &amp; Customer Service", "Integrated call center and customer service operations that deliver responsive support and easy access to help for beneficiaries and providers across the service journey.")],
    "more": "Explore all services"},
  "suite": {
    "eyebrow": "Premium care services", "h2": "Private by design.",
    "lede": "Two services shaped around privacy, responsiveness and effortless access to healthcare.",
    "concierge": {"t": "Concierge Medicine",
      "intro": "Integrated, personalized healthcare that gives the beneficiary a smoother and more private experience.",
      "hours": "Care manager · 8 AM – midnight",
      "perks": [("Dedicated care manager", "Personal assistance and continuous follow-up from 8 AM to midnight."),
                ("Private medical supervision", "A dedicated physician oversees the health plan and follows medical needs."),
                ("Priority access", "Appointments at major hospitals made easier."),
                ("Medical coordination", "Pre-surgery approvals and procedures managed, with accommodation arranged when needed."),
                ("Medication services", "Home delivery and management of prescription refills."),
                ("Proactive check-ups", "Regular health follow-up and preventive screening, and more.")]},
    "elite": {"t": "Elite &amp; VIP Services",
      "intro": "Services designed for a high level of privacy, responsiveness and ease of access to healthcare.",
      "hours": "Account manager · 9 AM – 9 PM",
      "perks": [("Dedicated account manager", "Available 9 AM to 9 PM, with booking support in under two hours."),
                ("Priority access", "Appointments at major hospitals made easier."),
                ("Medical coordination", "Pre-surgery approvals and procedures managed, with accommodation arranged when needed."),
                ("Medication services", "Home delivery and management of prescription refills."),
                ("Proactive check-ups", "Regular health follow-up and preventive screening.")]}},
  "why": {
    "eyebrow": "Why Tamayah",
    "quote": "Better claims management starts with the right combination of <em>technology and expertise.</em>",
    "paras": ["At Tamayah, we understand that effective claims management is more than processing transactions. It is about creating an efficient, transparent and reliable experience for all stakeholders.",
              "Our technology-enabled operating model allows us to manage complex claims processes while maintaining a strong focus on accuracy, efficiency, transparency and service quality.",
              "We work closely with our partners to understand their operational needs and deliver solutions that support their objectives and contribute to a more efficient healthcare ecosystem.",
              "We strive to deliver accurate processing, timely resolution and reliable outcomes while creating sustainable value for our partners and their customers."],
    "values_h": "Our value",
    "values": [("Technology-Driven Efficiency", "We leverage modern technology and digital solutions to streamline claims processes, reduce operational complexity and enhance processing efficiency."),
               ("Accuracy &amp; Quality", "Our structured processes and specialized expertise support accurate claims handling and consistent service quality across the claims lifecycle."),
               ("Speed &amp; Responsiveness", "We are committed to timely processing and responsive operations, helping our partners achieve faster and more efficient claims resolution."),
               ("Transparency", "We promote transparency throughout our operations, with structured processes and clear handling of claims and settlement activities."),
               ("Regulatory Compliance", "We operate within the applicable regulatory framework and maintain a strong commitment to professional and regulatory standards.")]},
  "vmc": {
    "vision_h": "Our vision", "vision": "To be the region’s most trusted health benefits administrator, where <em>every riyal spent buys better health.</em>",
    "mission_h": "Our mission", "mission": "We give insurers, self-funded employers and health systems the technology, network and expertise to run their health programs efficiently, transparently and at scale.",
    "commit_h": "Our commitment",
    "commit": ["We are committed to continuously improving the way healthcare claims and benefits are managed by combining specialized expertise, operational excellence and advanced technology.",
               "Through continuous development and operational excellence, we aim to help our partners achieve greater efficiency while delivering a smoother and more reliable claims experience."]},
  "about": {
    "eyebrow": "About Tamayah", "h1": "Who we are.",
    "lede": "Tamayah is a specialized provider of medical claims management and settlement solutions, operating under the supervision and oversight of the Insurance Authority.",
    "paras": ["We bring together advanced technology, specialized expertise and operational excellence to simplify and streamline the medical claims lifecycle. From medical authorization management and claims processing to settlement and financial reconciliation, our solutions are designed to deliver greater efficiency, accuracy, transparency and speed.",
              "By combining intelligent digital solutions with experienced operational teams, we help our partners optimize claims operations, enhance service quality and maintain compliance with applicable regulatory and professional standards."]},
  "solutions_page": {"eyebrow": "What we do", "h1": "Services for the whole claims lifecycle."},
  "why_page": {"h1": "Technology and expertise, in the right combination."},
  "lead": {
    "eyebrow": "Leadership", "h2": "Leadership",
    "rows": [("Chairman Board of Managers", ["Mohammed AlSaeed"]),
             ("Board Members", ["Sultan Alkhomashi", "Abdullah Abahussain"]),
             ("Chief Executive Officer", ["Eng. Mohammed Hamad <span style=\"white-space:nowrap\">Al-Quraishah</span>"])]},
  "cta_block": {
    "eyebrow": "Partner with Tamayah", "h2": "Partner with Tamayah.",
    "text": "Whether you are looking to enhance claims processing efficiency, streamline medical authorization management, or improve settlement and reconciliation processes, Tamayah is ready to support your journey.",
    "text2": "Together, we can build a more efficient, transparent and technology-enabled healthcare claims and benefits administration ecosystem.",
    "email": "Email us", "call": "Call 920011978"},
  "contact": {
    "eyebrow": "Contact us", "h2": "Contact us.",
    "lede": "We are glad to connect, explore opportunities for collaboration and build innovative solutions that meet your needs and support your goals.",
    "rows": {"email": "Email", "phone": "Phone", "linkedin": "LinkedIn", "x": "X"},
    "linkedin_text": "Tamayah"},
  "footer": {"explore": "Explore", "contact": "Contact", "reg": "Tamayah operates under the supervision and oversight of the Insurance Authority and is authorized to conduct transactions through the Nphies platform.", "rights": "© 2026 Tamayah. All rights reserved."},
  "views": "Open"
},
"ar": {
  "lang": "ar", "dir": "rtl", "name": "تماية",
  "other": "en", "other_label": "EN", "this_label": "العربية",
  "skip": "انتقل إلى المحتوى", "menu": "القائمة", "lang_label": "اللغة",
  "nav": {"index": "الرئيسية", "about": "من نحن", "solutions": "ماذا نقدم", "why": "لماذا تماية؟", "leadership": "القيادة", "contact": "تواصل معنا"},
  "cta": "شاركنا النجاح",
  "titles": {
    "index": "تماية | حلول إدارة وتسوية المطالبات الطبية",
    "about": "من نحن | تماية",
    "solutions": "ماذا نقدم | تماية",
    "why": "لماذا تماية؟",
    "leadership": "القيادة | تماية",
    "contact": "تواصل معنا | شاركنا النجاح"},
  "desc": "تماية شركة متخصصة في تقديم حلول إدارة وتسوية المطالبات الطبية في المملكة العربية السعودية، وتعمل تحت إشراف ورقابة هيئة التأمين.",
  "hero": {
    "eyebrow": "إدارة وتسوية المطالبات الطبية",
    "lines": ["المطالبات والمنافع", "الصحية، بكفاءة", "<em>وشفافية.</em>"],
    "lede": "تماية شركة متخصصة في تقديم حلول إدارة وتسوية المطالبات الطبية. نجمع بين التقنيات المتقدمة والخبرات المتخصصة والتميز التشغيلي لجعل إدارة المطالبات والمنافع الصحية أكثر كفاءة وشفافية وموثوقية.",
    "primary": "شاركنا النجاح", "secondary": "اكتشف ما نقدم",
    "meta": ["تحت إشراف <b>هيئة التأمين</b>", "مصرّح لها عبر منصة <b>نفيس</b>", "أكثر من <b>1,700</b> مقدم خدمة"]},
  "stack_aria": "رحلة مطالبة توضيحية: الموافقة، التحقق، التسوية، المطابقة، الإغلاق",
  "states": [
    ("الموافقة الطبية", "مراجعة وفق المنافع وشروط الوثيقة"),
    ("التحقق من المطالبة", "استقبال ومراجعة وتحقق"),
    ("التسوية", "معالجة بإجراءات واضحة"),
    ("المطابقة المالية", "تحديد الفروقات ومعالجتها"),
    ("إغلاق المطالبة", "إغلاق دقيق وشفاف")],
  "reg": {"tag": "الوضع التنظيمي",
          "text": "تعمل تماية تحت إشراف ورقابة هيئة التأمين، ومصرّح لها بإجراء المعاملات عبر منصة نفيس.",
          "count": 1700, "count_label": "مقدم خدمة صحية"},
  "aud": {
    "eyebrow": "من نخدم", "h2": "مصممة لكل أطراف رحلة المطالبات.",
    "lede": "الإدارة الفعالة للمطالبات لا تقتصر على معالجة المعاملات، بل تتمثل في بناء تجربة تتسم بالكفاءة والشفافية والموثوقية لجميع الأطراف ذات العلاقة.",
    "items": [
      ("شركات التأمين", "التكنولوجيا وشبكة مقدمي الخدمات والخبرات المتخصصة لإدارة البرامج الصحية بكفاءة وشفافية وعلى نطاق واسع.", "solutions"),
      ("أصحاب العمل الذين يمولون برامجهم ذاتيًا", "إجراءات منظمة ومعالجة واضحة للمطالبات وأنشطة التسوية في البرامج التي تموّلونها.", "solutions"),
      ("المنشآت الصحية", "معالجة دقيقة وحلول في الوقت المناسب عبر دورة المطالبات، مع شفافية في التسوية.", "why"),
      ("مقدمو الخدمات الصحية", "معالجة في الوقت المناسب واستجابة فعالة تساعدكم على تسوية أسرع وأكثر كفاءة للمطالبات.", "solutions"),
      ("المستفيدون", "تجربة أكثر سلاسة عبر مركز الاتصال وخدمة العملاء، إلى جانب خدمات الرعاية الخاصة والنخبة.", "solutions#suite")]},
  "eco": {
    "eyebrow": "ماذا نقدم", "h2": "منظومة متكاملة للمطالبات والمنافع الصحية.",
    "lede": "في تماية، ندير رحلة المطالبات والمنافع الصحية من خلال منهجية متكاملة تجمع بين التكنولوجيا والخبرة والانضباط التشغيلي. صُممت خدماتنا لدعم شركائنا عبر مختلف مراحل دورة المطالبات، بما يضمن كفاءة المعالجة، ودقة اتخاذ القرار، وشفافية التسويات.",
    "core": [
      ("إدارة الموافقات الطبية", "نتولى إدارة ومراجعة طلبات الموافقات الطبية بكفاءة ودقة، مع ضمان توافقها مع المنافع والتغطيات التأمينية المعتمدة، وشروط وأحكام الوثائق، والمتطلبات واللوائح التنظيمية ذات الصلة."),
      ("إدارة المطالبات الطبية", "نستقبل المطالبات الطبية ونراجعها ونتحقق من صحتها ونعالجها من خلال أنظمة متقدمة مدعومة بالتكنولوجيا، بما يسهم في تعزيز الدقة والكفاءة وسرعة معالجة المطالبات والوصول إلى قرارات وحلول في الوقت المناسب."),
      ("تسوية المطالبات والمطابقة المالية", "ندير عمليات تسوية المطالبات والمطابقة المالية، ونعمل على تحديد الفروقات والتباينات ومعالجتها، بما يضمن دقة وشفافية إغلاق المطالبات وتسويتها.")],
    "layers": [
      ("نتائج صحية", "إدارة صحة السكان", "نقدم برامج متخصصة لإدارة صحة السكان (PHM) تهدف إلى الوقاية من المضاعفات، وتحسين النتائج الصحية، والحد من الاستخدام غير الضروري للخدمات الصحية، بما يسهم في رفع جودة الرعاية وتعزيز كفاءة الإنفاق الصحي."),
      ("تجربة الخدمة", "مركز الاتصال وخدمة العملاء", "نقدم خدمات متكاملة لمركز الاتصال وخدمة العملاء، بهدف ضمان سرعة الاستجابة، وسهولة الوصول إلى الدعم، وتحسين تجربة المستفيدين ومقدمي الخدمات في مختلف مراحل رحلة الخدمة.")],
    "more": "استكشف جميع الخدمات"},
  "suite": {
    "eyebrow": "خدمات الرعاية المتميزة", "h2": "خصوصية في صميم التصميم.",
    "lede": "خدمتان مصممتان حول الخصوصية وسرعة الاستجابة وسهولة الوصول إلى الرعاية الصحية.",
    "concierge": {"t": "الطب بنظام الرعاية الخاصة <span class=\"ltr\">(Concierge Medicine)</span>",
      "intro": "خدمة رعاية صحية متكاملة ومخصصة توفر للمستفيد تجربة أكثر سهولة وخصوصية.",
      "hours": "مدير الرعاية · 8 صباحًا – 12 منتصف الليل",
      "perks": [("مدير رعاية مخصص", "متاح من الساعة 8 صباحًا حتى 12 منتصف الليل لتقديم المساعدة الشخصية والمتابعة المستمرة."),
                ("إشراف طبي خاص", "طبيب مخصص للإشراف على الخطة الصحية للمستفيد ومتابعة احتياجاته الطبية."),
                ("أولوية الوصول", "تسهيل الحصول على المواعيد لدى كبرى المستشفيات."),
                ("التنسيق الطبي", "إدارة الموافقات والإجراءات الطبية قبل العمليات، إلى جانب تنسيق ترتيبات الإقامة عند الحاجة."),
                ("خدمات الأدوية", "توصيل الأدوية إلى المنزل وإدارة طلبات إعادة صرف الوصفات."),
                ("فحوصات طبية استباقية", "متابعة دورية للحالة الصحية وإجراء الفحوصات الوقائية، وغيرها من الخدمات.")]},
    "elite": {"t": "خدمات النخبة وكبار الشخصيات",
      "intro": "خدمات مصممة لتوفير مستوى عالٍ من الخصوصية والاستجابة وسهولة الوصول إلى الرعاية الصحية.",
      "hours": "مدير الحساب · 9 صباحًا – 9 مساءً",
      "perks": [("مدير حساب مخصص", "متاح من الساعة 9 صباحًا حتى 9 مساءً، مع دعم حجز المواعيد خلال أقل من ساعتين."),
                ("أولوية الوصول", "تسهيل الحصول على المواعيد لدى كبرى المستشفيات."),
                ("التنسيق الطبي", "إدارة الموافقات والإجراءات الطبية قبل العمليات، إلى جانب تنسيق ترتيبات الإقامة عند الحاجة."),
                ("خدمات الأدوية", "توصيل الأدوية إلى المنزل وإدارة طلبات إعادة صرف الوصفات."),
                ("فحوصات طبية استباقية", "متابعة دورية للحالة الصحية والفحوصات الوقائية.")]}},
  "why": {
    "eyebrow": "لماذا تماية؟",
    "quote": "لأن الإدارة الأفضل للمطالبات تبدأ بالمزيج الصحيح بين <em>التكنولوجيا والخبرة.</em>",
    "paras": ["في تماية، ندرك أن الإدارة الفعالة للمطالبات لا تقتصر على معالجة المعاملات، بل تتمثل في بناء تجربة تتسم بالكفاءة والشفافية والموثوقية لجميع الأطراف ذات العلاقة.",
              "يتيح لنا نموذجنا التشغيلي المدعوم بالتكنولوجيا إدارة عمليات المطالبات المعقدة بكفاءة، مع الحفاظ على تركيزنا على الدقة والكفاءة والشفافية وجودة الخدمة.",
              "ونعمل بشكل وثيق مع شركائنا لفهم احتياجاتهم التشغيلية وتقديم حلول تدعم أهدافهم، وتسهم في بناء منظومة رعاية صحية أكثر كفاءة وفعالية.",
              "ونسعى إلى تقديم معالجة دقيقة، وتسويات في الوقت المناسب، ونتائج موثوقة، بما يحقق قيمة مستدامة لشركائنا وعملائهم."],
    "values_h": "قيمنا",
    "values": [("الكفاءة المدعومة بالتكنولوجيا", "نوظف التقنيات الحديثة والحلول الرقمية لتبسيط عمليات المطالبات، والحد من التعقيدات التشغيلية، وتعزيز كفاءة وسرعة المعالجة."),
               ("الدقة والجودة", "تسهم عملياتنا المنظمة وخبراتنا المتخصصة في دعم دقة معالجة المطالبات والحفاظ على مستوى ثابت من جودة الخدمة عبر مختلف مراحل دورة المطالبة."),
               ("السرعة والاستجابة", "نلتزم بالمعالجة في الوقت المناسب والاستجابة الفعالة، بما يساعد مقدمي الخدمة على تحقيق تسوية أسرع وأكثر كفاءة للمطالبات."),
               ("الشفافية", "نعزز الشفافية في مختلف عملياتنا من خلال إجراءات واضحة ومنظمة، وآليات محددة لإدارة المطالبات وأنشطة التسوية المالية."),
               ("الالتزام بالأنظمة", "نعمل ضمن الأطر التنظيمية المعمول بها، ونولي التزامًا راسخًا بالمعايير المهنية والتنظيمية ذات الصلة.")]},
  "vmc": {
    "vision_h": "رؤيتنا", "vision": "أن نكون الجهة الأكثر موثوقية في المنطقة لإدارة المنافع الصحية، بحيث يحقق <em>كل ريال يُنفق نتائج صحية أفضل.</em>",
    "mission_h": "رسالتنا", "mission": "تمكين شركات التأمين وأصحاب العمل الذين يمولون برامجهم الصحية ذاتيًا والمنشآت الصحية، من خلال التكنولوجيا وشبكة مقدمي الخدمات والخبرات المتخصصة، لإدارة برامجهم الصحية بكفاءة وشفافية وعلى نطاق واسع.",
    "commit_h": "التزامنا",
    "commit": ["نلتزم بمواصلة تطوير وتحسين أساليب إدارة المطالبات والمنافع الصحية من خلال التكامل بين الكفاءات البشرية، كفاءة العمليات والتقنيات المتقدمة.",
               "ومن خلال التطوير المستمر والتميز التشغيلي، نهدف إلى مساعدة شركائنا على تحقيق مستويات أعلى من الكفاءة، مع تقديم تجربة أكثر سلاسة وموثوقية في إدارة المطالبات والمنافع الصحية."]},
  "about": {
    "eyebrow": "من نحن", "h1": "من نحن.",
    "lede": "تماية هي شركة متخصصة في تقديم حلول إدارة وتسوية المطالبات الطبية، تعمل تحت إشراف ورقابة هيئة التأمين.",
    "paras": ["نجمع بين التقنيات المتقدمة والخبرات المتخصصة والتميز التشغيلي لتبسيط دورة المطالبات الطبية وإدارتها بكفاءة أعلى. وتشمل حلولنا إدارة الموافقات الطبية، ومعالجة المطالبات، والتسويات المالية، والمطابقة والتسوية المحاسبية، بما يسهم في تعزيز الكفاءة والدقة والشفافية وسرعة الإنجاز.",
              "ومن خلال دمج الحلول الرقمية الذكية مع فرق تشغيلية ذات خبرة، نساعد مقدمي الخدمة على تحسين عمليات إدارة المطالبات، والارتقاء بجودة الخدمات، وضمان الالتزام بالمعايير التنظيمية والمهنية المعمول بها."]},
  "solutions_page": {"eyebrow": "ماذا نقدم", "h1": "خدمات تغطي دورة المطالبات بأكملها."},
  "why_page": {"h1": "التكنولوجيا والخبرة، بالمزيج الصحيح."},
  "lead": {
    "eyebrow": "القيادة", "h2": "القيادة",
    "rows": [("رئيس مجلس المديرين", ["محمد السعيد"]),
             ("أعضاء مجلس المديرين", ["سلطان الخمشي", "عبدالله أبا حسين"]),
             ("الرئيس التنفيذي", ["م. محمد بن حمد آل قريشة"])]},
  "cta_block": {
    "eyebrow": "شاركنا النجاح", "h2": "شاركنا النجاح.",
    "text": "سواء كنتم تسعون إلى رفع كفاءة معالجة المطالبات، أو تبسيط إدارة الموافقات الطبية، أو تحسين عمليات التسوية والمطابقة المالية، فإن تماية على استعداد لدعمكم في رحلتكم.",
    "text2": "معًا، نبني منظومة أكثر كفاءة وشفافية، ومدعومة بالتقنية المتقدمة لإدارة المطالبات والمنافع الصحية.",
    "email": "راسلنا", "call": "اتصل بنا 920011978"},
  "contact": {
    "eyebrow": "تواصل معنا", "h2": "تواصل معنا.",
    "lede": "يسعدنا التواصل معكم واستكشاف فرص التعاون وبناء حلول مبتكرة تلبي احتياجاتكم وتدعم أهدافكم.",
    "rows": {"email": "البريد الإلكتروني", "phone": "الهاتف", "linkedin": "لينكدإن", "x": "إكس"},
    "linkedin_text": "Tamayah"},
  "footer": {"explore": "استكشف", "contact": "تواصل معنا", "reg": "تعمل تماية تحت إشراف ورقابة هيئة التأمين، ومصرّح لها بإجراء المعاملات عبر منصة نفيس.", "rights": "© 2026 تماية. جميع الحقوق محفوظة."},
  "views": "افتح"
}}

# ---------------------------------------------------------------- SVG pieces
ARROW = '<svg class="flip" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

# The wing/leaf mark, redrawn from the logo's geometry as a reusable symbol.
SYMBOLS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
<defs>
  <linearGradient id="gWing" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#326B73" stop-opacity=".95"/><stop offset="1" stop-color="#326B73" stop-opacity=".18"/></linearGradient>
  <symbol id="wing" viewBox="-6 -6 540 372">
    <path class="wing-fill" d="M0 0H222C285 0 337 52 337 115V235C337 175 290 128 216 120L117 115A117 115 0 0 1 0 0Z"/>
    <path class="wing-line" d="M216 122V355C280 352 327 300 327 238"/>
    <path class="wing-line" d="M277 17C295 8 318 3 337 3H525C522 62 470 113 410 113H337"/>
  </symbol>
</defs></svg>'''

def wing(cls="", attrs=""):
    return f'<svg class="{cls}" viewBox="-6 -6 540 372" aria-hidden="true" focusable="false" {attrs}><use href="#wing"/></svg>'

def hero_svg():
    paths = [
        ("M-20 700C300 700 500 480 820 470S1300 300 1620 240", "0s"),
        ("M-20 560C260 560 520 470 820 470S1320 560 1620 640", "-1.4s"),
        ("M-20 420C300 420 560 430 820 470S1300 420 1620 400", "-2.8s"),
        ("M-20 250C300 240 540 400 820 470S1340 700 1620 800", "-4.2s"),
        ("M-20 830C400 830 600 600 820 470S1200 150 1620 120", "-5.6s"),
        ("M-20 120C340 140 620 330 820 470S1250 620 1620 520", "-3.5s"),
    ]
    base = "".join(f'<path class="path-base" d="{d}"/>' for d, _ in paths)
    glow = "".join(f'<path class="path-glow" style="--dl:{dl}" d="{d}"/>' for d, dl in paths)
    return f'''<svg class="mirror" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
  <g data-par="14">
    <use href="#wing" x="760" y="150" width="860" height="593" opacity=".95"/>
  </g>
  <g data-par="-8">{base}{glow}
    <circle cx="820" cy="470" r="44" fill="none" stroke="rgba(128,234,186,.35)"/>
    <circle cx="820" cy="470" r="86" fill="none" stroke="rgba(247,246,242,.10)"/>
    <circle cx="820" cy="470" r="6" fill="#80EABA"/>
  </g>
</svg>'''

# ---------------------------------------------------------------- Components
def href(c, page, ext=""):
    """Return an on-page anchor for a navigation item.

    `ext` is retained for the few content links which target a subsection.
    """
    anchors = dict(NAV_ITEMS)
    return f"{anchors[page]}{ext}"

def split_anchor(s):
    if "#" in s:
        p, a = s.split("#", 1)
        return p, "#" + a
    return s, ""

def header(c):
    L = c
    nav = "".join(f'<li><a href="{href(c,p)}" data-nav-link>{L["nav"][p]}</a></li>' for p, _ in NAV_ITEMS)
    drawer = "".join(
        f'<li><a class="dl" href="{href(c,p)}"><span>{L["nav"][p]}</span><small>0{i+1}</small></a></li>'
        for i, (p, _) in enumerate(NAV_ITEMS))
    # build proper switcher: both languages shown, current marked
    en_cur = "true" if L["lang"] == "en" else "false"
    ar_cur = "true" if L["lang"] == "ar" else "false"
    lang = (f'<div class="lang" role="group" aria-label="{L["lang_label"]}">'
            f'<a href="../en/index.html" hreflang="en" lang="en" aria-current="{en_cur}">EN</a>'
            f'<a href="../ar/index.html" hreflang="ar" lang="ar" aria-current="{ar_cur}">العربية</a></div>')
    return f'''<header class="header"><div class="wrap header__in">
  <a class="brand" href="#top" aria-label="{L["name"]}"><img src="../assets/Tamayah_Logo_NEG.png" width="2400" height="786" alt="{L["name"]}"></a>
  <nav class="nav" aria-label="Primary"><ul>{nav}</ul></nav>
  <div class="header__tools">{lang}
    <a class="btn" href="#partner">{L["cta"]}{ARROW}</a>
    <button class="burger" aria-expanded="false" aria-controls="drawer" aria-label="{L["menu"]}"><span></span><span></span></button>
  </div>
</div></header>
<div class="drawer" id="drawer"><nav aria-label="Mobile"><ul>{drawer}</ul></nav>
  <a class="btn" href="#partner">{L["cta"]}{ARROW}</a></div>'''

def hero(c):
    h = c["hero"]
    lines = "".join(f'<span class="line"><span style="--i:{i}">{t}</span></span>' for i, t in enumerate(h["lines"]))
    meta = "".join(f'<span>{m}</span>' for m in h["meta"])
    cards = ""
    for i, (t, s) in enumerate(c["states"]):
        last = i == len(c["states"]) - 1
        cards += f'''<div class="stack__card" data-pos="{i}"><div class="stack__top"><span class="chip"><i></i>{t}</span>{f'<span class="stack__tick">{TICK}</span>' if last else ""}</div>
<span class="sk w80" style="margin-block-start:22px"></span><span class="sk w60"></span><span class="sk w40"></span>
<p style="margin-block-start:22px;font-size:.9rem;color:rgba(247,246,242,.7)">{s}</p></div>'''
    legend = "".join("<i></i>" for _ in c["states"])
    return f'''<section class="hero" id="top">
  <div class="hero__bg" aria-hidden="true"><div class="hero__glow"></div><div class="hero__grid"></div>{hero_svg()}</div>
  <div class="wrap hero__body">
    <div>
      <span class="eyebrow fade-up">{h["eyebrow"]}</span>
      <h1 class="display h1">{lines}</h1>
      <p class="lede fade-up" style="--d:2;color:rgba(247,246,242,.82)">{h["lede"]}</p>
      <div class="hero__actions fade-up" style="--d:3">
        <a class="btn" href="#partner">{h["primary"]}{ARROW}</a>
        <a class="btn btn--ghost" href="#services">{h["secondary"]}</a>
      </div>
      <div class="hero__meta fade-up" style="--d:4">{meta}</div>
    </div>
    <div class="stack fade-up" style="--d:3" role="img" aria-label="{c["stack_aria"]}">{cards}<div class="stack__legend">{legend}</div></div>
  </div>
</section>'''

def ledger(c):
    r = c["reg"]
    return f'''<section class="ledger" aria-label="{r["tag"]}"><div class="wrap ledger__in">
  <div class="rv"><div class="count"><span data-count="{r["count"]}">{r["count"]:,}</span><sup>+</sup></div><span class="count-label">{r["count_label"]}</span></div>
  <div class="rv" style="--d:2"><span class="ledger__tag">{r["tag"]}</span><p class="ledger__txt">{r["text"]}</p></div>
</div></section>'''

def audiences(c):
    a = c["aud"]
    items = ""
    for i, (t, d, link) in enumerate(a["items"]):
        p, anc = split_anchor(link)
        target = anc or href(c, p)
        items += f'''<li><a class="aud__item rv" style="--d:{i}" href="{target}"><span class="aud__n">0{i+1}</span><h3>{t}</h3><p>{d}</p></a></li>'''
    return f'''<section class="section on-light"><div class="wrap">
  <div class="section__head"><span class="eyebrow rv">{a["eyebrow"]}</span><h2 class="display h2 rv" style="--d:1">{a["h2"]}</h2><p class="lede rv" style="--d:2">{a["lede"]}</p></div>
  <ul class="aud">{items}</ul></div></section>'''

def eco(c, link=True, head=True):
    e = c["eco"]
    svcs = ""
    for i, (t, d) in enumerate(e["core"]):
        svcs += f'''<li class="svc rv" style="--d:{i}"><div class="svc__node"><span class="svc__dot">0{i+1}</span></div>
<div class="svc__card"><h3 class="h3">{t}</h3><p>{d}</p></div></li>'''
    layers = "".join(f'''<div class="layer rv" style="--d:{i}"><span class="layer__tag">{tag}</span><h3 class="h3">{t}</h3><p>{d}</p></div>''' for i, (tag, t, d) in enumerate(e["layers"]))
    more = f'<p class="rv" style="margin-block-start:40px"><a class="link-arrow" href="#suite">{e["more"]}{ARROW}</a></p>' if link else ""
    headhtml = f'''<div class="section__head"><span class="eyebrow rv">{e["eyebrow"]}</span><h2 class="display h2 rv" style="--d:1">{e["h2"]}</h2><p class="lede rv" style="--d:2">{e["lede"]}</p></div>''' if head else ""
    return f'''<section class="section section--ink on-dark eco" id="services"><div class="wrap">
  {headhtml}
  <div class="eco__rail"><div class="eco__line" aria-hidden="true"></div><ol style="display:contents">{svcs}</ol></div>
  <div class="layers">{layers}</div>{more}
</div></section>'''

def suite(c):
    s = c["suite"]
    def col(k):
        d = s[k]
        perks = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in d["perks"])
        return f'''<div class="suite__col rv"><h3>{d["t"]}</h3><p>{d["intro"]}</p><span class="suite__hours">{d["hours"]}</span><ul class="perks">{perks}</ul></div>'''
    return f'''<section class="section suite on-dark" id="suite"><div class="wrap">
  {wing("suite__mark")}
  <div class="section__head"><span class="eyebrow rv">{s["eyebrow"]}</span><h2 class="display h2 rv" style="--d:1">{s["h2"]}</h2><p class="lede rv" style="--d:2">{s["lede"]}</p></div>
  <div class="suite__grid">{col("concierge")}{col("elite")}</div></div></section>'''

def values(c, num=True):
    w = c["why"]
    rows = "".join(f'<li class="val"><h3><small>0{i+1}</small>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(w["values"]))
    return f'<ul class="values">{rows}</ul>'

def why(c, full=False):
    w = c["why"]
    paras = ""
    if full:
        paras = '<div class="prose rv" style="margin-block-end:clamp(48px,7vw,96px)">' + "".join(f"<p>{p}</p>" for p in w["paras"]) + "</div>"
    return f'''<section class="section on-light" id="why"><div class="wrap">
  <div class="section__head"><span class="eyebrow rv">{w["eyebrow"]}</span><p class="big-quote rv" style="--d:1;color:var(--ink)">{w["quote"]}</p></div>
  {paras}
  <h3 class="eyebrow rv" style="margin-block-end:28px">{w["values_h"]}</h3>
  {values(c)}
</div></section>'''

def vmc(c):
    v = c["vmc"]
    commit = "".join(f"<p>{p}</p>" for p in v["commit"])
    return f'''<section class="section section--ink on-dark vmc-sec"><div class="wrap vmc">
  <div class="vmc__vision rv"><span class="eyebrow">{v["vision_h"]}</span><p class="big-quote" style="margin-block-start:22px">{v["vision"]}</p></div>
  <div class="vmc__cols">
    <div class="rv"><h3>{v["mission_h"]}</h3><p>{v["mission"]}</p></div>
    <div class="rv" style="--d:2"><h3>{v["commit_h"]}</h3>{commit}</div>
  </div></div></section>'''

def leadership(c, head=True):
    l = c["lead"]
    rows = "".join(f'''<div class="lead__row rv"><span class="lead__role">{r}</span><ul class="lead__names">{"".join(f"<li>{n}</li>" for n in names)}</ul></div>''' for r, names in l["rows"])
    headhtml = f'<div class="section__head"><span class="eyebrow rv">{l["eyebrow"]}</span><h2 class="display h2 rv" style="--d:1">{l["h2"]}</h2></div>' if head else ""
    return f'''<section class="section section--black on-dark" id="leadership"><div class="wrap">
  {headhtml}
  <div class="lead">{rows}</div></div></section>'''

def cta(c):
    b = c["cta_block"]
    return f'''<section class="section cta on-dark" id="partner">
  <svg class="cta__wing" viewBox="-6 -6 540 372" aria-hidden="true" focusable="false">
    <g class="a"><path class="wing-fill" d="M0 0H222C285 0 337 52 337 115V235C337 175 290 128 216 120L117 115A117 117 0 0 1 0 0Z"/><path class="wing-line" d="M216 122V355C280 352 327 300 327 238"/></g>
    <g class="b"><path class="wing-line" d="M277 17C295 8 318 3 337 3H525C522 62 470 113 410 113H337"/></g>
  </svg>
  <div class="wrap"><span class="eyebrow rv">{b["eyebrow"]}</span>
    <h2 class="display h1 rv" style="--d:1;margin-block-start:22px">{b["h2"]}</h2>
    <div class="prose rv" style="--d:2;margin-block-start:28px"><p class="lede">{b["text"]}</p><p>{b["text2"]}</p></div>
    <div class="cta__actions rv" style="--d:3"><a class="btn" href="mailto:{EMAIL}">{b["email"]}{ARROW}</a><a class="btn btn--ghost" href="tel:{PHONE}"><span class="ltr">{b["call"] if c["lang"]=="ar" else b["call"]}</span></a></div>
  </div></section>'''

def contact(c, head=True):
    k = c["contact"]; r = k["rows"]
    headhtml = f'<span class="eyebrow rv">{k["eyebrow"]}</span><h2 class="display h2 rv" style="--d:1">{k["h2"]}</h2><p class="lede rv" style="--d:2">{k["lede"]}</p>' if head else ""
    return f'''<section class="section on-light" id="contact"><div class="wrap contact">
  <div class="contact__brand">{headhtml}
    <img class="rv" style="--d:3" src="../assets/Tamayah_Logo_POS.png" width="2400" height="786" alt="{c["name"]}" loading="lazy"></div>
  <dl class="contact__list rv">
    <div class="contact__row"><dt>{r["email"]}</dt><dd><a class="ltr" href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
    <div class="contact__row"><dt>{r["phone"]}</dt><dd><a class="ltr" href="tel:{PHONE}">{PHONE}</a></dd></div>
    <div class="contact__row"><dt>{r["linkedin"]}</dt><dd><a class="ltr" href="{LINKEDIN_URL}" target="_blank" rel="noopener">{k["linkedin_text"]}</a></dd></div>
    <div class="contact__row"><dt>{r["x"]}</dt><dd><a class="ltr" href="https://x.com/{X_HANDLE}" target="_blank" rel="noopener">@{X_HANDLE}</a></dd></div>
  </dl></div></section>'''

def about_body(c):
    a = c["about"]
    paras = "".join(f"<p>{p}</p>" for p in a["paras"])
    return f'''<section class="section on-light" id="about"><div class="wrap split">
  <div><span class="eyebrow rv">{a["eyebrow"]}</span><h2 class="display h2 rv" style="--d:1;margin-block-start:22px">{a["h1"]}</h2></div>
  <div class="prose rv" style="--d:1">{paras}</div></div></section>'''

def phero(c, eyebrow, h1, lede=""):
    ld = f'<p class="lede fade-up" style="--d:2">{lede}</p>' if lede else ""
    return f'''<section class="phero"><div class="wrap">
  {wing("phero__wing", 'data-par="10"')}
  <span class="eyebrow fade-up">{eyebrow}</span>
  <h1 class="display h1 fade-up" style="--d:1;font-size:clamp(2.4rem,5vw + .5rem,5.4rem)">{h1}</h1>{ld}</div></section>'''

def footer(c):
    f = c["footer"]
    nav = "".join(f'<li><a href="{href(c,p)}">{c["nav"][p]}</a></li>' for p, _ in NAV_ITEMS)
    r = c["contact"]["rows"]
    return f'''<footer class="footer"><div class="wrap">
  <div class="footer__top">
    <div><a class="brand" href="#top" aria-label="{c["name"]}"><img src="../assets/Tamayah_Logo_NEG.png" width="2400" height="786" alt="{c["name"]}" loading="lazy"></a><p class="footer__reg">{f["reg"]}</p></div>
    <div><h4>{f["explore"]}</h4><ul>{nav}</ul></div>
    <div><h4>{f["contact"]}</h4><ul>
      <li><a class="ltr" href="tel:{PHONE}">{PHONE}</a></li>
      <li><a class="ltr" href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a class="ltr" href="{LINKEDIN_URL}" target="_blank" rel="noopener">LinkedIn · Tamayah</a></li>
      <li><a class="ltr" href="https://x.com/{X_HANDLE}" target="_blank" rel="noopener">X · @{X_HANDLE}</a></li></ul></div>
  </div>
  <div class="footer__bot"><span>{f["rights"]}</span><span>Riyadh · Saudi Arabia</span></div>
</div></footer>'''.replace('<span>Riyadh · Saudi Arabia</span>', '')

def page_body(c, page):
    if page == "index":
        return hero(c) + ledger(c) + about_body(c) + audiences(c) + eco(c) + suite(c) + why(c, full=True) + vmc(c) + leadership(c) + cta(c) + contact(c)
    if page == "about":
        a = c["about"]
        return phero(c, a["eyebrow"], a["h1"], a["lede"]) + about_body(c) + ledger(c) + vmc(c) + cta(c)
    if page == "solutions":
        s = c["solutions_page"]
        return phero(c, s["eyebrow"], s["h1"], c["eco"]["lede"]) + eco(c, link=False, head=False) + suite(c) + cta(c)
    if page == "why":
        w = c["why"]
        return phero(c, w["eyebrow"], c["why_page"]["h1"]) + why(c, full=True) + cta(c)
    if page == "leadership":
        l = c["lead"]
        return phero(c, l["eyebrow"], l["h2"]) + leadership(c, head=False) + cta(c)
    if page == "contact":
        k = c["contact"]
        return phero(c, k["eyebrow"], k["h2"], k["lede"]) + contact(c, head=False)
    raise ValueError(page)

def render(lang, page):
    c = CONTENT[lang]
    other = "ar" if lang == "en" else "en"
    title = c["titles"][page]
    body = page_body(c, page)
    return f'''<!doctype html>
<html lang="{lang}" dir="{c["dir"]}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title, quote=False)}</title>
<meta name="description" content="{html.escape(c["desc"])}">
<meta name="theme-color" content="#132028">
<link rel="alternate" hreflang="en" href="../en/index.html">
<link rel="alternate" hreflang="ar" href="../ar/index.html">
<link rel="icon" type="image/png" href="../assets/mark.png">
<link rel="preload" href="../assets/fonts/readex-pro-{"arabic" if lang=="ar" else "latin"}-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<a class="skip" href="#main">{c["skip"]}</a>
{SYMBOLS}
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
<title>Tamayah | تماية</title><meta name="theme-color" content="#132028">
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#132028;color:#F7F6F2;font-family:system-ui,sans-serif;text-align:center}
a{color:#80EABA;margin:0 12px;font-size:1.2rem}img{width:220px;margin-bottom:28px}</style>
<script>
(function(){var l;try{l=localStorage.getItem('tamayah-lang')}catch(e){}
if(!l){l=(navigator.language||'en').toLowerCase().indexOf('ar')===0?'ar':'en'}
location.replace(l+'/index.html')})();
</script></head>
<body><div><img src="assets/Tamayah_Logo_NEG.png" alt="Tamayah تماية"><br><a href="en/index.html">English</a><a href="ar/index.html" lang="ar">العربية</a></div></body></html>
'''

def main():
    for lang in ("en", "ar"):
        os.makedirs(os.path.join(ROOT, lang), exist_ok=True)
        with open(os.path.join(ROOT, lang, "index.html"), "w", encoding="utf-8") as f:
            f.write(render(lang, "index"))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(ROOT_INDEX)
    print("built 2 one-page language variants")

if __name__ == "__main__":
    main()
