// SpongeBob SquigglePants+ site: the screenshot slideshow and Patchy.
(function () {
  "use strict";
  var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Footer year
  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  // Slideshow in the gold frame: fades every few seconds, dots jump to a picture, hover pauses it
  var slides = document.querySelector(".slides");
  if (slides) {
    var pics = slides.querySelectorAll("img");
    var caption = document.getElementById("slide-caption");
    var dots = document.getElementById("dots");
    var current = 0, timer = null;
    function show(i) {
      pics[current].classList.remove("on");
      if (dots) dots.children[current].firstChild.removeAttribute("aria-current");
      current = (i + pics.length) % pics.length;
      pics[current].classList.add("on");
      if (dots) dots.children[current].firstChild.setAttribute("aria-current", "true");
      if (caption) caption.textContent = pics[current].getAttribute("data-caption") || "";
    }
    function play() {
      if (reduced) return;
      stop();
      timer = window.setInterval(function () { show(current + 1); }, 3500);
    }
    function stop() { if (timer) window.clearInterval(timer); timer = null; }
    if (dots) {
      Array.prototype.forEach.call(pics, function (pic, i) {
        var li = document.createElement("li");
        var b = document.createElement("button");
        b.type = "button";
        b.setAttribute("aria-label", "Show picture " + (i + 1) + ": " + (pic.getAttribute("data-caption") || pic.alt));
        b.addEventListener("click", function () { show(i); play(); });
        li.appendChild(b);
        dots.appendChild(li);
      });
    }
    show(0);
    play();
    var frame = slides.closest(".showcase") || slides;
    frame.addEventListener("mouseenter", stop);
    frame.addEventListener("mouseleave", play);
    frame.addEventListener("focusin", stop);
    frame.addEventListener("focusout", play);
  }

  // Patchy: rises up when seen; poking him wobbles him and he says something
  var spot = document.querySelector(".patchy-spot");
  if (spot) {
    var btn = spot.querySelector(".patchy");
    var bubble = spot.querySelector(".bubble");
    var lines = [
      "Ahoy, SpongeBob fans!",
      "Seven IconBob games, me hearties! Steer 'em with the D-Pad!",
      "Watch the credits to the very end, then look at the Options wall...",
      "100 percent! For real this time!",
      "Puzzle de Pants! It was lost at sea, and now it's found!",
      "Potty! Stop squawkin' and download it!",
      "Arrr, that tickles!"
    ];
    var n = 0, hide = null;
    function seen() { spot.classList.add("is-in"); }
    if ("IntersectionObserver" in window && !reduced) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) { seen(); io.disconnect(); } });
      }, { threshold: 0.15 });
      io.observe(spot);
    } else {
      seen();
    }
    btn.addEventListener("click", function () {
      btn.classList.remove("poked");
      void btn.offsetWidth; // restart the wobble
      if (!reduced) btn.classList.add("poked");
      bubble.textContent = lines[n % lines.length];
      n++;
      spot.classList.add("show-bubble");
      if (hide) window.clearTimeout(hide);
      hide = window.setTimeout(function () { spot.classList.remove("show-bubble"); }, 3200);
    });
  }
})();
