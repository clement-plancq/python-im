[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/clement-plancq/python-im/master)


# Objectifs



Le cours a pour objectif de vous rendre autonome en programmation Python : apprendre les bases du langage, utiliser des modules, comprendre les messages d'erreur, trouver et comprendre la documentation.


L'accent sera mis sur le traitement de données textuelles et les problèmes liés aux données multilingues.



# Évaluation



Vous serez évalués de la façon suivante :



* devoirs hebdomadaires : 30%

* devoir sur table en novembre : 30%

* projet : 40%



# Programme



Tous les supports sont sur [github](https://github.com/clement-plancq/python-im).



### 16 septembre 2019 : Passage en revue des bases en Python (Grands Moulins, 7.02)


  * [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-1.ipynb) ou [ici](https://clement-plancq.github.io/python-im/python-1.html) pour la version non interactive

  * Notebook : [pierre-feuilles-ciseaux](https://clement-plancq.github.io/python-im/chifoumi.ipynb)

  Télécharger le fichier .ipynb et dans le même dossier taper la commande

  `> python3 -m jupyter notebook chifoumi.ipynb`

  * Exos : script qui détermine si un nombre est pair ou impair (utilisez `input()`), [Power of Thor - Episode 1](https://www.codingame.com/training/easy/power-of-thor-episode-1)

### 23 septembre 2019 : Passage en revue des bases en Python (suite)
  * [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-1.ipynb) ou [ici](https://clement-plancq.github.io/python-im/python-1.html) pour la version non interactive

  * Notebook : [pierre-feuilles-ciseaux](https://clement-plancq.github.io/python-im/chifoumi.ipynb)

  * Exos : 
    - faîtes votre propre chifoumi en vous inspirant du notebook
	- script devinette, l'utilisateur a 3 essais pour deviner un chiffre entre 0 et 10
	- [Power of Thor - Episode 1](https://www.codingame.com/training/easy/power-of-thor-episode-1)



### 30 septembre 2019 : Précisions, fichiers et chaînes de car. (Grands Moulins, 7.02)
  * [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-2.ipynb) ou [ici](https://clement-plancq.github.io/python-im/python-2.html) pour la version non interactive
  * Exos :  
    - pour un mot donné par l'utilisateur, comptez et affichez le nombre de voyelles et de consonnes
    - pour ceux qui ne l'ont pas fait : chifoumi avec plusieurs manches, le premier à deux victoires gagne la partie
    - [temperatures (CodinGame)](https://www.codingame.com/ide/puzzle/temperatures)

### 7 octobre 2019 : Structures de données
  * python-2 : [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-2.ipynb), [html](https://clement-plancq.github.io/python-im/python-2.html) et python-3 [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-3.ipynb), [html](https://clement-plancq.github.io/python-im/python-3.html)
  * Exos : 
    * À partir du fichier Lexique383.tsv (voir [lexique.org](http://www.lexique.org/)) générez 3 fichiers avec les colonnes 'ortho', 'phon', 'lemme' pour les noms, les verbes et les adjectifs
    * Lisez attentivement les slides python-3
    * Pour ceux qui sont à l'aise [mime-type (CodinGame)](https://www.codingame.com/training/easy/mime-type)

### 14 octobre : Structures de données
 * python-3 [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-3.ipynb), [html](https://clement-plancq.github.io/python-im/python-3.html)
 * Exos :
  1. reprendre le script ``voyelles.py`` et compter le nb d'occurrences de chaque voyelle et chaque consonne à l'aide d'un objet Counter
  2. compter le nb d'occurrences de chaque mot de [brise marine](https://raw.githubusercontent.com/clement-plancq/python-im/master/brise-marine.txt). Utilisez un objet Counter
  3. à partir du fichier tsv [sem_Ef9POe.conll](https://raw.githubusercontent.com/clement-plancq/python-im/master/sem_Ef9POe.conll)
    * pour chaque POS listez les types classés par ordre d'occurrence décroissante,  
    * pour chaque type de chunk indiquez les longueurs min et max (en nb de mots)

### 21 octobre 2019 : Fonctions ~~et regex~~
 * python-4 : [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-4.ipynb), [html](https://clement-plancq.github.io/python-im/python-4.html)

 * Exos :
   1. Marché
      1. Créer un dictionnaire qui encode le tableau des prix suivants:
    bananes : 2€/kg, clémentines: 3,25€/kg, pommes: 3€/kg, poires: 3,5€/kg, mangues: 3€/pièce
      2. Ajouter le raisin blanc à 4€/kg et les oranges à 2,5€/kg
      3. Calculer le prix d'un panier contenant 2kg de bananes, 1,5kg de raisin blanc, 2kg de pommes, 3 mangues
   2. Prénoms  
      Travail sur l'export csv de [Liste des prénoms 2004 à 2018 (opendata.paris.fr)](https://opendata.paris.fr/explore/dataset/liste_des_prenoms/)
      1. Quels sont les 10 prénoms les plus courants
      2. Quels sont les 10 prénoms féminins et masculins les plus courants 
      3. Indiquez le nombre de naissances par an et par sexe
      4. Quels sont les prénoms masculins et féminins qui sont en baisse en 2017 et 2018
   3. Moyennes
      Écrivez un script qui reçoit un fichier csv de tableau de notes à double entrée élèves/matières comme vu en cours. Le script doit calculer les moyennes
      de chaque élève et chaque matière. Utilisez des dictionnaires.

### 4 novembre 2019

### 18 novembre 2019 : évaluation

### 25 novembre 2019

### 2 décembre 2019

### 9 décembre 2019

### 16 décembre 2019

# Outils



Vous aurez besoin d'un interpréteur Python et d'un éditeur de texte.



## Python & co.

Vous travaillerons avec Python3.



Les supports de cours sont sous forme de diapos html et surtout de notebooks. Pour utiliser les notebooks (anciennement ipython notebook maintenant jupyter notebook) vous aurez besoin d'installer [Jupyter](http://jupyter.org/) sur votre machine de travail.

Je vous incite également à utiliser le shell interactif `ipython` qui est une version améliorée du shell `python` (ipython est inclus dans jupyter).





Deux options pour l'installation :



* installer uniquement les outils nécessaires avec pip :

	1. installer Python3

	```

	sudo apt-get install python3

	```



	2. installer pip

	```

	sudo apt-get install python3-pip

	```



	3. installer jupyter

	```

	python3 -m pip install jupyter

	```



* installer [anaconda](https://www.continuum.io/downloads). La solution de facilité qui comprend python3, pip, jupyter et une foule de modules dont on ne se serivra pas.





## Éditeur de texte

Pas un traitement de texte, pas un IDE, un *[éditeur de texte](https://fr.wikipedia.org/wiki/%C3%89diteur_de_texte)*.



# Ressources



Il y a beaucoup, beaucoup de ressources disponibles pour apprendre Python. Ce qui suit n'est qu'une sélection.



## Livres



* How to think like a computer scientist, by Jeffrey Elkner, Allen B. Downey, and Chris Meyers.

Vous pouvez l'acheter. Vous pouvez aussi le lire [ici](http://openbookproject.net/thinkcs/python/english3e/)

* Dive into Python, by Mark Pilgrim.

[Ici](http://www.diveintopython3.net/) vous pouvez le lire ou télécharger le pdf.

* Learning Python, by Mark Lutz.

* Beginning Python, by Magnus Lie Hetland.

* Python Algorithms: Mastering Basic Algorithms in the Python Language, by Magnus Lie Hetland.

Peut-être un peu costaud pour des débutants.

* Programmation Efficace. Les 128 Algorithmes Qu'Il Faut Avoir Compris et Codés en Python au Cours de sa Vie, by Christoph Dürr and Jill-Jênn Vie.

Si le cours vous paraît trop facile. Le code Python est clair, les difficultés sont commentées. Les algos sont très costauds.



## Web


Je vous conseille vivement d'utiliser un (ou plus) des sites et tutoriels ci-dessous.



* [Coding Game](https://www.codingame.com/home). Vous le retrouverez dans les exercices hebdomadaires.

* [Code Academy](https://www.codecademy.com/fr/learn/python)

* [newcoder.io](http://newcoder.io/). Des projets commentés, commencer par 'Data Visualization'

* [Google's Python Class](https://developers.google.com/edu/python/). Guido a travaillé chez eux. Pas [ce Guido](http://vignette2.wikia.nocookie.net/pixar/images/1/10/Guido.png/revision/latest?cb=20140314012724), [celui-là](https://en.wikipedia.org/wiki/Guido_van_Rossum#/media/File:Guido_van_Rossum_OSCON_2006.jpg)

* [Mooc Python](https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session02/about). Un mooc sur la plateforme FUN, pas fun mais carré.

* [Code combat](https://codecombat.com/)
