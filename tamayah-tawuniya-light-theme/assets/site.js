/* Tamayah (Tawuniya-aligned light option) — progressive enhancement.
   Without this file every panel is visible, links work and the form posts via mailto. */
(() => {
  const d = document, root = d.documentElement;
  const rtl = root.dir === 'rtl';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, c = d) => c.querySelector(s);
  const $$ = (s, c = d) => [...c.querySelectorAll(s)];
  const header = $('.header');

  /* ---------- Active section: nav state + language switch keeps the section ---------- */
  let currentSection = '';
  const navLinks = $$('[data-nav-link]');
  const tracked = $$('main section[id]');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => entries.forEach(e => {
      if (!e.isIntersecting) return;
      currentSection = e.target.id;
      navLinks.forEach(a => {
        if (a.getAttribute('href') === `#${currentSection}`) a.setAttribute('aria-current', 'true');
        else a.removeAttribute('aria-current');
      });
    }), { rootMargin: '-35% 0px -60% 0px' });
    tracked.forEach(s => io.observe(s));
  }
  $$('.lang a').forEach(a => a.addEventListener('click', () => {
    try { localStorage.setItem('tamayah-lang', a.getAttribute('hreflang')); } catch { /* storage unavailable */ }
    const hash = location.hash || (currentSection && currentSection !== 'top' ? `#${currentSection}` : '');
    if (hash) a.href = a.href.split('#')[0] + hash;
  }));

  /* ---------- Header: divider on scroll, desktop CTA after the hero ---------- */
  const onScroll = () => header.classList.toggle('is-solid', scrollY > 8);
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  const hero = $('.hero');
  if (hero && 'IntersectionObserver' in window) {
    new IntersectionObserver(([e]) => root.classList.toggle('past-hero', !e.isIntersecting), { rootMargin: '-120px 0px 0px 0px' }).observe(hero);
  } else root.classList.add('past-hero');

  /* ---------- Mobile menu: focus trap, Escape, focus restore ---------- */
  const burger = $('.burger'), drawer = $('#drawer');
  if (burger && drawer) {
    const outside = [$('main'), $('footer'), $('.brand'), $('.lang')].filter(Boolean);
    const focusables = () => [burger, ...$$('a, button', drawer)];
    const set = (open, restore) => {
      burger.setAttribute('aria-expanded', open);
      drawer.classList.toggle('is-open', open);
      drawer.toggleAttribute('inert', !open);
      outside.forEach(el => el.toggleAttribute('inert', open));
      d.body.style.overflow = open ? 'hidden' : '';
      if (open) $('a', drawer).focus();
      else if (restore) burger.focus();
    };
    drawer.setAttribute('inert', '');
    burger.addEventListener('click', () => set(burger.getAttribute('aria-expanded') !== 'true', true));
    drawer.addEventListener('click', e => { if (e.target.closest('a')) set(false, false); });
    d.addEventListener('keydown', e => {
      if (!drawer.classList.contains('is-open')) return;
      if (e.key === 'Escape') { e.preventDefault(); set(false, true); return; }
      if (e.key !== 'Tab') return;
      const f = focusables(), first = f[0], last = f[f.length - 1];
      if (e.shiftKey && d.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && d.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    matchMedia('(min-width:1180px)').addEventListener('change', e => e.matches && set(false, false));
  }

  /* ---------- Reveal once ---------- */
  const reveal = $$('.rv');
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { threshold: .12, rootMargin: '0px 0px -6% 0px' });
    reveal.forEach(t => io.observe(t));
  } else reveal.forEach(t => t.classList.add('in'));

  /* ---------- Counter (disabled for reduced motion) ---------- */
  const fmt = new Intl.NumberFormat('en-US');
  $$('[data-count]').forEach(el => {
    const to = +el.dataset.count;
    if (reduce || !('IntersectionObserver' in window)) return;
    el.textContent = '0';
    const io = new IntersectionObserver(([e]) => {
      if (!e.isIntersecting) return; io.disconnect();
      const t0 = performance.now(), dur = 1200;
      const step = t => { const k = Math.min(1, (t - t0) / dur), v = 1 - Math.pow(1 - k, 3);
        el.textContent = fmt.format(Math.round(to * v)); if (k < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    }, { threshold: .5 });
    io.observe(el);
  });

  /* ---------- Accessible tabs (audience explorer, journey explorer, care comparison) ---------- */
  const tabsets = [];
  $$('[data-tabs]').forEach(box => {
    const list = $('[role=tablist]', box);
    const tabs = $$('[role=tab]', list);
    const panels = tabs.map(t => d.getElementById(t.getAttribute('aria-controls')));
    const prefix = box.dataset.hash;
    const mobileOnly = 'mobileOnly' in box.dataset;
    let active = 0, enabled = true;

    const select = (i, { focus = false, hash = false } = {}) => {
      active = (i + tabs.length) % tabs.length;
      tabs.forEach((t, n) => {
        const on = n === active;
        t.setAttribute('aria-selected', on);
        t.tabIndex = on ? 0 : -1;
        t.classList.toggle('is-done', n < active);
        if (enabled) panels[n].hidden = !on;
      });
      box.style.setProperty('--p', tabs.length > 1 ? active / (tabs.length - 1) : 1);
      box.classList.toggle('is-complete', active === tabs.length - 1);
      if (focus) tabs[active].focus();
      if (hash && prefix) history.replaceState(null, '', `#${panels[active].id}`);
      if (hash && list.classList.contains('seg--scroll')) {  // user-initiated only: no scroll on load
        const t = tabs[active];
        list.scrollTo({ left: t.offsetLeft - list.offsetWidth / 2 + t.offsetWidth / 2, behavior: reduce ? 'auto' : 'smooth' });
      }
    };
    tabs.forEach((t, n) => t.addEventListener('click', () => select(n, { hash: true })));
    list.addEventListener('keydown', e => {
      const fwd = rtl ? 'ArrowLeft' : 'ArrowRight', back = rtl ? 'ArrowRight' : 'ArrowLeft';
      const map = { [fwd]: active + 1, [back]: active - 1, ArrowDown: active + 1, ArrowUp: active - 1, Home: 0, End: tabs.length - 1 };
      if (!(e.key in map)) return;
      e.preventDefault();
      select(map[e.key], { focus: true, hash: true });
    });
    $$('[data-step]', box).forEach(b => b.addEventListener('click', () => select(active + +b.dataset.step, { focus: true, hash: true })));

    const setEnabled = on => {
      enabled = on;
      panels.forEach((p, n) => {
        if (on) { p.setAttribute('role', 'tabpanel'); p.hidden = n !== active; }
        else { p.removeAttribute('role'); p.hidden = false; }
      });
    };
    if (mobileOnly) {
      const mq = matchMedia('(max-width:899.98px)');
      setEnabled(mq.matches);
      mq.addEventListener('change', e => setEnabled(e.matches));
    }
    const fromHash = () => {
      if (!prefix || !location.hash.startsWith(`#${prefix}`)) return false;
      const n = panels.findIndex(p => `#${p.id}` === location.hash);
      if (n < 0) return false;
      select(n);
      return true;
    };
    if (!fromHash()) select(0);
    tabsets.push(fromHash);
  });
  addEventListener('hashchange', () => tabsets.forEach(f => f()));
  // Panels are revealed by JS, so a deep link must scroll after tabs are wired
  if (location.hash) { const t = d.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }

  /* ---------- Enquiry form (mailto prototype — no data leaves the browser until the user sends it) ---------- */
  const form = $('#enquiry');
  if (form) {
    const ds = form.dataset;
    const roleSel = $('#role', form);
    $$('[data-audience]').forEach(a => a.addEventListener('click', () => { roleSel.value = a.dataset.audience; }));

    const emailOk = v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
    const rules = {
      name: v => v.trim() ? '' : ds.eName,
      org: v => v.trim() ? '' : ds.eOrg,
      role: v => v ? '' : ds.eRole,
      email: v => !v.trim() ? ds.eEmail : emailOk(v.trim()) ? '' : ds.eEmailFmt,
      phone: v => !v.trim() || /^\+?[0-9\s-]{6,}$/.test(v.trim()) ? '' : ds.ePhone,
      msg: v => v.trim() ? '' : ds.eMsg,
      consent: (v, el) => el.checked ? '' : ds.eConsent,
    };
    const check = id => {
      const el = d.getElementById(id), err = d.getElementById(`${id}-err`);
      const msg = rules[id](el.value, el);
      el.setAttribute('aria-invalid', msg ? 'true' : 'false');
      err.textContent = msg; err.hidden = !msg;
      return !msg;
    };
    Object.keys(rules).forEach(id => {
      const el = d.getElementById(id);
      el.addEventListener('blur', () => { if (el.dataset.touched || el.value) { el.dataset.touched = '1'; check(id); } });
      el.addEventListener('input', () => { if (el.getAttribute('aria-invalid') === 'true') check(id); });
      el.addEventListener('change', () => { if (el.getAttribute('aria-invalid') === 'true') check(id); });
    });
    const summary = $('.form__summary', form), ok = $('.form__ok', form);
    form.addEventListener('submit', e => {
      e.preventDefault();
      ok.textContent = '';
      const bad = Object.keys(rules).filter(id => !check(id));
      if (bad.length) {
        summary.textContent = bad.length === 1 ? ds.eSummary1 : ds.eSummary.replace('{n}', bad.length);
        summary.hidden = false;
        d.getElementById(bad[0]).focus();
        return;
      }
      summary.hidden = true;
      const v = id => d.getElementById(id).value.trim();
      const body = [['name', v('name')], ['org', v('org')], ['role', roleSel.selectedOptions[0].text], ['email', v('email')], ['phone', v('phone')], ['msg', v('msg')]]
        .filter(([, val]) => val).map(([k, val]) => `${ds[`l${k[0].toUpperCase()}${k.slice(1)}`]}: ${val}`).join('\n');
      location.href = `mailto:${ds.email}?subject=${encodeURIComponent(ds.subject)}&body=${encodeURIComponent(body)}`;
      ok.textContent = ds.ok;
    });
  }
})();
