/* xSyphon — iFX EXPO Cyprus 2026 microsite
   Zero-dependency vanilla JS. All market data is illustrative (client-side simulation). */
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Live ticker (simulated random-walk quotes) ---------- */
  var instruments = [
    { sym: "EUR/USD", px: 1.16720, dp: 5 },
    { sym: "GBP/USD", px: 1.31840, dp: 5 },
    { sym: "USD/JPY", px: 160.215, dp: 3 },
    { sym: "AUD/USD", px: 0.62510, dp: 5 },
    { sym: "USD/CNH", px: 7.28400, dp: 4 },
    { sym: "XAU/USD", px: 4724.50, dp: 2 },
    { sym: "XAG/USD", px: 32.185, dp: 3 },
    { sym: "XAU/CNH", px: 1102.40, dp: 2 },
    { sym: "BTC/USD", px: 71240.0, dp: 1 }
  ];
  instruments.forEach(function (i) { i.base = i.px; i.chg = (Math.random() - 0.5) * 0.4; });

  function fmt(n, dp) {
    return n.toLocaleString("en-US", { minimumFractionDigits: dp, maximumFractionDigits: dp });
  }
  function tickEl(i) {
    var up = i.chg >= 0;
    return '<span class="tk"><span class="sym">' + i.sym + '</span>' +
      '<span class="px">' + fmt(i.px, i.dp) + '</span>' +
      '<span class="chg ' + (up ? "up" : "down") + '">' + (up ? "▲" : "▼") + " " + Math.abs(i.chg).toFixed(2) + "%</span></span>";
  }
  var track = document.getElementById("tickerTrack");
  function renderTicker() {
    if (!track) return;
    var html = instruments.map(tickEl).join("");
    track.innerHTML = html + html; // duplicate for seamless marquee loop
  }
  renderTicker();
  if (!reduce) {
    setInterval(function () {
      instruments.forEach(function (i) {
        var vol = i.base * 0.00018 + (i.dp <= 2 ? i.base * 0.0002 : 0);
        i.px = Math.max(0, i.px + (Math.random() - 0.5) * vol * 4);
        i.chg = ((i.px - i.base) / i.base) * 100;
      });
      renderTicker();
    }, 1600);
  }

  /* ---------- AI rotor ("Pricing · Execution · Liquidity · Risk") ---------- */
  var words = ["Pricing", "Execution", "Liquidity", "Risk", "Aggregation"];
  var rword = document.getElementById("rword"), wi = 0;
  if (rword && !reduce) {
    setInterval(function () {
      wi = (wi + 1) % words.length;
      rword.style.opacity = 0;
      setTimeout(function () { rword.textContent = words[wi]; rword.style.opacity = 1; }, 220);
    }, 2200);
    rword.style.transition = "opacity .25s ease";
  }

  /* ---------- Count-up stats ---------- */
  function countUp(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var prefix = el.getAttribute("data-prefix") || "";
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduce) { el.textContent = prefix + target + suffix; return; }
    var dur = 1100, start = performance.now();
    function step(now) {
      var t = Math.min(1, (now - start) / dur);
      var eased = 1 - Math.pow(1 - t, 3);
      var val = target % 1 === 0 ? Math.round(target * eased) : (target * eased).toFixed(1);
      el.textContent = prefix + val + suffix;
      if (t < 1) requestAnimationFrame(step);
      else el.textContent = prefix + target + suffix;
    }
    requestAnimationFrame(step);
  }

  /* ---------- Reveal on scroll + trigger counters ---------- */
  var counted = false;
  function fireCounters() {
    if (counted) return; counted = true;
    document.querySelectorAll(".stat .num[data-count]").forEach(countUp);
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
    var statsIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { fireCounters(); statsIo.disconnect(); } });
    }, { threshold: 0.3 });
    var statsEl = document.querySelector(".stats"); if (statsEl) statsIo.observe(statsEl);
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });
    fireCounters();
  }
  setTimeout(fireCounters, 1400); // safety for above-the-fold

  /* ---------- Aggregation engine canvas (anonymised LPs -> core -> YOU) ---------- */
  var canvas = document.getElementById("aggCanvas");
  if (canvas && !reduce) {
    var ctx = canvas.getContext("2d"), W, H, dpr, lps = [], particles = [], coreX, coreY, clientX, clientY;
    var coreFlash = 0, beam = 0, surge = 0, frame = 0, NLP = 12;
    function resize() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = canvas.clientWidth; H = canvas.clientHeight;
      canvas.width = W * dpr; canvas.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      coreX = W * 0.58; coreY = H * 0.5; clientX = W * 0.92; clientY = H * 0.5;
      lps = [];
      for (var i = 0; i < NLP; i++) {
        var t = i / (NLP - 1);
        lps.push({ x: W * (0.07 + 0.02 * Math.sin(t * 6.28)), y: H * 0.08 + t * H * 0.84, ph: Math.random() * 6.28 });
      }
    }
    function lerp(a, b, t) { return a + (b - a) * t; }
    function pos(p, t) { return [lerp(p.sx, p.tx, t), lerp(p.sy, p.ty, t)]; }
    function spawn(boost) {
      var src = lps[(Math.random() * lps.length) | 0];
      particles.push({ sx: src.x, sy: src.y, tx: coreX, ty: coreY, stage: 0, t: 0, sp: (boost ? 0.022 : 0.013) + Math.random() * 0.01 });
    }
    function draw() {
      frame++;
      ctx.clearRect(0, 0, W, H);
      // faint feed lines LP -> core
      ctx.lineWidth = 1;
      for (var a = 0; a < lps.length; a++) {
        ctx.strokeStyle = "rgba(61,220,108,0.07)";
        ctx.beginPath(); ctx.moveTo(lps[a].x, lps[a].y); ctx.lineTo(coreX, coreY); ctx.stroke();
      }
      // core -> client rail
      ctx.strokeStyle = "rgba(61,220,108,0.16)"; ctx.lineWidth = 1.4;
      ctx.beginPath(); ctx.moveTo(coreX, coreY); ctx.lineTo(clientX, clientY); ctx.stroke();

      // anonymised LP nodes (pulsing glowing dots, no labels)
      for (var b = 0; b < lps.length; b++) {
        var lp = lps[b], pr = 2.6 + Math.sin(frame * 0.05 + lp.ph) * 0.9;
        ctx.shadowColor = "rgba(61,220,108,0.9)"; ctx.shadowBlur = 8;
        ctx.fillStyle = "rgba(120,235,160,0.9)";
        ctx.beginPath(); ctx.arc(lp.x, lp.y, pr, 0, 7); ctx.fill();
        ctx.shadowBlur = 0;
      }

      // comet particles with glowing trails
      for (var k = particles.length - 1; k >= 0; k--) {
        var p = particles[k]; p.t += p.sp;
        if (p.t >= 1) {
          if (p.stage === 0) { p.stage = 1; p.sx = coreX; p.sy = coreY; p.tx = clientX; p.ty = clientY; p.t = 0; p.sp = 0.05 + Math.random() * 0.02; coreFlash = 1; beam = 1; }
          else { particles.splice(k, 1); continue; }
        }
        var h = pos(p, p.t), tl = pos(p, Math.max(0, p.t - (p.stage ? 0.18 : 0.1)));
        var grd = ctx.createLinearGradient(tl[0], tl[1], h[0], h[1]);
        var c = p.stage ? "92,232,128" : "61,220,108";
        grd.addColorStop(0, "rgba(" + c + ",0)"); grd.addColorStop(1, "rgba(" + c + ",0.9)");
        ctx.strokeStyle = grd; ctx.lineWidth = p.stage ? 2.4 : 1.6; ctx.lineCap = "round";
        ctx.beginPath(); ctx.moveTo(tl[0], tl[1]); ctx.lineTo(h[0], h[1]); ctx.stroke();
        ctx.shadowColor = "rgba(" + c + ",0.9)"; ctx.shadowBlur = 10;
        ctx.fillStyle = "rgba(200,255,215,0.95)";
        ctx.beginPath(); ctx.arc(h[0], h[1], p.stage ? 2.4 : 1.8, 0, 7); ctx.fill();
        ctx.shadowBlur = 0;
      }

      // purification flash ring at core
      if (coreFlash > 0.01) {
        ctx.strokeStyle = "rgba(140,255,180," + coreFlash + ")"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(coreX, coreY, 16 + (1 - coreFlash) * 30, 0, 7); ctx.stroke();
        coreFlash *= 0.9;
      }
      // sharp output beam core -> client
      if (beam > 0.01) {
        ctx.strokeStyle = "rgba(150,255,190," + beam + ")"; ctx.lineWidth = 2.5;
        ctx.shadowColor = "rgba(92,232,128,0.9)"; ctx.shadowBlur = 16;
        ctx.beginPath(); ctx.moveTo(coreX, coreY); ctx.lineTo(clientX, clientY); ctx.stroke();
        ctx.shadowBlur = 0; beam *= 0.86;
      }

      // glowing core
      var cr = 15 + coreFlash * 8;
      var g = ctx.createRadialGradient(coreX, coreY, 2, coreX, coreY, cr + 24);
      g.addColorStop(0, "rgba(120,255,160,0.95)"); g.addColorStop(0.4, "rgba(61,220,108,0.5)"); g.addColorStop(1, "rgba(61,220,108,0)");
      ctx.fillStyle = g; ctx.beginPath(); ctx.arc(coreX, coreY, cr + 24, 0, 7); ctx.fill();
      ctx.save(); ctx.translate(coreX, coreY); ctx.rotate(frame * 0.01);
      ctx.strokeStyle = "rgba(92,232,128,0.7)"; ctx.lineWidth = 1.4;
      ctx.beginPath(); ctx.arc(0, 0, 18, 0.4, 2.6); ctx.stroke();
      ctx.beginPath(); ctx.arc(0, 0, 18, 3.6, 5.8); ctx.stroke(); ctx.restore();
      ctx.fillStyle = "#04140a"; ctx.strokeStyle = "rgba(140,255,180,0.95)"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(coreX, coreY, 12, 0, 7); ctx.fill(); ctx.stroke();
      ctx.fillStyle = "#7fffb0"; ctx.font = "bold 12px ui-monospace, monospace"; ctx.textAlign = "center";
      ctx.fillText("X", coreX, coreY + 4);

      // client node
      ctx.strokeStyle = "rgba(120,235,160,0.85)"; ctx.fillStyle = "rgba(10,16,12,0.92)"; ctx.lineWidth = 1.6;
      ctx.beginPath(); ctx.arc(clientX, clientY, 12, 0, 7); ctx.fill(); ctx.stroke();
      ctx.fillStyle = "rgba(233,245,236,0.95)"; ctx.font = "9px ui-monospace, monospace"; ctx.textAlign = "center";
      ctx.fillText("YOU", clientX, clientY + 3);

      // periodic surge for drama
      if (surge > 0) { if (frame % 2 === 0) { spawn(true); surge--; } }
      requestAnimationFrame(draw);
    }
    resize(); window.addEventListener("resize", resize);
    setInterval(function () { spawn(false); }, 150);
    setInterval(function () { surge += 10; }, 4200); // convergence burst every few seconds
    // initial convergence burst when the section first scrolls into view
    if ("IntersectionObserver" in window) {
      var burstIo = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { surge += 22; burstIo.disconnect(); } });
      }, { threshold: 0.3 });
      burstIo.observe(canvas);
    }
    for (var s = 0; s < 8; s++) spawn(false);
    draw();
  }

  /* ---------- Hero particle field (deep-liquidity drift) ---------- */
  var hc = document.getElementById("heroCanvas");
  if (hc && !reduce) {
    var hx = hc.getContext("2d"), hw, hh, hdpr, motes = [];
    function hresize() {
      hdpr = Math.min(window.devicePixelRatio || 1, 2);
      hw = hc.clientWidth; hh = hc.clientHeight;
      hc.width = hw * hdpr; hc.height = hh * hdpr; hx.setTransform(hdpr, 0, 0, hdpr, 0, 0);
      var n = Math.min(70, Math.round(hw * hh / 16000));
      motes = [];
      for (var i = 0; i < n; i++) motes.push({ x: Math.random() * hw, y: Math.random() * hh, r: Math.random() * 1.6 + 0.4, s: Math.random() * 0.25 + 0.05, a: Math.random() * 0.5 + 0.1 });
    }
    function hdraw() {
      hx.clearRect(0, 0, hw, hh);
      for (var i = 0; i < motes.length; i++) {
        var m = motes[i]; m.y -= m.s; m.x += Math.sin((m.y + i) * 0.01) * 0.18;
        if (m.y < -4) { m.y = hh + 4; m.x = Math.random() * hw; }
        hx.fillStyle = "rgba(61,220,108," + m.a + ")";
        hx.beginPath(); hx.arc(m.x, m.y, m.r, 0, 7); hx.fill();
      }
      requestAnimationFrame(hdraw);
    }
    hresize(); window.addEventListener("resize", hresize); hdraw();
  }

  /* ---------- Decode / scramble headline ---------- */
  (function () {
    var head = document.getElementById("decodeHead");
    if (!head) return;
    var lines = head.querySelectorAll(".line");
    if (reduce) { lines.forEach(function (l) { l.textContent = l.getAttribute("data-text"); }); return; }
    var chars = "ABCDEFGHJKLMNPRSTUVWXYZ0123456789#$%&/<>";
    lines.forEach(function (line, li) {
      var target = line.getAttribute("data-text"), len = target.length, revealed = 0;
      var delay = li * 360;
      setTimeout(function () {
        var iv = setInterval(function () {
          var out = "";
          for (var i = 0; i < len; i++) {
            if (i < revealed || target[i] === " ") out += target[i];
            else out += '<span class="scramble">' + chars[(Math.random() * chars.length) | 0] + "</span>";
          }
          line.innerHTML = out;
          revealed += 1;
          if (revealed > len) { clearInterval(iv); line.textContent = target; }
        }, 38);
      }, delay);
    });
  })();

  /* ---------- Parallax tilt on hero stat cards ---------- */
  (function () {
    var box = document.getElementById("statTilt");
    if (!box || reduce) return;
    var cards = box.querySelectorAll(".stat");
    function tilt(rx, ry, px, py) {
      cards.forEach(function (c) {
        c.style.transform = "rotateX(" + rx + "deg) rotateY(" + ry + "deg)";
        var gl = c.querySelector(".glow"); if (gl) { gl.style.setProperty("--mx", px + "%"); gl.style.setProperty("--my", py + "%"); }
      });
    }
    box.addEventListener("mousemove", function (e) {
      var r = box.getBoundingClientRect();
      var dx = (e.clientX - r.left) / r.width - 0.5, dy = (e.clientY - r.top) / r.height - 0.5;
      tilt((-dy * 8).toFixed(2), (dx * 10).toFixed(2), ((dx + 0.5) * 100).toFixed(0), ((dy + 0.5) * 100).toFixed(0));
    });
    box.addEventListener("mouseleave", function () { tilt(0, 0, 50, 0); });
    if (window.DeviceOrientationEvent) {
      window.addEventListener("deviceorientation", function (ev) {
        if (ev.gamma == null) return;
        var ry = Math.max(-10, Math.min(10, ev.gamma / 4)), rx = Math.max(-8, Math.min(8, (ev.beta - 45) / 5));
        tilt((-rx).toFixed(2), ry.toFixed(2), 50, 0);
      });
    }
  })();

  /* ---------- Config injection (placeholders -> real values when known) ---------- */
  var CONFIG = window.XSYPHON_CONFIG || {};
  if (CONFIG.formEndpoint) document.getElementById("leadForm").setAttribute("action", CONFIG.formEndpoint);
  if (CONFIG.calendlyUrl) {
    var bc = document.getElementById("bookCal"); if (bc) bc.setAttribute("href", CONFIG.calendlyUrl);
  }

  /* ---------- Lead form (Formspree AJAX + offline mailto fallback) ---------- */
  var form = document.getElementById("leadForm"), msg = document.getElementById("formMsg");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var action = form.getAttribute("action") || "";
      var data = new FormData(form);
      function showOK() { msg.className = "form-msg ok"; msg.textContent = "Thank you — our liquidity desk will be in touch within 24 hours."; form.reset(); }
      function showErr(t) { msg.className = "form-msg err"; msg.textContent = t; }
      // Not configured yet, or offline -> mailto fallback
      if (action.indexOf("FORMSPREE_ID") !== -1 || !navigator.onLine) {
        var body = "";
        data.forEach(function (v, k) { if (v) body += k + ": " + v + "\n"; });
        window.location.href = "mailto:" + (CONFIG.fallbackEmail || "desk@xsyphon.com") +
          "?subject=" + encodeURIComponent("iFX EXPO Cyprus 2026 lead") + "&body=" + encodeURIComponent(body);
        msg.className = "form-msg ok"; msg.textContent = "Opening your email app to send us your details…";
        return;
      }
      var btn = form.querySelector("button[type=submit]"); var orig = btn.textContent; btn.textContent = "Sending…"; btn.disabled = true;
      fetch(action, { method: "POST", body: data, headers: { Accept: "application/json" } })
        .then(function (r) { if (r.ok) showOK(); else r.json().then(function (j) { showErr((j.errors && j.errors[0] && j.errors[0].message) || "Something went wrong — please try again."); }); })
        .catch(function () { showErr("Network issue — please try again, or email desk@xsyphon.com."); })
        .then(function () { btn.textContent = orig; btn.disabled = false; });
    });
  }

  /* ---------- Proof of speed: "Ping Syphon Core" (illustrative) ---------- */
  (function () {
    var btn = document.getElementById("pingBtn");
    if (!btn) return;
    var log = document.getElementById("pingLog"), prog = document.getElementById("pingProg"),
        bar = prog ? prog.querySelector("i") : null, res = document.getElementById("pingResult"),
        rLat = document.getElementById("rLat"), rSlip = document.getElementById("rSlip"),
        rRoute = document.getElementById("rRoute"), rStatus = document.getElementById("rStatus");
    var busy = false;
    function line(html) { log.innerHTML = html; }
    function run() {
      if (busy) return; busy = true;
      btn.disabled = true; btn.textContent = "Routing…";
      res.classList.remove("show");
      prog.style.display = "block"; bar.style.width = "0%";
      var lat = (4.6 + Math.random() * 0.6).toFixed(1);   // 4.6 - 5.2 ms
      var n = 12;
      var steps = [
        '<span class="dim">$ route --order EURUSD 5.0M --mode best</span>',
        'connecting to ' + n + ' tier-1 sources…',
        'aggregating depth-of-book…',
        'filtering <span class="ok">last-look = 0</span> · selecting best bid/offer…',
        'executing via Syphon Core…'
      ];
      var i = 0;
      var iv = setInterval(function () {
        line(steps.slice(0, i + 1).join("\n"));
        bar.style.width = Math.min(100, (i + 1) / steps.length * 100) + "%";
        i++;
        if (i >= steps.length) {
          clearInterval(iv);
          setTimeout(function () {
            bar.style.width = "100%";
            rLat.textContent = lat + "ms"; rSlip.textContent = "0.0"; rRoute.textContent = n + " LPs";
            rStatus.textContent = "Filled"; res.classList.add("show");
            line(steps.join("\n") + '\n<span class="ok">✓ filled — best execution, zero slippage.</span>');
            btn.disabled = false; btn.textContent = "▸ Ping again"; busy = false;
          }, 380);
        }
      }, 320);
    }
    btn.addEventListener("click", run);
  })();

  /* ---------- Register service worker for offline use ---------- */
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () { navigator.serviceWorker.register("sw.js").catch(function () {}); });
  }
})();
