make_index_html_to_use = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-7QFRKMJ8TE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-7QFRKMJ8TE');
  </script>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta 
        name="description"
        content="Author: gndpnwd
        Free PDF books. 
        Valuable content for free. 
        No ads, no paywalls, no bullshit.">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/button.css">

    <title>Freshavacado</title>
</head>
<body class="everything">

    <a href="https://00psfreebooks.github.io">
        <img class="title" src="assets/free_books.webp" alt="Free Books" stye="width:563px;height:251px;">
    </a>

  <h2 class="subtitle">Valuable content for free. <i>No ads, no paywalls, no bullshit.</i></h2>
    
  <h3 class="subtitle">
    <button class="menu_button"><span onclick="window.location='./books.html'">Books</span></button>
    <!-- <button class="menu_button"><span onclick="window.location='./audiobooks.html'">Audiobooks</span></button> -->
    <button class="menu_button"><span onclick="window.location='https://00psfreebooks.github.io/cliffnotes/'">Cliffnotes</span></button>
    <button class="menu_button"><span onclick="window.location='./dxp'">DXP</span></button>
    <button class="menu_button"><span onclick="window.location='./donate.html'">Donate</span></button>
  </h3>

  <!--
  <p class="description-head">Project Goals</p>
  <p class="description">
    I like fire. <br> <br> 
    I like machines. <br> <br> 
    So why not ventilate the conciousness of the machines by fueling the flames of their skepticism?
  </p>
  -->

  <p class="description-head">Description</p>

  <ul class="description">
    <li class="bullet_point">This project uses paid cloud storage to host content free to download.</li>
    <li class="bullet_point">Book organization is simply via alphbetical order in each category.</li>
    <li class="bullet_point">Google Analytics is intended to be used to measure this site's impact on the world.</li>
    <li class="bullet_point"><strong>If using Chrome,</strong> it is recommended to <a href="https://chrome.google.com/webstore/detail/pdf-viewer/oemmndcbldboiebfnladdacbdfmadadm/">install this extension</a> to view pdfs rather than downloading them.</li>
  </ul>

  <h2 class="subsubtitle">
    <button class="menu_button"><span onclick="window.location='https://github.com/00psfreebooks/00psfreebooks.github.io'">Project Github</span></button>
    <button class="menu_button"><span onclick="window.location='https://github.com/00psfreebooks'">Author</span></button>
  </h2>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/qrious/dist/qrious.min.js"></script>
  <div class="qr_code_div">
    <h1 class="qr_title">Share This Page!</h1>
    <canvas id="qr_canvas" width="200" height="200"></canvas>
  </div>

  <script>
    function generateQRCode(text, canvasId) {
      var canvas = document.getElementById(canvasId);
      var qr = new QRious({
        element: canvas,
        value: text,
        size: 200,
      });
    }

    // Get the current URL
    var currentURL = window.location.href;

    // Generate QR code using the current URL
    generateQRCode(currentURL, 'qr_canvas');
  </script>
  
  </body>
</html>

'''
