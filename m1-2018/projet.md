# Projet Python (M1 - 2018/2019)

## Consignes

* Projet à rendre le 13 janvier *au plus tard*

* Projet collectif, par groupe de 2 ou 3 (sauf exception)


Le rendu devra comporter :

  1. une documentation du projet traitant les points suivants :

   * Les objectifs du projet

   * Les données (origine, format, statut juridique) et les traitements opérés sur celles-ci

   * Les méthodes utilisées (comment vous vous êtes répartis le travail, comment vous avez identifié les pbs et les avez résolus, différentes étapes du projet, ...)

   * L'implémentation ou les implémentations (modélisation le cas échéant, modules et/ou API utilisés, différents langages le cas échéant)

   * Les résultats (fichiers output, visualisations, ...) et une discussion sur ces résultats (ce que vous auriez aimé faire et ce que vous avez pu faire par ex.)
   C'est de la doc technique, pas une dissertation. La doc pourra prendre la format d'un ou plusieurs fichiers, d'un site web, d'un notebook, à votre convenance

  2. le code Python et les codes annexes (JS par ex.) que vous avez produit.

Le code *doit* être commenté.

  3. les données en input et en output (ou un échantillon si le volume est important)

## Sujet

  1. Open Data
  Vous travaillerez sur au moins 3 données issues de l'open data dont l'une sera accédée via une API. L'idée ici est de croiser ces données, trouver des variables en commun pour créer un nouveau tableau de données.  
  Exemple : à partir des fichiers d'[adresse des établissements d'enseignements supérieurs du premier et second degrés](https://www.data.gouv.fr/fr/datasets/adresse-et-geolocalisation-des-etablissements-denseignement-du-premier-et-second-degres-1/), [des taux de chômage par département](https://www.insee.fr/fr/statistiques/2012804#tableau-TCRD_025_tab1_departements) et de l'[API des indicateurs relatifs  à l'éducation prioritaire pour les écoles](https://data.education.gouv.fr/explore/dataset/fr-en-ecoles-ep/api/), vous dresserez un tableau des départements français où apparaitront le taux de chômage, le nombre d'écoles, collèges et lycées publics et privés, le nombre d'écoles en éducation prioritaire ainsi que le nombre d'élèves concernés.  
  Vous utiliserez le module [requests](http://docs.python-requests.org/en/master/) pour interroger l'API.

  2. UD et graphes
  Vous concevrez un programme ou un module qui prend en entrée un fichier ou des fichiers au format UD. Chacune des phrases contenues dans le ou les fichiers d'entrée devra être représentée en mémoire sous forme de [graphe](https://fr.wikipedia.org/wiki/Graphe_(type_abstrait)).  
  votre programme devra être capable de trouver et afficher les chemin de dépendance entre deux mots (ou deux lemmes ou deux POS) donnée par l'utilisateur.  
  Sur les graphes et leur implémentation vous pouvez consulter [Graphs in Python](https://www.python-course.eu/graphs_python.php), [Python Patterns - Implementing Graphs](https://www.python.org/doc/essays/graphs/) et également la documentation de l'outil [Grew](http://grew.fr)
