# CJAJLK Fitness V0.1 — Lot 2

Livraison du 2 novembre 2026. Bibliothèque de 30 exercices ; séances et suivi indisponibles.

## Lancer avec VS Code Live Server, sans Python

1. Décompressez le ZIP. Ouvrez le dossier **CJAJLK_Fitness_Lot2_V0.1** dans VS Code.
2. Faites un clic droit sur **index.html**, puis **Open with Live Server**.
3. Ouvrez l’adresse affichée dans Edge. Choisissez **Exercices** dans la navigation.

Aucune compilation, aucun compte, aucune installation de Python ou de Node n’est nécessaire pour utiliser l’application. Le double-clic sur index.html (adresse file:) n’est pas le mode de lancement pris en charge.

## Retrouver les profils du Lot 1

La base locale et les sauvegardes gardent exactement leur nom, leur version et leur format. L’original du Lot 1 n’a pas été remplacé.

Avant de changer d’adresse, exportez une sauvegarde chiffrée depuis les paramètres du Lot 1. Gardez le fichier et son mot de passe.

Pour retrouver automatiquement les profils, utilisez **le même navigateur, le même profil Edge, le même nom d’hôte et le même port** que pour le Lot 1. Par exemple, 127.0.0.1:5500 et localhost:5500 sont deux stockages différents ; 5500 et 5501 aussi. Le chemin du dossier peut changer. Si vos profils n’apparaissent pas, retournez à l’ancienne adresse pour exporter, puis restaurez le fichier depuis les paramètres du Lot 2. Ne videz pas les données du navigateur pour résoudre ce problème. La restauration remplace toutes les données de l’adresse courante après confirmation.

Les profils ne sont pas transférés automatiquement du PC au téléphone. Utilisez la sauvegarde chiffrée pour ce transfert.

## Ce qui fonctionne

- Profils indépendants, bilan initial, matériel et santé déclarée, stockage IndexedDB, sauvegarde et restauration chiffrées du Lot 1.
- Catalogue de 30 fiches avec installation, geste, respiration, vigilance, repères généraux et variantes.
- Recherche insensible aux accents et cinq filtres cumulables : famille, matériel principal, position, zone et prise en main.
- Fiches consultables sans créer de profil. Retour à la liste avec conservation des filtres.
- Distinction entre disponibilité personnelle (jusqu’à 7/7) et jours recommandés, non définis dans ce lot.

## Démonstrations : Internet requis

Les 30 fiches donnent accès à une démonstration externe identifiée, photographique ou vidéo, avec de vraies personnes. Dix-neuf proposent en plus l’affichage d’une photo NHS dans l’application, sur demande. Les onze autres ouvrent une page ou une vidéo de référence. Certaines sources réunissent plusieurs mouvements : le nom anglais à repérer est donné dans la fiche. Leurs variantes ne sont pas toutes filmées ; le texte explique les différences.

Les photos et vidéos ne sont **pas incluses dans le ZIP ni garanties hors ligne**. Leurs droits restent ceux des éditeurs. Aucune requête distante de démonstration n’est déclenchée avant votre action. Les sources reçoivent les informations habituelles d’une connexion (par exemple adresse IP), jamais le contenu de vos profils. Elles peuvent proposer des cookies, un lecteur tiers ou des contenus complémentaires. Les ressources sont principalement en anglais. Voir SOURCES_DEMONSTRATIONS.md.

## Hors ligne et mobile

Sur PC, après un premier chargement et une actualisation à l’adresse locale, l’application peut mettre en cache son interface et ses fiches. Les médias externes restent en ligne. L’installation PWA n’a pas été validée dans cette livraison.

Sur téléphone, localhost et 127.0.0.1 désignent le téléphone. L’adresse réseau du PC peut servir à essayer l’affichage si le serveur et le réseau l’autorisent ; n’exposez pas le serveur sur Internet. Une adresse réseau en HTTP n’est généralement pas un contexte sécurisé : service worker, hors ligne et sauvegarde chiffrée peuvent y être indisponibles. Pour ces fonctions sur Android, utiliser un hébergement HTTPS ou localhost sur le téléphone. Aucun essai sur téléphone Android physique n’a été réalisé ici.

## Santé et périmètre

Le catalogue n’est pas un programme personnalisé. Les précautions ne sont ni effacées ni présumées résolues. Aucun entraînement automatique, aucune séance guidée, aucun minuteur, historique de séance ni graphique de progression ne sont activés. Une disponibilité de 7 jours ne crée pas 7 séances. Le poids disponible (jusqu’à 10 kg par haltère) ne devient jamais une prescription de charge.

Les repères de découverte ne sont pas une posologie individuelle. Aucun mouvement ni aucune variante n’est universellement sûr. En cas de restriction ou de doute médical, faites clarifier les activités permises avant de pratiquer. Le contenu n’a pas reçu de validation clinique individuelle.

## Vérifications

Lire TESTS_ET_LIMITES.md et consulter preuves-tests/. Les tests automatisés de chiffrement et de catalogue se relancent avec Node (facultatif pour les développeurs) : node --test tests/*.test.mjs. L’utilisation courante reste entièrement sans Node ni Python.
