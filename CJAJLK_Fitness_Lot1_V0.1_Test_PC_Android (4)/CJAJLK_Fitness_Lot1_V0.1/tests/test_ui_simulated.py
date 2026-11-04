"""Contrôle navigateur du rendu et des interactions avec IndexedDB simulé.
La politique de ce conteneur interdit la navigation HTTP en Chromium ; ce test injecte
l'interface dans about:blank, sans prétendre vérifier le service worker/offline réel.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
import re
import base64
BASE=Path(__file__).resolve().parents[1]
OUT=Path('/mnt/data/cjfitness_tests');OUT.mkdir(exist_ok=True)
html=(BASE/'index.html').read_text(encoding='utf-8')
html=re.sub(r'<script type="module"[^>]*></script>','',html)
html=re.sub(r'<link rel="stylesheet"[^>]*>',f'<style>{(BASE/"styles.css").read_text()}</style>',html)
icon=base64.b64encode((BASE/'assets/icon-192.png').read_bytes()).decode()
html=html.replace('./assets/icon-192.png',f'data:image/png;base64,{icon}')
# Stub simulates local IndexedDB transactional CRUD with asynchronous completion.
stub=r'''
(function(){
const stores={profiles:new Map(),health:new Map(),settings:new Map()};
const database={objectStoreNames:{contains:(name)=>stores[name]!=null},createObjectStore:(name)=>{stores[name]=new Map();},transaction:(names,mode)=>{
 const tx={oncomplete:null,onerror:null,onabort:null};let scheduled=false;
 const complete=()=>{if(!scheduled){scheduled=true;setTimeout(()=>tx.oncomplete?.(),0);}};
 tx.objectStore=name=>({
  get(key){const r={};queueMicrotask(()=>{r.result=stores[name].get(key);r.onsuccess?.();complete();});return r;},
  getAll(){const r={};queueMicrotask(()=>{r.result=[...stores[name].values()];r.onsuccess?.();complete();});return r;},
  put(value){const r={};queueMicrotask(()=>{const key=value.id??value.profileId??value.key;stores[name].set(key,structuredClone(value));r.result=key;r.onsuccess?.();complete();});return r;},
  delete(key){const r={};queueMicrotask(()=>{stores[name].delete(key);r.onsuccess?.();complete();});return r;},
  clear(){const r={};queueMicrotask(()=>{stores[name].clear();r.onsuccess?.();complete();});return r;}
 });return tx;}};
Object.defineProperty(window,'indexedDB',{configurable:true,value:{open(){const r={result:database};queueMicrotask(()=>r.onsuccess?.());return r;}}});
window.__mockStore=stores;
})();
'''
sources=[]
for name in ['src/db.js','src/backup.js','src/app.js']:
    source=(BASE/name).read_text(encoding='utf-8')
    source=re.sub(r'^import .*?;\s*$', '',source,flags=re.M)
    source=re.sub(r'\bexport\s+','',source)
    sources.append(source)
combined='\n'.join(sources)

def make_profile(page, name, health=False, dumbbell=False):
    if page.get_by_role('button',name='Créer mon premier profil').count():page.get_by_role('button',name='Créer mon premier profil').click()
    else:page.get_by_role('button',name='+ Profil').click()
    page.locator('#name').fill(name)
    page.get_by_role('button',name='Continuer').click()
    page.get_by_role('button',name='Continuer').click()
    if health:
        page.locator('#health-consent').check()
        page.locator('#weight').fill('80')
        page.locator('input[name=limitations][value=dos]').check()
    page.get_by_role('button',name='Continuer').click()
    if dumbbell:page.locator('input[name=equipment][value="haltères"]').check()
    page.get_by_role('button',name='Continuer').click()
    page.get_by_role('button',name='Enregistrer le profil').click()
    page.get_by_text('Bonjour, '+name).wait_for()

with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 c=b.new_context(viewport={'width':390,'height':844})
 page=c.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content(html)
 page.add_script_tag(content=stub)
 page.add_script_tag(content=combined)
 page.get_by_role('button',name='Créer mon premier profil').wait_for()
 page.screenshot(path=str(OUT/'01_welcome_mobile.png'),full_page=True)
 make_profile(page,'CJ',health=True,dumbbell=True)
 page.screenshot(path=str(OUT/'02_home_mobile.png'),full_page=True)
 page.get_by_role('button',name='Profil',exact=True).first.click()
 assert page.get_by_text('1 haltère(s) · 10 kg chacun').count()==1
 assert page.get_by_text('Précautions déclarées',exact=False).count()>0
 page.screenshot(path=str(OUT/'03_profile_mobile.png'),full_page=True)
 make_profile(page,'Invité')
 assert page.get_by_text('Bonjour, Invité').count()==1
 page.get_by_role('button',name='Profil',exact=True).first.click()
 page.locator('[data-switch]').first.click()
 page.get_by_role('button',name='Accueil',exact=True).first.click()
 page.get_by_text('Bonjour, CJ').wait_for()
 # Verify per-profile data and withdrawal of consent.
 page.get_by_role('button',name='Profil',exact=True).first.click()
 page.get_by_role('button',name='Modifier').click()
 page.get_by_role('button',name='Continuer').click()
 page.get_by_role('button',name='Continuer').click()
 page.locator('#health-consent').uncheck()
 page.get_by_role('button',name='Continuer').click()
 page.get_by_role('button',name='Continuer').click()
 page.get_by_role('button',name='Enregistrer le profil').click()
 page.get_by_role('button',name='Profil',exact=True).first.click()
 assert page.get_by_text('Aucune donnée de santé enregistrée').count()==1
 assert page.evaluate('window.__mockStore.health.size')==0
 page.get_by_role('button',name='Entraînements',exact=True).first.click()
 assert page.get_by_text('Pas encore activé').count()==3
 page.get_by_role('button',name='Progrès',exact=True).first.click()
 assert page.get_by_text('Aucune séance enregistrée').count()==1
 assert not errors,errors
 print('PASS — Chromium UI: création, navigation, 2 profils, 1 haltère 10 kg, consentement, révocation, absence de fausses séances (IndexedDB simulé)')
 c2=b.new_context(viewport={'width':1366,'height':900});p2=c2.new_page();p2.set_content(html);p2.add_script_tag(content=stub);p2.add_script_tag(content=combined);p2.get_by_role('button',name='Créer mon premier profil').wait_for();p2.screenshot(path=str(OUT/'04_welcome_desktop.png'),full_page=True)
 print('PASS — rendus mobile & desktop simulés capturés')
 c2.close();c.close();b.close()
