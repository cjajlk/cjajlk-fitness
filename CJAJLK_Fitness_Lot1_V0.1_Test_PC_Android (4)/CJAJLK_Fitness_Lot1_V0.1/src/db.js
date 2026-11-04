const NAME='cjajlk-fitness-v01';
const VERSION=1;
let databasePromise;
export function db(){
  if(!databasePromise){
    databasePromise=new Promise((resolve,reject)=>{
      const req=indexedDB.open(NAME,VERSION);
      req.onupgradeneeded=()=>{
        const d=req.result;
        if(!d.objectStoreNames.contains('profiles')) d.createObjectStore('profiles',{keyPath:'id'});
        if(!d.objectStoreNames.contains('health')) d.createObjectStore('health',{keyPath:'profileId'});
        if(!d.objectStoreNames.contains('settings')) d.createObjectStore('settings',{keyPath:'key'});
      };
      req.onsuccess=()=>resolve(req.result);
      req.onerror=()=>reject(req.error);
    }).catch(e=>{databasePromise=null;throw e;});
  }
  return databasePromise;
}
async function request(store,mode,fn){
  const d=await db();
  return new Promise((resolve,reject)=>{
    const tx=d.transaction(store,mode), object=tx.objectStore(store);
    let result;
    let request;
    try{request=fn(object); if(request) {request.onsuccess=()=>{result=request.result;};}} catch(e){reject(e);return;}
    tx.oncomplete=()=>resolve(result);
    tx.onerror=()=>reject(tx.error);
    tx.onabort=()=>reject(tx.error||new Error('Transaction annulée'));
  });
}
export const get=(store,key)=>request(store,'readonly',s=>s.get(key));
export const all=(store)=>request(store,'readonly',s=>s.getAll());
export const put=(store,value)=>request(store,'readwrite',s=>s.put(value));
export const remove=(store,key)=>request(store,'readwrite',s=>s.delete(key));
export async function setting(key,fallback=null){return (await get('settings',key))?.value ?? fallback;}
export const setSetting=(key,value)=>put('settings',{key,value});
export async function deleteProfile(id){
  const d=await db();
  return new Promise((resolve,reject)=>{
    const tx=d.transaction(['profiles','health'],'readwrite');
    tx.objectStore('profiles').delete(id);
    tx.objectStore('health').delete(id);
    tx.oncomplete=()=>resolve(); tx.onerror=()=>reject(tx.error);
  });
}
export async function snapshot(){return {schemaVersion:1,exportedAt:new Date().toISOString(),profiles:await all('profiles'),health:await all('health'),settings:await all('settings')};}
export async function replaceSnapshot(data){
  const d=await db();
  return new Promise((resolve,reject)=>{
    const tx=d.transaction(['profiles','health','settings'],'readwrite');
    for(const name of ['profiles','health','settings']) tx.objectStore(name).clear();
    for(const p of data.profiles) tx.objectStore('profiles').put(p);
    for(const h of data.health) tx.objectStore('health').put(h);
    for(const s of data.settings) tx.objectStore('settings').put(s);
    tx.oncomplete=()=>resolve();tx.onerror=()=>reject(tx.error);
  });
}
