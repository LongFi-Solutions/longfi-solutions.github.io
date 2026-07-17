(function () {
  var EXPECTED = window.LF_DOCS_EXPECTED, KEY = "lf-docs-gate", root = document.documentElement;
  var form = document.getElementById("lf-gate-form"), pw = document.getElementById("lf-gate-pw"), err = document.getElementById("lf-gate-err");
  if (!form) return;
  if (localStorage.getItem(KEY) === EXPECTED) root.classList.add("lf-unlocked");
  function sha(t){return crypto.subtle.digest("SHA-256", new TextEncoder().encode(t)).then(function(b){return Array.from(new Uint8Array(b)).map(function(x){return x.toString(16).padStart(2,"0");}).join("");});}
  form.addEventListener("submit", function (e) {
    e.preventDefault(); var v = pw.value || ""; if (!v) return;
    sha("longfi-docs:" + v).then(function (h) {
      if (h === EXPECTED) { try { localStorage.setItem(KEY, EXPECTED); } catch (_) {} root.classList.add("lf-unlocked"); }
      else { err.textContent = "That password is not correct."; }
    });
  });
  if (!root.classList.contains("lf-unlocked")) { try { pw.focus(); } catch (_) {} }
})();
