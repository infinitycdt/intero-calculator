import streamlit as st
import urllib.parse

# --- Page Configuration ---
st.set_page_config(
    page_title="Infinity CDT | Intero System",
    page_icon="🏗️",
    layout="wide"
)

# --- Constants & Contact Data ---
BRAND_GOLD = "#D4AF37"
BRAND_BLACK = "#0d0d0d"  # Used for contrast elements
BRAND_WHITE = "#ffffff"
TEXT_COLOR = "#333333"
WHATSAPP_NUMBER = "201062796287"
EMAIL_ADDRESS = "connect@infinitycdt.com"

# --- Logic Constants ---
KITCHEN_COST = 72500   # 14500 * 5
FURNITURE_COST = 360500
EXTRA_BATH_COST = 45000

# --- UI Customization (Light Professional Theme) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    * {{ font-family: 'Cairo', 'Montserrat', sans-serif; }}

    /* Main Background - White */
    .stApp {{
        background-color: {BRAND_WHITE};
        color: {TEXT_COLOR};
    }}

    /* Hero Section */
    .hero-section {{
        height: 40vh;
        background: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.7)), 
                    url('https://images.unsplash.com/photo-1600607686527-6fb886090705?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-bottom: 5px solid {BRAND_GOLD};
        margin-bottom: 40px;
        text-align: center;
        color: #000;
    }}

    /* Cards Styling (Light Theme) */
    .glass-card {{
        background: #F8F9FA;
        border: 1px solid #E9ECEF;
        border-radius: 20px;
        padding: 40px;
        margin: -60px auto 40px auto;
        max-width: 1000px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.08);
        position: relative;
    }}

    .specs-box {{
        background: #FFFBF0; /* Light Gold Tint */
        border-right: 4px solid {BRAND_GOLD};
        padding: 20px;
        border-radius: 8px;
        margin: 25px 0;
        text-align: right;
        color: #444;
    }}

    /* Inputs Styling */
    .stTextInput input, .stNumberInput input, .stSelectbox div, .stTextArea textarea {{
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #DDDDDD !important;
        border-radius: 8px !important;
    }}
    
    /* Buttons */
    .stButton>button {{
        background: {BRAND_GOLD} !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 15px 40px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
        transition: 0.3s;
        width: 100%;
    }}
    .stButton>button:hover {{
        background: #b5952f !important;
        transform: translateY(-2px);
    }}

    /* Headings */
    h1, h2, h3 {{ color: #000; }}
    h4 {{ color: {BRAND_GOLD}; }}

    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    try:
        # يرجى التأكد من وجود ملف logo.png في نفس المجلد
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown(f"<h1 style='color:{BRAND_GOLD}; text-align:center;'>INFINITY CDT</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🌐 Quick Links")
    st.markdown(f"""
        <div style='display:flex; flex-direction:column; gap:10px;'>
            <a href="https://www.facebook.com/InfinityCDT" style="color:#555; text-decoration:none;">Facebook Page</a>
            <a href="https://www.instagram.com/InfinityCDT" style="color:#555; text-decoration:none;">Instagram Profile</a>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("Engineering Excellence © 2026")

# --- Hero Banner ---
st.markdown(f"""
    <div class="hero-section">
        <h5 style='color:{BRAND_GOLD}; letter-spacing:5px; font-weight:600;'>INFINITY CONSTRUCTION</h5>
        <h1 style='font-size: 4rem; font-weight:800; margin:0;'>INTERO</h1>
        <p style='font-size: 1.2rem; font-weight:400; color:#555;'>Precision Finishing Estimator System v2.1</p>
    </div>
    """, unsafe_allow_html=True)

# --- Data Dictionary ---
packages = {
    'i-Modern': {'price': 8200, 'target': 'First Home', 'specs': 'Elsewedy | Sanchi | GLC/Sipes | Laser Cut Ceramics'},
    'i-Smart': {'price': 10500, 'target': 'Tech Families', 'specs': 'Schneider Avatar | Smart Prep | Porcelain 60x120 | Jotun'},
    'i-Elite': {'price': 16500, 'target': 'Luxury Apts', 'specs': 'Legrand | Grohe Built-in | Spanish Porcelain | Sound System'},
    'i-Signature': {'price': 28000, 'target': 'VIP Palaces', 'specs': 'KNX Automation | Book-match Marble | Engineered Wood'}
}

# --- Floor Options (Professional Naming) ---
floor_options = [
    "Ground Floor + Garden (أرضي بحديقة)",
    "Raised Ground Floor (أرضي مرتفع)",
    "First Floor (دور أول)",
    "Typical Floor (دور متكرر)",
    "Last Floor (دور أخير)",
    "Roof / Penthouse (رووف)"
]

# --- Main Form ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# 1. Client Details
st.markdown(f"<h4>1. بيانات العميل (Client Details)</h4>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("الاسم (Full Name)")
with col2:
    phone = st.text_input("رقم الهاتف (Mobile / WhatsApp)")

st.markdown("---")

# 2. Unit Specs (Updated with Floor)
st.markdown(f"<h4>2. مواصفات الوحدة (Unit Specs)</h4>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    area = st.number_input("المساحة (Area SQM)", min_value=50, value=120, step=5)
    rooms = st.number_input("عدد الغرف (Rooms)", min_value=1, value=3)
with c2:
    floor_level = st.selectbox("الدور السكني (Floor Level)", floor_options, index=3)
    baths = st.number_input("عدد الحمامات (Baths)", min_value=1, value=2)

st.markdown("---")

# 3. Package
st.markdown(f"<h4>3. باقة التشطيب (Package)</h4>", unsafe_allow_html=True)
selected_p = st.selectbox("Choose Package", list(packages.keys()), index=1)

st.markdown(f"""
    <div class="specs-box">
        <strong style="color:{BRAND_GOLD}; font-size:1.2rem;">{selected_p}</strong>
        <p style="margin:5px 0;">{packages[selected_p]['specs']}</p>
        <hr style="border-top:1px dashed #ccc;">
        <strong>Price/SQM: {packages[selected_p]['price']:,} EGP</strong>
    </div>
""", unsafe_allow_html=True)

# 4. Add-ons
st.markdown(f"<h4>4. الإضافات (Optional Add-ons)</h4>", unsafe_allow_html=True)
ac1, ac2 = st.columns(2)
with ac1:
    add_kitchen = st.checkbox(f"Smart Kitchen ({KITCHEN_COST:,} EGP)")
with ac2:
    add_furniture = st.checkbox(f"Full Furniture ({FURNITURE_COST:,} EGP)")

# Calculate Button
st.markdown("<br>", unsafe_allow_html=True)
calculate_btn = st.button("عرض عرض السعر (Generate Estimate)")
st.markdown('</div>', unsafe_allow_html=True)

# --- Results Section ---
if calculate_btn:
    if not name or not phone:
        st.warning("⚠️ يرجى استكمال البيانات الأساسية (الاسم ورقم الهاتف)")
    else:
        # Logic
        base_cost = area * packages[selected_p]['price']
        kitchen_price = KITCHEN_COST if add_kitchen else 0
        furniture_price = FURNITURE_COST if add_furniture else 0
        extra_baths = max(0, baths - 2) * EXTRA_BATH_COST
        total = base_cost + kitchen_price + furniture_price + extra_baths

        st.markdown("---")
        st.markdown(f"""
            <div style='text-align:center; padding: 20px;'>
                <h2 style='color:#555;'>Total Estimated Investment</h2>
                <h1 style='color:{BRAND_GOLD}; font-size:4rem; margin:0;'>{total:,} <span style='font-size:1.5rem; color:#000;'>EGP</span></h1>
                <p>Unit: {area}m² | {floor_level}</p>
            </div>
        """, unsafe_allow_html=True)

        # WhatsApp Link Generation
        wa_msg = (
            f"Infinity CDT Inquiry:\n"
            f"Client: {name} ({phone})\n"
            f"Unit: {area}m, {floor_level}\n"
            f"Pkg: {selected_p}\n"
            f"Total Est: {total:,} EGP"
        )
        encoded_msg = urllib.parse.quote(wa_msg)
        wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_msg}"

        st.markdown(f"""
            <div style='text-align:center; margin-bottom:40px;'>
                <a href="{wa_link}" target="_blank">
                    <button style="background:#25D366; color:#fff; border:none; padding:15px 50px; border-radius:30px; font-size:1.2rem; cursor:pointer;">
                        📱 تواصل عبر واتساب للمعاينة
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

# --- Feedback & Complain Section ---
st.markdown("---")
st.markdown(f"<h3 style='text-align:center; color:#555;'>We Value Your Voice</h3>", unsafe_allow_html=True)

c_feed, c_comp = st.columns(2)

# Feedback Column
with c_feed:
    with st.expander("📝 Give Feedback (رأيك يهمنا)"):
        with st.form("feedback_form"):
            st.write("Rate your experience (تقييمك):")
            # Using emojis to simulate the logo/star rating visually
            rating_feed = st.radio("Infinity Rating:", ["💎", "💎💎", "💎💎💎", "💎💎💎💎", "💎💎💎💎💎"], index=4, horizontal=True)
            comment_feed = st.text_area("Your Comment (تعليقك):")
            submit_feed = st.form_submit_button("Submit Feedback")
            
            if submit_feed:
                subject = f"Feedback from {name} - {rating_feed}"
                body = f"Rating: {rating_feed}\nComment: {comment_feed}"
                mailto_link = f"mailto:{EMAIL_ADDRESS}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
                st.markdown(f"<a href='{mailto_link}' target='_blank'>📥 اضغط هنا لإرسال الإيميل</a>", unsafe_allow_html=True)

# Complaint Column
with c_comp:
    with st.expander("⚠️ File a Complaint (تقديم شكوى)"):
        with st.form("complain_form"):
            st.write("Severity (درجة الأهمية):")
            rating_comp = st.select_slider("Select Level", options=["Low", "Medium", "High", "Critical", "Urgent"])
            comment_comp = st.text_area("Complaint Details (تفاصيل الشكوى):")
            submit_comp = st.form_submit_button("Submit Complaint")
            
            if submit_comp:
                subject = f"COMPLAINT: {name} - Level {rating_comp}"
                body = f"Level: {rating_comp}\nDetails: {comment_comp}\nPhone: {phone}"
                mailto_link = f"mailto:{EMAIL_ADDRESS}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
                st.markdown(f"<a href='{mailto_link}' target='_blank'>📥 اضغط هنا لإرسال الشكوى رسمياً</a>", unsafe_allow_html=True)
