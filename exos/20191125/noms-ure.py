# -*- coding: utf-8 -*-

"""
Trouver les noms en 'ure' dans lexique.org
"""

import csv
import re   

lexique = 'Lexique383.tsv'
res = []

with open(lexique) as input:
    reader = csv.DictReader(input, delimiter="\t")
    for item in reader:
        if item['cgram'] == 'NOM' and re.match(r".+ure$", item['lemme']):
            res.append((item['ortho'], item['phon'], item['lemme']))

for item in res:
    print("/".join(item))