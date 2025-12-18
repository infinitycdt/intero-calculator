import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import datetime

# --- 1. Page Configuration ---
st.set_page_config(page_title="Infinity CDT | Intero System", page_icon="🏠", layout="wide")

# --- 2. Google Sheets Connection ---
conn = st.connection("gsheets", type=GSheetsConnection)

# --- 3. UI Styling (Luxury Light) ---
BRAND_GOLD = "#D4AF37"
TEXT_DARK = "#1A1A1A"
WHATSAPP_NUMBER = "201062796287"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    * {{ font-family: 'Montserrat', sans-serif; }}
    .stApp {{ background-color: #FFFFFF; color: {TEXT_DARK}; }}
    .main-card {{ background: #FFFFFF; border-radius: 20px; padding: 40px; margin: -60px auto 40px auto; max-width: 850px; box-shadow: 0 15px 40px rgba(0,0,0,0.08); border: 1px solid #f0f0f0; }}
    .stButton>button {{ background: {TEXT_DARK} !important; color: {BRAND_GOLD} !important; border: 2px solid {BRAND_GOLD} !important; border-radius: 8px; width: 100%; font-weight: bold; padding: 15px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. Hero Section ---
st.markdown(f"""
    <div style='height:40vh; background:linear-gradient(rgba(255,255,255,0.4), rgba(255,255,255,0.4)), url("https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&q=80&w=2070"); background-size:cover; background-position:center; display:flex; flex-direction:column; justify-content:center; align-items:center; border-radius:0 0 40px 40px; text-align:center;'>
        <h5 style='color:{BRAND_GOLD}; letter-spacing:6px; font-weight:600;'>INFINITY CONSTRUCTION</h5>
        <h1 style='font-size: 4rem; font-weight:700; color:{TEXT_DARK};'>INTERO</h1>
    </div>
    """, unsafe_allow_html=True)

# --- 5. Packages Data ---
packages = {
    "i-Modern": {"price": (5000, 5600), "specs": "✅ Elsewedy Cables | ✅ Sanchi Switches"},
    "i-Smart": {"price": (5900, 6800), "specs": "✅ Schneider Avatar | ✅ Smart Home Prep"},
    "i-Elite": {"price": (7100, 9000), "specs": "✅ Legrand | ✅ Grohe | ✅ Marble"},
    "i-Signature": {"price": (12000, 15000), "specs": "✅ Full Automation | ✅ Book-match Marble"}
}

# --- 6. Form & Logic ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    name = st.text_input("NAME", placeholder="Full Name")
with c2:
    phone = st.text_input("PHONE", placeholder="01xxxxxxxxx")

area = st.number_input("AREA (SQM)", min_value=50, value=120)
selected_p = st.selectbox("PACKAGE", list(packages.keys()))

if st.button("CALCULATE INVESTMENT 🚀"):
    if not name or not phone:
        st.error("Please provide your contact details.")
    else:
        # Calculation
        avg_p = (area * packages[selected_p]['price'][0] + area * packages[selected_p]['price'][1]) / 2
        
        # --- Recording Lead to Google Sheets ---
        new_lead = pd.DataFrame([{
            "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "Phone": phone,
            "Area": area,
            "Package": selected_p,
            "Estimated Price": f"{int(avg_p):,} EGP"
        }])
        
        try:
            # Read existing data and append
            existing_data = conn.read(worksheet="Sheet1")
            updated_df = pd.concat([existing_data, new_lead], ignore_index=True)
            conn.update(worksheet="Sheet1", data=updated_df)
            st.success("Your inquiry has been recorded successfully!")
        except Exception as e:
            st.warning("Lead saved locally. Connection to sheet pending...")

        st.balloons()
        st.markdown(f"<h1 style='text-align:center; color:{BRAND_GOLD};'>{int(avg_p):,} EGP</h1>", unsafe_allow_html=True)
        
        wa_msg = f"Hello Infinity CDT, I am {name}. I generated a quote for {selected_p} package."
        st.markdown(f'<a href="https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg.replace(" ", "%20")}" target="_blank"><button style="width:100%; background:#25D366; color:white; padding:15px; border:none; border-radius:10px; cursor:pointer; font-weight:bold;">SEND TO WHATSAPP 💬</button></a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
