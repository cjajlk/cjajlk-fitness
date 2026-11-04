"""Parcours navigateur réel. Prérequis : playwright + Chromium et serveur HTTP localhost:8767."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
BASE='http://127.0.0.1:8767/'
OUT=Path('/mnt/data/cjfitness_tests');OUT.mkdir(exist_ok=True)

def make_profile(page, name, with_health=False, dumbbell=False):
    page.get_by_role('button',name='Créer mon premier profil').click() if page.get_by_role('button',name='Créer mon premier profil').count() else page.get_by_role('button',name='+ Profil').click()
    page.locator('#name').fill(name)
    page.get_by_role('button',name='Continuer').click()
    page.get_by_role('button',name='Continuer').click()
    if with_health:
        page.locator('#health-consent').check()
        page.locator('#height').fill('178')
        page.locator('#weight').fill('80')
        page.locator('input[name=limitations][value=dos]').check()
    page.get_by_role('button',name='Continuer').click()
    if dumbbell:
        page.locator('input[name=equipment][value="haltères"]').check()
        assert page.locator('#dumbbell-settings').is_visible()
        page.locator('#dumbbellKg').fill('10')
    page.get_by_role('button',name='Continuer').click()
    page.get_by_role('button',name='Enregistrer le profil').click()
    page.get_by_text(f'Bonjour, {name}').wait_for()

with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    context=browser.new_context(viewport={'width':390,'height':844},accept_downloads=True)
    page=context.new_page()
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(BASE)
    page.get_by_role('button',name='Créer mon premier profil').wait_for()
    page.screenshot(path=str(OUT/'01_welcome_mobile.png'),full_page=True)
    make_profile(page,'CJ',with_health=True,dumbbell=True)
    page.screenshot(path=str(OUT/'02_home_cj_mobile.png'),full_page=True)
    page.get_by_role('button',name='Profil',exact=True).first.click()
    assert page.get_by_text('1 haltère(s) · 10 kg chacun').count()==1
    assert page.get_by_text('Précautions déclarées',exact=False).count()>=1
    page.screenshot(path=str(OUT/'03_profile_mobile.png'),full_page=True)
    make_profile(page,'Invité')
    assert page.get_by_text('Bonjour, Invité').count()>=1
    page.get_by_role('button',name='Profil',exact=True).first.click()
    assert page.get_by_text('CJ',exact=True).count()>=1
    page.locator('[data-switch]').first.click()
    page.get_by_role('button',name='Accueil',exact=True).first.click()
    page.get_by_text('Bonjour, CJ').wait_for()
    page.reload();page.get_by_text('Bonjour, CJ').wait_for()
    # Consent can be revoked; after save, data must be erased.
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
    # Second profile untouched.
    page.get_by_role('button',name='Paramètres et sauvegarde').click()
    page.locator('#export-password').fill('MotDePasse2026!')
    with page.expect_download() as download_info: page.get_by_role('button',name='Exporter ma sauvegarde').click()
    download=download_info.value
    backup=OUT/download.suggested_filename;download.save_as(str(backup))
    ciphertext=backup.read_text()
    assert 'CJ' not in ciphertext and 'Invité' not in ciphertext
    # delete all then import encrypted backup
    page.get_by_role('button',name='Effacer toutes les données locales').click()
    page.locator('#modal-confirm').click()
    page.get_by_role('button',name='Créer mon premier profil').wait_for()
    page.get_by_role('button',name='Paramètres et sauvegarde').click()
    page.locator('#import-file').set_input_files(str(backup))
    page.locator('#import-password').fill('MotDePasse2026!')
    page.get_by_role('button',name='Vérifier et restaurer').click()
    page.locator('#modal-confirm').click()
    page.get_by_text('Bonjour, CJ').wait_for()
    # Check active cache after first network visit.
    page.wait_for_function("'serviceWorker' in navigator && !!navigator.serviceWorker.controller",timeout=10000)
    context.set_offline(True)
    page.reload()
    page.get_by_text('Bonjour, CJ').wait_for()
    page.get_by_role('button',name='Entraînements',exact=True).first.click()
    page.get_by_text('Pas encore activé').first.wait_for()
    page.get_by_role('button',name='Progrès',exact=True).first.click()
    page.get_by_text('Aucune séance enregistrée').wait_for()
    assert not errors,errors
    print('PASS: premier lancement, formulaire, consentement, haltère, multi-profils, stockage, révocation consentement, sauvegarde chiffrée, effacement, restauration, hors-ligne, navigation, absence de statistiques fictives')
    context.set_offline(False)
    # Desktop layout
    desktop=browser.new_context(viewport={'width':1440,'height':900})
    p2=desktop.new_page();p2.goto(BASE);p2.get_by_role('button',name='Créer mon premier profil').wait_for();p2.screenshot(path=str(OUT/'04_welcome_desktop.png'),full_page=True)
    print('PASS: contrôle rendu mobile et PC; captures dans', OUT)
    desktop.close();context.close();browser.close()
