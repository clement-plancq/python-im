# -*- coding: utf-8 -*-

# À partir de l’export csv de https://opendata.paris.fr/explore/dataset/les-titres-les-plus-pretes/ 
# vous compterez le nombre d’ouvrages par ‘type de document’ et vous afficherez les types par ordre décroissant

from collections import Counter

sep = ';'
cnt = Counter()

with open('les-titres-les-plus-pretes.csv') as f_livres:
    for line in f_livres:
        if line.startswith("Rang;"):
            continue
        line = line.rstrip()
        cols = line.split(sep)
        cnt[cols[1]] += int(cols[2])

# La fonction most_common renvoie la liste des tuples par ordre décroissant
# (https://docs.python.org/3.7/library/collections.html#collections.Counter.most_common)
for cat, nb in cnt.most_common():
    print(f"{cat} : {nb} prêts")
