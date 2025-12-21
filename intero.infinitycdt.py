<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Infinity CDT – Finishing Pricing System</title>

<!-- Google Font -->
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">

<style>
:root{
  --black:#0d0d0d;
  --gold:#d4af37;
  --gray:#f4f4f4;
}
*{box-sizing:border-box;font-family:'Cairo',sans-serif}
body{margin:0;background:#fff;color:#111}
header{text-align:center;padding:30px}
header img{max-width:220px}
.container{max-width:1100px;margin:auto;padding:20px}
.card{
  background:#fff;
  border-radius:16px;
  box-shadow:0 10px 30px rgba(0,0,0,.08);
  padding:25px;
  margin-bottom:25px
}
h2{margin-top:0}
.row{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
label{font-weight:600}
input,select{
  width:100%;padding:12px;border-radius:10px;
  border:1px solid #ccc;font-size:15px
}
button{
  background:var(--black);color:#fff;
  padding:14px;border:0;border-radius:12px;
  font-size:16px;cursor:pointer
}
button:hover{opacity:.9}
.result{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
  gap:15px
}
.box{
  background:var(--gray);
  border-radius:14px;
  padding:20px;
  text-align:center
}
.box h3{margin:5px 0}
.lang{text-align:right;margin-bottom:15px}
.footer{text-align:center;padding:20px;color:#666;font-size:14px}
</style>
</head>

<body>

<header>
  <img src="logo.png" alt="Infinity CDT">
  <h1>Infinity CDT – Finishing Pricing System</h1>
  <p>Construction & Decoration</p>
</header>

<div class="container">

<div class="lang">
<select id="lang" onchange="switchLang()">
  <option value="en">English</option>
  <option value="ar">العربية</option>
</select>
</div>

<div class="card">
<h2 id="t_project">Project Information</h2>
<div class="row">
  <div>
    <label id="t_area">Unit Area (m²)</label>
    <input type="number" id="area" value="100">
  </div>
  <div>
    <label id="t_package">Package</label>
    <select id="package"></select>
  </div>
</div>
</div>

<div class="card">
<h2 id="t_options">Optional Add-ons</h2>
<div class="row">
  <div><input type="checkbox" data-price="25000"> Kitchen</div>
  <div><input type="checkbox" data-price="60000"> Furniture</div>
  <div><input type="checkbox" data-price="50000"> Smart Home</div>
  <div><input type="checkbox" data-price="30000"> Landscape</div>
</div>
</div>

<div class="card">
<button onclick="calculate()">Calculate Price</button>
</div>

<div class="card">
<h2 id="t_result">Pricing Result</h2>
<div class="result">
  <div class="box"><h3 id="min">0</h3><p>Min</p></div>
  <div class="box"><h3 id="avg">0</h3><p>Average</p></div>
  <div class="box"><h3 id="max">0</h3><p>Max</p></div>
</div>
</div>

</div>

<div class="footer">
© Infinity CDT – Integrated Finishing System
</div>

<script>
// 🔗 Google Sheet CSV
const SHEET_URL = "PUT_YOUR_PUBLISHED_CSV_LINK_HERE";

let PACKAGES = {};
let LANG = "en";

fetch(SHEET_URL)
.then(r=>r.text())
.then(t=>{
  const rows = t.split("\n").slice(1);
  rows.forEach(r=>{
    const [key,en,ar,price] = r.split(",");
    PACKAGES[key]={en,ar,price:parseFloat(price)};
  });
  loadPackages();
});

function loadPackages(){
  const s=document.getElementById("package");
  s.innerHTML="";
  Object.keys(PACKAGES).forEach(k=>{
    const o=document.createElement("option");
    o.value=k;
    o.text=LANG==="ar"?PACKAGES[k].ar:PACKAGES[k].en;
    s.appendChild(o);
  });
}

function calculate(){
  const area=+document.getElementById("area").value;
  const pkg=PACKAGES[package.value].price*(area/100);
  let extras=0;
  document.querySelectorAll("input[type=checkbox]:checked")
  .forEach(c=>extras+=+c.dataset.price);

  const sub=pkg+extras;
  document.getElementById("avg").innerText=sub.toLocaleString()+" EGP";
  document.getElementById("min").innerText=(sub*.9).toLocaleString()+" EGP";
  document.getElementById("max").innerText=(sub*1.1).toLocaleString()+" EGP";
}

function switchLang(){
  LANG=document.getElementById("lang").value;
  loadPackages();
}
</script>

</body>
</html>
