import streamlit as st

# --- 1. Page Configuration (Quotes added to icon) ---
st.set_page_config(
    page_title="Infinity CDT | Intero System",
    page_icon="🏠",
    layout="wide"
)

# --- 2. Constants & Contact Data (Quotes added to strings) ---
BRAND_GOLD = "#D4AF37"
BRAND_BLACK = "#0d0d0d"
WHATSAPP_NUMBER = "201062796287"
EMAIL_ADDRESS = "connect@infinitycdt.com"

# --- 3. UI Customization ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    
    * {{ font-family: 'Montserrat', sans-serif; }}

    .stApp {{
        background-color: {BRAND_BLACK};
        color: #ffffff;
    }}

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
        border-left: 3px solid {BRAND_GOLD};
        padding: 20px;
        border-radius: 12px;
        margin: 25px 0;
    }}

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

    input, select, .stSelectbox div {{
        background-color: #1a1a1a !important;
        color: white !important;
        border: 1px solid #333 !important;
        border-radius: 12px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. Sidebar ---
with st.sidebar:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown(f"<h2 style='color:{BRAND_GOLD}; text-align:center;'>INFINITY CDT</h2>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🌐 FOLLOW US")
    st.markdown(f"""
        <a href="https://www.facebook.com/InfinityCDT" target="_blank" style="color:#888; text-decoration:none; display:block; margin:10px 0;">Facebook</a>
        <a href="https://www.instagram.com/InfinityCDT" target="_blank" style="color:#888; text-decoration:none; display:block; margin:10px 0;">Instagram</a>
        <a href="https://www.tiktok.com/@infinitycdt" target="_blank" style="color:#888; text-decoration:none; display:block; margin:10px 0;">TikTok</a>
        <a href="https://www.threads.com/@infinitycdt" target="_blank" style="color:#888; text-decoration:none; display:block; margin:10px 0;">Threads</a>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ✉️ INQUIRIES")
    st.write(f"Email: {EMAIL_ADDRESS}")
    st.write(f"Support: +{WHATSAPP_NUMBER}")
    
    st.markdown("---")
    st.caption("Engineering Excellence © 2025")

# --- 5. Hero Banner ---
st.markdown(f"""
    <div class="hero-section">
        <h5 style='color:{BRAND_GOLD}; letter-spacing:8px; font-weight:300;'>INFINITY CONSTRUCTION</h5>
        <h1 style='font-size: 4.8rem; font-weight:700; margin:5px 0;'>INTERO</h1>
        <p style='font-size: 1.3rem; font-weight:300; opacity:0.6;'>Precision Finishing Estimator System</p>
    </div>
    """, unsafe_allow_html=True)

# --- 6. Data Dictionary (Corrected Dictionary Syntax) ---
packages = {
    "i-Modern": {
        "range": (5000, 5600),
        "target": "First Home / Investment",
        "specs": "✅ Elsewedy Cables | ✅ Sanchi Switches | ✅ GLC/Sipes Paints | ✅ Laser Cut Ceramics"
    },
    "i-Smart": {
        "range": (5900, 6800),
        "target": "Tech Lovers / Families",
        "specs": "✅ Schneider Avatar Switches | ✅ Smart Home Prep | ✅ Indian/UAE Porcelain (60x120) | ✅ Jotun Fenomastic"
    },
    "i-Elite": {
        "range": (7100, 9000),
        "target": "Villas / Luxury Apartments",
        "specs": "✅ Legrand Switches | ✅ Grohe Built-in Tanks | ✅ Spanish Porcelain / Marble | ✅ Sound System Prep"
    },
    "i-Signature": {
        "range": (12000, 15000),
        "target": "Penthouses / VIP Palaces",
        "specs": "✅ Full Automation (KNX/Control4) | ✅ Book-match Marble | ✅ Engineered Wood | ✅ Custom Bespoke Designs"
    }
}

# --- 7. Form ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("YOUR NAME", placeholder="Full Name")
with col2:
    phone = st.text_input("WHATSAPP", placeholder="01xxxxxxxxx")

area = st.number_input("UNIT AREA (SQM)", min_value=50, value=120, step=10)
selected_p = st.selectbox("CHOOSE FINISHING PACKAGE", list(packages.keys()))

st.markdown(f"""
    <div class="specs-box">
        <strong style="color:{BRAND_GOLD}; text-transform:uppercase; font-size:0.8rem;">{selected_p} Package Includes:</strong><br>
        <span style="font-size:0.9rem; opacity:0.8;">{packages[selected_p]['specs']}</span><br>
        <small style="opacity:0.5;">Target: {packages[selected_p]['target']}</small>
    </div>
""", unsafe_allow_html=True)

calculate_btn = st.button("GENERATE ESTIMATE 🚀")
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. Results ---
if calculate_btn:
    if not name or not phone:
        st.error("Please provide your name and phone to generate the report.")
    else:
        st.balloons()
        min_p = area * packages[selected_p]['range'][0]
        max_p = area * packages[selected_p]['range'][1]
        avg_p = (min_p + max_p) / 2
        
        st.markdown(f"""
            <div style='text-align:center; padding: 40px 0;'>
                <h3 style='color:{BRAND_GOLD}; font-weight:300; letter-spacing:2px;'>ESTIMATED INVESTMENT</h3>
                <h1 style='font-size: 6rem; margin:0;'>{int(avg_p):,} <small style='font-size:1.2rem; opacity:0.4;'>EGP</small></h1>
                <p style='opacity:0.6; font-size:1.1rem;'>Estimate for {area} sqm under the {selected_p} package.</p>
            </div>
        """, unsafe_allow_html=True)
        
        wa_msg = f"Hello Infinity CDT, I'm {name}. I've generated a quote for the {selected_p} package for my {area}sqm unit. Let's discuss the next steps."
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg.replace(' ', '%20')}"
        
        st.markdown(f"""
            <div style='text-align:center; margin-bottom: 60px;'>
                <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
                    <button style="background:#25D366; color:white; border:none; padding:22px 80px; border-radius:50px; font-weight:bold; cursor:pointer; font-size:1.3rem; box-shadow: 0 10px 30px rgba(37, 211, 102, 0.2);">
                        START YOUR CONSULTATION 💬
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.2; padding-bottom:40px;'>INFINITY CDT | Intero Pro v3.0</p>", unsafe_allow_html=True)
