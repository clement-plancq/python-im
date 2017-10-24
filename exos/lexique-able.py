#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## exo cours 4
## Pour chaque verbe du premier groupe (utilisez le lemme) vous vérifierez s'il existe un adjectif en -able. Vous donnerez les décomptes en résultat (combien de verbes avec adjectif -able, combien sans)
## Pour chaque adjectif en -able vous vérifierez s'il existe un dérivé négatif (in-X-able, touchable/intouchable par ex.). En plus de l'affichage des comptes vous donnerez le pourcentage d'adjectifs en -able pour lesquels le dérivé négatif est plus fréquent (utilisez la colonne '7_freqlemfilms2).

import re

data = "/data/rsrc/lexique381/Lexique381.csv"
verbs = set()
adjs_freq_able = set()

pat_able = re.compile("[aiu]ble$")

with open(data, 'r') as f:
    for line in f:
        row = line.split('\t')
        lemma, pos, freq = row[2], row[3], row[6]
        if pos == 'VER' and lemma[-2:] == 'er':
            verbs.add(lemma)
        elif pos == 'ADJ' and  pat_able.search(lemma):
                adjs_freq_able.add((lemma, freq))


                
# Question 1
list_ables = [lemma for lemma, freq in adjs_freq_able]
cpt_able = len([verb for verb in verbs for adj in list_ables if re.match('{}e?[aiu]ble$'.format(verb[:-2]), adj)])

cpt_nonable = len(verbs)-cpt_able

print("Nb verbes en er : {}, nb ables : {}, nb non ables : {}".format(len(verbs), cpt_able, cpt_nonable))
print('=' * 50)

# Question 2
in_et_able = [(adj_x_able, adj_in_x_able) for adj_x_able in adjs_freq_able for adj_in_x_able in adjs_freq_able if re.match('^i[nmr]{}'.format(adj_x_able[0]), adj_in_x_able[0])]

print("{} adjectifs dérivés en able ont une forme négative (sur {})".format(len(in_et_able), len(adjs_freq_able)))
neg_freq = [(adj_x_able[0], adj_in_x_able[0]) for adj_x_able, adj_in_x_able in in_et_able if adj_x_able[1] < adj_in_x_able[1]]
print("dont {0:.2%} % ont des formes négatives plus fréquentes".format(len(neg_freq)/len(in_et_able)))
#print(repr(in_et_able))
