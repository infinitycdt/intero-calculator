<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>Infinity CDT - Integrated Finishing System</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">

<style>
body{margin:0;font-family:'Cairo',sans-serif;background:#fff;color:#111}
header{text-align:center;padding:25px;border-bottom:1px solid #eee}
header img{max-width:200px}
.container{max-width:1200px;margin:auto;padding:20px}
.card{background:#fff;border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,.08);padding:25px;margin-top:20px}
.row{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
label{font-weight:600}
input,select{width:100%;padding:12px;border-radius:10px;border:1px solid #ccc}
button{background:#000;color:#fff;border:0;padding:14px 22px;border-radius:12px;font-size:16px;cursor:pointer}
button:hover{opacity:.9}
.summary-box{background:#f7f7f7;border-radius:12px;padding:12px;margin-bottom:8px}
.error{color:#b30000;font-weight:600}
footer{text-align:center;padding:30px;color:#666}
</style>
</head>

<body>

<header>
  <img src="logo.png" alt="Infinity CDT">
  <h1>Infinity CDT – نظام تشطيب متكامل</h1>
</header>

<div class="container">

<!-- بيانات العميل -->
<div class="card">
<h2>بيانات العميل</h2>
<div class="row">
  <div>
    <label>الاسم *</label>
    <input id="clientName">
  </div>
  <div>
    <label>رقم الموبايل *</label>
    <input id="clientPhone" placeholder="01XXXXXXXXX">
  </div>
  <div>
    <label>البريد الإلكتروني (اختياري)</label>
    <input id="clientEmail">
  </div>
  <div>
    <label>الموقع / المنطقة *</label>
    <select id="clientLocation">
      <option value="">اختر المنطقة</option>
      <option>مصر الجديدة</option>
      <option>مدينة نصر</option>
      <option>التجمع</option>
      <option>القطامية</option>
      <option>المعادي</option>
      <option>زهراء المعادي</option>
      <option>مدينتي</option>
      <option>الشروق</option>
      <option>الرحاب</option>
      <option>بدر</option>
      <option>العبور</option>
      <option>العاصمة الادارية</option>
    </select>
  </div>
</div>
<p id="zoneError" class="error"></p>
</div>

<!-- بيانات المشروع -->
<div class="card">
<h2>بيانات المشروع</h2>
<div class="row">
  <div>
    <label>المساحة (م²)</label>
    <input type="number" id="area" value="120">
  </div>
  <div>
    <label>الباقة</label>
    <select id="packageSelect">
      <option value="">جاري تحميل الباقات...</option>
    </select>
  </div>
</div>
</div>

<!-- إضافات -->
<div class="card">
<h2>إضافات اختيارية</h2>
<div class="row">
  <label><input type="checkbox" data-price="25000"> مطبخ</label>
  <label><input type="checkbox" data-price="60000"> فرش</label>
  <label><input type="checkbox" data-price="50000"> سمارت هوم</label>
  <label><input type="checkbox" data-price="30000"> لاندسكيب</label>
</div>
</div>

<div class="card">
<button onclick="calculate()">عرض السعر</button>
</div>

<!-- عرض السعر -->
<div class="card">
<h2>عرض سعر مخصص</h2>
<div id="quotation"></div>
<button onclick="sendWhatsApp()">إرسال على واتساب</button>
</div>

</div>

<footer>
© Infinity CDT – Construction & Decoration
</footer>

<script>
// ===== الإعدادات =====
const SHEET_URL = "PUT_YOUR_PUBLISHED_CSV_LINK_HERE";
const VAT = 0.14;

const ZONES = [
"مصر الجديدة","مدينة نصر","التجمع","القطامية","المعادي",
"زهراء المعادي","مدينتي","الشروق","الرحاب",
"بدر","العبور","العاصمة الادارية"
];

let PACKAGES = {};
let FINAL_TOTAL = 0;

// تحميل الباقات
fetch(SHEET_URL)
.then(res => res.text())
.then(csv => {
  const rows = csv.split("\n").slice(1);
  const select = document.getElementById("packageSelect");
  select.innerHTML = '<option value="">اختر الباقة</option>';

  rows.forEach(r=>{
    const [name, price] = r.split(",");
    if(name && price){
      PACKAGES[name.trim()] = Number(price);
      const opt = document.createElement("option");
      opt.value = name.trim();
      opt.textContent = `${name.trim()} - ${Number(price).toLocaleString()} ج/م²`;
      select.appendChild(opt);
    }
  });
});

// الحساب
function calculate(){
  const name = clientName.value.trim();
  const phone = clientPhone.value.trim();
  const location = clientLocation.value;
  const area = Number(document.getElementById("area").value);
  const pkg = packageSelect.value;

  if(!name || !phone || !location || !pkg){
    alert("من فضلك أكمل جميع البيانات الأساسية");
    return;
  }

  if(!ZONES.includes(location)){
    zoneError.innerText="نأسف، المنطقة خارج نطاق الخدمة";
    return;
  } else zoneError.innerText="";

  let extras = 0;
  document.querySelectorAll("input[type=checkbox]:checked")
    .forEach(e=>extras+=Number(e.dataset.price));

  const base = PACKAGES[pkg] * area;
  const subtotal = base + extras;
  const vat = subtotal * VAT;
  FINAL_TOTAL = subtotal + vat;

  quotation.innerHTML = `
    <div class="summary-box">الاسم: <b>${name}</b></div>
    <div class="summary-box">الموبايل: <b>${phone}</b></div>
    <div class="summary-box">المنطقة: <b>${location}</b></div>
    <div class="summary-box">الباقة: <b>${pkg}</b></div>
    <div class="summary-box">السعر الأساسي: <b>${base.toLocaleString()} ج</b></div>
    <div class="summary-box">الإضافات: <b>${extras.toLocaleString()} ج</b></div>
    <div class="summary-box">الضريبة: <b>${vat.toLocaleString()} ج</b></div>
    <div class="summary-box"><b>الإجمالي: ${FINAL_TOTAL.toLocaleString()} ج</b></div>
  `;
}

function sendWhatsApp(){
  if(!FINAL_TOTAL){alert("احسب السعر أولا");return;}
  const msg = quotation.innerText;
  window.open("https://wa.me/201062796287?text="+encodeURIComponent(msg));
}
</script>

</body>
</html>
