# -*- coding: utf-8 -*-

"""
Correction de l'examen Python du 18/11/2019
Première partie sur le fichier 'les_etablissements_hospitaliers_franciliens.csv'
"""

import csv
from collections import Counter

def main():
    input_file = 'les_etablissements_hospitaliers_franciliens.csv'
    data = [] # structure de données principale
    # chaque élément sera une ligne du fichier représentée dans un dictionnaire
    # les clés sont les en-têtes de colonne
    with open(input_file) as input:
        reader = csv.DictReader(input, delimiter=';')                                                               
        for item in reader:
            data.append(item)      

    # question 1 : combien y-a-t'il d'établissements
    print(f"Nb d'établissements : {len(data)}")
    print('-' * 15)

    # question 2 : compter les établissements par département
    departements = Counter()
    for item in data:
        departements[item['DEPT']] += 1
    print(f"Nb d'établissements par département")
    for dept, nb in departements.items():
        print(f"\t{dept} : {nb}")
    print('-' * 15)

    # question 3 : Compter les établissements de type
    # ‘Centres Hospitaliers Spécialisés Lutte Maladies Mentales’ par département
    departements = Counter()
    for item in data:
        if item['TYPE_ETABLISSEMENT'] == 'Centres Hospitaliers Spécialisés Lutte Maladies Mentales':
            departements[item['DEPT']] += 1  
    print(f"Nb d'établissements de type 'Luttes Maladies Mentales' par département")
    for dept, nb in departements.items():
        print(f"\t{dept} : {nb}")
    print('-' * 15)

    # question 4 : Combien d’établissements ont ouvert au XXe siècle ? Au XXIe siècle ?
    siecles = Counter()
    for item in data:
        if item['DATE_OUVERTURE'].startswith('19'):
            siecles['20'] += 1
        elif item['DATE_OUVERTURE'].startswith('20'):
            siecles['21'] += 1
    print(f"Ouverture d'établissements par siècle")
    for siecle, nb in siecles.items():
        print(f"\t{siecle} : {nb}")
    print('-' * 15)


if __name__ == "__main__":
    main()