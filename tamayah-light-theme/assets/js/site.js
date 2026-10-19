/* Tamayah — shared micro-interactions (no dependencies)
   1. Header: scrolled state
   2. Mobile menu: toggle, Escape, close on link tap, scroll lock
   3. Scroll reveal: .reveal / .rule-draw via IntersectionObserver
   4. Scroll-spy: highlights the nav link of the section in view
   5. Counter: animates stage numbers (.count) when revealed
*/
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* 0. Image set: ?images=simple uses the minimal photo set ------------- */
  var set = new URLSearchParams(location.search).get("images");
  if (set === "simple") {
    document.querySelectorAll('img[src^="assets/img/"]').forEach(function (img) {
      img.src = img.getAttribute("src").replace("assets/img/", "assets/img/simple/");
    });
    document.querySelectorAll('a[href^="option-"], a[href="index.html"]').forEach(function (a) {
      a.href += (a.href.indexOf("?") > -1 ? "&" : "?") + "images=simple";
    });
  }

  /* 1. Header ------------------------------------------------------------ */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* 2. Mobile menu ------------------------------------------------------- */
  var toggle = document.querySelector(".nav__toggle");
  var menu = document.getElementById("menu");
  function setMenu(open) {
    if (!toggle || !menu) return;
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    menu.classList.toggle("is-open", open);
    menu.setAttribute("aria-hidden", String(!open));
    document.body.classList.toggle("menu-open", open);
  }
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      setMenu(toggle.getAttribute("aria-expanded") !== "true");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) setMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setMenu(false);
    });
    window.matchMedia("(min-width: 901px)").addEventListener("change", function (m) {
      if (m.matches) setMenu(false);
    });
  }

  /* 3. Scroll reveal ----------------------------------------------------- */
  var revealables = document.querySelectorAll(".reveal, .rule-draw");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -10% 0px", threshold: 0.12 }
    );
    revealables.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealables.forEach(function (el) {
      el.classList.add("in");
    });
  }

  /* 4. Scroll-spy -------------------------------------------------------- */
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav__link[href^="#"]'));
  var sections = links
    .map(function (a) {
      return document.querySelector(a.getAttribute("href"));
    })
    .filter(Boolean);
  if (sections.length && "IntersectionObserver" in window) {
    var current = null;
    var spy = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) current = entry.target.id;
        });
        links.forEach(function (a) {
          a.classList.toggle("is-active", a.getAttribute("href") === "#" + current);
        });
      },
      { rootMargin: "-35% 0px -55% 0px", threshold: 0 }
    );
    sections.forEach(function (s) {
      spy.observe(s);
    });
  }

  /* 5. Counters ---------------------------------------------------------- */
  var counters = document.querySelectorAll(".count");
  if (counters.length && "IntersectionObserver" in window && !reduceMotion) {
    var cio = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          cio.unobserve(entry.target);
          var el = entry.target;
          var target = parseInt(el.getAttribute("data-count") || el.textContent, 10);
          var pad = (el.getAttribute("data-count") || el.textContent).length;
          var start = null;
          function tick(ts) {
            if (!start) start = ts;
            var p = Math.min((ts - start) / 700, 1);
            var eased = 1 - Math.pow(1 - p, 3);
            var v = Math.max(1, Math.round(target * eased));
            el.textContent = String(v).padStart(pad, "0");
            if (p < 1) requestAnimationFrame(tick);
          }
          requestAnimationFrame(tick);
          /* safety: if frames never arrive (backgrounded tab), settle on the final value */
          setTimeout(function () {
            el.textContent = String(target).padStart(pad, "0");
          }, 900);
        });
      },
      { threshold: 0.5 }
    );
    counters.forEach(function (el) {
      el.setAttribute("data-count", el.textContent.trim());
      cio.observe(el);
    });
  }
})();
