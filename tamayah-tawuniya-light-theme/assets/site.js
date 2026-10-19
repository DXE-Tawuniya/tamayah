/* Tamayah (Tawuniya-aligned light option) — progressive enhancement.
   The page is fully readable and navigable without this file. */
(() => {
  const d = document, root = d.documentElement;
  root.classList.remove('no-js');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const $ = (s, c = d) => c.querySelector(s);
  const $$ = (s, c = d) => [...c.querySelectorAll(s)];

  /* remember language choice and keep the current section */
  $$('.lang a').forEach(a => a.addEventListener('click', () => {
    try { localStorage.setItem('tamayah-lang', a.getAttribute('hreflang')); } catch { /* storage unavailable */ }
    if (location.hash) a.href += location.hash;
  }));

  /* active menu item follows the visible section */
  const navLinks = $$('[data-nav-link]');
  const navSections = navLinks.map(a => $(a.getAttribute('href'))).filter(Boolean);
  if ('IntersectionObserver' in window && navSections.length) {
    const navObserver = new IntersectionObserver(entries => entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      navLinks.forEach(link => {
        if (link.getAttribute('href') === `#${entry.target.id}`) link.setAttribute('aria-current', 'true');
        else link.removeAttribute('aria-current');
      });
    }), { rootMargin: '-28% 0px -62% 0px', threshold: 0 });
    navSections.forEach(section => navObserver.observe(section));
  }

  /* header solid state */
  const header = $('.header');
  const onScroll = () => header && header.classList.toggle('is-solid', scrollY > 16);

  /* mobile drawer */
  const burger = $('.burger'), drawer = $('.drawer');
  if (burger && drawer) {
    const set = open => {
      burger.setAttribute('aria-expanded', open);
      drawer.classList.toggle('is-open', open);
      drawer.toggleAttribute('inert', !open);
      d.body.style.overflow = open ? 'hidden' : '';
      if (open) header.classList.add('is-solid');
      else onScroll();
    };
    drawer.setAttribute('inert', '');
    burger.addEventListener('click', () => set(burger.getAttribute('aria-expanded') !== 'true'));
    drawer.addEventListener('click', e => { if (e.target.closest('a')) set(false); });
    d.addEventListener('keydown', e => { if (e.key === 'Escape' && drawer.classList.contains('is-open')) { set(false); burger.focus(); } });
    matchMedia('(min-width:1180px)').addEventListener('change', e => e.matches && set(false));
  }

  /* reveal on scroll */
  const targets = $$('.rv');
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { threshold: .12, rootMargin: '0px 0px -6% 0px' });
    targets.forEach(t => io.observe(t));
  } else targets.forEach(t => t.classList.add('in'));

  /* claim lifeline: steps fill in sequence; pausable (WCAG 2.2.2) */
  const steps = $$('.step'), pp = $('.pp');
  if (steps.length) {
    let cur = 0, timer = 0, paused = reduce, visible = false;
    const paint = () => steps.forEach((s, i) => {
      s.classList.toggle('is-done', i < cur);
      s.classList.toggle('is-on', i === cur);
    });
    const tick = () => { cur = (cur + 1) % steps.length; paint(); };
    const run = () => {
      clearInterval(timer);
      if (!paused && visible && !d.hidden) timer = setInterval(tick, 2400);
    };
    if (reduce) cur = steps.length - 1;
    paint();
    if (pp && !reduce) {
      pp.hidden = false;
      const label = $('.sr-only', pp);
      pp.addEventListener('click', () => {
        paused = !paused;
        pp.setAttribute('aria-pressed', paused);
        label.textContent = paused ? pp.dataset.labelPlay : pp.dataset.labelPause;
        run();
      });
    }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([e]) => { visible = e.isIntersecting; run(); }, { threshold: .25 }).observe($('.steps'));
    } else { visible = true; run(); }
    d.addEventListener('visibilitychange', run);
  }

  /* counters */
  const fmt = new Intl.NumberFormat('en-US');
  $$('[data-count]').forEach(el => {
    const to = +el.dataset.count;
    if (reduce || !('IntersectionObserver' in window)) { el.textContent = fmt.format(to); return; }
    el.textContent = '0';
    const io = new IntersectionObserver(([e]) => {
      if (!e.isIntersecting) return; io.disconnect();
      const t0 = performance.now(), dur = 1800;
      const step = t => { const k = clamp((t - t0) / dur), v = 1 - Math.pow(1 - k, 4);
        el.textContent = fmt.format(Math.round(to * v)); if (k < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    }, { threshold: .6 });
    io.observe(el);
  });

  let ticking = false;
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(() => { ticking = false; onScroll(); }); } }, { passive: true });
  onScroll();
})();
