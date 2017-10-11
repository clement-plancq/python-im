#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Exo sur fichier conll output de SEM
##  1. pour chaque POS listez les types classés par ordre d'occurrence décroissante,
##  2. pour chaque type de chunk indiquez les longueurs min et max (en nb de mots).

from collections import defaultdict
import operator

conll_file = 'sem_Ef9POe.conll'
dict_pos = defaultdict(dict)
dict_chunk = defaultdict(list)

with open(conll_file) as f:
    for line in f:
        line = line.rstrip()
        if line == "":
            continue
        form, pos, chunk  = line.split('\t')
        dict_pos[pos].setdefault(form, 0)
        dict_pos[pos][form] += 1
        if chunk[0] == 'B':
            dict_chunk[chunk[2:]].append(list())
            dict_chunk[chunk[2:]][-1].append(form)
        elif chunk[0] == 'I':
            dict_chunk[chunk[2:]][-1].append(form)

for chunk, list_ck in dict_chunk.items():
    print("{} : {}, {}".format(chunk, min([len(l) for l in list_ck]), max([len(l) for l in list_ck])))
                       
#for pos, types in dict_pos.items():
#    print("{} : ".format(pos), end='')
#    for form, occ in sorted(types.items(), key=operator.itemgetter(1), reverse=True):
#        print("{} ({}) ".format(form, occ), end='')
#    print()
