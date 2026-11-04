const FORMAT='CJAJLK_FITNESS_BACKUP';
const ITERATIONS=180000;
const encoder=new TextEncoder(), decoder=new TextDecoder();
const to64=data=>{const bytes=new Uint8Array(data);let result='';for(let i=0;i<bytes.length;i+=8192)result+=String.fromCharCode(...bytes.subarray(i,i+8192));return btoa(result);};
const from64=text=>Uint8Array.from(atob(text),c=>c.charCodeAt(0));
async function aesKey(password,salt,usage){
  const secret=await crypto.subtle.importKey('raw',encoder.encode(password),'PBKDF2',false,['deriveKey']);
  return crypto.subtle.deriveKey({name:'PBKDF2',salt,iterations:ITERATIONS,hash:'SHA-256'},secret,{name:'AES-GCM',length:256},false,usage);
}
export async function encryptBackup(data,password){
  if(password.length<8)throw Error('Choisissez au moins 8 caractères pour le mot de passe de sauvegarde.');
  const salt=crypto.getRandomValues(new Uint8Array(16));
  const iv=crypto.getRandomValues(new Uint8Array(12));
  const key=await aesKey(password,salt,['encrypt']);
  const cipher=await crypto.subtle.encrypt({name:'AES-GCM',iv},key,encoder.encode(JSON.stringify(data)));
  return JSON.stringify({format:FORMAT,version:1,kdf:'PBKDF2-SHA256',iterations:ITERATIONS,cipher:'AES-256-GCM',salt:to64(salt),iv:to64(iv),data:to64(cipher)},null,2);
}
export async function decryptBackup(text,password){
  if(text.length>2_000_000)throw Error('Fichier de sauvegarde trop volumineux.');
  let body;
  try{body=JSON.parse(text)}catch{throw Error('Ce fichier ne contient pas une sauvegarde valide.');}
  if(body?.format!==FORMAT||body.version!==1||body.iterations!==ITERATIONS||typeof body.salt!=='string'||typeof body.iv!=='string'||typeof body.data!=='string')throw Error('Format de sauvegarde non reconnu.');
  try{
    const salt=from64(body.salt),iv=from64(body.iv);
    if(salt.length!==16||iv.length!==12)throw Error('Données invalides');
    const key=await aesKey(password,salt,['decrypt']);
    const plain=await crypto.subtle.decrypt({name:'AES-GCM',iv},key,from64(body.data));
    const out=JSON.parse(decoder.decode(plain));
    validateBackup(out);return out;
  }catch{throw Error('Mot de passe incorrect ou fichier corrompu. Aucune donnée n’a été modifiée.');}
}
export function validateBackup(data){
  if(!data||data.schemaVersion!==1||!Array.isArray(data.profiles)||!Array.isArray(data.health)||!Array.isArray(data.settings)||data.profiles.length>100||data.health.length>100||data.settings.length>50)throw Error('Structure de sauvegarde incompatible.');
  const ids=new Set();
  for(const p of data.profiles){
    if(!p||typeof p.id!=='string'||p.id.length>100||ids.has(p.id)||typeof p.name!=='string'||!p.name.trim()||p.name.length>70||!Array.isArray(p.goals)||!Array.isArray(p.equipment))throw Error('Profil de sauvegarde invalide.');
    ids.add(p.id);
  }
  for(const h of data.health){if(!h||!ids.has(h.profileId)||!Array.isArray(h.limitations))throw Error('Données de santé incohérentes.');}
  for(const s of data.settings){if(!s||typeof s.key!=='string'||s.key.length>100)throw Error('Paramètres incohérents.');}
}
