<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Infinity CDT – Integrated Finishing System</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

  <!-- Meta Pixel -->
  <script>
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '1893075388269127');
    fbq('track', 'PageView');
  </script>

  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background: #fff;
      color: #111;
    }
    header {
      position: sticky;
      top: 0;
      background: #000;
      color: #fff;
      padding: 15px 30px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    header img {
      height: 45px;
    }
    .lang-toggle button {
      background: transparent;
      border: 1px solid gold;
      color: gold;
      padding: 5px 12px;
      cursor: pointer;
      margin-left: 5px;
    }
    section {
      padding: 60px 30px;
      max-width: 1100px;
      margin: auto;
    }
    h1, h2 {
      color: #000;
    }
    .gold {
      color: #b89b5e;
    }
    .packages {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
    }
    .card {
      border: 1px solid #ddd;
      padding: 20px;
      border-radius: 8px;
    }
    .cta {
      background: #b30000;
      color: #fff;
      padding: 12px 25px;
      border: none;
      font-size: 16px;
      cursor: pointer;
    }
    input, select {
      width: 100%;
      padding: 10px;
      margin-top: 10px;
    }
    footer {
      background: #000;
      color: #fff;
      padding: 30px;
      text-align: center;
    }
  </style>
</head>

<body>

<header>
  <div>
    <img src="logo.png" alt="Infinity CDT Logo"/>
  </div>
  <div class="lang-toggle">
    <button onclick="setLang('ar')">AR</button>
    <button onclick="setLang('en')">EN</button>
  </div>
</header>

<section id="hero">
  <h1 id="hero-title" class="gold">Integrated Finishing System</h1>
  <p id="hero-desc">
    Choose your package, calculate your cost, and let Infinity CDT handle the rest.
  </p>
</section>

<section>
  <h2 id="packages-title">5 Finishing Packages</h2>
  <div class="packages">
    <div class="card">Economic</div>
    <div class="card">Standard</div>
    <div class="card">Plus</div>
    <div class="card">Premium</div>
    <div class="card">Luxury</div>
  </div>
</section>

<section>
  <h2 id="calc-title">Cost Calculator</h2>

  <input id="name" placeholder="Name"/>
  <input id="phone" placeholder="Phone"/>
  <input id="area" type="number" placeholder="Area (m²)"/>

  <select id="location">
    <option>New Cairo</option>
    <option>Nasr City</option>
    <option>Heliopolis</option>
    <option>Maadi</option>
    <option>Madinaty</option>
    <option>El Shorouk</option>
    <option>El Rehab</option>
    <option>New Capital</option>
  </select>

  <select id="package">
    <option value="8000">Economic</option>
    <option value="10000">Standard</option>
    <option value="12000">Plus</option>
    <option value="15000">Premium</option>
    <option value="18000">Luxury</option>
  </select>

  <button class="cta" onclick="calculate()">Calculate & WhatsApp</button>

  <h3 id="result"></h3>
</section>

<footer>
  <p>
    Infinity CDT – Construction & Decoration<br/>
    WhatsApp: +2 01062796287
  </p>
</footer>

<script>
  let lang = 'en';

  const text = {
    en: {
      heroTitle: "Integrated Finishing System",
      heroDesc: "Choose your package, calculate your cost, and let Infinity CDT handle the rest.",
      packages: "5 Finishing Packages",
      calc: "Cost Calculator"
    },
    ar: {
      heroTitle: "نظام تشطيب متكامل",
      heroDesc: "اختار الباقة، احسب التكلفة، وسيب الباقي على Infinity CDT.",
      packages: "٥ باقات تشطيب",
      calc: "حاسبة التكلفة"
    }
  };

  function setLang(l) {
    lang = l;
    document.getElementById("hero-title").innerText = text[l].heroTitle;
    document.getElementById("hero-desc").innerText = text[l].heroDesc;
    document.getElementById("packages-title").innerText = text[l].packages;
    document.getElementById("calc-title").innerText = text[l].calc;
  }

  function calculate() {
    const area = document.getElementById("area").value;
    const rate = document.getElementById("package").value;
    const total = area * rate * 1.14;

    fbq('track', 'Lead');

    document.getElementById("result").innerText =
      "Estimated Total: " + total.toLocaleString() + " EGP";

    const msg =
`Client Name: ${name.value}
Phone: ${phone.value}
Area: ${area} m²
Location: ${location.value}
Package: ${package.options[package.selectedIndex].text}
Final Price: ${total.toLocaleString()} EGP`;

    window.location.href =
      "https://wa.me/201062796287?text=" + encodeURIComponent(msg);
  }
</script>

</body>
</html>
