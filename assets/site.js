/* Tamayah — progressive enhancement. The site is fully readable without this file. */
(() => {
  const d = document, root = d.documentElement;
  root.classList.remove('no-js');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const $ = (s, c = d) => c.querySelector(s);
  const $$ = (s, c = d) => [...c.querySelectorAll(s)];

  /* remember language choice */
  $$('.lang a').forEach(a => a.addEventListener('click', () => {
    try { localStorage.setItem('tamayah-lang', a.getAttribute('hreflang')); } catch (e) {}
  }));

  /* header solid state */
  const header = $('.header');
  const onScroll = () => header && header.classList.toggle('is-solid', scrollY > 24);

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
    matchMedia('(min-width:1040px)').addEventListener('change', e => e.matches && set(false));
  }

  /* reveal on scroll */
  const targets = $$('.rv, .val');
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { threshold: .14, rootMargin: '0px 0px -6% 0px' });
    targets.forEach(t => io.observe(t));
  } else targets.forEach(t => t.classList.add('in'));

  /* hero claim stack: cycles through the claim states */
  const stack = $('.stack');
  if (stack) {
    const cards = $$('.stack__card', stack), dots = $$('.stack__legend i', stack);
    let cur = 0;
    const paint = () => {
      cards.forEach((c, i) => c.dataset.pos = (i - cur + cards.length) % cards.length);
      dots.forEach((x, i) => x.classList.toggle('on', i === cur));
    };
    paint();
    if (!reduce) setInterval(() => { if (!d.hidden) { cur = (cur + 1) % cards.length; paint(); } }, 2800);
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
      const tick = t => { const k = clamp((t - t0) / dur), v = 1 - Math.pow(1 - k, 4);
        el.textContent = fmt.format(Math.round(to * v)); if (k < 1) requestAnimationFrame(tick); };
      requestAnimationFrame(tick);
    }, { threshold: .6 });
    io.observe(el);
  });

  /* scroll-linked: services pathway + CTA wing */
  const eco = $('.eco'), ecoRail = $('.eco__rail'), svcs = $$('.svc');
  const cta = $('.cta');
  const linked = () => {
    const vh = innerHeight;
    if (eco && ecoRail) {
      const r = ecoRail.getBoundingClientRect();
      const p = reduce ? 1 : clamp((vh * .78 - r.top) / (r.height * .9 + vh * .1));
      eco.style.setProperty('--p', p.toFixed(3));
      svcs.forEach((s, i) => s.classList.toggle('lit', reduce || p >= (i + .35) / svcs.length || s.getBoundingClientRect().top < vh * .55));
    }
    if (cta) {
      const r = cta.getBoundingClientRect();
      cta.style.setProperty('--p', reduce ? 1 : clamp((vh - r.top) / (vh * .9)).toFixed(3));
    }
  };

  /* hero pointer parallax */
  const par = $$('[data-par]');
  let mx = 0, my = 0, px = 0, py = 0, raf;
  if (par.length && !reduce && matchMedia('(pointer:fine)').matches) {
    addEventListener('pointermove', e => { mx = e.clientX / innerWidth - .5; my = e.clientY / innerHeight - .5; if (!raf) raf = requestAnimationFrame(loop); });
    const loop = () => {
      px += (mx - px) * .06; py += (my - py) * .06;
      par.forEach(el => { const k = +el.dataset.par; el.style.transform = `translate3d(${px * k}px,${py * k}px,0)`; });
      raf = (Math.abs(mx - px) > .001 || Math.abs(my - py) > .001) ? requestAnimationFrame(loop) : 0;
    };
  }

  let ticking = false;
  const frame = () => { ticking = false; onScroll(); linked(); };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }, { passive: true });
  addEventListener('resize', frame);
  frame();
})();
