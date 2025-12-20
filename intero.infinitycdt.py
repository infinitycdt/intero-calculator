import streamlit as st
import pandas as pd
import urllib.parse
import uuid
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ======================================================
# 1) PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Infinity CDT | Finishing System",
    page_icon="🏗️",
    layout="wide"
)

# ======================================================
# 2) META PIXEL
# ======================================================
META_PIXEL = """
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1893075388269127');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1893075388269127&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
"""
st.markdown(META_PIXEL, unsafe_allow_html=True)

# ======================================================
# 3) GLOBAL STYLE (تحسين الموبايل)
# ======================================================
st.markdown(
    """
    <style>
    .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        font-size: 16px;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1100px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ======================================================
# 4) BRANDING & CONSTANTS
# ======================================================
BRAND_GOLD = "#D4AF37"
BRAND_BLACK = "#0D0D0D"
BRAND_WHITE = "#FFFFFF"
TEXT_COLOR = "#333333"

WHATSAPP_NUMBER = "201062796287"
BASE_AREA = 100
VAT_RATE = 0.14  # الضريبة 14% بدل 15% [file:78]

CRM_SHEET_NAME = "Infinity_Leads"
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1s775JnxtYjOhK60eo1-WeGEse87DonSdguvQiU0tDDs/edit?usp=sharing"  # [file:78]

# ======================================================
# 5) LANGUAGE STRINGS
# ======================================================
STRINGS = {
    "ar": {
        "app_title": "نظام تسعير التشطيب - Infinity CDT",
        "hero_title": "احسب متوسط تكلفة تشطيب شقتك في ثواني",
        "hero_sub": "اختر الباقة والمساحة وبعض الخيارات الإضافية لتحصل على متوسط سعر شامل مع تفاصيل واضحة.",
        "project_info": "بيانات المشروع",
        "area_label": "مساحة الوحدة (م²)",
        "pkg_label": "اختر الباقة الأساسية",
        "options_title": "الإضافات الاختيارية",
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
        "cta_button": "إرسال كل التفاصيل على واتساب",
        "core_items_title": "✅ البنود الأساسية المشمولة",
        "optional_items_title": "✨ الإضافات الممكنة",
        "client_info": "بيانات العميل",
        "client_name": "اسم العميل (إجباري)",
        "client_mobile": "رقم الموبايل (إجباري)",
        "client_email": "البريد الإلكتروني (اختياري)",
        "inspection_area": "منطقة المعاينة (اختياري)",
        "whatsapp_error": "من فضلك أدخل اسم العميل ورقم الموبايل أولاً.",
        "summary_title": "ملخص السعر النهائي",
        "payment_plan": "نظام السداد المقترح",
        "lead_saved": "تم حفظ بياناتك في النظام، وسنتواصل معك قريباً.",
        "lead_error": "حدث خطأ أثناء حفظ البيانات في Google Sheet.",
    },
    "en": {
        "app_title": "Finishing Pricing System - Infinity CDT",
        "hero_title": "Estimate Your Apartment Finishing Cost in Seconds",
        "hero_sub": "Choose package, area and options to get a realistic average price with clear details.",
        "project_info": "Project Information",
        "area_label": "Unit Area (m²)",
        "pkg_label": "Choose Main Package",
        "options_title": "Optional Add-ons",
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
        "cta_button": "Send details via WhatsApp",
        "core_items_title": "✅ Included Core Items",
        "optional_items_title": "✨ Possible Upgrades",
        "client_info": "Client Information",
        "client_name": "Client Name (Required)",
        "client_mobile": "Mobile Number (Required)",
        "client_email": "Email (Optional)",
        "inspection_area": "Inspection Area (Optional)",
        "whatsapp_error": "Please enter client name and mobile first.",
        "summary_title": "Final Price Summary",
        "payment_plan": "Suggested Payment Plan",
        "lead_saved": "Your data has been saved, our team will contact you soon.",
        "lead_error": "Error while saving data to Google Sheet.",
    },
}

# ======================================================
# 6) PACKAGES (من ملف الأسعار 2026) [file:76]
# ======================================================
PACKAGES = {
    "Economy": {
        "label_ar": "Economy (اقتصادي)",
        "label_en": "Economy",
        "total": 350000,
        "sqm": 3500,
        "tag_ar": "🟢 اقتصادي",
        "tag_en": "🟢 Economic",
    },
    "i-Modern": {
        "label_ar": "i-Modern (الحداثة)",
        "label_en": "i-Modern",
        "total": 503000,
        "sqm": 5030,
        "tag_ar": "🔵 متوسط",
        "tag_en": "🔵 Mid-range",
    },
    "i-Smart": {
        "label_ar": "i-Smart (الذكاء)",
        "label_en": "i-Smart",
        "total": 716350,
        "sqm": 7164,
        "tag_ar": "🔵 متوسط",
        "tag_en": "🔵 Mid-range",
    },
    "i-Elite": {
        "label_ar": "i-Elite (النخبة)",
        "label_en": "i-Elite",
        "total": 1048750,
        "sqm": 10488,
        "tag_ar": "🟡 فاخر",
        "tag_en": "🟡 Luxury",
    },
    "i-Signature": {
        "label_ar": "i-Signature (البصمة)",
        "label_en": "i-Signature",
        "total": 1624000,
        "sqm": 16240,
        "tag_ar": "🔴 فندقي",
        "tag_en": "🔴 Hotel-grade",
    },
}

# ======================================================
# 7) DETAILED ITEMS (مقتطف – يمكنك استكماله من شيت تسعير البنود) [file:76]
# ======================================================
ITEMS = [
    {
        "section": "أولاً: التجهيزات والموقع (Preliminaries)",
        "code": 1,
        "name": "رفع مساحي و رسومات",
        "unit": "مقطوعية",
        "qty": 1,
        "Economy_UP": 5000.0, "Economy_Total": 5000.0, "Economy_Notes": "2D", "Economy_Status": "اختياري",
        "i-Modern_UP": 5000.0, "i-Modern_Total": 5000.0, "i-Modern_Notes": "2D", "i-Modern_Status": "أساسي",
        "i-Smart_UP": 30000.0, "i-Smart_Total": 30000.0, "i-Smart_Notes": "تصميم + إشراف", "i-Smart_Status": "أساسي",
        "i-Elite_UP": 45000.0, "i-Elite_Total": 45000.0, "i-Elite_Notes": "3D + مهندس مقيم", "i-Elite_Status": "أساسي",
        "i-Signature_UP": 75000.0, "i-Signature_Total": 75000.0, "i-Signature_Notes": "VR + إدارة كاملة", "i-Signature_Status": "أساسي",
    },
    {
        "section": "أولاً: التجهيزات والموقع (Preliminaries)",
        "code": 2,
        "name": "بند تأمين الموقع (Site Protection)",
        "unit": "مقطوعية",
        "qty": 1,
        "Economy_UP": 800.0, "Economy_Total": 800.0, "Economy_Notes": "نظافة بسيطة", "Economy_Status": "اختياري",
        "i-Modern_UP": 2000.0, "i-Modern_Total": 2000.0, "i-Modern_Notes": "نظافة فقط", "i-Modern_Status": "أساسي",
        "i-Smart_UP": 5000.0, "i-Smart_Total": 5000.0, "i-Smart_Notes": "تغليف مصعد", "i-Smart_Status": "أساسي",
        "i-Elite_UP": 8000.0, "i-Elite_Total": 8000.0, "i-Elite_Notes": "تغليف أرضيات", "i-Elite_Status": "أساسي",
        "i-Signature_UP": 15000.0, "i-Signature_Total": 15000.0, "i-Signature_Notes": "حماية شاملة", "i-Signature_Status": "أساسي",
    },
    # أكمل باقي البنود من شيت "تسعير البنود" بنفس الهيكل عند الحاجة [file:76]
]

# ======================================================
# 8) OPTIONAL BIG ITEMS (من جدول البنود الاختيارية) [file:76]
# ======================================================
OPTIONAL_BIG_ITEMS = [
    {
        "name": "شاتر وموتور (Motorized Shutter)",
        "min_price": 4500,
        "unit": "م2",
        "note": "Motor Somfy + تحكم ذكي",
        "included_in": "Elite - Signature",
    },
    {
        "name": "كبائن شاور زجاج (Shower Cabins)",
        "min_price": 3500,
        "unit": "م2",
        "note": "زجاج 10مم + ستانلس 304",
        "included_in": "Elite - Signature",
    },
    # يمكنك إضافة بقية البنود الاختيارية هنا
]

# ======================================================
# 9) GOOGLE SHEETS (CRM) [file:78]
# ======================================================
@st.cache_resource(show_spinner=False)
def get_gsheet_client():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "infinity-crm-key.json", scope
    )
    client = gspread.authorize(creds)
    return client

def append_lead_row(data: dict):
    try:
        client = get_gsheet_client()
        sheet = client.open_by_url(GOOGLE_SHEET_URL).worksheet(CRM_SHEET_NAME)
    except Exception:
        return False

    row = [
        data.get("lead_id"),
        data.get("timestamp"),
        data.get("lang"),
        data.get("client_name"),
        data.get("client_mobile"),
        data.get("client_email"),
        data.get("inspection_area"),
        data.get("area"),
        data.get("package"),
        data.get("base_total"),
        data.get("extras_total"),
        data.get("subtotal"),
        data.get("vat"),
        data.get("grand_total"),
        "; ".join([f"{k}:{v}" for k, v in data.get("extras_dict", {}).items()]),
    ]
    try:
        sheet.append_row(row, value_input_option="USER_ENTERED")
        return True
    except Exception:
        return False

# ======================================================
# 10) HELPERS
# ======================================================
def get_items_for_package(pkg_key: str) -> pd.DataFrame:
    rows = []
    for it in ITEMS:
        rows.append({
            "البند الرئيسي": it["section"],
            "رقم": it["code"],
            "البند": it["name"],
            "الوحدة": it["unit"],
            "الكمية": it["qty"],
            "سعر الوحدة": it[f"{pkg_key}_UP"],
            "الإجمالي": it[f"{pkg_key}_Total"],
            "الحالة": it[f"{pkg_key}_Status"],
            "ملاحظات": it[f"{pkg_key}_Notes"],
        })
    return pd.DataFrame(rows)

def build_whatsapp_message(
    lang, client_name, client_mobile, client_email, inspection_area,
    area, pkg_key, base_total, extra_items_details,
    subtotal, vat, grand_total, min_price, avg_price, max_price, price_per_m2
):
    lines = []
    lines.append("Infinity CDT - Finishing Inquiry")
    lines.append("-------------------------------")
    lines.append(f"Client: {client_name}")
    lines.append(f"Mobile: {client_mobile}")
    if client_email:
        lines.append(f"Email: {client_email}")
    lines.append(f"Inspection Area: {inspection_area}")
    lines.append("")
    lines.append(f"Unit Area: {area} m²")
    lines.append(f"Package: {pkg_key}")
    lines.append(f"Base Total: {base_total:,.0f} EGP")
    if extra_items_details:
        lines.append("")
        lines.append("Extra Items:")
        for k, v in extra_items_details.items():
            lines.append(f"- {k}: {v:,.0f} EGP")
    lines.append("")
    lines.append(f"Subtotal: {subtotal:,.0f} EGP")
    lines.append(f"VAT (14%): {vat:,.0f} EGP")
    lines.append(f"Grand Total: {grand_total:,.0f} EGP")
    lines.append("")
    lines.append(f"Estimated Min: {min_price:,.0f} EGP")
    lines.append(f"Weighted Avg: {avg_price:,.0f} EGP")
    lines.append(f"Estimated Max: {max_price:,.0f} EGP")
    lines.append(f"Approx. Price/m²: {price_per_m2:,.0f} EGP")
    return "\n".join(lines)

# ======================================================
# 11) SIDEBAR (LANG + BRAND + SOCIAL + CLIENT FORM)
# ======================================================
with st.sidebar:
    lang_choice = st.radio("Language / اللغة", ["العربية", "English"])
    lang = "ar" if lang_choice == "العربية" else "en"
    t = STRINGS[lang]

    st.markdown(f"### {t['app_title']}")
    st.markdown("---")
    st.markdown("**Infinity for Construction, Decorations, Low Current and IT Solutions**")
    st.caption("Integrated Finishing Pricing System 2026")

    st.markdown("#### 🌐 تواصل معنا / Contact")
    st.markdown("[Facebook](https://www.facebook.com/InfinityCDT)")
    st.markdown("[Instagram](https://www.instagram.com/InfinityCDT)")
    st.markdown("[TikTok](https://www.tiktok.com/@infinitycdt)")
    st.markdown("[Threads](https://www.threads.com/@infinitycdt)")
    st.markdown("[Website](https://www.intero.infinitycdt.com/)")
    st.markdown("[WhatsApp](https://wa.me/201062796287)")
    st.caption("1 Mostafa Al Nahass St, Abbas El Akkad, Nasr Center Building, Cairo, Egypt")

    with st.expander("🧾 " + t["client_info"], expanded=True):
        client_name = st.text_input(t["client_name"])
        client_mobile = st.text_input(t["client_mobile"])
        client_email = st.text_input(t["client_email"])

        areas = [
            "New Cairo", "6th of October", "Sheikh Zayed",
            "Nasr City", "Heliopolis", "Maadi", "Alexandria", "OTHER"
        ]
        inspection_area = st.selectbox(t["inspection_area"], areas, index=len(areas) - 1)

# ======================================================
# 12) MAIN HEADER
# ======================================================
st.title(t["hero_title"])
st.write(t["hero_sub"])

# ======================================================
# 13) PROJECT INPUTS (تصميم بسيط مناسب للموبايل)
# ======================================================
st.markdown("### " + t["project_info"])
c1 = st.container()
c2 = st.container()

with c1:
    area = st.number_input(t["area_label"], min_value=40, max_value=1000, value=100, step=10)

with c2:
    if lang == "ar":
        options = list(PACKAGES.keys())
        def fmt(k): return PACKAGES[k]["label_ar"] + " - " + PACKAGES[k]["tag_ar"]
    else:
        options = list(PACKAGES.keys())
        def fmt(k): return PACKAGES[k]["label_en"] + " - " + PACKAGES[k]["tag_en"]
    pkg_key = st.selectbox(t["pkg_label"], options=options, format_func=fmt)

# ======================================================
# 14) OPTIONAL ITEMS
# ======================================================
st.markdown("### " + t["options_title"])

extra_items_details = {}

with st.expander("الإضافات الداخلية (مطبخ / فرش / سمارت / لاندسكيب)", expanded=False):
    add_kitchen = st.checkbox("مطبخ كامل")
    if add_kitchen:
        kitchen_cost = st.number_input("تكلفة المطبخ التقديرية (جنيه)", min_value=0, value=25000, step=5000)
        extra_items_details["مطبخ كامل"] = kitchen_cost

    add_furniture = st.checkbox("فرش أساسي")
    if add_furniture:
        furniture_cost = st.number_input("تكلفة الفرش التقديرية (جنيه)", min_value=0, value=60000, step=5000)
        extra_items_details["فرش أساسي"] = furniture_cost

    add_smart = st.checkbox("نظام Smart Home")
    if add_smart:
        smart_cost = st.number_input("تكلفة نظام Smart Home (جنيه)", min_value=0, value=50000, step=5000)
        extra_items_details["Smart Home"] = smart_cost

    add_landscape = st.checkbox("لاندسكيب / بلكونة")
    if add_landscape:
        landscape_cost = st.number_input("تكلفة اللاندسكيب / البلكونة (جنيه)", min_value=0, value=30000, step=5000)
        extra_items_details["لاندسكيب / بلكونة"] = landscape_cost

with st.expander("البنود الاختيارية المتقدمة (من جدول الإضافات)", expanded=False):
    for opt in OPTIONAL_BIG_ITEMS:
        col1, col2 = st.columns([3, 1])
        with col1:
            checked = st.checkbox(f"{opt['name']} ({opt['note']})")
        with col2:
            if checked:
                val = st.number_input(
                    f"سعر {opt['name']}",
                    min_value=0,
                    value=int(opt["min_price"]),
                    step=1000
                )
                extra_items_details[opt["name"]] = val

# ======================================================
# 15) CALCULATIONS
# ======================================================
base_total = PACKAGES[pkg_key]["total"] * (area / BASE_AREA)
extra_total = sum(extra_items_details.values())
subtotal = base_total + extra_total
vat = subtotal * VAT_RATE
grand_total = subtotal + vat

avg_price = subtotal
min_price = avg_price * 0.9
max_price = avg_price * 1.1
price_per_m2 = avg_price / area if area else 0

# ======================================================
# 16) RESULT SECTION
# ======================================================
st.markdown("### " + t["result_title"])
st.caption(t["result_sub"])

mc1, mc2, mc3 = st.columns(3)
with mc1:
    st.metric(label=t["min_price"], value=f"{min_price:,.0f} EGP")
with mc2:
    st.metric(label=t["avg_price"], value=f"{avg_price:,.0f} EGP", delta=f"{price_per_m2:,.0f} EGP / m²")
with mc3:
    st.metric(label=t["max_price"], value=f"{max_price:,.0f} EGP")

st.markdown("### " + t["summary_title"])
st.write(f"- الإجمالي الأساسي: {base_total:,.0f} EGP")
st.write(f"- الإضافات: {extra_total:,.0f} EGP")
st.write(f"- الإجمالي قبل الضريبة: {subtotal:,.0f} EGP")
st.write(f"- الضريبة (14%): {vat:,.0f} EGP")
st.write(f"- الإجمالي النهائي (شامل الضريبة): {grand_total:,.0f} EGP")

st.markdown("#### " + t["payment_plan"])
st.write("- 35% من التكلفة عند التعاقد")
st.write("- 30% عند الانتهاء من مرحلة التأسيس (كهرباء – سباكة – تكييف)")
st.write("- 30% عند الانتهاء من السيراميك والجبسمبورد والتسليم النهائي")

# ======================================================
# 17) TABS (DETAILS + COMPARISON)
# ======================================================
tab1, tab2 = st.tabs([STRINGS[lang]["details_tab"], STRINGS[lang]["compare_tab"]])

with tab1:
    st.markdown("#### " + STRINGS[lang]["core_items_title"])
    if ITEMS:
        df_items = get_items_for_package(pkg_key)
        st.dataframe(df_items, use_container_width=True)
    else:
        st.info("سيتم إضافة تفاصيل البنود الكاملة لاحقاً.")

with tab2:
    st.markdown("#### ملخص الباقات الخمس")
    comp_rows = []
    for k, v in PACKAGES.items():
        comp_rows.append({
            "الباقة": v["label_ar"] if lang == "ar" else v["label_en"],
            "الإجمالي (100 م²)": v["total"],
            "سعر المتر": v["sqm"],
            "التصنيف": v["tag_ar"] if lang == "ar" else v["tag_en"],
        })
    df_comp = pd.DataFrame(comp_rows)
    st.table(df_comp)

# ======================================================
# 18) WHATSAPP + CRM SAVE
# ======================================================
st.markdown("### " + t["cta_title"])

if st.button(t["cta_button"]):
    if not client_name or not client_mobile:
        st.error(t["whatsapp_error"])
    else:
        lead_id = str(uuid.uuid4())
        ts = datetime.datetime.now().isoformat()

        lead_data = {
            "lead_id": lead_id,
            "timestamp": ts,
            "lang": lang,
            "client_name": client_name,
            "client_mobile": client_mobile,
            "client_email": client_email,
            "inspection_area": inspection_area,
            "area": area,
            "package": pkg_key,
            "base_total": base_total,
            "extras_total": extra_total,
            "subtotal": subtotal,
            "vat": vat,
            "grand_total": grand_total,
            "extras_dict": extra_items_details,
        }

        saved = append_lead_row(lead_data)
        if saved:
            st.success(t["lead_saved"])
        else:
            st.warning(t["lead_error"])

        msg = build_whatsapp_message(
            lang, client_name, client_mobile, client_email, inspection_area,
            area, pkg_key, base_total, extra_items_details,
            subtotal, vat, grand_total,
            min_price, avg_price, max_price, price_per_m2
        )
        encoded_msg = urllib.parse.quote(msg)
        wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_msg}"
        st.markdown(f"[اضغط هنا لفتح الواتساب وإرسال التفاصيل]({wa_url})")
