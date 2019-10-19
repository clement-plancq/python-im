# -*- coding: utf-8 -*-

"""
Compte de nb de mots d'un fichier
Version pas subtile avec ' ' comme séparateur
"""

from collections import defaultdict, Counter
import operator

fichier = "../../brise-marine.txt"

cnt_words = Counter()

with open(fichier, 'r') as file:
    for line in file:
        line = line.rstrip()
        for w in line.split(' '):
            cnt_words[w.lower()] += 1

# Affichage par ordre décroissant
for w, occ in sorted(cnt_words.items(), key=operator.itemgetter(1), reverse=True):
    print(f"{w} : {occ}")