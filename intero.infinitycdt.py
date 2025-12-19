import streamlit as st
import urllib.parse

# ================== 1) Page Config ==================
st.set_page_config(
    page_title="Infinity CDT | Finishing System",
    page_icon="🏗️",
    layout="wide"
)

# ================== 2) Constants & Branding ==================
BRAND_GOLD  = "#D4AF37"
BRAND_BLACK = "#0D0D0D"
BRAND_WHITE = "#FFFFFF"
TEXT_COLOR  = "#333333"

WHATSAPP_NUMBER = "201062796287"
EMAIL_ADDRESS   = "connect@infinitycdt.com"

BASE_AREA = 100  # الأرقام المرجعية للباقات في الإكسل تقريباً على 100 م² [file:6]

# ================== 3) Language Dictionary ==================
STRINGS = {
    "ar": {
        "app_title": "نظام تسعير التشطيب - Infinity CDT",
        "hero_title": "احسب متوسط تكلفة تشطيب شقتك في ثواني",
        "hero_sub": "اختر الباقة والمساحة وبعض الخيارات الإضافية لتحصل على متوسط سعر شامل مع تفاصيل واضحة.",
        "project_info": "بيانات المشروع",
        "area_label": "مساحة الوحدة (م²)",
        "floor_label": "مستوى الجودة التشطيبية",
        "pkg_label": "اختر الباقة الأساسية",
        "options_title": "الإضافات الاختيارية",
        "kitchen_opt": "مطبخ كامل",
        "furniture_opt": "فرش أساسي",
        "smart_opt": "نظام Smart Home",
        "landscape_opt": "لاندسكيب / بلكونة",
        "result_title": "نتيجة التسعير",
        "result_sub": "هذه الأرقام تقديرية لمساعدتك على فهم متوسط تكلفة الاستثمار في التشطيب.",
        "min_price": "الحد الأدنى التقريبي",
        "avg_price": "المتوسط المرجّح",
        "max_price": "الحد الأعلى التقريبي",
        "per_m2": "سعر المتر التقريبي",
        "included_heading": "ماذا يشمل هذا السعر؟",
        "compare_tab": "مقارنة الباقات",
        "details_tab": "تفاصيل البنود",
        "cta_title": "عايز عرض سعر أدق لمشروعك؟",
        "cta_button": "تواصل معنا على واتساب",
        "core_items_title": "✅ البنود الأساسية المشمولة",
        "optional_items_title": "✨ الإضافات الممكنة",
        "compare_intro": "ملخص مبسط لأهم الفروقات بين الباقات الأربع.",

        "pkg_modern": "Modern (الحداثة)",
        "pkg_smart": "Smart (الذكاء)",
        "pkg_elite": "Elite (النخبة)",
        "pkg_signature": "Signature (البصمة)",
        "pkg_economic": "اقتصادية",
        "pkg_mid": "متوسطة",
        "pkg_lux": "فاخرة",
        "pkg_hotel": "فندقية",

        "col_design": "التصاميم والإشراف",
        "col_plumbing": "السباكة",
        "col_electric": "الكهرباء",
        "col_floor": "أرضيات الاستقبال",
        "col_bed": "أرضيات غرف النوم",
        "col_paint": "الدهانات",
        "col_smart": "السمارت هوم",
        "col_warranty": "الضمان",

    },
    "en": {
        "app_title": "Finishing Pricing System - Infinity CDT",
        "hero_title": "Estimate Your Apartment Finishing Cost in Seconds",
        "hero_sub": "Choose package, area and options to get a realistic average price with clear details.",
        "project_info": "Project Information",
        "area_label": "Unit Area (m²)",
        "floor_label": "Finishing Quality Level",
        "pkg_label": "Choose Main Package",
        "options_title": "Optional Add-ons",
        "kitchen_opt": "Full Kitchen",
        "furniture_opt": "Basic Furniture",
        "smart_opt": "Smart Home System",
        "landscape_opt": "Landscape / Balcony",
        "result_title": "Pricing Result",
        "result_sub": "Values are indicative to help you understand the investment level.",
        "min_price": "Estimated Minimum",
        "avg_price": "Weighted Average",
        "max_price": "Estimated Maximum",
        "per_m2": "Approx. price per m²",
        "included_heading": "What is included in this price?",
        "compare_tab": "Packages Comparison",
        "details_tab": "Scope Details",
        "cta_title": "Want a more accurate quotation?",
        "cta_button": "Contact us on WhatsApp",
        "core_items_title": "✅ Included Core Items",
        "optional_items_title": "✨ Possible Upgrades",
        "compare_intro": "A simplified summary of the main differences between the four packages.",

        "pkg_modern": "Modern",
        "pkg_smart": "Smart",
        "pkg_elite": "Elite",
        "pkg_signature": "Signature",
        "pkg_economic": "Economic",
        "pkg_mid": "Mid-range",
        "pkg_lux": "Luxury",
        "pkg_hotel": "Hotel-grade",

        "col_design": "Design & Supervision",
        "col_plumbing": "Plumbing",
        "col_electric": "Electrical",
        "col_floor": "Reception Flooring",
        "col_bed": "Bedroom Flooring",
        "col_paint": "Paints",
        "col_smart": "Smart Home",
        "col_warranty": "Warranty",
    }
}

# ================== 4) Package Data (من الإكسل) ==================
PACKAGES = {
    # الإجماليات من Sheet "ملخص الأسعار" [file:6]
    "Modern": {
        "total": 503000,
        "tag_ar": "🟢 اقتصادية",
        "tag_en": "🟢 Economic",
    },
    "Smart": {
        "total": 716350,
        "tag_ar": "🔵 متوسطة",
        "tag_en": "🔵 Mid-range",
    },
    "Elite": {
        "total": 1048750,
        "tag_ar": "🟡 فاخرة",
        "tag_en": "🟡 Luxury",
    },
    "Signature": {
        "total": 1624000,
        "tag_ar": "🔴 فندقية",
        "tag_en": "🔴 Hotel-grade",
    },
}

# ================== 5) Global CSS ==================
st.markdown(f"""
<style>
    html, body, .stApp {{
        background-color: #F5F5F5;
        color: {TEXT_COLOR};
        font-family: "Segoe UI", "Cairo", sans-serif;
    }}
    .main-block {{
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 1rem;
    }}
    .price-number {{
        font-size: 1.4rem;
        font-weight: 700;
        color: {BRAND_GOLD};
    }}
    .pkg-tag {{
        font-size: 0.85rem;
        color: #666666;
    }}
    @media (max-width: 768px) {{
        .main-block {{
            padding: 1rem;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# ================== 6) Sidebar: Language & Branding ==================
with st.sidebar:
    lang_choice = st.radio("Language / اللغة", ["العربية", "English"])
    lang = "ar" if lang_choice == "العربية" else "en"
    t = STRINGS[lang]

    st.markdown(f"### {t['app_title']}")
    st.markdown("---")
    st.markdown("**Infinity CDT**")
    st.caption("Precision Finishing Estimator v2.1")

# ================== 7) Hero Section ==================
st.markdown(
    f"<h2 style='text-align:center;'>{t['hero_title']}</h2>",
    unsafe_allow_html=True
)
st.markdown(
    f"<p style='text-align:center; color:#666;'>{t['hero_sub']}</p>",
    unsafe_allow_html=True
)
st.markdown("<br>", unsafe_allow_html=True)

# ================== 8) Layout: Inputs (Left) / Results (Right) ==================
col_left, col_right = st.columns([1.1, 1])

with col_left:
    st.markdown(f"<div class='main-block'><h4>{t['project_info']}</h4>", unsafe_allow_html=True)

    area = st.number_input(
        t["area_label"],
        min_value=40,
        max_value=400,
        value=100,
        step=5
    )

    finishing_level = st.selectbox(
        t["floor_label"],
        ["Standard", "High", "Premium"],
        index=1
    )

    pkg_name = st.selectbox(
        t["pkg_label"],
        list(PACKAGES.keys())
    )

    st.markdown("---")
    st.markdown(f"#### {t['options_title']}")

    opt_kitchen   = st.checkbox(t["kitchen_opt"])
    opt_furniture = st.checkbox(t["furniture_opt"])
    opt_smart     = st.checkbox(t["smart_opt"])
    opt_land      = st.checkbox(t["landscape_opt"])

    st.markdown("</div>", unsafe_allow_html=True)

# ================== 9) Pricing Logic (مبسّط لكن واقعي) ==================
base_total = PACKAGES[pkg_name]["total"]
base_scaled = base_total * (area / BASE_AREA)  # Scaling حسب المساحة [file:6]

# إضافات تقديرية من منطقك السابق [file:4]
extras = 0
if opt_kitchen:
    extras += 72500      # KITCHEN_COST [file:4]
if opt_furniture:
    extras += 360500     # FURNITURE_COST [file:4]
if opt_smart:
    extras += 35000      # مستوى متوسط للسمارت
if opt_land:
    extras += 25000      # لاندسكيب بسيط

level_factor = {
    "Standard": 0.95,
    "High": 1.00,
    "Premium": 1.08,
}[finishing_level]

min_price = base_scaled * 0.9 * level_factor
avg_price = base_scaled * level_factor + extras * 0.6
max_price = base_scaled * 1.1 * level_factor + extras

price_per_m2 = avg_price / area

# ================== 10) Results with st.metric ==================
with col_right:
    st.markdown(f"<div class='main-block'><h4>{t['result_title']}</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#777;'>{t['result_sub']}</p>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            label=t["min_price"],
            value=f"{min_price:,.0f} EGP"
        )

    with c2:
        st.metric(
            label=t["avg_price"],
            value=f"{avg_price:,.0f} EGP",
            delta=f"{price_per_m2:,.0f} EGP / m²"
        )

    with c3:
        st.metric(
            label=t["max_price"],
            value=f"{max_price:,.0f} EGP"
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ================== 11) Tabs: Comparison & Details ==================
tab_compare, tab_details = st.tabs([t["compare_tab"], t["details_tab"]])

with tab_compare:
    st.markdown(f"#### {t['compare_intro']}")
    # ملخص مبسّط لأهم الفروق، مأخوذ من جدول المقارنة في الإكسل [file:6]
    if lang == "ar":
        st.markdown("""
| الميزة | Modern | Smart | Elite | Signature |
| --- | --- | --- | --- | --- |
| التصاميم والإشراف | تصميم وإشراف | تصميم + إشراف متقدم | 3D + مهندس مقيم | VR + إدارة كاملة |
| السباكة | خامات BR محلية | جاهز للسمارت | Grohe دفن كامل | نظام فندقي كامل |
| الكهرباء | سويدي أصلي معياري | تجهيز للسمارت | أحمال عالية | Schneider كامل |
| أرضيات الاستقبال | سيراميك فرز أول | سيراميك بقطع ليزر | بورسلين 60x60 | بورسلين إسباني فاخر |
| السمارت هوم | غير مشمول | إنارة ذكية | إنارة + تكييف | تحكم كامل (صوت+ستائر) |
| الدهانات | بلاستيك مط | نصف لامع | قطيفة/سواحيلي | ديكورية خاصة |
| الضمان | 5 سنوات | 7 سنوات | 10 سنوات | مدى الحياة |
""")
    else:
        st.markdown("""
| Feature | Modern | Smart | Elite | Signature |
| --- | --- | --- | --- | --- |
| Design & Supervision | Design + Basic Supervision | Detailed Drawings | 3D + Site Engineer | VR + Full Management |
| Plumbing | Local BR Materials | Smart-ready | Grohe Concealed | Full Hotel-grade System |
| Electrical | Original Swedish | Smart-ready | High Loads | Full Schneider System |
| Reception Flooring | First-grade Ceramic | Laser-cut Ceramic | 60x60 Porcelain | Spanish Porcelain |
| Smart Home | Not Included | Smart Lighting | Lighting + AC | Full Control (Voice + Curtains) |
| Paints | Matt | Semi-gloss | Special Effects | Decorative Paints |
| Warranty | 5 Years | 7 Years | 10 Years | Lifetime |
""")

with tab_details:
    st.markdown(f"### {t['included_heading']}")

    with st.expander(t["core_items_title"], expanded=True):
        if lang == "ar":
            st.markdown("- سباكة كاملة (حمامين + مطبخ) حسب الباقة.")
            st.markdown("- تأسيس كهرباء كامل + لوحة وقواطع وحمايات.")
            st.markdown("- محارة، جبس، وأسقف معلقة حسب التصميم.")
            st.markdown("- أرضيات (سيراميك / بورسلين / HDF / خشب هندسي).")
            st.markdown("- دهانات داخلية (Jotun / GLC) حسب المستوى.")
            st.markdown("- تأسيس مواسير تكييف فريون.")
            st.markdown("- أبواب داخلية + باب مصفح رئيسي.")
            st.markdown("- شبابيك ألوميتال حسب الباقة.")
        else:
            st.markdown("- Full plumbing (2 bathrooms + kitchen) according to package.")
            st.markdown("- Complete electrical works + panel + breakers.")
            st.markdown("- Plastering, gypsum and false ceilings as per design.")
            st.markdown("- Flooring (ceramic / porcelain / HDF / engineered wood).")
            st.markdown("- Interior paints (Jotun / GLC) based on level.")
            st.markdown("- Refrigerant piping for AC.")
            st.markdown("- Internal doors + main armored door.")
            st.markdown("- Aluminum windows according to package.")

    with st.expander(t["optional_items_title"], expanded=False):
        if lang == "ar":
            st.markdown("- مطابخ مخصصة (HPL / Polylic / Gloss Max).")
            st.markdown("- فرش غرف نوم، ريسبشن، وسفرة بمستويات مختلفة.")
            st.markdown("- أنظمة Smart Home (إنارة، تكييف، صوت، ستائر).")
            st.markmarkdown("- لاندسكيب، برجولات، نجيلة صناعي، إضاءة خارجية.")
            st.markdown("- شاتر وموتور، كبائن شاور زجاج، ورق حائط مستورد.")
        else:
            st.markdown("- Custom kitchens (HPL / Polylic / Gloss Max).")
            st.markdown("- Furniture for bedrooms, reception and dining room.")
            st.markdown("- Smart Home systems (lighting, AC, audio, curtains).")
            st.markdown("- Landscape, pergolas, artificial grass, outdoor lighting.")
            st.markdown("- Motorized shutters, glass shower cabins, imported wallpaper.")

# ================== 12) Call To Action (WhatsApp) ==================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"### {t['cta_title']}")

msg_lines = [
    f"Language: {lang_choice}",
    f"Area: {area} m²",
    f"Package: {pkg_name}",
    f"Finishing Level: {finishing_level}",
    f"Average Price: {avg_price:,.0f} EGP"
]
msg = "\n".join(msg_lines)
wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"

st.link_button(t["cta_button"], wa_link)
