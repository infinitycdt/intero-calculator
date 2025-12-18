import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import datetime

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Infinity CDT | Intero",
    page_icon="🏠",
    layout="wide"
)

# --- 2. Google Sheets Connection ---
conn = st.connection("gsheets", type=GSheetsConnection)

# --- 3. Dynamic UI (System Auto Mode) ---
BRAND_GOLD = "#D4AF37"
WHATSAPP_NUMBER = "201062796287"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    
    * {{ font-family: 'Montserrat', sans-serif; }}

    /* Default Light Mode Variables */
    :root {{
        --bg-color: #FFFFFF;
        --card-bg: #FDFDFD;
        --text-main: #1A1A1A;
        --text-sub: #666666;
        --input-bg: #F8F9FA;
        --border-color: #EEEEEE;
        --shadow: rgba(0,0,0,0.05);
    }}

    /* Auto Switch to Dark Mode based on System Settings */
    @media (prefers-color-scheme: dark) {{
        :root {{
            --bg-color: #0D0D0D;
            --card-bg: #161616;
            --text-main: #FFFFFF;
            --text-sub: #AAAAAA;
            --input-bg: #1F1F1F;
            --border-color: #333333;
            --shadow: rgba(0,0,0,0.4);
        }}
    }}

    .stApp {{
        background-color: var(--bg-color);
        color: var(--text-main);
        transition: all 0.5s ease;
    }}

    /* Hero Section */
    .hero-section {{
        height: 35vh;
        background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
                    url('https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&q=80&w=2070');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 0 0 30px 30px;
        text-align: center;
    }}

    /* Adaptive Main Card */
    .main-card {{
        background: var(--card-bg);
        border-radius: 20px;
        padding: 40px;
        margin: -50px auto 40px auto;
        max-width: 850px;
        box-shadow: 0 15px 40px var(--shadow);
        border: 1px solid var(--border-color);
        transition: background 0.5s ease;
    }}

    .specs-box {{
        background: rgba(212, 175, 55, 0.08);
        border-left: 4px solid {BRAND_GOLD};
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0;
    }}

    /* Elegant Golden Button */
    .stButton>button {{
        background: {BRAND_GOLD} !important;
        color: #000 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 15px 40px !important;
        font-weight: 700 !important;
        width: 100%;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background: #FFFFFF !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
    }}

    /* Inputs adjustment for Auto Mode */
    input, select, .stSelectbox div {{
        background-color: var(--input-bg) !important;
        color: var(--text-main) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
    }}

    h1, h2, h3, h4, h5 {{ color: var(--text-main); }}
    p, label {{ color: var(--text-sub); }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. Sidebar ---
with st.sidebar:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown(f"<h2 style='color:{BRAND_GOLD}; text-align:center;'>INFINITY CDT</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Engineering Excellence © 2025")

# --- 5. Hero Banner ---
st.markdown(f"""
    <div class="hero-section">
        <h5 style='color:{BRAND_GOLD}; letter-spacing:5px;'>INFINITY CONSTRUCTION</h5>
        <h1 style='font-size: 3.5rem; font-weight:700; color:white;'>INTERO</h1>
    </div>
    """, unsafe_allow_html=True)

# --- 6. Packages Data ---
packages = {
    "i-Modern": {"price": (5000, 5600), "specs": "✅ Elsewedy Cables | ✅ Sanchi Switches"},
    "i-Smart": {"price": (5900, 6800), "specs": "✅ Schneider Avatar | ✅ Smart Home Prep"},
    "i-Elite": {"price": (7100, 9000), "specs": "✅ Legrand | ✅ Grohe | ✅ Marble"},
    "i-Signature": {"price": (12000, 15000), "specs": "✅ Full Automation | ✅ Book-match Marble"}
}

# --- 7. Main Calculator ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    name = st.text_input("FULL NAME")
with c2:
    phone = st.text_input("PHONE")

area = st.number_input("AREA (SQM)", min_value=50, value=120)
selected_p = st.selectbox("PACKAGE", list(packages.keys()))

st.markdown(f"""
    <div class="specs-box">
        <strong style="font-size:0.8rem;">{selected_p} DETAILS:</strong><br>
        <span style="font-size:0.9rem;">{packages[selected_p]['specs']}</span>
    </div>
""", unsafe_allow_html=True)

if st.button("CALCULATE INVESTMENT 🚀"):
    if not name or not phone:
        st.error("Please provide contact details.")
    else:
        # Calculation
        avg_p = (area * packages[selected_p]['price'][0] + area * packages[selected_p]['price'][1]) / 2
        
        # Log to GSheets
        new_lead = pd.DataFrame([{
            "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "Phone": phone,
            "Area": area,
            "Package": selected_p,
            "Estimated Price": f"{int(avg_p):,} EGP"
        }])
        
        try:
            existing_data = conn.read(worksheet="Sheet1")
            updated_df = pd.concat([existing_data, new_lead], ignore_index=True)
            conn.update(worksheet="Sheet1", data=updated_df)
            st.success("Inquiry recorded.")
        except:
            st.info("Local Preview: Data logging skipped.")

        st.balloons()
        st.markdown(f"<h1 style='text-align:center; color:{BRAND_GOLD};'>{int(avg_p):,} EGP</h1>", unsafe_allow_html=True)
        
        wa_msg = f"Hello Infinity CDT, I am {name}. I generated a quote for {selected_p}."
        st.markdown(f'<a href="https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg.replace(" ", "%20")}" target="_blank"><button style="width:100%; background:#25D366; color:white; padding:15px; border:none; border-radius:12px; cursor:pointer; font-weight:bold;">SEND TO WHATSAPP 💬</button></a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
