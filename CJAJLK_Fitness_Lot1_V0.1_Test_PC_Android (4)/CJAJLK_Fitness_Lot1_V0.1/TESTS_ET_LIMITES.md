# CJAJLK Fitness — Rapport de vérification du Lot 1

**Date : 02/11/2026 — Statut : prototype pour tests locaux.**

## Vérifications réussies

- Analyse de syntaxe des modules JavaScript via Node (`node --check`) : OK.
- Contrôle des fichiers attendus, manifest PWA, service worker, ressources locales, absence de CDN : OK.
- Cinq tests automatisés sur la sauvegarde chiffrée : aller-retour, mauvaise clé, mot de passe trop court, structure invalide, volumétrie : **5/5 OK**.
- Vérification visuelle et interactive avec Chromium et un stockage simulé : **OK** pour le lancement, l'interface responsive, l'assistant de création, deux profils, un haltère de 10 kg, consentement et retrait du consentement, navigation et indicateurs honnêtes non remplis.
- Captures internes générées : accueil mobile, profil, accueil PC.

## Tests encore obligatoires avant validation définitive

- Test réel IndexedDB / rechargement de navigateur : **non vérifié ici**.
- Test du service worker en mode avion / PWA installée : **non vérifié ici**.
- Export/import via téléchargements du navigateur sur Windows et Android : **non vérifié ici** (chiffrement et déchiffrement du module validés).
- Essai sur Samsung réel, contraste, lisibilité, clavier virtuel et ergonomie tactile : **à faire**.
- Publication GitHub Pages : **non effectuée**.
- Tests complets du cahier des charges (20 cas) : **non effectués**, ils incluent les Lots 2 à 6.

## Précision sur les tests Chromium

La politique de l'environnement de test interdit toute navigation URL dans Chromium, y compris `localhost`. Pour contrôler l'interface, les fichiers HTML/CSS/JS ont été injectés directement et IndexedDB a été simulé en mémoire. Ces tests permettent de repérer des défauts de rendu et d'interaction (navigation mobile corrigée), **mais ne remplacent pas les tests navigateur réel et hors ligne**.

## Règle de publication

Ne pas diffuser publiquement une version qui manipule des données de santé sans audit de confidentialité, de sécurité et revue du questionnaire et des textes. Le stockage local IndexedDB n'est pas chiffré au repos, même si les fichiers d'export sont chiffrés.
