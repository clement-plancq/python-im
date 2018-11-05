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



### 17 septembre 2018 : Passage en revue des bases en Python (Grands Moulins, 7.02)


  * [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-1.ipynb) ou [ici](https://clement-plancq.github.io/python-im/python-1.html) pour la version non interactive

  * Notebook : [pierre-feuilles-ciseaux](https://clement-plancq.github.io/python-im/chifoumi.ipynb)

  Télécharger le fichier .ipynb et dans le même dossier taper la commande

  `> jupyter notebook chifoumi.ipynb`

  * Exos : Chifoumi, Devinette, [Power of Thor - Episode 1](https://www.codingame.com/training/easy/power-of-thor-episode-1)

### 24 septembre 2018 : Précisions, fichiers et chaînes de car. (Grands Moulins, 7.02)
  * [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-2.ipynb) ou [ici](https://clement-plancq.github.io/python-im/python-2.html) pour la version non interactive
  * Exos : pour un mot donné par l'utilisateur, comptez et affichez le nombre de voyelles et de consonnes. Pour ceux qui sont à l'aise : [temperatures (CodinGame)](https://www.codingame.com/ide/puzzle/temperatures)

### 1er octobre 2018 : Structures de données
  * [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-3.ipynb) ou [ici](https://clement-plancq.github.io/python-im/python-3.html) pour la version non interactive
  * Exos : 
    * À partir du fichier tsv [sem_Ef9POe.conll](https://clement-plancq.github.io/python-im/sem_Ef9POe.conll) : pour chaque POS listez les types classés par ordre d'occurrence décroissante, pour chaque type de chunk indiquez les longueurs min et max (en nb de mots).
    * Pour ceux qui sont à l'aise : [mime-type (CodinGame)](https://www.codingame.com/training/easy/mime-type)

### 8 octobre 2018 : Structures de données (2)
  * [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-3.ipynb) ou [ici](https://clement-plancq.github.io/python-im/python-3.html) pour la version non interactive
  * Notebook : [dictonnaire de rimes](https://clement-plancq.github.io/python-im/dico-rimes.ipynb)
  * Exos : 
    1. compter le nb d'occurrences de chaque mot de [brise marine](https://clement-plancq.github.io/python-im/brise-marine.txt). Utilisez un objet Counter comme vu sur la [diapo](https://clement-plancq.github.io/python-im/python-3.html#Module-collections)
    2. reprendre le script ``voyelles.py`` et compter le nb d'occurrences de chaque voyelle et chaque consonne
	  
### 15 octobre 2018 : structures de données (3)
 * [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-3.ipynb) ou [ici](https://clement-plancq.github.io/python-im/python-3.html) pour la version non interactive
  * Notebook : [dictonnaire de rimes](https://clement-plancq.github.io/python-im/dico-rimes.ipynb)
  * Exos :
    1. À partir de l'export csv de [https://opendata.paris.fr/explore/dataset/les-titres-les-plus-pretes/](https://opendata.paris.fr/explore/dataset/les-titres-les-plus-pretes/) vous compterez le nombre d'ouvrages par 'type de document' et vous afficherez les types par ordre décroissant
    2. À partir de l'export csv de [https://opendata.paris.fr/explore/dataset/logements_sociaux_finances_a_paris/](https://opendata.paris.fr/explore/dataset/logements_sociaux_finances_a_paris/) vous compterez le nombre de logements sociaux financés par arrondissement. Pour les cinq arrondissements où l'on trouve le plus de logements financés vous afficherez l'évolution par année avec l'année 2001 et l'année précédente comme références.

### 22 octobre 2018 : fonctions et expressions régulières
* [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-4.ipynb) ou [ici](https://clement-plancq.github.io/python-im/python-4.html) pour la version non interactive
* Exos :
  * Le suffixe -able (ou -ible ou -uble) est utilisé pour former des adjectifs à partir des verbes. Vous travaillerez avec les données de lexique3.81.

    1. Pour chaque verbe du premier groupe (utilisez le lemme) vous vérifierez s’il existe un adjectif en -able. Vous donnerez les décomptes en résultat (combien de verbes avec adjectif -able, combien sans)
    2. Pour chaque adjectif en -able vous vérifierez s’il existe un dérivé négatif (in-X-able, touchable/intouchable par ex. En plus de l’affichage des comptes vous donnerez le pourcentage d’adjectifs en -able pour lesquels le dérivé négatif est plus fréquent (utilisez la colonne ‘7_freqlemfilms2).
  * [mime-type (CodinGame)](https://www.codingame.com/training/easy/mime-type)

### 5 novembre 2018
### 12 novembre 2018
### 19 novembre 2018 : examen
### 26 novembre 2018
### 3 décembre 2018
### 10 décembre 2018
### 17 décembre 2018


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
