# -*- coding: utf-8 -*-

"""
Trouver les noms avec les suffixes 'ure', 'ment', 'a|ible', 'ette', 'ion', 'age' dans lexique.org
"""

import csv
import re   
from collections import defaultdict

lexique = 'Lexique383.tsv'
suffixes = ['ure', 'ment', '(a|i)ble', 'ette', 'ion', 'age']
res = defaultdict(set)

with open(lexique) as input:
    reader = csv.DictReader(input, delimiter="\t")
    for item in reader:
        if item['cgram'] == 'NOM' or item['cgram'] == 'ADJ':
            for suf in suffixes:
                if re.match(rf".+{suf}$", item['lemme']):
                    res[suf].add((item['lemme']))

for suf in res:
    print(f"{suf} : ")
    for item in res[suf]:
        print(f"\t{item}")