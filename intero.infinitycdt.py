import streamlit as st
import pandas as pd
import urllib.parse
import os
from datetime import datetime

# --- 1. System Configuration & Database Setup ---
DB_FILE = 'intero_customers_db.csv'
ADMIN_PASSWORD = "admin"  # كلمة مرور لوحة التحكم (يمكنك تغييرها)

# Initialize Database if not exists
def init_db():
    if not os.path.exists(DB_FILE):
        df = pd.DataFrame(columns=["Date", "Client Name", "Phone", "Area", "Package", "Total Estimate", "Status"])
        df.to_csv(DB_FILE, index=False)

def save_lead(name, phone, area, package, total):
    df = pd.read_csv(DB_FILE)
    new_data = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Client Name": name,
        "Phone": phone,
        "Area": area,
        "Package": package,
        "Total Estimate": total,
        "Status": "New"
    }
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(DB_FILE, index=False)

# --- 2. Page Configuration ---
st.set_page_config(
    page_title="Infinity CDT | Intero System Pro",
    page_icon="🏗️",
    layout="wide"
)

# --- Constants ---
BRAND_GOLD = "#D4AF37"
BRAND_BLACK = "#0d0d0d"
BRAND_WHITE = "#ffffff"
TEXT_COLOR = "#333333"

# Default Prices (Can be overridden in Admin)
if 'prices' not in st.session_state:
    st.session_state.prices = {
        'i-Modern': 8200,
        'i-Smart': 10500,
        'i-Elite': 16500,
        'i-Signature': 28000
    }

# --- UI Styling ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    * {{ font-family: 'Cairo', 'Montserrat', sans-serif; }}
    .stApp {{ background-color: {BRAND_WHITE}; color: {TEXT_COLOR}; }}
    
    /* Hero Section */
    .hero-section {{
        padding: 40px 20px;
        background: linear-gradient(135deg, #fdfbf7 0%, #fff 100%);
        border-bottom: 3px solid {BRAND_GOLD};
        text-align: center;
        margin-bottom: 30px;
    }}
    
    /* Custom Cards */
    .metric-card {{
        background: #F8F9FA;
        border-left: 5px solid {BRAND_GOLD};
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }}
    
    /* Buttons */
    .stButton>button {{
        background: {BRAND_GOLD} !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        border: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. Sidebar Navigation ---
with st.sidebar:
    st.markdown(f"<h2 style='color:{BRAND_GOLD}; text-align:center;'>INFINITY CDT</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio("القائمة (Menu)", ["🏠 Home (Estimator)", "🛠️ Engineering Tools", "🔐 Admin Dashboard"])
    
    st.markdown("---")
    st.info("System v3.0 | Database Connected ✅")

# --- 4. Main Logic based on Menu ---

# ==========================
# A. HOME (ESTIMATOR)
# ==========================
if menu == "🏠 Home (Estimator)":
    # Hero
    st.markdown(f"""
        <div class="hero-section">
            <h1 style='color:{BRAND_BLACK}; margin:0;'>INTERO SYSTEM</h1>
            <p style='color:{BRAND_GOLD}; font-weight:bold;'>Integrated Cost Estimation & CRM</p>
        </div>
    """, unsafe_allow_html=True)

    # Input Form
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📋 بيانات العميل")
        name = st.text_input("اسم العميل (Client Name)")
        phone = st.text_input("رقم الهاتف (Phone)")
        
        st.subheader("📐 مواصفات الوحدة")
        area = st.number_input("المساحة (Area SQM)", 50, 1000, 120)
        floor = st.selectbox("الدور", ["Ground", "Typical", "Last/Roof"])

    with col2:
        st.subheader("🎨 الباقة المختارة")
        pkg_name = st.selectbox("اختر الباقة", list(st.session_state.prices.keys()))
        
        # Display Current Price
        price_sqm = st.session_state.prices[pkg_name]
        st.markdown(f"""
            <div class="metric-card">
                <h4>{pkg_name}</h4>
                <h2 style='color:{BRAND_GOLD}'>{price_sqm:,} EGP / m²</h2>
                <small>Includes Materials & Finishing</small>
            </div>
        """, unsafe_allow_html=True)
        
        add_kitchen = st.checkbox("Add Smart Kitchen (+72,500)")
        add_furniture = st.checkbox("Add Full Furniture (+360,500)")

    # Calculation
    if st.button("احسب واحفظ العرض (Calculate & Save)", use_container_width=True):
        if name and phone:
            base_cost = area * price_sqm
            extras = (72500 if add_kitchen else 0) + (360500 if add_furniture else 0)
            total_cost = base_cost + extras
            
            # Save to Database (CSV)
            init_db()
            save_lead(name, phone, area, pkg_name, total_cost)
            
            st.success("✅ تم حفظ بيانات العميل في قاعدة البيانات بنجاح!")
            
            st.markdown("---")
            st.markdown(f"""
                <div style='text-align:center; background:#000; color:#fff; padding:30px; border-radius:15px;'>
                    <h3>Total Investment</h3>
                    <h1 style='color:{BRAND_GOLD}; font-size:3.5rem;'>{total_cost:,} EGP</h1>
                    <p>{pkg_name} Package | {area} m²</p>
                </div>
            """, unsafe_allow_html=True)
            
            # WhatsApp Link
            msg = urllib.parse.quote(f"Hi Infinity,\nNew Inquiry:\nClient: {name}\nArea: {area}m\nPkg: {pkg_name}\nTotal: {total_cost:,}")
            st.markdown(f"<br><center><a href='https://wa.me/201062796287?text={msg}' target='_blank' style='background:#25D366; color:white; padding:10px 30px; text-decoration:none; border-radius:20px; font-weight:bold;'>Send via WhatsApp 🟢</a></center>", unsafe_allow_html=True)
            
        else:
            st.error("⚠️ يرجى إدخال الاسم ورقم الهاتف لحفظ البيانات.")

# ==========================
# B. ENGINEERING TOOLS
# ==========================
elif menu == "🛠️ Engineering Tools":
    st.title("🛠️ الأدوات الهندسية المساعدة")
    st.markdown("أدوات سريعة لحساب الكميات بناءً على الملفات المرفقة (Inspired by Idea 01).")
    
    tool_choice = st.selectbox("اختر الأداة", ["حاسبة الدهانات (Paint)", "حاسبة السيراميك (Ceramics)"])
    
    if tool_choice == "حاسبة الدهانات (Paint)":
        wall_area = st.number_input("مساحة الحوائط (متر مربع)", value=100)
        coats = st.slider("عدد الأوجه (Coats)", 1, 4, 3)
        coverage = 10  # m2 per liter (approx)
        
        needed = (wall_area * coats) / coverage
        st.info(f"💡 تحتاج تقريباً **{needed:.1f} لتر** من الدهان (بافتراض التغطية 10م²/لتر).")
        
    elif tool_choice == "حاسبة السيراميك (Ceramics)":
        floor_area = st.number_input("مساحة الأرضية (متر مربع)", value=50)
        waste_ratio = st.slider("نسبة الهالك (Waste %)", 5, 15, 10)
        
        total_needed = floor_area * (1 + waste_ratio/100)
        cartons = total_needed / 1.44  # Average carton size
        
        st.info(f"💡 تحتاج إلى شراء **{total_needed:.1f} متر مربع**.")
        st.warning(f"📦 ما يعادل تقريباً **{int(cartons)+1} كرتونة** (بافتراض الكرتونة 1.44م²).")

# ==========================
# C. ADMIN DASHBOARD
# ==========================
elif menu == "🔐 Admin Dashboard":
    st.title("🔐 لوحة تحكم الإدارة")
    
    pwd = st.text_input("أدخل كلمة المرور", type="password")
    
    if pwd == ADMIN_PASSWORD:
        st.success("تم تسجيل الدخول بنجاح")
        
        # 1. Price Management
        st.subheader("💰 إدارة أسعار الباقات")
        with st.form("price_update"):
            c1, c2 = st.columns(2)
            new_modern = c1.number_input("سعر i-Modern", value=st.session_state.prices['i-Modern'])
            new_smart = c2.number_input("سعر i-Smart", value=st.session_state.prices['i-Smart'])
            new_elite = c1.number_input("سعر i-Elite", value=st.session_state.prices['i-Elite'])
            new_sig = c2.number_input("سعر i-Signature", value=st.session_state.prices['i-Signature'])
            
            if st.form_submit_button("تحديث الأسعار"):
                st.session_state.prices['i-Modern'] = new_modern
                st.session_state.prices['i-Smart'] = new_smart
                st.session_state.prices['i-Elite'] = new_elite
                st.session_state.prices['i-Signature'] = new_sig
                st.success("تم تحديث الأسعار للنظام الحالي!")

        st.markdown("---")
        
        # 2. Database View
        st.subheader("📂 قاعدة بيانات العملاء (CRM)")
        init_db()
        df = pd.read_csv(DB_FILE)
        st.dataframe(df, use_container_width=True)
        
        # Download Button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 تحميل البيانات (Excel/CSV)",
            csv,
            "intero_customers.csv",
            "text/csv",
            key='download-csv'
        )
        
        # Analytics
        if not df.empty:
            st.markdown("---")
            st.subheader("📊 إحصائيات سريعة")
            total_value = df['Total Estimate'].sum()
            st.metric("إجمالي قيمة العروض المقدمة", f"{total_value:,.0f} EGP")
    
    elif pwd:
        st.error("كلمة المرور غير صحيحة")

# --- Footer ---
st.markdown("<br><br><div style='text-align:center; color:#888; font-size:0.8rem;'>Powered by Infinity CDT Intelligence Engine</div>", unsafe_allow_html=True)
