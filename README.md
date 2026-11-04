# CJAJLK Fitness

Application locale de découverte sportive, à lancer avec **VS Code / Live Server**, sans Python et sans compilation.

## Version à utiliser

Ouvrir [CJAJLK_Fitness_Lot2_Visuel_V0.1](CJAJLK_Fitness_Lot2_Visuel_V0.1/), puis faire un clic droit sur son fichier `index.html` → **Open with Live Server**.

Cette version comprend les 30 exercices, le choix libre du coach masculin ou féminin par profil, les vues statiques réalistes intégrées, la recherche et les filtres. Les visuels sont générés par IA et inclus dans le projet. Attendre **Visuels prêts hors ligne ✓** avant de couper la connexion.

Les profils restent stockés localement dans le navigateur. Le choix du coach est conservé dans le profil et les sauvegardes chiffrées. Pour retrouver les profils d'une version précédente, utiliser le même navigateur, le même nom d'hôte et le même port, ou restaurer une sauvegarde chiffrée. Ne pas enregistrer ces sauvegardes personnelles dans Git.

## Documentation et tests

- [Guide de lancement et fonctionnement hors ligne](CJAJLK_Fitness_Lot2_Visuel_V0.1/README.md).
- [Tests effectués et limites](CJAJLK_Fitness_Lot2_Visuel_V0.1/TESTS_ET_LIMITES.md).
- [Captures PC et Android émulé, pour les deux coachs](CJAJLK_Fitness_Lot2_Visuel_V0.1/preuves-tests/captures/).

Validation de la livraison : 11 tests de modules et 17 contrôles de parcours Edge, plus un contrôle de relance complète du navigateur. Le format Android a été vérifié par émulation ; aucun téléphone Android physique n'a été testé. Les séances guidées, animations de coach et suivi sportif ne sont pas encore activés.

Les tests de modules peuvent être relancés avec Node, uniquement pour le développement :

```sh
cd CJAJLK_Fitness_Lot2_Visuel_V0.1
node --test tests/*.test.mjs
```

Node et Python ne sont pas nécessaires pour utiliser l'application.

## Historique conservé

- `CJAJLK_Fitness_Lot1_V0.1_Test_PC_Android (4)/` : livraison initiale, conservée comme référence.
- `CJAJLK_Fitness_Lot2_V0.1/` : premier Lot 2 avec références externes, conservé comme historique.
- `CJAJLK_Fitness_Lot2_Visuel_V0.1/` : version corrigée à utiliser.

Les précautions de santé déclarées restent prioritaires. La bibliothèque ne déclenche aucun programme personnalisé, et une disponibilité de 7 jours ne devient pas une recommandation de 7 séances.
