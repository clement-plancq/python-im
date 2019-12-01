#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
rouver dans le fichier fr_sequoia-ud-test.conllu les mots qui ont au moins une lettre redoublée (ex: attaque).
Sortie : mot, lettre
"""

import re
import unicodedata

data = "fr_sequoia-ud-test.conllu"
with open(data, 'r') as input:
    for line in input:
        if re.match(r'^\d', line):
            word = line.split('\t')[1]
            m = re.search(r'(\w)\1', word, re.U)
            if m:
                if unicodedata.category(m.group(1)) == 'Ll': # on évite les chiffres
                    print(word, m.group(1))
