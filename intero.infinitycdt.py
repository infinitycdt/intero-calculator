import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title=Infinity CDT  Intero System,
    page_icon=🏠,
    layout=wide
)

# --- Constants & Contact Data ---
BRAND_GOLD = #D4AF37
BRAND_BLACK = #0d0d0d
WHATSAPP_NUMBER = 201062796287
EMAIL_ADDRESS = connect@infinitycdt.com

# --- UI Customization (Figma  Luxury Style) ---
st.markdown(f
    style
    @import url('httpsfonts.googleapis.comcss2family=Montserratwght@300;400;600;700&display=swap');
    
     {{ font-family 'Montserrat', sans-serif; }}

    .stApp {{
        background-color {BRAND_BLACK};
        color #ffffff;
    }}

     Hero Section with High-Quality Image Placeholder 
    .hero-section {{
        height 45vh;
        background linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url('httpsimages.unsplash.comphoto-1613545325278-f24b0cae1224auto=format&fit=crop&q=80&w=2070');
        background-size cover;
        background-position center;
        display flex;
        flex-direction column;
        justify-content center;
        align-items center;
        border-radius 0 0 40px 40px;
        margin-bottom 40px;
        text-align center;
    }}

     Glassmorphism Effect 
    .glass-card {{
        background rgba(255, 255, 255, 0.03);
        backdrop-filter blur(15px);
        border 1px solid rgba(255, 255, 255, 0.1);
        border-radius 25px;
        padding 40px;
        margin -80px auto 40px auto;
        max-width 900px;
        box-shadow 0 25px 50px rgba(0,0,0,0.6);
    }}

    .specs-box {{
        background rgba(212, 175, 55, 0.05);
        border-left 3px solid {BRAND_GOLD};
        padding 20px;
        border-radius 12px;
        margin 25px 0;
    }}

     Premium Buttons 
    .stButtonbutton {{
        background {BRAND_GOLD} !important;
        color #000 !important;
        border none !important;
        border-radius 50px !important;
        padding 18px 50px !important;
        font-weight 700 !important;
        font-size 1.1rem !important;
        letter-spacing 1.5px;
        transition 0.4s all ease;
        width 100%;
        margin-top 20px;
    }}
    .stButtonbuttonhover {{
        background #ffffff !important;
        transform translateY(-3px);
        box-shadow 0 10px 25px rgba(212, 175, 55, 0.4);
    }}

     Custom Inputs 
    input, select, .stSelectbox div {{
        background-color #1a1a1a !important;
        color white !important;
        border 1px solid #333 !important;
        border-radius 12px !important;
    }}
    style
    , unsafe_allow_html=True)

# --- Sidebar Corporate Links ---
with st.sidebar
    try
        st.image(logo.png, use_container_width=True)
    except
        st.markdown(fh2 style='color{BRAND_GOLD}; text-aligncenter;'INFINITY CDTh2, unsafe_allow_html=True)
    
    st.markdown(---)
    st.markdown(### 🌐 FOLLOW US)
    st.markdown(f
        a href=httpswww.facebook.comInfinityCDT style=color#888; text-decorationnone; displayblock; margin10px 0;Facebooka
        a href=httpswww.instagram.comInfinityCDT style=color#888; text-decorationnone; displayblock; margin10px 0;Instagrama
        a href=httpswww.tiktok.com@infinitycdt style=color#888; text-decorationnone; displayblock; margin10px 0;TikToka
        a href=httpswww.threads.com@infinitycdt style=color#888; text-decorationnone; displayblock; margin10px 0;Threadsa
    , unsafe_allow_html=True)
    
    st.markdown(---)
    st.markdown(### ✉️ INQUIRIES)
    st.write(fEmail connect@infinitycdt.com)
    st.write(fSupport +201062796287)
    
    st.markdown(---)
    st.caption(Engineering Excellence © 2025)

# --- Hero Banner ---
st.markdown(f
    div class=hero-section
        h5 style='color{BRAND_GOLD}; letter-spacing8px; font-weight300;'INFINITY CONSTRUCTIONh5
        h1 style='font-size 4.8rem; font-weight700; margin5px 0;'INTEROh1
        p style='font-size 1.3rem; font-weight300; opacity0.6;'Precision Finishing Estimator Systemp
    div
    , unsafe_allow_html=True)

# --- Data Dictionary (Merged from your CSV files) ---
packages = {
    i-Modern {
        range (5000, 5600),
        target First Home  Investment,
        specs ✅ Elsewedy Cables  ✅ Sanchi Switches  ✅ GLCSipes Paints  ✅ Laser Cut Ceramics
    },
    i-Smart {
        range (5900, 6800),
        target Tech Lovers  Families,
        specs ✅ Schneider Avatar Switches  ✅ Smart Home Prep  ✅ IndianUAE Porcelain (60x120)  ✅ Jotun Fenomastic
    },
    i-Elite {
        range (7100, 9000),
        target Villas  Luxury Apartments,
        specs ✅ Legrand Switches  ✅ Grohe Built-in Tanks  ✅ Spanish Porcelain  Marble  ✅ Sound System Prep
    },
    i-Signature {
        range (12000, 15000),
        target Penthouses  VIP Palaces,
        specs ✅ Full Automation (KNXControl4)  ✅ Book-match Marble  ✅ Engineered Wood  ✅ Custom Bespoke Designs
    }
}

# --- Main Calculator Form ---
st.markdown('div class=glass-card', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1
    name = st.text_input(YOUR NAME, placeholder=Full Name)
with col2
    phone = st.text_input(WHATSAPP, placeholder=01xxxxxxxxx)

area = st.number_input(UNIT AREA (SQM), min_value=50, value=120, step=10)
selected_p = st.selectbox(CHOOSE FINISHING PACKAGE, list(packages.keys()))

st.markdown(f
    div class=specs-box
        strong style=color{BRAND_GOLD}; text-transformuppercase; font-size0.8rem;{selected_p} Package Includesstrongbr
        span style=font-size0.9rem; opacity0.8;{packages[selected_p]['specs']}spanbr
        small style=opacity0.5;Target {packages[selected_p]['target']}small
    div
, unsafe_allow_html=True)

calculate_btn = st.button(GENERATE ESTIMATE 🚀)
st.markdown('div', unsafe_allow_html=True)

# --- Results Rendering ---
if calculate_btn
    if not name or not phone
        st.error(Please provide your name and phone to generate the report.)
    else
        st.balloons()
        min_p = area  packages[selected_p]['range'][0]
        max_p = area  packages[selected_p]['range'][1]
        avg_p = (min_p + max_p)  2
        
        st.markdown(f
            div style='text-aligncenter; padding 40px 0;'
                h3 style='color{BRAND_GOLD}; font-weight300; letter-spacing2px;'ESTIMATED INVESTMENTh3
                h1 style='font-size 6rem; margin0;'{int(avg_p),} small style='font-size1.2rem; opacity0.4;'EGPsmallh1
                p style='opacity0.6; font-size1.1rem;'Estimate for {area} sqm under the {selected_p} package.p
            div
        , unsafe_allow_html=True)
        
        # Professional WhatsApp Message
        wa_msg = fHello Infinity CDT, I'm {name}. I've generated a quote for the {selected_p} package for my {area}sqm unit. Let's discuss the next steps.
        whatsapp_url = fhttpswa.me{WHATSAPP_NUMBER}text={wa_msg.replace(' ', '%20')}
        
        st.markdown(f
            div style='text-aligncenter; margin-bottom 60px;'
                a href={whatsapp_url} target=_blank style=text-decorationnone;
                    button style=background#25D366; colorwhite; bordernone; padding22px 80px; border-radius50px; font-weightbold; cursorpointer; font-size1.3rem; box-shadow 0 10px 30px rgba(37, 211, 102, 0.2);
                        START YOUR CONSULTATION 💬
                    button
                a
            div
        , unsafe_allow_html=True)

st.markdown(fp style='text-aligncenter; opacity0.2; padding-bottom40px;'INFINITY CDT  Intero Pro v3.0p, unsafe_allow_html=True)
