import streamlit as st

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Infinity CDT | Intero System",
    page_icon="🏠",
    layout="wide"
)

# --- 2. Branding Constants ---
BRAND_GOLD = "#D4AF37"
BRAND_WHITE = "#FFFFFF"
BRAND_GRAY = "#F8F9FA"
TEXT_DARK = "#1A1A1A"
WHATSAPP_NUMBER = "201062796287"
EMAIL_ADDRESS = "connect@infinitycdt.com"

# --- 3. UI Customization (Luxury Light Style) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    
    * {{ font-family: 'Montserrat', sans-serif; }}

    /* Background Setup */
    .stApp {{
        background-color: {BRAND_WHITE};
        color: {TEXT_DARK};
    }}

    /* Hero Section - Bright & Airy */
    .hero-section {{
        height: 40vh;
        background: linear-gradient(rgba(255,255,255,0.4), rgba(255,255,255,0.4)), 
                    url('https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&q=80&w=2070');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 0 0 40px 40px;
        margin-bottom: 40px;
        text-align: center;
        border-bottom: 1px solid #eee;
    }}

    /* Elegant Content Card */
    .main-card {{
        background: {BRAND_WHITE};
        border-radius: 20px;
        padding: 40px;
        margin: -60px auto 40px auto;
        max-width: 850px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.08);
        border: 1px solid #f0f0f0;
    }}

    .specs-box {{
        background: #fdfaf0;
        border-left: 4px solid {BRAND_GOLD};
        padding: 20px;
        border-radius: 8px;
        margin: 20px 0;
    }}

    /* Buttons - Luxury Gold */
    .stButton>button {{
        background: {TEXT_DARK} !important;
        color: {BRAND_GOLD} !important;
        border: 2px solid {BRAND_GOLD} !important;
        border-radius: 8px !important;
        padding: 15px 40px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        letter-spacing: 1px;
        transition: 0.3s all ease;
        width: 100%;
        margin-top: 10px;
    }}
    .stButton>button:hover {{
        background: {BRAND_GOLD} !important;
        color: {TEXT_DARK} !important;
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.3);
    }}

    /* Input Fields Style */
    input, select, .stSelectbox div {{
        background-color: {BRAND_GRAY} !important;
        color: {TEXT_DARK} !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 8px !important;
    }}

    /* Results Styling */
    .result-value {{
        color: {BRAND_GOLD};
        font-weight: 700;
        font-size: 4.5rem;
        margin: 0;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. Sidebar ---
with st.sidebar:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown(f"<h2 style='color:{TEXT_DARK}; text-align:center;'>INFINITY CDT</h2>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🌐 SOCIAL MEDIA")
    st.markdown(f"""
        <a href="https://www.facebook.com/InfinityCDT" target="_blank" style="color:#666; text-decoration:none; display:block; margin:8px 0;">Facebook</a>
        <a href="https://www.instagram.com/InfinityCDT" target="_blank" style="color:#666; text-decoration:none; display:block; margin:8px 0;">Instagram</a>
        <a href="https://www.tiktok.com/@infinitycdt" target="_blank" style="color:#666; text-decoration:none; display:block; margin:8px 0;">TikTok</a>
        <a href="https://www.threads.com/@infinitycdt" target="_blank" style="color:#666; text-decoration:none; display:block; margin:8px 0;">Threads</a>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ✉️ CONTACT")
    st.write(f"Email: {EMAIL_ADDRESS}")
    st.write(f"WhatsApp: +{WHATSAPP_NUMBER}")
    
    st.markdown("---")
    st.caption("Engineering Excellence © 2025")

# --- 5. Hero Banner ---
st.markdown(f"""
    <div class="hero-section">
        <h5 style='color:{BRAND_GOLD}; letter-spacing:6px; font-weight:600;'>Infinity Construction and Decorations</h5>
        <h1 style='font-size: 4rem; font-weight:700; margin:5px 0; color:{TEXT_DARK};'>INTERO</h1>
        <p style='font-size: 1.1rem; color:#555;'>Your Gateway to Precision Interior Finishing</p>
    </div>
    """, unsafe_allow_html=True)

# --- 6. Data (Your Real Packages) ---
packages = {{
    "i-Modern": {{
        "price": (5000, 5600),
        "target": "First Home / Investment",
        "specs": "✅ Elsewedy Cables | ✅ Sanchi Switches | ✅ GLC/Sipes Paints | ✅ Laser Cut Ceramics"
    }},
    "i-Smart": {{
        "price": (5900, 6800),
        "target": "Tech Lovers / Families",
        "specs": "✅ Schneider Avatar Switches | ✅ Smart Home Prep | ✅ Indian/UAE Porcelain | ✅ Jotun Fenomastic"
    }},
    "i-Elite": {{
        "price": (7100, 9000),
        "target": "Luxury Apartments / Villas",
        "specs": "✅ Legrand Switches | ✅ Grohe Built-in Tanks | ✅ Spanish Porcelain / Marble | ✅ Sound System Prep"
    }},
    "i-Signature": {{
        "price": (12000, 15000),
        "target": "VIP Penthouses / Palaces",
        "specs": "✅ Full Automation (KNX/Control4) | ✅ Book-match Marble | ✅ Engineered Wood | ✅ Custom Designs"
    }}
}}

# --- 7. Main Calculator ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("NAME", placeholder="Full Name")
with col2:
    phone = st.text_input("PHONE", placeholder="01xxxxxxxxx")

area = st.number_input("AREA (SQM)", min_value=50, value=120, step=10)
selected_p = st.selectbox("PACKAGE", list(packages.keys()))

st.markdown(f"""
    <div class="specs-box">
        <strong style="color:{TEXT_DARK}; font-size:0.8rem;">{selected_p} DETAILS:</strong><br>
        <span style="font-size:0.9rem; color:#444;">{packages[selected_p]['specs']}</span>
    </div>
""", unsafe_allow_html=True)

calculate_btn = st.button("CALCULATE INVESTMENT 🚀")
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. Results ---
if calculate_btn:
    if not name or not phone:
        st.error("Please provide your contact details.")
    else:
        st.balloons()
        p_data = packages[selected_p]
        avg_p = (area * p_data['price'][0] + area * p_data['price'][1]) / 2
        
        st.markdown(f"""
            <div style='text-align:center; padding: 20px 0;'>
                <h3 style='color:#666; font-weight:400;'>ESTIMATED INVESTMENT</h3>
                <h1 class="result-value">{int(avg_p):,} <small style='font-size:1.2rem; color:#999;'>EGP</small></h1>
                <p style='color:#777;'>Estimate for {area} sqm under {selected_p} package.</p>
            </div>
        """, unsafe_allow_html=True)
        
        wa_msg = f"Hello Infinity CDT, I am {name}. I generated a quote for {selected_p} package ({area} sqm). Please contact me."
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg.replace(' ', '%20')}"
        
        st.markdown(f"""
            <div style='text-align:center; margin-bottom: 40px;'>
                <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
                    <button style="background:#25D366; color:white; border:none; padding:18px 60px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:1.1rem; box-shadow: 0 10px 20px rgba(37, 211, 102, 0.1);">
                        SEND TO WHATSAPP 💬
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.3; padding-bottom:30px;'>INFINITY CDT | Intero System v3.2</p>", unsafe_allow_html=True)
