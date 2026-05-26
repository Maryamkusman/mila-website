// Mobile nav toggle
const toggle = document.getElementById("navToggle");
const links  = document.getElementById("navLinks");
if (toggle && links) {
  toggle.addEventListener("click", () => links.classList.toggle("open"));
}

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
