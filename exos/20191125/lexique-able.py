#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Pour chaque verbe du premier groupe (utilisez le lemme) vous vérifierez s'il existe un adjectif en -able. Vous donnerez les décomptes en résultat (combien de verbes avec adjectif -able, combien sans)

import csv
import re

data = "Lexique383.tsv"
verbs = set()
adjs_able = set()

with open(data, 'r') as input:
    reader = csv.DictReader(input, delimiter='\t')
    for line in reader:
        lemma, pos = line['lemme'], line['cgram']
        if pos == 'VER' and lemma[-2:] == 'er':
            verbs.add(lemma)
        elif pos == 'ADJ' and  re.search(r"[aiu]ble$", lemma):
                adjs_able.add(lemma)

cpt_able = 0
for verb in verbs:
    for adj in adjs_able:
        if verb[-3] == 'c':
            if re.match(rf'^{verb[:-3]}(c|ç)[aiu]ble$', adj):
                cpt_able += 1
        else:
            if re.match(rf'^{verb[:-2]}e?[aiu]ble$', adj):
                cpt_able += 1

cpt_nonable = len(verbs) - cpt_able

print(f"Nb verbes en er : {len(verbs)}, nb ables : {cpt_able}, nb non ables : {cpt_nonable}")
