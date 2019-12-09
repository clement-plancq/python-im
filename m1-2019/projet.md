# Projet Python (M1 - 2019/2020)

## Consignes

* Projet à rendre le 10 janvier 2020 *au plus tard*

* Projet individuel ou collectif, par groupe de 2

Le rendu devra comporter :

1. une documentation du projet traitant les points suivants :

   * Les objectifs du projet

   * Les données (origine, format, statut juridique) et les traitements opérés sur celles-ci

   * Les méthodes utilisées (comment vous vous êtes répartis le travail, comment vous avez identifié les problèmes et les avez résolus, différentes étapes du projet, ...)

   * L'implémentation ou les implémentations (modélisation le cas échéant, modules et/ou API utilisés, différents langages le cas échéant)

   * Les résultats (fichiers output, visualisations, ...) et une discussion sur ces résultats (ce que vous auriez aimé faire et ce que vous avez pu faire par ex.)
   C'est de la doc technique, pas une dissertation. La doc pourra prendre la forme d'un ou plusieurs fichiers, d'un site web, d'un notebook, à votre convenance

2. le code Python et les codes annexes (JS par ex.) que vous avez produit.
  
    Le code *doit* être commenté.

3. les données en input et en output (ou un échantillon si le volume est important)

## Sujets

Vous choisirez un sujet parmi les deux :

1. Open Data

    Vous travaillerez sur 3 données issues de l'open data.

    * [https://www.data.gouv.fr/fr/datasets/panorama-des-festivals/](https://www.data.gouv.fr/fr/datasets/panorama-des-festivals/)
    * [https://www.data.gouv.fr/fr/datasets/densites-de-population-par-commune/](https://www.data.gouv.fr/fr/datasets/densites-de-population-par-commune/)
    * [https://www.data.gouv.fr/fr/datasets/revenus-des-francais-a-la-commune/](https://www.data.gouv.fr/fr/datasets/revenus-des-francais-a-la-commune/)
  
    Vous travaillerez sur ces données, soit avec [sqlite3](https://docs.python.org/3.8/library/sqlite3.html) soit avec [pandas](https://pandas.pydata.org/) de façon à répondre aux questions suivantes:
    - Compter le nombre de festival par domaine pour chaque commune puis chaque département puis par mois
    - Comparer le nombre de festival avec les revenus par commune puis la densité de population
    - Comparer les festivals ayant lieu en juin/juillet/août avec ceux ayant lieu les autres mois de l'année. Y-a-t'il plus de festivals dans les zones peu denses en été ou pendant les autres mois ?
    - Trouver au moins deux questions se rapportant à ces données et répondez y.

    N'hésitez pas à produire des graphiques. 

2. UD et graphes

  Vous concevrez un programme ou un module qui prend en entrée un fichier ou des fichiers au format UD. Chacune des phrases contenues dans le ou les fichiers d'entrée devra être représentée en mémoire sous forme de [graphe](https://fr.wikipedia.org/wiki/Graphe_(type_abstrait)).  
  votre programme devra être capable de trouver et afficher les chemins de dépendance entre deux mots (ou deux lemmes ou deux POS) donnés par l'utilisateur.  
  Sur les graphes et leur implémentation vous pouvez consulter [Graphs in Python](https://www.python-course.eu/graphs_python.php), [Python Patterns - Implementing Graphs](https://www.python.org/doc/essays/graphs/) et également la documentation de l'outil [Grew](http://grew.fr)
