# CJAJLK Fitness — Rapport du correctif visuel du Lot 2

4 novembre 2026 · Version V0.1 · 30 exercices · choix du coach par profil.

## Résultat

Les liens et aperçus distants ont été remplacés dans le parcours par des images locales. Les 30 exercices disposent d’une version masculine et féminine, chacune avec deux vues. Ces 120 vues sont stockées dans 30 fichiers de planches, dont l’interface cadre uniquement les vues du coach choisi. Le décor et les tenues suivent l’identité bleu nuit, violet et turquoise. Les images sont explicitement étiquetées **fixes et générées par IA**. Aucun lecteur ou animation fictive n’est affiché.

Les planches ont été examinées visuellement. Leurs séparations ont aussi été mesurées pour éviter de montrer le personnage de l’autre ligne ; les rectangles utilisés par l’interface sont consignés dans inventaire-visuels.json. Les angles de trois-quarts sont indiqués comme tels lorsqu’une vue frontale serait peu utile, par exemple face à un mur ou sur un rameur.

## Tests de modules

**11 tests sur 11 réussis** : les cinq tests du chiffrement du Lot 2, la conservation exacte du catalogue et de ses précautions, la recherche/filtres, la présence des 30 fichiers locaux et des deux coachs/deux vues, l’absence de coach imposé ou déduit du sexe, la compatibilité des sauvegardes anciennes et nouvelles et l’absence de liens/lecteurs distants dans les modules du parcours. Le seul ajustement au texte d’un exercice remplace « vidéo » par « visuel » pour le rameur.

## Parcours Edge vérifiés

Microsoft Edge 156.0.4314.58, automatisé sans fenêtre, profils de test isolés et stockage réel IndexedDB. Les profils personnels de votre navigateur n’ont pas été ouverts ni modifiés.

1. Ancien profil du Lot 2 repris strictement sans modification ni coach imposé.
2. Sans choix : fiches consultables, aucun coach de remplacement affiché.
3. Choix féminin : seul le champ coach et la date du profil actif changent, santé intacte.
4. 30 fiches avec coach féminin : deux angles locaux chargés, aucun lien externe.
5. 30 fiches avec coach masculin : deux angles locaux chargés, aucun lien externe.
6. Commandes Deux angles / Face / Profil : une ou deux images fixes, aucun faux lecteur vidéo.
7. Recherche sans accents, filtres cumulés, résultat vide et retour conservant la recherche.
8. Deux profils : préférences indépendantes, choix dans le bilan et modification immédiate dans Profil.
9. Modification du bilan existant : coach et précautions conservés.
10. Sauvegarde chiffrée avec les deux coachs lisible par le module de sauvegarde original.
11. Restauration par l’interface : coach féminin restauré après changement, profils et santé présents.
12. Choix du coach conservé après fermeture puis réouverture de page.
13. Hors ligne : les 30 fiches et les deux vues du coach féminin restent disponibles après rechargement et cache HTTP vidé.
14. Hors ligne : les 30 fiches et les deux vues du coach masculin restent disponibles après rechargement et cache HTTP vidé.
15. Version féminine déclarée absente : message explicite, aucun coach masculin substitué.
16. Format Android émulé : deux coachs, fiches, vues et captures à 393 px ; aucun débordement à 320, 393 et 768 px.
17. Aucune requête externe ni erreur JavaScript dans les parcours testés.

Contrôle supplémentaire : Fermeture complète puis relance du profil Edge de test : préférences male/female indépendantes, santé et disponibilité 7/7 conservées. Un redémarrage de Windows n’a pas été testé.

Le parcours hors ligne a été testé après rechargement et effacement du cache HTTP du navigateur, en conservant le cache applicatif : les 30 fiches ont chargé leurs deux vues pour chacun des deux coachs. Le changement de coach a lui aussi fonctionné hors ligne.

## Profils, sauvegardes et précautions

src/db.js et src/backup.js sont identiques octet pour octet au Lot 2 original. La base ne change ni de nom ni de version ; le chiffrement et le schéma de sauvegarde restent identiques. Le choix de coach ajoute uniquement un champ facultatif coach (male/female) au profil. Une sélection modifie ce champ et la date du profil actif ; le test compare les autres champs et les renseignements de santé avant/après. Deux profils distincts conservent des choix différents. Une sauvegarde ancienne sans préférence reste utilisable et n’impose aucun coach.

Les alertes, la disponibilité de 7/7 et la distinction avec les jours recommandés restent présentes. Aucun programme, séance guidée, historique sportif ou suivi du Lot 3 n’a été activé.

## PC et mobile

| Environnement | Vérification réelle | Résultat / limite |
|---|---|---|
| Edge PC, 1440 × 1100 | Bibliothèque et 30 fiches pour chaque coach, deux angles, recherche, profils et sauvegardes | Réussi |
| Edge PC, profil persistant | Fermeture complète et relance avec deux préférences de coach et précautions | Réussi |
| Edge hors ligne après cache | Rechargement, changement de coach et 60 versions de fiches avec vues locales | Réussi |
| Pixel 7 émulé, 393 × 851 | Deux coachs, bibliothèque, fiche, commandes d’angle et captures | Réussi |
| Largeurs 320, 393 et 768 px | Fiches des deux coachs sans débordement horizontal | Réussi |
| Téléphone Android physique | Aucun appareil disponible | Non testé |
| VS Code Live Server | Fichiers statiques compatibles, sans compilation ni Python ; banc de test sur serveur statique local équivalent | Extension non pilotée ici |
| PWA installée sur Android, mode avion matériel et stockage Android | Non exécutés sur appareil réel | Non validés |

## Captures livrées

- PC-bibliotheque-female.png et PC-bibliotheque-male.png.
- PC-entree-bibliotheque-female.png et PC-entree-bibliotheque-male.png (accueil et choix du coach).
- PC-fiche-female.png et PC-fiche-male.png.
- Android-emule-bibliotheque-female.png et Android-emule-bibliotheque-male.png.
- Android-emule-fiche-female.png et Android-emule-fiche-male.png.

Les captures réelles de l’interface se trouvent dans captures/ à côté du rapport séparé, et dans preuves-tests/captures/ dans l’application ; elles ont été examinées avant la mise en archive. Les noms des profils visibles sont fictifs. Les captures Android proviennent de l’émulation, pas d’un téléphone physique.

## Limites et vérification locale

Les images illustrent des positions statiques et ne couvrent pas la totalité du mouvement ni toutes les variantes. Aucun tournage, analyse biomécanique ni validation clinique individuelle n’est revendiqué. Les animations sont à développer ultérieurement. Les visuels peuvent différer légèrement entre deux angles ; les consignes et précautions écrites restent la référence.

Le cache des visuels occupe environ 60.1 Mo, en plus de l’interface. Il nécessite un premier chargement complet, un contexte sécurisé (localhost/HTTPS) et un stockage disponible. Le navigateur peut l’effacer ; aucune conservation indéfinie n’est garantie. L’app ne déclenche aucun téléchargement externe d’exercice. Les documents de références éditoriales antérieures restent séparés de l’interface et ne sont pas chargés à l’usage.

Sur votre PC : ouvrir index.html avec Live Server à la même origine que l’ancienne application, contrôler le profil, choisir un coach, attendre « Visuels prêts hors ligne ✓ », fermer/rouvrir et tester sans connexion. Sur un vrai Android : utiliser HTTPS/localhost sur l’appareil, attendre la préparation, essayer les deux coachs en mode avion et vérifier le défilement, les vues et les sauvegardes. Ces essais sur appareil réel restent nécessaires avant de déclarer Android entièrement validé.
