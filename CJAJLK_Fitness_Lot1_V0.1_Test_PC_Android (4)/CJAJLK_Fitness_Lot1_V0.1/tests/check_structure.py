from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'manifest.webmanifest').read_text())
assert manifest['display']=='standalone'
for asset in ['index.html','styles.css','src/app.js','src/db.js','src/backup.js','sw.js','assets/icon-192.png','assets/icon-512.png','manifest.webmanifest']:
 assert (ROOT/asset).is_file(),asset
sw=(ROOT/'sw.js').read_text()
for asset in ['src/app.js','src/db.js','src/backup.js','styles.css','index.html','assets/icon-192.png','assets/icon-512.png']:
 assert asset in sw,asset
source=(ROOT/'src/app.js').read_text()
assert 'serviceWorker' in source
assert 'no' in source and 'yes' in source
assert 'data-action="export"' in source
assert 'healthConsent' in source
assert 'Aucune séance enregistrée' in source
assert 'Pas encore activé' in source
assert not any(s in source for s in ['https://fonts.google','https://cdnjs.cloudflare','https://unpkg.com'])
print('PASS — ressources, manifest, cache hors ligne, consentement, export, affichage honnête du périmètre')
