import streamlit as st

# --- إعدادات الهوية البصرية لـ Infinity CDT ---
BRAND_GOLD = "#D4AF37"
BRAND_BLACK = "#1A1A1A"
WHATSAPP = "201557990224"

st.set_page_config(
    page_title="Infinity CDT | Intero Calculator",
    page_icon="🏠",
    layout="centered"
)

# --- CSS مخصص للفخامة (Luxury Black & Gold) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }}
    .stApp {{ background-color: #ffffff; background-image: url("https://www.transparenttextures.com/patterns/architect.png"); }}
    .main-card {{
        background: white; padding: 2rem; border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1); border-top: 5px solid {BRAND_GOLD};
    }}
    .stButton>button {{
        background: {BRAND_BLACK}; color: {BRAND_GOLD} !important;
        border: 1px solid {BRAND_GOLD}; border-radius: 10px; font-weight: bold; height: 3.5em; width: 100%;
    }}
    .package-box {{
        background: #fdfaf0; border: 1px solid {BRAND_GOLD};
        padding: 15px; border-radius: 10px; margin-bottom: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- بيانات الباقات الرسمية لـ Infinity CDT ---
packages = {
    "i-Modern": {
        "price": (5000, 5600),
        "desc": "الحداثة بأفضل قيمة",
        "specs": "• أسلاك سويدي معتمدة\n• مفاتيح Sanchi/Kaptika\n• دهانات GLC/Sipes\n• سيراميك ليزر فرز أول"
    },
    "i-Smart": {
        "price": (5900, 6800),
        "desc": "الرفاهية التكنولوجية",
        "specs": "• لوحة Schneider + مفاتيح Avatar\n• تأسيس Smart Home وكاميرات\n• بورسلين هندي/إماراتي\n• دهانات Jotun Fenomastic"
    },
    "i-Elite": {
        "price": (7100, 9000),
        "desc": "فخامة النخبة VIP",
        "specs": "• لوحة ABB/Hager + مفاتيح Legrand\n• خزان دفن Grohe + كبائن شاور\n• رخام تريستا أو بورسلين إسباني\n• أنظمة صوتية وتكييف مركزي"
    },
    "i-Signature": {
        "price": (12000, 15000),
        "desc": "تصميم استثنائي خاص",
        "specs": "• Full Automation (Control4/KNX)\n• رخام مستورد Book-match\n• خشب طبيعي Engineered Wood\n• ديكورات وتجاليد حوائط خاصة"
    }
}

# --- واجهة المستخدم ---
st.markdown(f"<div style='text-align:center;'><h1 style='color:{BRAND_BLACK};'>Intero | مقايسة انفينيتي الذكية 📐</h1></div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("اسم العميل")
    with col2:
        phone = st.text_input("رقم الموبايل")

    area = st.number_input("مساحة الوحدة (م²)", min_value=50, max_value=2000, value=120, step=5)
    
    selected_p = st.selectbox("اختر باقة التشطيب", list(packages.keys()))
    
    # عرض المواصفات الفنية للباقة
    st.markdown(f"""
        <div class="package-box">
            <strong style="color:{BRAND_GOLD};">💎 مواصفات باقة {selected_p}:</strong><br>
            <small>{packages[selected_p]['specs'].replace('\n', '<br>')}</small>
        </div>
    """, unsafe_allow_html=True)
    
    btn = st.button("إصدار عرض السعر الفوري 🚀")
    st.markdown('</div>', unsafe_allow_html=True)

if btn:
    if not name or not phone:
        st.error("يرجى إدخال البيانات كاملة.")
    else:
        st.balloons()
        p_data = packages[selected_p]
        total_min = area * p_data['price'][0]
        total_max = area * p_data['price'][1]
        
        st.markdown(f"### التقرير الهندسي المبدئي لـ: {name}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("التكلفة التقديرية (تبدأ من)", f"{total_min:,} ج.م")
        with c2:
            st.metric("متوسط سعر المتر", f"{p_data['price'][0]:,} ج.م")

        # رابط واتساب
        msg = f"مرحباً Infinity CDT، أنا {name}، قمت بعمل مقايسة لباقة {selected_p} لمساحة {area}م على رابط intero. أريد حجز معاينة."
        st.markdown(f"""
            <a href="https://wa.me/{WHATSAPP}?text={msg}" target="_blank">
                <button style="width:100%; background-color:#25D366; color:white; padding:15px; border:none; border-radius:10px; font-weight:bold; cursor:pointer; font-size:1.1em;">
                    ارسل المقايسة للشركة واحجز معاينة الآن 💬
                </button>
            </a>
        """, unsafe_allow_html=True)