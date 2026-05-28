// Mobile nav toggle
const toggle = document.getElementById("navToggle");
const links  = document.getElementById("navLinks");
if (toggle && links) {
  toggle.addEventListener("click", () => links.classList.toggle("open"));
}

// Reveal contact success banner when Formspree redirects back with ?sent=1
if (new URLSearchParams(location.search).get("sent") === "1") {
  document.querySelectorAll("[data-flash-on-sent]").forEach(el => el.removeAttribute("hidden"));
}

// Rewrite the Formspree _next field to an absolute URL on the current origin,
// so the thank-you redirect works on any domain (localhost, Pages, custom).
document.querySelectorAll("input[data-next-on-load]").forEach(el => {
  el.value = location.origin + "/contact/?sent=1";
});

// Scroll reveal
const observer = new IntersectionObserver(
  (entries) => entries.forEach(e => { if (e.isIntersecting) e.target.classList.add("visible"); }),
  { threshold: 0.12 }
);
document.querySelectorAll(".reveal").forEach(el => observer.observe(el));

// Demo tab switcher
(function () {
  const tabs   = document.querySelectorAll(".demo-tab");
  const panels = document.querySelectorAll(".demo-panel");
  if (!tabs.length) return;

  function show(id, animate) {
    tabs.forEach(t => t.classList.toggle("active", t.dataset.panel === id));
    panels.forEach(p => {
      if (p.id === "panel-" + id) {
        p.classList.remove("active", "is-animating");
        if (animate) {
          void p.offsetWidth; // force reflow so CSS animations restart
          p.classList.add("active", "is-animating");
        } else {
          p.classList.add("active");
        }
      } else {
        p.classList.remove("active", "is-animating");
      }
    });
  }

  // Show first panel statically on load — no animation until clicked
  show(tabs[0].dataset.panel, false);

  tabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      show(tab.dataset.panel, true);
    });
  });
})();
