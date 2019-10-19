# -*- coding: utf-8 -*-

"""
Exercice pour le 14/10/2019
À partir du fichier Lexique383.tsv (voir http://www.lexique.org/)
 générez 3 fichiers avec les colonnes 'ortho', 'phon', 'lemme' pour les noms, les verbes et les adjectifs
Version defaultdict
"""
from collections import defaultdict

cats = ['NOM', 'VER', 'ADJ']
res = defaultdict(list)

with open('Lexique383.tsv') as lexique:
    for line in lexique:
        cells = line.split('\t')
        current_cat = cells[3]
        if current_cat in cats:
            res[current_cat].append(cells[:3])
                
for cat in cats:
    with open(cat+'.csv', 'w') as out:
        for item in res[cat]:
            print(",".join(item), file=out)