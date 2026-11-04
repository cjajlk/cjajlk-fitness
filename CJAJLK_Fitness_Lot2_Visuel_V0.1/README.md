# CJAJLK Fitness V0.1 — Lot 2 visuel et choix du coach

Livraison du 4 novembre 2026. 30 exercices, coach masculin ou féminin, images fixes intégrées et consultables hors ligne après préparation.

## Ouvrir dans VS Code / Live Server

1. Décompresser le ZIP, puis ouvrir le dossier CJAJLK_Fitness_Lot2_Visuel_V0.1 dans VS Code.
2. Clic droit sur index.html → Open with Live Server. Ouvrir l’adresse affichée dans Edge.
3. Dans Profil, choisir Coach masculin ou Coach féminin. Ce choix est libre et indépendant du sexe de la personne. Il est aussi modifiable directement dans la bibliothèque.
4. Ouvrir Exercices. Les commandes Deux angles / Face ou Trois-quarts / Profil montrent des **images fixes**, sans lecteur vidéo et sans quitter l’interface.
5. Laisser terminer la préparation jusqu’à l’indication **Visuels prêts hors ligne ✓**. Tous les visuels sont alors mis en cache, y compris ceux de l’autre coach, afin de pouvoir changer de coach hors ligne.

L’application ne demande ni Python, ni Node, ni compilation. Le double-clic ouvrant une adresse file: n’est pas le mode de lancement pris en charge.

## Retrouver les profils existants

La base IndexedDB, sa version et le format des sauvegardes chiffrées restent identiques. Les profils anciens sont reconnus sans réécriture et sans coach imposé. Ils demandent simplement un choix de coach pour afficher les images. Aucun choix n’est déduit du nom, du sexe, de l’âge ou des renseignements de santé.

Utiliser le même profil Edge, le même nom d’hôte et le même port que précédemment pour retrouver automatiquement les données. 127.0.0.1:5500, localhost:5500 et 127.0.0.1:5501 sont trois origines distinctes. Le chemin du dossier peut changer. Si les profils n’apparaissent pas à la nouvelle adresse, exporter une sauvegarde depuis l’ancienne adresse puis la restaurer dans cette version. La restauration remplace les données de l’adresse courante après confirmation.

Le nouveau choix est un champ facultatif du profil ; il est automatiquement inclus dans l’export chiffré. Les sauvegardes anciennes restent importables. Les anciennes versions de l’application ne permettent pas de gérer ce choix ; utiliser cette version pour modifier les profils et les préférences de coach.

## Ce qui est livré

- 30 exercices conservés avec leurs explications, précautions, variantes, repères et recherche/filtres.
- 60 versions de coach (30 masculines et 30 féminines), chacune avec deux angles : **120 vues fixes**, contenues dans 30 planches locales.
- Personnages adultes sportifs réalistes, studio moderne bleu nuit, violet et turquoise. Images générées par IA avec l’outil de création d’images intégré.
- Fiches qui affichent uniquement le coach choisi. Si une version est déclarée absente ou si son fichier ne charge pas, un message explicite remplace le visuel, sans substitution par l’autre coach.
- Préférences propres à chaque profil, modifiables depuis Profil ou la bibliothèque et conservées dans le stockage local et les sauvegardes.
- Aucune page externe ni vidéo distante dans le parcours des exercices.

## Hors ligne et Android

Les images sont **incluses dans les fichiers livrés**, pour environ 60.1 Mo de visuels. La mise en cache nécessite une première ouverture complète depuis localhost ou HTTPS et de la place dans le stockage du navigateur. Les médias ne dépendent d’aucun hébergeur externe. L’indication de préparation doit être terminée avant de couper la connexion. L’effacement du stockage du navigateur supprime également les profils et les caches ; garder des sauvegardes chiffrées.

Sur téléphone, 127.0.0.1 et localhost désignent le téléphone. Une adresse réseau HTTP du PC permet éventuellement de voir l’interface en ligne, mais n’autorise généralement pas le service worker et les fonctions de chiffrement. Pour un vrai usage hors ligne Android, servir les fichiers en HTTPS ou depuis localhost sur le téléphone, puis attendre la préparation complète. Aucun transfert automatique de profil PC → téléphone : utiliser une sauvegarde chiffrée.

Le format Android a été vérifié par émulation Pixel 7 sur PC. **Aucun téléphone Android physique n’était disponible : cette vérification matérielle reste à faire.** L’installation PWA et les politiques d’éviction du cache Android n’ont pas été validées sur appareil réel.

## Santé et périmètre

Les données de santé et les alertes restent présentes. Changer de coach ne modifie ni bilan, ni restriction. Les limitations déclarées restent à clarifier avant pratique ; aucun programme personnalisé n’est déclenché. Les 7 jours éventuellement disponibles ne deviennent pas 7 jours recommandés.

Les visuels montrent une position, pas une trajectoire complète ni une démonstration filmée validée par un professionnel. Ils ne sont pas animés et ne couvrent pas toutes les variantes. Se référer aux consignes écrites et à ses restrictions personnelles. Les séances guidées, le coach animé, l’historique et le suivi ne sont pas activés dans ce Lot 2.

Voir TESTS_ET_LIMITES.md pour les contrôles réels et preuves-tests/ pour les captures des deux versions. Les tests Node dans tests/ sont facultatifs pour les développeurs : node --test tests/*.test.mjs. Node n’est pas nécessaire à l’utilisation.
