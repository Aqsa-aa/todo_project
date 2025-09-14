const cacheName = 'todo-app-cache-v1';
const staticAssets = [
  '/',
  '/static/todo/styles.css',
  '/static/pwa/manifest.json'
];

// Install event
self.addEventListener('install', async e => {
  const cache = await caches.open(cacheName);
  await cache.addAll(staticAssets);
  return self.skipWaiting();
});

// Activate event
self.addEventListener('activate', e => {
  self.clients.claim();
});

// Fetch event
self.addEventListener('fetch', async e => {
  const req = e.request;
  const cache = await caches.open(cacheName);
  const cachedResponse = await cache.match(req);
  return cachedResponse || fetch(req);
});
