# CJAJLK Fitness V0.1 — Lot 2 : tests et limites

Date : 2 novembre 2026. Base utilisée : dossier Lot 1 fourni dans E:\cj_project\cjajlk-fitness.

## Résultat et périmètre

Lot 2 implémenté et vérifié dans Microsoft Edge 156.0.4314.58, en mode automatisé sans fenêtre, avec des profils de test isolés. Le stockage réel du navigateur a été utilisé. Les données personnelles déjà présentes dans votre Edge n’ont pas été ouvertes ni modifiées. Les captures ont été examinées visuellement : bibliothèque PC et mobile, fiche PC avec photo réelle NHS et fiche mobile.

L’application est un ensemble de fichiers statiques HTML/CSS/JavaScript, directement utilisable avec VS Code Live Server, sans Python. Le banc de tests a utilisé un serveur statique local équivalent ; l’extension Live Server de VS Code n’a pas été pilotée dans cette session. La validation antérieure du Lot 1 sous Edge/Live Server vient de la conversation de référence.

## Tests automatisés réussis

**7 tests de modules sur 7** : sauvegarde/restauration AES-GCM fidèle, mauvais mot de passe refusé, mot de passe trop court refusé, format et santé orpheline refusés, sauvegarde volumineuse, 30 fiches uniques et complètes, recherche/filtres cumulés. Les refus de chiffrement sont testés au niveau module ; la restauration normale est également testée par l’interface.

**15 contrôles de parcours Edge sur 15** :

1. Profil complet créé par le bilan original du Lot 1.
2. Lot 1 → Lot 2 : profils, santé, matériel, mesures et paramètres strictement identiques.
3. Disponibilité 7/7 distinguée de la fréquence recommandée.
4. Recherche sans accents, fiche pédalier, retour avec filtres, précaution et absence de démarrage.
5. Filtres cumulés et résultat vide.
6. 30 fiches ouvrables avec consignes, adaptations, vigilance et lien de démonstration.
7. Photo réelle NHS chargée sur demande et affichée.
8. Export chiffré du Lot 2 conserve les données du Lot 1.
9. Modification du bilan et restauration chiffrée par l’interface.
10. Deux profils indépendants, changement de profil et santé du premier préservée.
11. Persistance IndexedDB après fermeture et réouverture de page.
12. Mode hors ligne : rechargement, catalogue et fiche accessibles après cache.
13. Émulation tactile 320, 390 et 768 px : catalogue, filtre, fiche et absence de débordement horizontal.
14. Aucune statistique fictive sans profil.
15. Aucune erreur JavaScript non interceptée.

**Test supplémentaire réussi** : fermeture complète du navigateur de test persistant, puis nouveau lancement Edge ; le profil, les restrictions de santé, les 7 jours disponibles et l’haltère de 10 kg sont toujours présents. Aucun redémarrage de Windows n’a été effectué.

**Ressources externes** : 33 URL distinctes vérifiées par requête HTTP, toutes accessibles (200) à la date du test : 19 photos et 14 pages/vidéos de référence partagées entre les 30 fiches. Cela vérifie l’accessibilité de la ressource, pas la lecture intégrale de chaque vidéo ni sa disponibilité future. La photo de la fiche 06 a été réellement chargée dans Edge et son rendu a été examiné. Les 30 démonstrations n’ont pas toutes été visionnées intégralement. La fiche Bird Dog renvoie à la vidéo référencée par NHS Fife ; la page NHS Fife elle-même a refusé une requête automatisée, d’où le lien direct à cette vidéo.

## Conservation du Lot 1

Le code de stockage src/db.js et le code de sauvegarde src/backup.js sont identiques octet pour octet au Lot 1. Le nom de la base et son schéma ne changent pas. Les profils, mesures, objectifs, équipements et renseignements de santé créés dans le Lot 1 ont été retrouvés sans conversion dans le Lot 2. Deux profils indépendants ont été vérifiés. La copie originale du Lot 1 est restée intacte.

Les changements portent sur la bibliothèque, ses fiches, l’affichage de disponibilité, les textes de périmètre et le cache de cette nouvelle copie. Le service worker du Lot 2 utilise un cache propre à son adresse ; il ne supprime pas les caches du Lot 1. Il ne met pas en cache les médias externes. Les empreintes de contrôle figurent dans preuves-tests/integrite-lot1.txt.

## PC et mobile : ce qui a réellement été testé

| Environnement | Vérification | Résultat / limite |
|---|---|---|
| Edge PC, 1440 × 1000 | Catalogue, 30 fiches, photo, bilan, export/import, profils | Réussi |
| Edge PC, profil persistant | Fermeture puis relance du navigateur | Réussi |
| Edge, mode hors ligne après cache | Rechargement, navigation vers bibliothèque et fiche rameur | Réussi, médias externes exclus |
| Émulation tactile, 390 × 844 | Catalogue, filtres, fiche et rendu | Réussi |
| Largeurs 320 et 768 px | Catalogue sans débordement horizontal | Réussi |
| Téléphone Android physique / Chrome Android | Non disponible dans cette session | Non testé |
| VS Code Live Server réel | Compatible par construction statique ; lancement manuel à refaire | Non piloté ici |
| Installation PWA, mode avion Android, HTTPS public | Non exécutés | Non validés |

## Limites à connaître

- Les démonstrations réalistes sont **en ligne**, avec 19 aperçus photographiques NHS sur demande et 11 accès externes. Aucun film ni photo d’exercice n’est embarqué dans le ZIP. Les variantes ne possèdent pas chacune leur propre vidéo.
- Les liens peuvent changer, être bloqués ou demander des cookies. Les références éditoriales ne constituent pas une validation médicale de cette application. Le catalogue initial de 30 noms prévu dans le cahier des charges n’était pas accessible dans les fichiers du Lot 1 : ce lot fournit une sélection explicite de 30 mouvements, listée dans SOURCES_DEMONSTRATIONS.md.
- Aucun test physique des mouvements, aucune revue clinique professionnelle, aucun audit d’accessibilité exhaustif ou de sécurité complet n’a été effectué.
- Les tests protègent la continuité de fonctionnement ; ils ne garantissent pas la conservation des données si le navigateur est vidé, utilisé en navigation privée ou ouvert sur une autre origine. Exporter une sauvegarde reste nécessaire.
- Les fonctions du Lot 3 et des Lots 4–5 restent indisponibles : aucune séance guidée ni suivi réellement enregistré. Les repères de répétitions/durée sont généraux et ne composent aucun programme.

## Vérification manuelle recommandée sur votre installation

1. Dans le Lot 1 à votre adresse habituelle, exporter une sauvegarde chiffrée et noter l’adresse exacte (hôte et port).
2. Ouvrir index.html du Lot 2 via Live Server avec le même profil Edge et la même origine ; contrôler le profil, les équipements, le bilan et les précautions. Sinon restaurer la sauvegarde à la nouvelle adresse.
3. Dans Exercices, rechercher « pedalier », combiner les filtres, ouvrir une fiche, revenir aux résultats ; afficher une photo et ouvrir une démonstration avec Internet.
4. Fermer et rouvrir Edge. Après une première actualisation en ligne, passer hors ligne et vérifier une fiche. Les démonstrations externes restent indisponibles hors ligne.
5. Sur un vrai téléphone, vérifier défilement, listes, clavier, lien externe et lisibilité. Pour les sauvegardes et le hors ligne, utiliser HTTPS ou localhost sur ce téléphone, pas simplement l’adresse réseau HTTP du PC.

Les captures et résultats bruts se trouvent dans preuves-tests/. Ils ne contiennent que des profils de test fictifs.
