import streamlit as st

# --- Configuration & Branding ---
BRAND_GOLD = "#D4AF37"
BRAND_BLACK = "#1A1A1A"
WHATSAPP_NUMBER = "201062796287" # Updated Number
EMAIL_ADDRESS = "info@infinitycdt.com"

st.set_page_config(
    page_title="Infinity CDT | Intero Calculator",
    page_icon="🏠",
    layout="centered"
)

# --- Custom Luxury CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Poppins', sans-serif; }}
    
    .stApp {{ 
        background-color: #ffffff; 
        background-image: url("https://www.transparenttextures.com/patterns/architect.png"); 
    }}
    
    .main-card {{
        background: white; padding: 2rem; border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1); border-left: 5px solid {BRAND_GOLD};
    }}
    
    .stButton>button {{
        background: {BRAND_BLACK}; color: {BRAND_GOLD} !important;
        border: 1px solid {BRAND_GOLD}; border-radius: 10px; font-weight: bold; 
        height: 3.5em; width: 100%; transition: 0.3s;
    }}
    
    .stButton>button:hover {{
        background: {BRAND_GOLD}; color: {BRAND_BLACK} !important;
    }}

    .package-box {{
        background: #fdfaf0; border: 1px solid {BRAND_GOLD};
        padding: 15px; border-radius: 10px; margin-bottom: 20px;
    }}
    
    .sidebar-text {{ font-size: 0.9rem; color: #555; }}
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar: Logo & Social Media ---
with st.sidebar:
    # Company Logo (Please ensure logo.png is in the same GitHub folder)
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown(f"<h1 style='color:{BRAND_GOLD}; text-align:center;'>INFINITY CDT</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📞 CONTACT US")
    st.markdown(f"**Email:** {EMAIL_ADDRESS}")
    st.markdown(f"**WhatsApp:** +20 106 279 6287")
    
    st.markdown("---")
    st.markdown("### 🌐 FOLLOW US")
    st.markdown(f"""
        <a href="https://www.facebook.com/InfinityCDT" target="_blank">Facebook</a><br>
        <a href="https://www.instagram.com/InfinityCDT" target="_blank">Instagram</a><br>
        <a href="https://www.tiktok.com/@infinitycdt" target="_blank">TikTok</a><br>
        <a href="https://www.threads.com/@infinitycdt" target="_blank">Threads</a>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Engineering Excellence © 2025")

# --- Package Data (Based on your final prices) ---
packages = {
    "i-Modern": {
        "price": (5000, 5600),
        "specs": "• Elsewedy Cables (Certified)\n• SanChi/Kaptika Switches\n• GLC/Sipes Paints\n• 1st Grade Ceramic Flooring"
    },
    "i-Smart": {
        "price": (5900, 6800),
        "specs": "• Schneider Panel + Avatar Switches\n• Smart Home & CCTV Prep\n• Indian/UAE Porcelain (60x120)\n• Jotun Fenomastic Paints"
    },
    "i-Elite": {
        "price": (7100, 9000),
        "specs": "• ABB/Hager Panel + Legrand Switches\n• Grohe Built-in Tanks\n• Spanish Porcelain or Trista Marble\n• Sound System & Central AC Prep"
    },
    "i-Signature": {
        "price": (12000, 15000),
        "specs": "• Full Automation (KNX/Control4)\n• Imported Book-match Marble\n• Engineered Natural Wood\n• Bespoke Interior Design"
    }
}

# --- Main Interface ---
st.markdown(f"<h1 style='color:{BRAND_BLACK}; text-align:center;'>Intero | Smart Calculator 📐</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Get an instant engineering quote for your unit.</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name", placeholder="e.g. Eng. Mina")
    with col2:
        phone = st.text_input("Mobile Number", placeholder="01xxxxxxxxx")

    area = st.number_input("Unit Area (sqm)", min_value=50, max_value=2000, value=120, step=5)
    
    selected_p = st.selectbox("Choose Finishing Package", list(packages.keys()))
    
    st.markdown(f"""
        <div class="package-box">
            <strong style="color:{BRAND_GOLD};">💎 {selected_p} Specifications:</strong><br>
            <small style="white-space: pre-wrap;">{packages[selected_p]['specs']}</small>
        </div>
    """, unsafe_allow_html=True)
    
    calculate_btn = st.button("Generate Instant Quote 🚀")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Results ---
if calculate_btn:
    if not name or not phone:
        st.error("Please provide your name and contact number.")
    else:
        st.balloons()
        p_data = packages[selected_p]
        total_min = area * p_data['price'][0]
        total_max = area * p_data['price'][1]
        avg_total = (total_min + total_max) / 2
        
        st.markdown(f"### 📄 Preliminary Quote for: {name}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Estimated Total Cost", f"{int(avg_total):,} EGP")
        with c2:
            st.metric("Price per sqm", f"{p_data['price'][0]:,} EGP")

        st.info(f"The estimate for this package ranges from **{total_min:,} EGP** to **{total_max:,} EGP** based on final material selection.")

        # WhatsApp Message
        msg = f"Hello Infinity CDT, I'm {name}. I generated a quote for {selected_p} package for a {area}sqm unit on Intero. I would like to book an inspection."
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"
        
        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank">
                <button style="width:100%; background-color:#25D366; color:white; padding:15px; border:none; border-radius:10px; font-weight:bold; cursor:pointer; font-size:1.1em;">
                    Send Quote to WhatsApp & Book Inspection 💬
                </button>
            </a>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#888;'>Infinity CDT | Your Path to Engineering Excellence</p>", unsafe_allow_html=True)
