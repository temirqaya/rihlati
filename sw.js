const CACHE = 'rihlati-v94';
const FILES = ['./', './index.html', './qt/', './qt/index.html', './tr/', './tr/index.html',
  './manifest.webmanifest', './icon-192.png', './icon-512.png', './apple-touch-icon.png', './favicon.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES))); self.skipWaiting(); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))); self.clients.claim(); });
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (url.origin !== self.location.origin) return;            // счётчик и прочие чужие адреса — без кэша
  if (/\/audio\//.test(url.pathname)) return;                   // звуки — напрямую из сети (iPhone и Range-запросы)
  const nav = e.request.mode === 'navigate' || /\.html?$|\/$/.test(url.pathname);
  const fresh = nav ? new Request(e.request.url, {cache: 'no-cache'}) : e.request;
  e.respondWith(fetch(fresh).then(r => { if (r.ok) { const copy = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); } return r; })
    .catch(() => caches.match(e.request, {ignoreSearch: true}).then(r => {
      if (r) return r;
      if (!nav) return Response.error();
      const lang = /\/qt\//.test(url.pathname) ? './qt/index.html' : /\/tr\//.test(url.pathname) ? './tr/index.html' : './index.html';
      return caches.match(lang);                                // без сети — страница своего языка
    })));
});
