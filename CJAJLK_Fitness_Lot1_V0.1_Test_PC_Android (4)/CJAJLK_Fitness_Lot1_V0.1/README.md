# CJAJLK Fitness — Lot 1 · Socle PWA (2 novembre 2026)

Projet testable **sans dépendances externes**, à partir du cahier des charges V0.1 approuvé.

## Fonctions réellement disponibles dans ce lot

- Design bleu nuit / violet / turquoise, responsive mobile/PC et navigation à quatre onglets.
- Accueil « Votre rythme, vos progrès », rappel de non-finalité médicale.
- Création, modification, sélection et suppression de plusieurs profils indépendants.
- Bilan en cinq étapes : pseudo, objectifs, niveau, durée, jours, consentement et précautions facultatives, équipement.
- Choix d'un ou deux haltères de 0,5 à 10 kg chacun. Un profil CJ peut choisir 1 × 10 kg.
- Enregistrement IndexedDB, persistance lors des rechargements, sans connexion serveur.
- Export chiffré AES-GCM avec mot de passe (PBKDF2), import validé et confirmation avant remplacement des données.
- Suppression totale des données locales et retrait de consentement par édition (efface les données de santé du profil).
- PWA avec service worker : application consultable hors ligne après première installation HTTPS/localhost.
- Affichage honnête de l'état à venir des programmes, du coach, des exercices et du suivi : **aucune fausse séance**.

## Non disponible à ce stade

Les 30 fiches d'exercices et leurs démonstrations (Lot 2), les trois programmes exécutables et les séances guidées (Lot 3), la saisie de performances vélo/pédalier/haltères (Lot 4), les graphiques de progrès (Lot 5), l'audit final (Lot 6). Ce Lot 1 **n'est pas une version de production ni un dispositif médical**.

## Comment tester sur PC

Ne pas ouvrir `index.html` en `file://` : IndexedDB pourrait fonctionner, mais le mode PWA/hors-ligne ne sera pas fiable.

```bash
cd CJAJLK_Fitness_Lot1_V0.1
python -m http.server 8080
```

Puis ouvrir `http://localhost:8080` dans Chrome/Edge. Cliquer « Créer mon premier profil ».

## Comment tester sur Android

Publier ce dossier tel quel sur **GitHub Pages** (HTTPS) ou un autre hébergement HTTPS. Ouvrir l'URL sur Android, puis « Installer l'application » via le navigateur. **Aucune publication GitHub n'a été faite dans ce lot.** Un téléphone n'accède pas à `localhost` du PC sans configuration réseau particulière.

Après une première connexion et l'installation du cache, rouvrir l'URL ou l'application en mode avion. Le navigateur peut toutefois supprimer les données locales : utiliser régulièrement l'export chiffré.

## Confidentialité — avertissement important

L'appareil peut contenir des données relatives à la santé. Les données IndexedDB ne sont **pas chiffrées au repos** et les profils sont accessibles à toute personne utilisant le même navigateur et le même appareil. Il ne faut pas saisir de secrets. Le fichier exporté est chiffré : conserver son mot de passe séparément et ne pas le perdre.

Aucune requête vers des services externes et aucun système d'analyse. Le service worker ne met en cache que les fichiers de l'application. Le formulaire de santé et les mensurations ne sont enregistrés qu'avec consentement explicite ; en cas de retrait, ces données sont effacées du profil.

Une revue juridique, de sécurité et de l'ergonomie des données sensibles est nécessaire avant publication publique.

## Structure

- `index.html`, `styles.css` — interface
- `src/app.js` — navigation et bilan de départ
- `src/db.js` — persistance IndexedDB
- `src/backup.js` — sauvegarde chiffrée
- `sw.js`, `manifest.webmanifest`, `assets/` — PWA
- `tests/` — vérifications d'intégration navigateur

## Prochain lot

Lot 2 : catalogue de 30 exercices originaux, variantes et démonstrations, avec revue humaine des consignes avant diffusion.
