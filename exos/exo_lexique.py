# -*- coding: utf-8 -*-

"""
Exercice pour le 14/10/2019
À partir du fichier Lexique383.tsv (voir http://www.lexique.org/)
 générez 3 fichiers avec les colonnes 'ortho', 'phon', 'lemme' pour les noms, les verbes et les adjectifs
"""

nouns = []
verbs = []
adjs = []

with open('Lexique383.tsv') as lexique:
    for line in lexique:
        cells = line.split('\t')
        if cells[3] == 'NOM':
            nouns.append(cells[0:3])
        elif cells[3] == 'VER':
            verbs.append(cells[:3])
        elif cells[3] == 'ADJ':
            adjs.append(cells[:3])

with open('noms.csv', 'w') as out:
    for item in nouns:
        print(",".join(item), file=out)

with open('verbs.csv', 'w') as out:
    for item in verbs:
        print(",".join(item), file=out)

with open('adjs.csv', 'w') as out:
    for item in adjs:
        print(",".join(item), file=out)
