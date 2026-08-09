<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Diane's Bathroom Remodel Options | DJM Project Pro's</title>
<style>
  :root {
    --orange: #E85D04;
    --dark: #1a1a1a;
    --charcoal: #2d2d2d;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    background: var(--dark);
    color: #eee;
    line-height: 1.5;
  }
  .header {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    border-bottom: 4px solid var(--orange);
    padding: 28px 20px 22px;
    text-align: center;
  }
  .logo { font-size: 28px; font-weight: 800; letter-spacing: 1px; color: #fff; }
  .logo span { color: var(--orange); }
  .tagline { font-size: 13px; color: #aaa; margin-top: 4px; letter-spacing: 0.5px; }
  .project-info {
    background: var(--charcoal);
    padding: 16px 20px;
    display: flex; flex-wrap: wrap; justify-content: center; gap: 24px;
    font-size: 14px; border-bottom: 1px solid #333;
  }
  .project-info strong { color: var(--orange); }
  .intro {
    max-width: 900px; margin: 28px auto 10px; padding: 0 20px; text-align: center;
  }
  .intro h1 { font-size: 26px; font-weight: 700; margin-bottom: 8px; }
  .intro p { color: #bbb; font-size: 15px; }

  /* 3D Viewer CTA */
  .viewer-cta {
    max-width: 600px; margin: 24px auto; text-align: center;
  }
  .viewer-btn {
    display: inline-flex; align-items: center; gap: 10px;
    background: var(--orange); color: #fff; border: none;
    padding: 14px 28px; font-size: 16px; font-weight: 700;
    border-radius: 8px; cursor: pointer; transition: all 0.2s;
    box-shadow: 0 4px 20px rgba(232,93,4,0.35);
  }
  .viewer-btn:hover { background: #ff6b1a; transform: translateY(-2px); }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 22px; max-width: 1200px; margin: 28px auto 40px; padding: 0 18px;
  }
  .card {
    background: var(--charcoal); border-radius: 12px; overflow: hidden;
    border: 1px solid #3a3a3a; transition: transform 0.2s, border-color 0.2s;
  }
  .card:hover { transform: translateY(-4px); border-color: var(--orange); }
  .card img {
    width: 100%; height: 280px; object-fit: cover; display: block; cursor: pointer;
  }
  .card-body { padding: 16px 18px 20px; }
  .card-label {
    display: inline-block; background: var(--orange); color: #fff;
    font-size: 12px; font-weight: 700; padding: 3px 10px; border-radius: 4px;
    margin-bottom: 8px; letter-spacing: 0.5px;
  }
  .card h3 { font-size: 17px; font-weight: 700; margin-bottom: 6px; color: #fff; }
  .card p { font-size: 13.5px; color: #bbb; margin-bottom: 12px; }
  .features { list-style: none; font-size: 13px; color: #ccc; }
  .features li { padding: 3px 0; padding-left: 16px; position: relative; }
  .features li::before { content: "✓"; position: absolute; left: 0; color: var(--orange); font-weight: 700; }
  .select-btn {
    display: block; width: 100%; margin-top: 14px; padding: 11px;
    background: transparent; border: 2px solid var(--orange); color: var(--orange);
    font-weight: 700; font-size: 14px; border-radius: 6px; cursor: pointer; transition: all 0.2s;
  }
  .select-btn:hover, .select-btn.selected { background: var(--orange); color: #fff; }

  .footer {
    background: #111; border-top: 3px solid var(--orange);
    padding: 28px 20px; text-align: center;
  }
  .footer h3 { font-size: 18px; margin-bottom: 8px; }
  .footer p { color: #999; font-size: 14px; margin-bottom: 6px; }
  .contact { margin-top: 14px; font-size: 15px; }
  .contact a { color: var(--orange); text-decoration: none; font-weight: 600; }

  /* ========== 3D ROOM VIEWER OVERLAY ========== */
  #roomViewer {
    display: none; position: fixed; inset: 0; z-index: 200;
    background: #0a0a0a; flex-direction: column;
  }
  #roomViewer.active { display: flex; }
  .viewer-topbar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 12px 18px; background: #111; border-bottom: 2px solid var(--orange);
    flex-shrink: 0;
  }
  .viewer-topbar h2 { font-size: 16px; font-weight: 700; }
  .viewer-topbar .close-viewer {
    background: none; border: none; color: #fff; font-size: 28px;
    cursor: pointer; line-height: 1; padding: 0 6px;
  }
  #viewerCanvas {
    flex: 1; width: 100%; cursor: grab; touch-action: none;
  }
  #viewerCanvas:active { cursor: grabbing; }
  .viewer-controls {
    display: flex; align-items: center; justify-content: center; gap: 12px;
    padding: 14px 12px; background: #111; border-top: 1px solid #333;
    flex-shrink: 0; flex-wrap: wrap;
  }
  .viewer-controls button {
    background: #2a2a2a; border: 1px solid #444; color: #eee;
    padding: 8px 14px; border-radius: 6px; font-size: 13px; font-weight: 600;
    cursor: pointer; transition: all 0.15s;
  }
  .viewer-controls button:hover { border-color: var(--orange); color: var(--orange); }
  .viewer-controls button.active-opt {
    background: var(--orange); border-color: var(--orange); color: #fff;
  }
  .opt-thumbs {
    display: flex; gap: 8px; overflow-x: auto; padding: 4px 0;
  }
  .opt-thumbs img {
    width: 64px; height: 48px; object-fit: cover; border-radius: 4px;
    border: 2px solid transparent; cursor: pointer; flex-shrink: 0;
    transition: border-color 0.15s;
  }
  .opt-thumbs img.active { border-color: var(--orange); }
  .viewer-hint {
    position: absolute; bottom: 90px; left: 50%; transform: translateX(-50%);
    background: rgba(0,0,0,0.7); color: #ccc; font-size: 12px;
    padding: 6px 14px; border-radius: 20px; pointer-events: none;
    transition: opacity 0.5s;
  }
  .viewer-hint.fade { opacity: 0; }

  /* Simple lightbox for grid images */
  .lightbox {
    display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.92);
    z-index: 100; align-items: center; justify-content: center; padding: 20px;
  }
  .lightbox.active { display: flex; }
  .lightbox img { max-width: 95%; max-height: 90vh; border-radius: 8px; }
  .lightbox-close {
    position: absolute; top: 18px; right: 24px; font-size: 32px;
    color: #fff; cursor: pointer; background: none; border: none;
  }

  @media (max-width: 600px) {
    .card img { height: 220px; }
    .intro h1 { font-size: 22px; }
    .opt-thumbs img { width: 52px; height: 40px; }
  }
</style>
</head>
<body>

<div class="header">
  <div class="logo">DJM <span>Project Pro's</span></div>
  <div class="tagline">Carbon County Home Improvement • Licensed & Insured</div>
</div>

<div class="project-info">
  <div><strong>Client:</strong> Diane</div>
  <div><strong>Address:</strong> 120 S Lincoln Ave, Walnutport PA</div>
  <div><strong>Scope:</strong> Tub Surround + Countertop + Fixtures</div>
</div>

<div class="intro">
  <h1>Your Bathroom Remodel Options</h1>
  <p>All designs keep your existing layout: tub on the left, vanity on the right (stopping before the toilet), toilet in the back-right corner, and your light brown tile floor.</p>
</div>

<div class="viewer-cta">
  <button class="viewer-btn" onclick="openRoomViewer()">
    <span style="font-size:20px">◉</span> Enter Interactive 3D Room Viewer
  </button>
</div>

<div class="grid">
  <div class="card">
    <img src="optA.jpg" alt="Option A" onclick="openLightbox(this.src)">
    <div class="card-body">
      <span class="card-label">OPTION A</span>
      <h3>Acrylic Shelves + Speckled Quartz</h3>
      <p>Practical & clean. Built-in shelving, grab bar ready, warm beige tones.</p>
      <ul class="features">
        <li>Beige acrylic surround with deep shelves</li>
        <li>Cream tub + brushed nickel fixtures</li>
        <li>Speckled quartz counter + gold accents</li>
        <li>Easiest install & lowest maintenance</li>
      </ul>
      <button class="select-btn" onclick="selectOption(this,'A')">Select Option A</button>
    </div>
  </div>

  <div class="card">
    <img src="optB.jpg" alt="Option B" onclick="openLightbox(this.src)">
    <div class="card-body">
      <span class="card-label">OPTION B</span>
      <h3>White Marble + Chrome</h3>
      <p>Bright, modern, and timeless. Large-format marble look with black fixtures.</p>
      <ul class="features">
        <li>White marble tile surround + niche</li>
        <li>Matte black fixtures</li>
        <li>White marble countertop + chrome</li>
        <li>Bright, high-end look</li>
      </ul>
      <button class="select-btn" onclick="selectOption(this,'B')">Select Option B</button>
    </div>
  </div>

  <div class="card">
    <img src="optC.jpg" alt="Option C" onclick="openLightbox(this.src)">
    <div class="card-body">
      <span class="card-label">OPTION C</span>
      <h3>Cream Subway + Gold</h3>
      <p>Warm traditional-modern. Soft cream tile, almond tub, brushed gold.</p>
      <ul class="features">
        <li>Cream subway tile walls</li>
        <li>Almond/beige tub + gold fixtures</li>
        <li>Light stone counter + gold hardware</li>
        <li>Warm, inviting atmosphere</li>
      </ul>
      <button class="select-btn" onclick="selectOption(this,'C')">Select Option C</button>
    </div>
  </div>

  <div class="card">
    <img src="optD.jpg" alt="Option D" onclick="openLightbox(this.src)">
    <div class="card-body">
      <span class="card-label">OPTION D</span>
      <h3>Sage Green Tile + Speckled</h3>
      <p>Fresh modern color. Soft sage vertical tile with black fixtures + glass.</p>
      <ul class="features">
        <li>Sage green vertical tile</li>
        <li>Matte black fixtures + glass panel</li>
        <li>Speckled quartz counter + gold</li>
        <li>Trendy yet timeless</li>
      </ul>
      <button class="select-btn" onclick="selectOption(this,'D')">Select Option D</button>
    </div>
  </div>

  <div class="card">
    <img src="optE.jpg" alt="Option E" onclick="openLightbox(this.src)">
    <div class="card-body">
      <span class="card-label">OPTION E</span>
      <h3>Warm Taupe Stone + Niches</h3>
      <p>Spa-level. Large stone-look tile with multiple recessed LED niches.</p>
      <ul class="features">
        <li>Warm taupe large-format tile</li>
        <li>Multiple LED recessed niches</li>
        <li>Brushed nickel fixtures</li>
        <li>Speckled quartz counter + gold</li>
      </ul>
      <button class="select-btn" onclick="selectOption(this,'E')">Select Option E</button>
    </div>
  </div>

  <div class="card">
    <img src="optF.jpg" alt="Option F" onclick="openLightbox(this.src)">
    <div class="card-body">
      <span class="card-label">OPTION F</span>
      <h3>Cream Subway + Clear Glass</h3>
      <p>Clean and bright. Classic cream subway with clear glass panel.</p>
      <ul class="features">
        <li>Cream subway tile</li>
        <li>Clear glass shower panel</li>
        <li>Brushed nickel fixtures (matched)</li>
        <li>Speckled quartz counter</li>
      </ul>
      <button class="select-btn" onclick="selectOption(this,'F')">Select Option F</button>
    </div>
  </div>
</div>

<div class="footer">
  <h3>Ready to choose?</h3>
  <p>Use the 3D Room Viewer above or select an option, then text or call to lock it in.</p>
  <div class="contact">
    <p><strong>Dylan Mabe</strong> • DJM Project Pro's</p>
    <p><a href="tel:2723945428">(272) 394-5428</a> &nbsp;|&nbsp; <a href="mailto:djmprojectpro@gmail.com">djmprojectpro@gmail.com</a></p>
    <p style="margin-top:10px;font-size:13px;color:#777;">Walnutport • Lehighton • Jim Thorpe • Carbon County PA</p>
  </div>
</div>

<!-- Simple Lightbox -->
<div class="lightbox" id="lightbox" onclick="closeLightbox()">
  <button class="lightbox-close" onclick="closeLightbox()">&times;</button>
  <img id="lightbox-img" src="" alt="Full view">
</div>

<!-- ========== INTERACTIVE 3D ROOM VIEWER ========== -->
<div id="roomViewer">
  <div class="viewer-topbar">
    <h2 id="viewerTitle">Option A — Acrylic Shelves + Speckled Quartz</h2>
    <button class="close-viewer" onclick="closeRoomViewer()">&times;</button>
  </div>
  <canvas id="viewerCanvas"></canvas>
  <div class="viewer-hint" id="viewerHint">Drag to look around • Scroll to zoom • Use thumbs to switch options</div>
  <div class="viewer-controls">
    <div class="opt-thumbs" id="optThumbs">
      <img src="optA.jpg" data-opt="A" class="active" onclick="switchOption('A')" alt="A">
      <img src="optB.jpg" data-opt="B" onclick="switchOption('B')" alt="B">
      <img src="optC.jpg" data-opt="C" onclick="switchOption('C')" alt="C">
      <img src="optD.jpg" data-opt="D" onclick="switchOption('D')" alt="D">
      <img src="optE.jpg" data-opt="E" onclick="switchOption('E')" alt="E">
      <img src="optF.jpg" data-opt="F" onclick="switchOption('F')" alt="F">
    </div>
    <button onclick="resetCamera()">Reset View</button>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
  // ========== OPTIONS DATA ==========
  const OPTIONS = {
    A: { file: 'optA.jpg', title: 'Option A — Acrylic Shelves + Speckled Quartz' },
    B: { file: 'optB.jpg', title: 'Option B — White Marble + Chrome' },
    C: { file: 'optC.jpg', title: 'Option C — Cream Subway + Gold' },
    D: { file: 'optD.jpg', title: 'Option D — Sage Green Tile + Speckled' },
    E: { file: 'optE.jpg', title: 'Option E — Warm Taupe Stone + Niches' },
    F: { file: 'optF.jpg', title: 'Option F — Cream Subway + Clear Glass' }
  };

  let currentOpt = 'A';
  let scene, camera, renderer, plane, textureLoader;
  let isDragging = false, prevX = 0, prevY = 0;
  let rotY = 0, rotX = 0, targetRotY = 0, targetRotX = 0;
  let zoom = 1.0, targetZoom = 1.0;
  let animId = null;

  // ========== THREE.JS SETUP ==========
  function initViewer() {
    const canvas = document.getElementById('viewerCanvas');
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;

    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x0a0a0a);

    camera = new THREE.PerspectiveCamera(50, w / h, 0.1, 100);
    camera.position.set(0, 0, 2.4);

    renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
    renderer.setSize(w, h);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    textureLoader = new THREE.TextureLoader();

    // Room-like plane with subtle depth
    const geo = new THREE.PlaneGeometry(2.2, 3.6);
    const mat = new THREE.MeshBasicMaterial({ map: null });
    plane = new THREE.Mesh(geo, mat);
    scene.add(plane);

    // Soft ambient light (keeps image looking natural)
    const amb = new THREE.AmbientLight(0xffffff, 1.0);
    scene.add(amb);

    loadTexture(OPTIONS[currentOpt].file);
    setupControls(canvas);
    animate();
  }

  function loadTexture(file) {
    textureLoader.load(file, (tex) => {
      tex.minFilter = THREE.LinearFilter;
      tex.magFilter = THREE.LinearFilter;
      plane.material.map = tex;
      plane.material.needsUpdate = true;
    });
  }

  function setupControls(canvas) {
    // Mouse
    canvas.addEventListener('mousedown', e => {
      isDragging = true; prevX = e.clientX; prevY = e.clientY;
    });
    window.addEventListener('mouseup', () => isDragging = false);
    window.addEventListener('mousemove', e => {
      if (!isDragging) return;
      const dx = e.clientX - prevX;
      const dy = e.clientY - prevY;
      targetRotY += dx * 0.004;
      targetRotX += dy * 0.003;
      targetRotX = Math.max(-0.35, Math.min(0.35, targetRotX));
      targetRotY = Math.max(-0.55, Math.min(0.55, targetRotY));
      prevX = e.clientX; prevY = e.clientY;
      hideHint();
    });

    // Touch
    canvas.addEventListener('touchstart', e => {
      if (e.touches.length === 1) {
        isDragging = true;
        prevX = e.touches[0].clientX;
        prevY = e.touches[0].clientY;
      }
    }, { passive: true });
    canvas.addEventListener('touchend', () => isDragging = false);
    canvas.addEventListener('touchmove', e => {
      if (!isDragging || e.touches.length !== 1) return;
      const dx = e.touches[0].clientX - prevX;
      const dy = e.touches[0].clientY - prevY;
      targetRotY += dx * 0.004;
      targetRotX += dy * 0.003;
      targetRotX = Math.max(-0.35, Math.min(0.35, targetRotX));
      targetRotY = Math.max(-0.55, Math.min(0.55, targetRotY));
      prevX = e.touches[0].clientX;
      prevY = e.touches[0].clientY;
      hideHint();
    }, { passive: true });

    // Zoom
    canvas.addEventListener('wheel', e => {
      e.preventDefault();
      targetZoom += e.deltaY * -0.0012;
      targetZoom = Math.max(0.7, Math.min(2.2, targetZoom));
      hideHint();
    }, { passive: false });

    window.addEventListener('resize', onResize);
  }

  function onResize() {
    const canvas = document.getElementById('viewerCanvas');
    if (!renderer || !camera) return;
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  }

  function animate() {
    animId = requestAnimationFrame(animate);
    // Smooth damping
    rotY += (targetRotY - rotY) * 0.12;
    rotX += (targetRotX - rotX) * 0.12;
    zoom += (targetZoom - zoom) * 0.12;

    plane.rotation.y = rotY;
    plane.rotation.x = rotX;
    camera.position.z = 2.4 / zoom;
    renderer.render(scene, camera);
  }

  function hideHint() {
    const hint = document.getElementById('viewerHint');
    if (hint && !hint.classList.contains('fade')) {
      hint.classList.add('fade');
    }
  }

  // ========== PUBLIC API ==========
  function openRoomViewer(opt) {
    if (opt) currentOpt = opt;
    document.getElementById('roomViewer').classList.add('active');
    document.getElementById('viewerTitle').textContent = OPTIONS[currentOpt].title;
    document.body.style.overflow = 'hidden';

    // Highlight active thumb
    document.querySelectorAll('#optThumbs img').forEach(img => {
      img.classList.toggle('active', img.dataset.opt === currentOpt);
    });

    // Init Three.js on first open
    setTimeout(() => {
      if (!renderer) initViewer();
      else {
        loadTexture(OPTIONS[currentOpt].file);
        onResize();
      }
      // Reset camera
      targetRotY = 0; targetRotX = 0; targetZoom = 1.0;
      document.getElementById('viewerHint').classList.remove('fade');
    }, 50);
  }

  function closeRoomViewer() {
    document.getElementById('roomViewer').classList.remove('active');
    document.body.style.overflow = '';
    if (animId) { cancelAnimationFrame(animId); animId = null; }
  }

  function switchOption(letter) {
    currentOpt = letter;
    document.getElementById('viewerTitle').textContent = OPTIONS[letter].title;
    document.querySelectorAll('#optThumbs img').forEach(img => {
      img.classList.toggle('active', img.dataset.opt === letter);
    });
    loadTexture(OPTIONS[letter].file);
    // Gentle reset
    targetRotY = 0; targetRotX = 0;
  }

  function resetCamera() {
    targetRotY = 0; targetRotX = 0; targetZoom = 1.0;
  }

  // ========== GRID HELPERS ==========
  function openLightbox(src) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox').classList.add('active');
  }
  function closeLightbox() {
    document.getElementById('lightbox').classList.remove('active');
  }
  function selectOption(btn, letter) {
    document.querySelectorAll('.select-btn').forEach(b => {
      b.classList.remove('selected');
      b.textContent = 'Select Option ' + b.textContent.replace(/.*Option /, '');
    });
    btn.classList.add('selected');
    btn.textContent = '✓ Selected Option ' + letter;
  }

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      closeRoomViewer();
      closeLightbox();
    }
  });
</script>

</body>
</html>
