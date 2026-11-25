# يولّد صفحات موقع OkiQ (الرئيسية + صفحة لكل تطبيق + الأسعار + السياسات). شغّله بعد أي تعديل بالنصوص:  python build_site.py
import html, os

HERE = os.path.dirname(os.path.abspath(__file__))
WA = "9647738181860"  # واتساب المبيعات

FACES = [
    dict(pkey="clinic", id="clinic", name="OkiQ عيادات", short="العيادات والأطباء",
         tag="عيادتك منظّمة من هاتفك", sub="الدور بلا ازدحام، وملف كامل لكل مريض، والوصفة والتذكير يصلان إلى هاتفه.",
         price="جرّبه أسبوعاً مجاناً، ثم 12$ شهرياً أو 120$ سنوياً.",
         feats=[("calendar", "الدور والمواعيد", "من وصل ومن ينتظر ومن انتهى، وتضيف السكرتيرة المراجع بضغطة فيأخذ رقم دوره."),
                ("doc", "ملف كامل لكل مريض", "الزيارات السابقة والتشخيص والوصفات، وصور التحاليل والأشعة وفيديو العمليات."),
                ("warn", "تنبيه الحساسية", "إذا كان لدى المريض حساسية من دواء يظهر تنبيه واضح في ملفه."),
                ("rx", "الوصفة على هاتف المريض", "يصله تشخيصه ووصفته عبر تطبيق OkiQ أو الواتساب."),
                ("chat", "المحادثة مع المريض", "رسائل مباشرة بين العيادة والمريض داخل التطبيق."),
                ("clock", "تذكير المواعيد", "رسالة تذكير للمراجع قبل موعده، وتذكير بالمبالغ المتبقية."),
                ("calplus", "الحجز من التطبيق", "يطلب المريض موعداً، والعيادة توافق أو تقترح وقتاً آخر."),
                ("users", "لكل موظف صلاحياته", "تسجّل السكرتيرة المواعيد والدفع، ولا ترى الملاحظات الطبية."),
                ("chart", "الحسابات والتقارير", "أجور المعاينات والمستلم والمصاريف وصافي كل شهر.")],
         video=None, video2=None,
         who="يستعمل الطبيب والسكرتيرة «OkiQ عيادات»، ويستعمل المراجع تطبيق «OkiQ»."),
    dict(pkey="generator", id="generator", name="OkiQ أمبيرات", short="أصحاب المولّدات",
         tag="مولّدتك في جيبك", sub="المشتركون والأمبيرات والجباية، وتذكير غير المسددين بالواتساب بضغطة واحدة.",
         price="جرّبه أسبوعاً مجاناً، ثم 12$ شهرياً أو 120$ سنوياً.",
         feats=[("users", "المشتركون والأمبيرات", "كل مشترك بخطوطه وأمبيراته ومنطقته وعنوانه."),
                ("money", "الجباية الشهرية", "تسجيل التسديد في ثوانٍ، ومعرفة من سدّد ومن بقي عليه."),
                ("wa", "تذكير غير المسددين", "إرسال متتابع بالواتساب لكل غير المسددين، مع علامة «أُرسل» لكل واحد."),
                ("edit", "تعديل سعر الشهر", "تغيير سعر الأمبير لجميع المشتركين دفعة واحدة."),
                ("wallet", "فاتورة الشهر والمصاريف", "الوقود والصيانة والرواتب، والصافي الحقيقي لكل شهر."),
                ("megaphone", "تبليغ المشتركين", "إطفاء أو صيانة أو تغيير في التشغيل، يصل إلى جميع المشتركين."),
                ("chart", "التقارير الشهرية", "الجباية والديون والصافي لكل شهر."),
                ("eye", "المشترك يرى حسابه", "يتابع المشترك اشتراكه وديونه من تطبيق «OkiQ».")],
         video=None, video2=None,
         who="يستعمل صاحب المولّدة والجابي «OkiQ أمبيرات»، ويستعمل المشترك تطبيق «OkiQ»."),
    dict(pkey="store", id="installments", name="OkiQ أقساط", short="محلات الأقساط",
         tag="أقساطك منظّمة، ولا يضيع دينار", sub="الزبائن والكفلاء وخطط الأقساط، وتذكير المتأخرين بالواتساب.",
         price="جرّبه أسبوعاً مجاناً، ثم 12$ شهرياً أو 120$ سنوياً.",
         feats=[("user", "الزبائن والكفلاء", "الاسم والهاتف والعنوان والكفيل والدين السابق."),
                ("calendar", "خطط الأقساط", "السعر الكلي والمقدّمة وعدد الأقساط، شهرياً أو أسبوعياً، وتاريخ أول قسط."),
                ("money", "تسديد القسط", "سجّل الدفعة في ثوانٍ، ويتحدّث الحساب تلقائياً."),
                ("warn", "المتأخرون بوضوح", "يظهر المتأخر بلون واضح، فتعرف من تتابع اليوم."),
                ("wa", "تذكير المتأخرين بالواتساب", "رسالة تذكير لكل متأخر بضغطة واحدة."),
                ("doc", "البيع بالدَّين والنقد", "كل حركة مسجّلة: بيع وتسديد ودَين."),
                ("list", "المخزون", "البضاعة والكميات وأسعار البيع."),
                ("users", "لكل موظف صلاحياته", "يرى كل موظف ويعمل ما تسمح له به فقط.")],
         video=None, video2=None,
         who="يستعمل صاحب المحل وموظفوه «OkiQ أقساط»، ويستعمل الزبون تطبيق «OkiQ»."),
    dict(pkey="trips", id="hajj", name="OkiQ حملات", short="حملات الحج والعمرة",
         tag="حملتك معك في كل خطوة", sub="الحجاج والغرف والمجموعات والبرنامج اليومي، والبث الصوتي المباشر، وزر «أنا تائه»، بواجهة واضحة لكبار السن.",
         price="مجاني لقوافل الحج طوال موسم الحج. للعمرة والزيارات اشتراك شهري يدفعه صاحب الحملة فقط.",
         feats=[("pilgrim", "ملف كامل لكل حاج", "الهاتفان والصورة والجواز والتأشيرة والمحرم ورقم السوار والمعلومات الصحية."),
                ("bed", "الغرف والمجموعات والحافلات", "كل حاج في غرفته ومجموعته، وعدّ الحجاج عند الحافلة بضغطة."),
                ("calendar", "برنامج الرحلة ونقاط التجمع", "يوماً بيوم، ويعرف الحاج الفقرة القادمة ويصل إلى نقطة التجمع بالخريطة."),
                ("live", "بث مباشر مثل الراديو", "يتكلم المرشد فيسمعه الحجاج في اللحظة نفسها، حتى وهواتفهم في جيوبهم."),
                ("siren", "زر «أنا تائه»", "يصل موقع الحاج إلى الحملة فوراً، وإذا ضعف الإنترنت تُجهَّز رسالة نصية للمرشد."),
                ("question", "الأسئلة والطلبات", "يسأل الحاج المرشد كتابةً أو بصوته، ولا يرى سؤاله غيره."),
                ("megaphone", "الإعلانات", "إعلان مثبّت في الأعلى، والبقية تُحذف بعد 24 ساعة، وتعرف من اطّلع عليها."),
                ("idcard", "بطاقة الحاج", "بطاقة فيها الفندق والغرفة وهاتف الحملة إذا تاه."),
                ("eye", "خصوصية", "الملاحظات الصحية والداخلية تراها الإدارة فقط.")],
         video=None, video2=None,
         who="يستعمل صاحب الحملة والمرشد والحاج «OkiQ حملات». يبحث الحاج عن حملته في التطبيق ويرسل طلب الانضمام، وتوافق الحملة بضغطة."),
    dict(pkey="school", id="school", name="OkiQ مدارس", short="المدارس والروضات",
         tag="المدرسة والأهل في مكان واحد", sub="الحضور والدرجات والواجبات والتبليغات، ويتابع ولي الأمر ابنه من هاتفه.",
         price="جرّبه أسبوعاً مجاناً، ثم 17$ شهرياً أو 170$ سنوياً.",
         feats=[("users", "الصفوف والطلاب", "كل صف بطلابه وموادّه وجدوله الأسبوعي."),
                ("check", "التحضير اليومي", "يحضّر المعلم الصف في ثوانٍ، ويعرف الأهل فوراً."),
                ("doc", "الدرجات وبطاقة التقرير", "الدرجات لكل مادة، وبطاقة تقرير جاهزة."),
                ("list", "الواجبات ونشاطات الصف", "ينشر المعلم الواجب، ويطّلع عليه الأهل."),
                ("megaphone", "التبليغات", "عطلة أو اجتماع أو تنبيه، يصل إلى جميع أولياء الأمور، وتعرف من قرأه."),
                ("chat", "ملاحظات المعلم والشكاوى", "تواصل منظّم بين المدرسة والأهل."),
                ("money", "الأقساط المدرسية", "من سدّد ومن بقي عليه."),
                ("user", "لكل معلم صلاحياته", "يرى كل معلم صفوفه فقط.")],
         video=None, video2=None,
         who="تستعمل الإدارة والمعلمون وأولياء الأمور «OkiQ مدارس»، ويطلب ولي الأمر الانضمام إلى مدرسة ابنه من التطبيق."),
    dict(id="internet", name="OkiQ إنترنت", short="موزعو الإنترنت",
         tag="برجك منظّم", sub="المشتركون والباقات والتجديد، وتبليغات الصيانة تصل إلى كل المشتركين.",
         price="جرّبه أسبوعاً مجاناً، ثم 12$ شهرياً أو 120$ سنوياً.", pkey="default",
         feats=[("users", "المشتركون والباقات", "كل مشترك بباقته وعنوانه وتاريخ تجديده."),
                ("calendar", "التجديد في وقته", "تعرف من ينتهي اشتراكه اليوم وغداً، ويصله تذكير قبل الانتهاء."),
                ("money", "الجباية والديون", "تسجيل التسديد في ثوانٍ، ومعرفة المتأخرين."),
                ("megaphone", "تبليغات البرج", "انقطاع أو صيانة، يصل التبليغ إلى جميع المشتركين."),
                ("chat", "ملاحظات المشتركين", "يرسل المشترك ملاحظته من التطبيق وتصلك مباشرة."),
                ("chart", "التقارير", "الجباية والمصاريف والصافي لكل شهر.")],
         video=None, video2=None,
         who="يستعمل صاحب البرج وموظفوه «OkiQ إنترنت»، ويستعمل المشترك تطبيق «OkiQ»."),
    dict(id="orders", name="OkiQ بيجات", short="المتاجر الأونلاين",
         tag="طلبات بيجك منظّمة", sub="من رسالة الزبون إلى باب بيته: مراحل الطلب، والمندوبون وفلوسهم، وأجرة التوصيل لكل محافظة.",
         price="جرّبه أسبوعاً مجاناً، ثم 12$ شهرياً أو 120$ سنوياً.", pkey="default",
         feats=[("list", "الطلبات بمراحلها", "جديد، قيد التجهيز، مع المندوب، تم التسليم، أو راجع."),
                ("wa", "حالة الطلب بالواتساب", "رسالة جاهزة للزبون بكل مرحلة بضغطة واحدة."),
                ("money", "فلوس المندوبين", "كم طلباً مع كل مندوب، وكم بذمته بعد خصم أجرته."),
                ("calendar", "أجرة التوصيل لكل محافظة", "تُملأ تلقائياً عند اختيار المحافظة."),
                ("doc", "المنتجات والمخزون", "ينقص المخزون مع كل طلب ويرجع إذا رجع الطلب."),
                ("warn", "الزبون المرجِّع", "تنبيه واضح على الزبون الذي أرجع طلبات سابقة."),
                ("users", "صلاحيات الموظفين", "المجهّز يرى الطلبات فقط، ولا يرى سعر الشراء."),
                ("chart", "المبيعات", "مبيعات اليوم والشهر، والمرتجعات، والمصاريف.")],
         video=None, video2=None,
         who="يستعمل صاحب البيج وموظفوه «OkiQ بيجات»، ويتابع الزبون طلباته من تطبيق «OkiQ»."),
]
ACCENT = dict(main="#2563EB", clinic="#0F9D8A", generator="#D97706", installments="#7C3AED", hajj="#4D7C0F",
              school="#0284C7", internet="#4F46E5", orders="#DB2777", muallimi="#F97316")
CONTACT = "العراق — التواصل عبر واتساب: +964 773 818 1860"

CSS = """
:root{--bg:#F4F8F7;--card:#fff;--line:#E5EBEA;--ink:#1F2937;--soft:#4B5563;--muted:#6B7280;--ac:#2563EB;--acsoft:#E8EFFD}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:Tajawal,system-ui,sans-serif;background:var(--bg);color:var(--ink);line-height:1.75;overflow-x:hidden;
 background-image:radial-gradient(700px 420px at 0 0,#CDEDE6cc,transparent 70%),radial-gradient(600px 500px at 100% 40%,#D3F0EA99,transparent 70%),radial-gradient(700px 500px at 0 100%,#E4E2EEaa,transparent 70%);background-attachment:fixed}
a{color:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:0 18px}
header{position:sticky;top:0;z-index:5;background:#ffffffd9;backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font:800 24px Nunito,Tajawal,sans-serif;direction:ltr}
.brand img{width:36px;height:36px}
nav{display:flex;align-items:center;gap:18px}
nav a{text-decoration:none;color:var(--soft);font-weight:700;font-size:15px;white-space:nowrap}
nav a:hover{color:var(--ac)}
.hero{padding:60px 0 36px;text-align:center}
.hero h1{font-size:clamp(32px,6vw,54px);font-weight:800;line-height:1.25}
.hero p{font-size:clamp(17px,2.4vw,20px);color:var(--soft);max-width:720px;margin:14px auto 0}
.hero .icon{width:104px;height:104px;border-radius:24px;box-shadow:0 14px 36px #0f172a22;margin-bottom:18px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-weight:800;font-size:17px;padding:14px 26px;border-radius:14px;text-decoration:none;border:0;cursor:pointer}
.main{background:var(--ac);color:#fff;box-shadow:0 10px 24px color-mix(in srgb,var(--ac) 30%,transparent)}
.ghost{background:var(--acsoft);color:var(--ac)}
.soon{border:1.5px dashed #C9D1CF;color:var(--muted);background:#fff8;cursor:default}
.dl{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:24px}
.note{font-size:13.5px;color:var(--muted);margin-top:12px}
h2{font-size:clamp(25px,4vw,32px);font-weight:800;text-align:center;margin-bottom:6px}
.lead{text-align:center;color:var(--muted);margin-bottom:26px}
section{padding:44px 0}
.grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(240px,1fr))}
.face,.feat,.step,.plan,.doc{background:var(--card);border:1px solid var(--line);border-radius:18px;box-shadow:0 3px 12px #0f172a0d}
.face{padding:20px;text-decoration:none;display:flex;flex-direction:column;gap:8px;transition:transform .2s}
.face:hover{transform:translateY(-3px)}
.face img{width:62px;height:62px}
.face b{font-size:20px;font-weight:800}
.face span{color:var(--muted);font-size:15px}
.face em{font-style:normal;font-weight:800;margin-top:auto}
.feat{padding:18px}
.feat .e{width:46px;height:46px;border-radius:50%;background:var(--acsoft);display:grid;place-items:center}
.feat .e{color:var(--ac)}.feat .e svg{width:24px;height:24px}
.feat b{display:block;font-size:17.5px;font-weight:800;margin:6px 0 2px}
.feat p{color:var(--muted);font-size:15px}
.steps{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));counter-reset:s}
.step{padding:22px 18px 18px;position:relative}
.step:before{counter-increment:s;content:counter(s);position:absolute;top:-14px;right:18px;width:30px;height:30px;border-radius:50%;background:var(--ac);color:#fff;font-weight:800;display:grid;place-items:center}
.step b{display:block;font-size:17px}
.step p{color:var(--muted);font-size:15px}
.pill{display:inline-block;background:var(--acsoft);color:var(--ac);padding:8px 18px;border-radius:30px;font-weight:800;margin-top:18px}
.cust{display:flex;gap:18px;align-items:center;background:#fff;border:2px solid var(--ac);border-radius:20px;padding:22px;flex-wrap:wrap}
.cust img{width:72px;height:72px}
.cust div{flex:1;min-width:200px}
table.price{width:100%;border-collapse:collapse;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 3px 12px #0f172a0d}
.price th,.price td{padding:14px 12px;border-bottom:1px solid var(--line);text-align:right;font-size:16px}
.price th{background:#F1F5F4;font-weight:800}
.price td img{width:34px;height:34px;vertical-align:middle;margin-left:8px}
.price .n{font-weight:800;white-space:nowrap}
.price .iqd{display:block;color:var(--muted);font-size:13px;font-weight:700}
.doc{padding:26px 24px;max-width:820px;margin:0 auto}
.doc h3{font-size:19px;margin:18px 0 6px}
.doc p,.doc li{color:var(--soft);font-size:16px}
.doc ul{padding-right:22px}
footer{padding:30px 0 40px;text-align:center;color:var(--muted);font-size:14px;border-top:1px solid var(--line);background:#ffffffa6}
footer a{color:var(--ink);text-decoration:none;font-weight:700;margin:0 8px}
footer .links{margin:10px 0}
@media (max-width:640px){nav a.hide{display:none}.hero{padding:40px 0 24px}section{padding:34px 0}.price th,.price td{font-size:14px;padding:10px 8px}}
"""

HEAD = """<!doctype html>
<html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="img/{img}.png">
<link rel="icon" href="img/{img}.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@500;700;800&family=Nunito:wght@800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
</head><body style="--ac:{ac};--acsoft:{acsoft}">
<header><div class="wrap"><a class="brand" href="index.html"><img src="img/logo.svg" alt="">OkiQ</a>
<nav><a href="index.html#apps">التطبيقات</a><a href="pricing.html">الأسعار</a><a class="hide" href="index.html#customers">للزبائن</a><a href="https://wa.me/{wa}">تواصل معنا</a></nav></div></header>
"""
FOOT = """<footer><div class="wrap">
<p><b style="font-family:Nunito,sans-serif;color:var(--ink)">OkiQ</b> — عملك كله في جيبك</p>
<p class="links"><a href="pricing.html">الأسعار</a><a href="terms.html">الشروط والأحكام</a><a href="privacy.html">سياسة الخصوصية</a><a href="refund.html">سياسة الإرجاع والإلغاء</a></p>
<p>{contact}</p>
<p style="margin-top:6px">© 2026 OkiQ. جميع الحقوق محفوظة.</p>
</div></footer>
<script src="site.js"></script>
</body></html>"""

def e(s): return html.escape(s, quote=True)
def soft(hexc, f=0.88):
    h=hexc.lstrip('#'); r,g,b=[int(h[i:i+2],16) for i in (0,2,4)]
    return '#%02X%02X%02X'%tuple(int(c+(255-c)*f) for c in (r,g,b))
def head(title, desc, img, ac):
    return HEAD.format(title=title, desc=desc, img=img, wa=WA, ac=ac, acsoft=soft(ac))
def foot(): return FOOT.format(contact=e(CONTACT))
import re as _re
_ICONS = {}
def icon(x):
    # الأيقونة داخل الصفحة نفسها، بلون التطبيق (currentColor)
    if x not in _ICONS:
        svg = open(os.path.join(HERE, "img", "i", x + ".svg"), encoding="utf-8").read()
        svg = _re.sub(r'(stroke|fill)="#[0-9A-Fa-f]{3,8}"', r'\1="currentColor"', svg)
        svg = _re.sub(r'<\?xml[^>]*>', '', svg)
        svg = _re.sub(r'<svg ', '<svg width="24" height="24" ', svg, count=1)
        _ICONS[x] = svg
    return _ICONS[x]
def feat(x, t, d): return f'<div class="feat"><div class="e">{icon(x)}</div><b>{e(t)}</b><p>{e(d)}</p></div>'

def dl_buttons(face_id):
    return f"""<div class="dl">
<a class="btn main" data-apk="{face_id}" href="#">تحميل للأندرويد</a>
<span class="btn soon">آيفون — قريباً</span>
</div>
<p class="note">إذا طلب الهاتف السماح بالتثبيت من «مصادر غير معروفة»، فوافق مرة واحدة وأكمل التثبيت.</p>"""

def face_page(f):
    ac = ACCENT[f["id"]]
    feats = "".join(feat(*x) for x in f["feats"])
    page = head(f"{f['name']} — {f['tag']}", e(f["sub"]), f["id"], ac)
    page += f"""<main>
<section class="hero"><div class="wrap">
<img class="icon" src="img/{f['id']}.png" alt="{e(f['name'])}">
<h1>{e(f['tag'])}</h1>
<p>{e(f['sub'])}</p>
{dl_buttons(f['id'])}
<span class="pill" data-price="{f['pkey']}">{e(f['price'])}</span>
<p class="note"><a href="pricing.html">تفاصيل الأسعار وطرق الدفع</a></p>
</div></section>
<section><div class="wrap"><h2>ماذا يقدّم {e(f['name'])}؟</h2><p class="lead">ميزات موجودة في التطبيق اليوم</p><div class="grid">{feats}</div></div></section>
<section><div class="wrap"><h2>كيف تبدأ؟</h2><p class="lead">{e(f['who'])}</p><div class="steps">
<div class="step"><b>حمّل التطبيق</b><p>من الزر في الأعلى، وثبّته على هاتفك.</p></div>
<div class="step"><b>أنشئ حسابك</b><p>برقم هاتفك، ثم أنشئ نشاطك باسمه وجرّبه أسبوعاً مجاناً.</p></div>
<div class="step"><b>أضف فريقك وزبائنك</b><p>أرسل لهم كود الدعوة، وينضمون إلى نشاطك بضغطة.</p></div>
</div>
<div class="dl" style="margin-top:28px"><a class="btn ghost" href="https://wa.me/{WA}?text={e('السلام عليكم، أودّ معرفة المزيد عن ' + f['name'])}">اسألنا بالواتساب</a></div>
</div></section>
</main>"""
    return page + foot()

def index_page():
    cards = "".join(f'<a class="face" href="{f["id"]}.html"><img src="img/{f["id"]}.png" alt=""><b>{e(f["name"])}</b><span>{e(f["tag"])} — {e(f["short"])}</span><em style="color:{ACCENT[f["id"]]}">التفاصيل والتحميل ←</em></a>' for f in FACES)
    cards += '<div class="face"><img src="img/muallimi.png" alt=""><b>OkiQ دروس</b><span>دروس تفاعلية للأطفال من الأول إلى السادس الابتدائي</span><em style="color:#F97316">قريباً</em></div>'
    why = [("live", "يعمل بلا إنترنت", "تعمل كالمعتاد، وعند عودة الإنترنت يتحدّث كل شيء تلقائياً."),
           ("users", "فريقك بصلاحياته", "لكل موظف حسابه، وأنت تحدد ما يراه وما يعمله."),
           ("wa", "واتساب وإشعارات", "تذكير الزبائن والمتأخرين بضغطة، وإشعارات فورية."),
           ("check", "عربي ومن بيئتنا", "مصمم لأعمالنا وأسعارنا، وسهل حتى لكبار السن.")]
    page = head("OkiQ — عملك كله في جيبك", "تطبيقات عربية لإدارة العيادات والمولّدات ومحلات الأقساط وحملات الحج والمدارس والإنترنت والمتاجر الأونلاين.", "main", ACCENT["main"])
    page += f"""<main>
<section class="hero"><div class="wrap">
<img class="icon" src="img/main.png" alt="OkiQ">
<h1>عملك كله في جيبك</h1>
<p>مجموعة تطبيقات عراقية لإدارة العيادات والمولّدات ومحلات الأقساط وحملات الحج والمدارس والإنترنت والمتاجر الأونلاين. كل تطبيق مصمم لعملك بالضبط، ويعمل حتى بلا إنترنت.</p>
<div class="dl"><a class="btn main" href="#apps">اختر تطبيقك</a><a class="btn ghost" href="pricing.html">الأسعار</a></div>
</div></section>
<section id="apps"><div class="wrap"><h2>اختر تطبيقك</h2><p class="lead">كل تطبيق مصمم لنوع عمل واحد، بمصطلحاته وشاشاته</p><div class="grid">{cards}</div></div></section>
<section id="customers"><div class="wrap">
<div class="cust"><img src="img/main.png" alt=""><div><b style="font-size:21px">OkiQ — للزبائن</b><p style="color:var(--muted)">مراجع عيادة أو مشترك مولّدة أو إنترنت أو زبون محل؟ حمّل «OkiQ» وتابع مواعيدك ووصفاتك وطلباتك وحسابك، وكل الجهات التي تتعامل معها في مكان واحد. التطبيق مجاني للزبائن.</p></div>
<a class="btn main" data-apk="main" href="#">تحميل للأندرويد</a></div>
</div></section>
<section><div class="wrap"><h2>لماذا OkiQ؟</h2><p class="lead">الأساس القوي نفسه في جميع التطبيقات</p><div class="grid">{"".join(feat(*x) for x in why)}</div></div></section>
</main>"""
    return page + foot()

def pricing_page():
    rows = '<tr><td><img src="img/main.png" alt="">OkiQ (للزبائن)</td><td class="n">مجاني</td><td class="n">مجاني</td></tr>'
    for f in FACES:
        if f["id"] == "hajj":
            rows += f'<tr><td><img src="img/hajj.png" alt="">{e(f["name"])}<span class="iqd">مجاني لقوافل الحج طوال موسم الحج</span></td><td class="n" data-m="trips">12$</td><td class="n" data-y="trips">120$</td></tr>'
            continue
        m = 17 if f["id"] == "school" else 12
        rows += f'<tr><td><img src="img/{f["id"]}.png" alt="">{e(f["name"])}</td><td class="n" data-m="{f["pkey"]}">{m}$</td><td class="n" data-y="{f["pkey"]}">{m*10}$</td></tr>'
    page = head("الأسعار — OkiQ", "أسعار اشتراكات تطبيقات OkiQ الشهرية والسنوية.", "main", ACCENT["main"])
    page += f"""<main>
<section class="hero"><div class="wrap"><h1>الأسعار</h1>
<p>أسعار واضحة بلا رسوم خفية. جرّب أي تطبيق <b data-trial>أسبوعاً</b> مجاناً بدون دفع، ثم اختر الاشتراك الشهري أو السنوي. يدفع صاحب النشاط فقط، والتطبيق مجاني لزبائنه وموظفيه.</p></div></section>
<section style="padding-top:0"><div class="wrap">
<table class="price"><thead><tr><th>التطبيق</th><th>شهرياً</th><th>سنوياً</th></tr></thead><tbody>{rows}</tbody></table>
<p class="note" style="text-align:center">الأسعار بالدولار الأمريكي، وتُدفع بالدينار العراقي حسب سعر الصرف يوم الدفع. الاشتراك السنوي يوفّر عليك شهرين.</p>
</div></section>
<section><div class="wrap"><h2>ماذا يشمل الاشتراك؟</h2><div class="grid">
{feat("users", "كل الموظفين", "عدد غير محدود من الموظفين بصلاحياتهم، بدون رسوم إضافية.")}
{feat("check", "كل الميزات", "جميع ميزات التطبيق والتحديثات الجديدة.")}
{feat("live", "نسخ احتياطي", "بياناتك محفوظة على السيرفر، وتعمل حتى بلا إنترنت.")}
{feat("chat", "دعم بالواتساب", "نجيبك على أسئلتك ونساعدك بالبدء.")}
</div></div></section>
<section><div class="wrap"><h2>طرق الدفع</h2><div class="grid">
{feat("card", "البطاقة المصرفية", "الدفع ببطاقات Visa وMastercard العراقية عبر بوابة دفع إلكتروني مرخّصة. لا نطّلع على رقم بطاقتك ولا نحفظه.")}
{feat("money", "التحويل", "التحويل إلى حسابنا، ويُفعَّل اشتراكك بعد تأكيد الاستلام.")}
</div>
<p class="note" style="text-align:center">لا يوجد تجديد تلقائي: تدفع عند رغبتك بالتجديد فقط. اطّلع على <a href="refund.html">سياسة الإرجاع والإلغاء</a>.</p>
</div></section>
</main>"""
    return page + foot()

def doc_page(file, title, body):
    page = head(f"{title} — OkiQ", title, "main", ACCENT["main"])
    page += f'<main><section class="hero" style="padding-bottom:10px"><div class="wrap"><h1>{title}</h1><p class="note">آخر تحديث: 25 تشرين الثاني 2026</p></div></section><section style="padding-top:10px"><div class="wrap"><div class="doc">{body}</div></div></section></main>'
    open(os.path.join(HERE, file), "w", encoding="utf-8").write(page + foot())

TERMS = """<p>مرحباً بك في OkiQ. باستخدامك لتطبيقاتنا أو موقعنا فإنك توافق على هذه الشروط.</p>
<h3>1. الخدمة</h3><p>OkiQ مجموعة تطبيقات لإدارة الأنشطة التجارية والخدمية (العيادات، والمولّدات، ومحلات الأقساط، وحملات الحج والعمرة، والمدارس، وموزعي الإنترنت، والمتاجر الأونلاين)، وتطبيق مجاني للزبائن يتابعون فيه حساباتهم ومواعيدهم.</p>
<h3>2. الحساب</h3><p>تُنشئ حسابك برقم هاتفك، وأنت مسؤول عن صحة بياناتك وعن المحافظة على سرية الدخول إلى حسابك وعن كل ما يتم من خلاله.</p>
<h3>3. الاشتراك والدفع</h3><ul><li>يحصل كل نشاط جديد على تجربة مجانية لمدة أسبوع.</li><li>بعد التجربة يتطلب الاستمرار اشتراكاً شهرياً أو سنوياً حسب <a href="pricing.html">الأسعار المعلنة</a>.</li><li>لا يوجد تجديد أو خصم تلقائي.</li><li>نُبلغ المشتركين قبل أي تغيير بالأسعار، ولا يؤثر التغيير على الفترة المدفوعة.</li></ul>
<h3>4. بياناتك</h3><p>البيانات التي تُدخلها لنشاطك (الزبائن، والمواعيد، والحسابات) ملكك. نحفظها ونعالجها فقط لتقديم الخدمة لك، وفق <a href="privacy.html">سياسة الخصوصية</a>.</p>
<h3>5. الاستخدام المقبول</h3><p>يُمنع استخدام الخدمة لأي غرض مخالف للقانون، أو لإرسال رسائل مزعجة، أو للإساءة إلى الآخرين، أو لمحاولة الوصول إلى بيانات لا تخصك. يحق لنا إيقاف أي حساب يخالف ذلك.</p>
<h3>6. التوفر</h3><p>نعمل على أن تكون الخدمة متاحة دائماً، لكن قد تحدث انقطاعات للصيانة أو لأسباب خارجة عن إرادتنا. التطبيق يحفظ عملك على الهاتف ويرسله عند عودة الاتصال.</p>
<h3>7. إنهاء الاستخدام</h3><p>يمكنك التوقف عن استخدام الخدمة في أي وقت. وعند طلبك نحذف بيانات نشاطك نهائياً.</p>
<h3>8. القانون المطبّق</h3><p>تخضع هذه الشروط للقوانين النافذة في جمهورية العراق.</p>
<h3>9. التواصل</h3><p>لأي سؤال عن هذه الشروط: <a href="https://wa.me/""" + WA + """">واتساب</a>.</p>"""

PRIVACY = """<p>خصوصيتك وخصوصية زبائنك مهمة لنا. توضح هذه السياسة ما نجمعه ولماذا.</p>
<h3>ما نجمعه</h3><ul><li><b>بيانات الحساب:</b> الاسم ورقم الهاتف.</li><li><b>بيانات النشاط:</b> ما تُدخله أنت في التطبيق، مثل أسماء الزبائن والمواعيد والحسابات والملاحظات.</li><li><b>بيانات تقنية:</b> نوع الجهاز ونسخة التطبيق وسجلات الأخطاء، لتحسين الخدمة.</li><li><b>الموقع:</b> فقط عند استعمال ميزة تحتاجه (مثل زر «أنا تائه» في الحملات)، وبإذنك.</li></ul>
<h3>كيف نستخدمها</h3><p>نستخدم البيانات فقط لتشغيل الخدمة: المزامنة بين أجهزتك وموظفيك، وإيصال الإشعارات والرسائل لزبائنك، والدعم الفني. <b>لا نبيع بياناتك ولا نشاركها مع أي جهة إعلانية.</b></p>
<h3>الدفع</h3><p>الدفع بالبطاقة يتم عبر بوابة دفع إلكتروني مرخّصة. <b>لا نطّلع على رقم بطاقتك ولا نحفظه</b>، ونستلم فقط تأكيد نجاح الدفع.</p>
<h3>الحفظ والحماية</h3><p>تُحفظ البيانات على خوادم سحابية آمنة ومشفّرة أثناء النقل، والوصول إليها محصور بصاحب النشاط ومن يمنحه الصلاحية.</p>
<h3>حقوقك</h3><p>يمكنك طلب نسخة من بياناتك أو حذفها نهائياً في أي وقت عبر <a href="https://wa.me/""" + WA + """">الواتساب</a>.</p>
<h3>الأطفال</h3><p>تطبيقات الأطفال التعليمية تُستخدم بإشراف ولي الأمر، ولا نجمع من الطفل بيانات شخصية غير ما يُدخله ولي الأمر.</p>"""

REFUND = """<p>نريدك أن تشترك وأنت مقتنع، لذلك نتبع سياسة بسيطة وواضحة.</p>
<h3>التجربة المجانية</h3><p>كل نشاط جديد يجرّب التطبيق أسبوعاً كاملاً مجاناً، بدون أي دفع وبدون إدخال بطاقة.</p>
<h3>الإلغاء</h3><ul><li>لا يوجد تجديد تلقائي ولا خصم تلقائي من بطاقتك.</li><li>يمكنك إيقاف الاشتراك في أي وقت بعدم تجديده، ويبقى فعّالاً حتى نهاية الفترة المدفوعة.</li></ul>
<h3>الإرجاع</h3><ul><li>يحق لك طلب استرجاع كامل المبلغ خلال <b>7 أيام</b> من تاريخ الدفع إذا لم تناسبك الخدمة.</li><li>بعد 7 أيام لا يُسترجع مبلغ الفترة الجارية.</li><li>إذا دفعت مرتين بالخطأ، أو حصل خلل تقني منعك من استخدام الخدمة، نعيد المبلغ كاملاً.</li></ul>
<h3>طريقة الطلب</h3><p>راسلنا على <a href="https://wa.me/""" + WA + """">الواتساب</a> برقم هاتف حسابك وتاريخ الدفع. نرد خلال يومي عمل، ويُعاد المبلغ بنفس طريقة الدفع خلال مدة أقصاها 14 يوم عمل حسب إجراءات بوابة الدفع والمصرف.</p>"""

JS = """// روابط تحميل ملفات الأندرويد. غيّر DL_BASE إذا رفعت الملفات بمكان ثاني.
const DL_BASE = 'https://github.com/okiqapp/okiqapp.github.io/releases/latest/download/';
document.querySelectorAll('[data-apk]').forEach(a => { a.href = DL_BASE + 'okiq-' + a.dataset.apk + '.apk'; });

// الأسعار تُقرأ من السيرفر (يتحكم بيها المطوّر من لوحة الإدارة)، والنص المكتوب بالصفحة احتياط فقط
const API = 'https://midad-api.mostafa1muhamd2jasm333333.workers.dev';
(async () => {
  if (!document.querySelector('[data-price],[data-m],[data-trial]')) return;
  try {
    const p = await (await fetch(API + '/pricing?cc=IQ')).json();
    const iqd = p.currency === 'IQD' ? p.rate : 0;
    const fmt = n => Math.round(n / 250) * 250;
    const ar = n => fmt(n).toLocaleString('en-US');
    const days = n => n === 1 ? 'يوماً واحداً' : n === 2 ? 'يومين' : n === 7 ? 'أسبوعاً' : n <= 10 ? n + ' أيام' : n + ' يوماً';
    const usd = k => p.usd[k] ?? p.usd.default;
    const year = m => Math.round(m * p.yearMonths * 100) / 100;
    document.querySelectorAll('[data-price]').forEach(el => {
      const m = usd(el.dataset.price);
      const paid = (p.trialDays > 0 ? 'جرّبه ' + days(p.trialDays) + ' مجاناً، ثم ' : '') + m + '$ شهرياً أو ' + year(m) + '$ سنوياً.';
      el.textContent = el.dataset.price === 'trips'
        ? 'مجاني لقوافل الحج طوال موسم الحج. للعمرة والزيارات: ' + paid
        : paid;
    });
    document.querySelectorAll('[data-m]').forEach(el => { const m = usd(el.dataset.m); el.innerHTML = m + '$' + (iqd ? '<span class="iqd">≈ ' + ar(m * iqd) + ' د.ع</span>' : ''); });
    document.querySelectorAll('[data-y]').forEach(el => { const y = year(usd(el.dataset.y)); el.innerHTML = y + '$' + (iqd ? '<span class="iqd">≈ ' + ar(y * iqd) + ' د.ع</span>' : ''); });
    document.querySelectorAll('[data-trial]').forEach(el => { el.textContent = days(p.trialDays); });
  } catch { /* يبقى النص الاحتياطي */ }
})();
"""

open(os.path.join(HERE, "site.css"), "w", encoding="utf-8").write(CSS)
open(os.path.join(HERE, "site.js"), "w", encoding="utf-8").write(JS)
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(index_page())
open(os.path.join(HERE, "pricing.html"), "w", encoding="utf-8").write(pricing_page())
doc_page("terms.html", "الشروط والأحكام", TERMS)
doc_page("privacy.html", "سياسة الخصوصية", PRIVACY)
doc_page("refund.html", "سياسة الإرجاع والإلغاء", REFUND)
for f in FACES:
    open(os.path.join(HERE, f["id"] + ".html"), "w", encoding="utf-8").write(face_page(f))
print("ok")
