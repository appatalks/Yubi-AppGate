/* Yubi AppGate – Minimal site JavaScript */
(function () {
  "use strict";

  /* ─── Mobile nav toggle ─────────────────────────────────────── */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");

  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
      toggle.setAttribute(
        "aria-expanded",
        links.classList.contains("open") ? "true" : "false"
      );
    });

    /* Close menu when a link is tapped */
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ─── FAQ accordion ─────────────────────────────────────────── */
  document.querySelectorAll(".faq-question").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.closest(".faq-item");
      var wasOpen = item.classList.contains("open");

      /* Close all siblings first */
      item.parentElement.querySelectorAll(".faq-item.open").forEach(function (el) {
        el.classList.remove("open");
      });

      if (!wasOpen) {
        item.classList.add("open");
      }
    });
  });

  /* ─── Scroll-triggered fade-in ──────────────────────────────── */
  var faders = document.querySelectorAll(".fade-in");

  if (faders.length && "IntersectionObserver" in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );

    faders.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    /* Fallback: show everything immediately */
    faders.forEach(function (el) {
      el.classList.add("visible");
    });
  }

  /* ─── Active nav link highlight ─────────────────────────────── */
  var path = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === path || (path === "" && href === "index.html")) {
      a.classList.add("active");
    }
  });
})();
