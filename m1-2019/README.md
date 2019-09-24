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
  * Exos : pour un mot donné par l'utilisateur, comptez et affichez le nombre de voyelles et de consonnes. Pour ceux qui sont à l'aise : [temperatures (CodinGame)](https://www.codingame.com/ide/puzzle/temperatures)

### 7 octobre 2019 : Structures de données
  * [slides](https://mybinder.org/v2/gh/clement-plancq/python-im/master?filepath=python-3.ipynb) ou [ici](https://clement-plancq.github.io/python-im/python-3.html) pour la version non interactive
  * Exos : 
    * À partir du fichier tsv [sem_Ef9POe.conll](https://clement-plancq.github.io/python-im/sem_Ef9POe.conll) : pour chaque POS listez les types classés par ordre d'occurrence décroissante, pour chaque type de chunk indiquez les longueurs min et max (en nb de mots).
    * Pour ceux qui sont à l'aise : [mime-type (CodinGame)](https://www.codingame.com/training/easy/mime-type)

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
