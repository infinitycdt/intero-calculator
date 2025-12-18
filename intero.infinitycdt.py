import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Infinity CDT | Intero System",
    page_icon="🏠",
    layout="wide"
)

# --- Constants & Contact Data ---
BRAND_GOLD = "#D4AF37"
BRAND_BLACK = "#0d0d0d"
WHATSAPP_NUMBER = "201062796287"  # تم تحديث الرقم بناءً على الكود الأصلي
EMAIL_ADDRESS = "connect@infinitycdt.com"

# --- New Pricing & Logic Constants (From Text File) ---
KITCHEN_COST = 14500 * 5  # 72,500 EGP
FURNITURE_COST = 360500   # 360,500 EGP
EXTRA_BATH_COST = 45000   # For each bath > 2

# --- UI Customization (Figma / Luxury Style) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    * {{ font-family: 'Cairo', 'Montserrat', sans-serif; }}

    .stApp {{
        background-color: {BRAND_BLACK};
        color: #ffffff;
    }}

    /* Hero Section */
    .hero-section {{
        height: 45vh;
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url('https://images.unsplash.com/photo-1613545325278-f24b0cae1224?auto=format&fit=crop&q=80&w=2070');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 0 0 40px 40px;
        margin-bottom: 40px;
        text-align: center;
    }}

    /* Glassmorphism Effect */
    .glass-card {{
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        padding: 40px;
        margin: -80px auto 40px auto;
        max-width: 900px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.6);
    }}

    .specs-box {{
        background: rgba(212, 175, 55, 0.05);
        border-right: 3px solid {BRAND_GOLD}; /* Changed to right for RTL/Arabic feel compatibility */
        padding: 20px;
        border-radius: 12px;
        margin: 25px 0;
        text-align: right;
    }}

    /* Premium Buttons */
    .stButton>button {{
        background: {BRAND_GOLD} !important;
        color: #000 !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 18px 50px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        letter-spacing: 1.5px;
        transition: 0.4s all ease;
        width: 100%;
        margin-top: 20px;
    }}
    .stButton>button:hover {{
        background: #ffffff !important;
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(212, 175, 55, 0.4);
    }}

    /* Custom Inputs */
    input, select, .stSelectbox div, .stNumberInput div {{
        background-color: #1a1a1a !important;
        color: white !important;
        border: 1px solid #333 !important;
        border-radius: 12px !important;
    }}
    
    /* Checkbox Styling */
    .stCheckbox label {{
        font-size: 1.1rem;
        color: {BRAND_GOLD};
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Corporate Links ---
with st.sidebar:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown(f"<h2 style='color:{BRAND_GOLD}; text-align:center;'>INFINITY CDT</h2>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🌐 FOLLOW US")
    st.markdown(f"""
        <a href="https://www.facebook.com/InfinityCDT" style="color:#888; text-decoration:none; display:block; margin:10px 0;">Facebook</a>
        <a href="https://www.instagram.com/InfinityCDT" style="color:#888; text-decoration:none; display:block; margin:10px 0;">Instagram</a>
        <a href="https://www.tiktok.com/@infinitycdt" style="color:#888; text-decoration:none; display:block; margin:10px 0;">TikTok</a>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ✉️ INQUIRIES")
    st.write(f"Email: {EMAIL_ADDRESS}")
    st.write(f"Support: +{WHATSAPP_NUMBER}")
    
    st.markdown("---")
    st.caption("Engineering Excellence © 2026")

# --- Hero Banner ---
st.markdown(f"""
    <div class="hero-section">
        <h5 style='color:{BRAND_GOLD}; letter-spacing:8px; font-weight:300;'>INFINITY CONSTRUCTION</h5>
        <h1 style='font-size: 4.8rem; font-weight:700; margin:5px 0;'>INTERO</h1>
        <p style='font-size: 1.3rem; font-weight:300; opacity:0.6;'>Precision Finishing Estimator System v2.0</p>
    </div>
    """, unsafe_allow_html=True)

# --- Data Dictionary (Updated Prices from New Text Document) ---
packages = {
    'i-Modern': {
        'price': 8200,
        'target': 'First Home / Investment',
        'specs': '✅ Elsewedy Cables | ✅ Sanchi Switches | ✅ GLC/Sipes Paints | ✅ Laser Cut Ceramics'
    },
    'i-Smart': {
        'price': 10500,
        'target': 'Tech Lovers / Families',
        'specs': '✅ Schneider Avatar Switches | ✅ Smart Home Prep | ✅ Indian/UAE Porcelain (60x120) | ✅ Jotun Fenomastic'
    },
    'i-Elite': {
        'price': 16500,
        'target': 'Villas / Luxury Apartments',
        'specs': '✅ Legrand Switches | ✅ Grohe Built-in Tanks | ✅ Spanish Porcelain / Marble | ✅ Sound System Prep'
    },
    'i-Signature': {
        'price': 28000,
        'target': 'Penthouses / VIP Palaces',
        'specs': '✅ Full Automation (KNX/Control4) | ✅ Book-match Marble | ✅ Engineered Wood | ✅ Custom Bespoke Designs'
    }
}

# --- Main Calculator Form ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Client Details
st.markdown(f"<h4 style='color:{BRAND_GOLD}; margin-bottom: 20px;'>1. بيانات العميل (Client Details)</h4>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("الاسم (Name)", placeholder="Full Name")
with col2:
    phone = st.text_input("رقم الهاتف (WhatsApp)", placeholder="01xxxxxxxxx")

st.markdown("---")

# Unit Details
st.markdown(f"<h4 style='color:{BRAND_GOLD}; margin-bottom: 20px;'>2. تفاصيل الوحدة (Unit Specs)</h4>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    area = st.number_input("المساحة (SQM)", min_value=50, value=120, step=10)
with c2:
    rooms = st.number_input("عدد الغرف (Rooms)", min_value=1, value=3, step=1)
with c3:
    baths = st.number_input("عدد الحمامات (Baths)", min_value=1, value=2, step=1)

st.markdown("---")

# Package Selection
st.markdown(f"<h4 style='color:{BRAND_GOLD}; margin-bottom: 20px;'>3. باقة التشطيب (Finishing Package)</h4>", unsafe_allow_html=True)
selected_p = st.selectbox("اختر الباقة المناسبة", list(packages.keys()), index=1) # Default to i-Smart

st.markdown(f"""
    <div class="specs-box">
        <strong style="color:{BRAND_GOLD}; text-transform:uppercase; font-size:1.1rem;">{selected_p} Package Includes</strong><br>
        <span style="font-size:0.9rem; opacity:0.9;">{packages[selected_p]['specs']}</span><br>
        <small style="opacity:0.6;">Target: {packages[selected_p]['target']}</small>
        <br><br>
        <strong style="color:#fff;">سعر المتر: {packages[selected_p]['price']:,} ج.م</strong>
    </div>
""", unsafe_allow_html=True)

# Add-ons Section (From Logic)
st.markdown(f"<h4 style='color:{BRAND_GOLD}; margin-bottom: 20px;'>4. إضافات حسب الطلب (Add-ons)</h4>", unsafe_allow_html=True)
ac1, ac2 = st.columns(2)
with ac1:
    add_kitchen = st.checkbox(f"مطبخ بولي لاك (Polylic) - {KITCHEN_COST:,} EGP")
    st.caption("تصميم وتنفيذ جود وود + مفصلات Soft Close (متوسط 5 متر طولي)")
with ac2:
    add_furniture = st.checkbox(f"باقة الفرش الكاملة - {FURNITURE_COST:,} EGP")
    st.caption("أخشاب (ماستر + أطفال + ريسبشن + سفرة)")

calculate_btn = st.button("احسب التكلفة التقديرية (GENERATE ESTIMATE) 🚀")
st.markdown('</div>', unsafe_allow_html=True)

# --- Results Rendering ---
if calculate_btn:
    if not name or not phone:
        st.error("⚠️ يرجى إدخال الاسم ورقم الهاتف لإظهار التقرير.")
    else:
        st.balloons()
        
        # --- Logic Implementation ---
        # 1. Base Cost
        base_cost = area * packages[selected_p]['price']
        
        # 2. Add-ons
        kitchen_price = KITCHEN_COST if add_kitchen else 0
        furniture_price = FURNITURE_COST if add_furniture else 0
        
        # 3. Extra Bathrooms Logic (If baths > 2, add 45,000 per extra bath)
        extra_baths_count = max(0, baths - 2)
        extra_baths_price = extra_baths_count * EXTRA_BATH_COST
        
        # 4. Total
        total_investment = base_cost + kitchen_price + furniture_price + extra_baths_price
        
        # Display
        st.markdown(f"""
            <div style='text-align:center; padding: 40px 0;'>
                <h3 style='color:{BRAND_GOLD}; font-weight:300; letter-spacing:2px;'>إجمالي الاستثمار التقديري</h3>
                <h1 style='font-size: 5rem; margin:0;'>{total_investment:,} <small style='font-size:1.2rem; opacity:0.4;'>EGP</small></h1>
                <p style='opacity:0.6; font-size:1.1rem;'>
                    Based on {area}m² | {selected_p} | {rooms} Rooms | {baths} Baths
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Logic Breakdown (Optional - visible to user)
        with st.expander("تفاصيل الحساب (Calculation Details)"):
            st.write(f"🔹 **Finishing Base:** {base_cost:,} EGP")
            if add_kitchen: st.write(f"🔹 **Kitchen:** {kitchen_price:,} EGP")
            if add_furniture: st.write(f"🔹 **Furniture:** {furniture_price:,} EGP")
            if extra_baths_count > 0: st.write(f"🔹 **Extra Baths ({extra_baths_count}):** {extra_baths_price:,} EGP")
        
        # Professional WhatsApp Message Construction
        kitchen_txt = "نعم" if add_kitchen else "لا"
        furniture_txt = "نعم" if add_furniture else "لا"
        
        wa_msg = (
            f"مرحباً Infinity CDT، أنا {name}.\n"
            f"استفسار بخصوص باقة {selected_p} لعام 2026:\n"
            f"- المساحة: {area}م\n"
            f"- الغرف: {rooms} | الحمامات: {baths}\n"
            f"- مطبخ: {kitchen_txt}\n"
            f"- فرش: {furniture_txt}\n"
            f"- السعر التقديري: {total_investment:,} ج.م\n"
            f"أرجو تحديد موعد للمعاينة."
        )
        
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg.replace(' ', '%20').replace('\n', '%0A')}"
        
        st.markdown(f"""
            <div style='text-align:center; margin-bottom: 60px;'>
                <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
                    <button style="background:#25D366; color:white; border:none; padding:22px 80px; border-radius:50px; font-weight:bold; cursor:pointer; font-size:1.3rem; box-shadow: 0 10px 30px rgba(37, 211, 102, 0.2);">
                        حجز معاينة فنية مجانية 📅
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

st.markdown(f"<p style='text-align:center; opacity:0.2; padding-bottom:40px;'>INFINITY CDT | Intero Pro v2.0 (2026 Logic)</p>", unsafe_allow_html=True)
