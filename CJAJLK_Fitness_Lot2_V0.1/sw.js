// Lot 2 : seules les ressources de cette copie sont mises en cache.
const PREFIX='cjajlk-fitness-lot2-'+encodeURIComponent(self.registration.scope)+'-';
const CACHE=PREFIX+'v1';
const FILES=['./','./index.html','./styles.css','./src/app.js','./src/db.js','./src/backup.js','./src/exercises.js','./src/library.js','./src/media.js','./manifest.webmanifest','./assets/icon-192.png','./assets/icon-512.png'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith(PREFIX)&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||new URL(e.request.url).origin!==self.location.origin||!e.request.url.startsWith(self.registration.scope))return;e.respondWith(caches.open(CACHE).then(c=>c.match(e.request).then(hit=>hit||fetch(e.request))));});
