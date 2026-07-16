(function () {
  var EXPECTED = window.LF_DOCS_EXPECTED, KEY = "lf-docs-gate", root = document.documentElement;
  if (!EXPECTED) return;
  if (localStorage.getItem(KEY) === EXPECTED) { root.classList.add("lf-unlocked"); return; }
  function sha(t){return crypto.subtle.digest("SHA-256", new TextEncoder().encode(t)).then(function(b){return Array.from(new Uint8Array(b)).map(function(x){return x.toString(16).padStart(2,"0");}).join("");});}
  function build() {
    if (document.getElementById("lf-gate")) return;
    var d = document.createElement("div"); d.id = "lf-gate";
    d.innerHTML =
      '<div class="lf-gate-card">' +
      '<img src="https://i.imgur.com/EY0cyDG.png" alt="LongFi Solutions" onerror="this.style.display=\'none\'"/>' +
      '<h1>LongFi Documentation</h1>' +
      '<p>Enter the password your LongFi contact gave you to view the documentation.</p>' +
      '<form id="lf-gate-form"><input id="lf-gate-pw" type="password" placeholder="Password" autocomplete="off" aria-label="Password" required />' +
      '<button type="submit">View documentation</button></form>' +
      '<div class="lf-gate-err" id="lf-gate-err"></div></div>';
    document.body.appendChild(d);
    var f = d.querySelector("#lf-gate-form"), pw = d.querySelector("#lf-gate-pw"), err = d.querySelector("#lf-gate-err");
    f.addEventListener("submit", function (e) {
      e.preventDefault(); var v = pw.value || ""; if (!v) return;
      sha("longfi-docs:" + v).then(function (h) {
        if (h === EXPECTED) { try { localStorage.setItem(KEY, EXPECTED); } catch (_) {} root.classList.add("lf-unlocked"); d.remove(); }
        else { err.textContent = "That password is not correct."; }
      });
    });
    pw.focus();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", build); else build();
})();
