# -*- coding: utf-8 -*-

"""
Python M1 2019-2020. 04/11/2019

Lit les notes d'un fichier à double entrée et calcule :
   - la moyenne de chaque élève
   - la moyenne de chaque matière
"""
import csv
import statistics
from collections import defaultdict

fichier = 'notes-classe.csv'
notes_eleves = {}
notes_matieres = defaultdict(list)

with open(fichier, 'r') as input:
   reader = csv.DictReader(input)
   for record in reader:
      # liste des matieres, c-a-d toutes les clés sauf 'eleve'
      matieres = [key for key in record.keys() if key != 'eleve']
      for item in matieres:
         notes_matieres[item].append(int(record.get(item)))
      notes = [int(record.get(key)) for key in matieres]
      notes_eleves[record['eleve']] = notes


# Moyennes des élèves
for eleve in notes_eleves:
   print(f"{eleve} : {statistics.mean(notes_eleves[eleve])}")

print(f"\n{'-'*10}\n")

# Moyennes des matières
for matiere in notes_matieres:
   print(f"{matiere} : {statistics.mean(notes_matieres[matiere])}")
