# -*- coding: utf-8 -*-

"""
Python M1 2019-2020. 04/11/2019

Lit les notes d'un fichier à double entrée et calcule :
   - la moyenne de chaque élève
   - la moyenne de chaque matière
Algo un peu béta avec la liste des matières en manuel
"""
import csv
import statistics
from collections import defaultdict

fichier = 'notes-classe.csv'
notes_eleves = {}
notes_matieres = defaultdict(list)

with open(fichier, 'r') as input:
   reader = csv.DictReader(input)
   for line in reader:
       eleve = line['eleve']
       notes_eleves[eleve] = []
       notes_eleves[eleve].append(int(line['maths']))
       notes_eleves[eleve].append(int(line['français']))
       notes_eleves[eleve].append(int(line['eps']))
       notes_eleves[eleve].append(int(line['techno']))
       notes_matieres['maths'].append(int(line['maths']))
       notes_matieres['français'].append(int(line['français']))
       notes_matieres['eps'].append(int(line['eps']))
       notes_matieres['techno'].append(int(line['techno']))

for eleve, notes in notes_eleves.items():
    moyenne = statistics.mean(notes)
    print(f"{eleve} : {moyenne}")
print()
for matiere, notes in notes_matieres.items():
    moyenne = statistics.mean(notes)
    print(f"{matiere} : {moyenne}")
