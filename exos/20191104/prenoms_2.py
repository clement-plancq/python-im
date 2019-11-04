# -*- coding: utf-8 -*-

"""
Python M1 2019-2020. 04/11/2019
Travail sur l’export csv de Liste des prénoms 2004 à 2018 (opendata.paris.fr)

    Quels sont les 10 prénoms les plus courants
    Quels sont les 10 prénoms féminins et masculins les plus courants
    Indiquez le nombre de naissances par an et par sexe
    Quels sont les prénoms masculins et féminins qui sont en baisse en 2017 et 2018

Deuxième version avec utilisation de DictReader du module csv
"""
import csv
from collections import Counter, defaultdict


def file2list(csv_file):
    """
    Read the given file into a list of dicts with csv.DictReader

    Args:
        csv_file: the path of the csv file
    Returns: 
        list of dicts. One line per item. Each line is a dict
    """
    content = []
    with open(csv_file) as input:
        reader = csv.DictReader(input, delimiter=';')
        for item in reader:
            content.append(item)
    return content

content = file2list("liste_des_prenoms.csv")

# Question 1 : quels sont les 10 prénoms les plus courants
prenoms = Counter()
for line in content:
        prenoms[line['Prenoms']] += int(line['Nombre'])

print("Question 1")
print("Les 10 prénoms les plus courants sont :")
for prenom, nb in prenoms.most_common(10):
    print(f"\t{prenom} : {nb}")
print("\n-----\n")

# Question 2 : quels sont les 10 prénoms féminins et masculins les plus courants
prenoms_m = Counter()
prenoms_f = Counter()

for line in content:
    if line['Sexe'] == 'F':
        prenoms_f[line['Prenoms']] += int(line['Nombre'])
    elif line['Sexe'] == 'M':
        prenoms_m[line['Prenoms']] += int(line['Nombre'])

print("Question 2")
print("Les 10 prénoms féminins les plus courants sont :")
for prenom, nb in prenoms_f.most_common(10):
    print(f"\t{prenom} : {nb}")

print("Les 10 prénoms masculins les plus courants sont :")
for prenom, nb in prenoms_m.most_common(10):
    print(f"\t{prenom} : {nb}")
print("\n-----\n")

# Question 3 : Indiquez le nombre de naissances par an et par sexe
# on veut avoir une structure de données de type dictionnaire de Counter
# ex: '2017': {'M': 335, 'F': 455}, '2016': {'M': 298, 'F': 422}, …
prenoms = defaultdict(Counter)

for line in content:
        if line['Sexe'] == 'F':
            prenoms[line['Annee']]['F'] += int(line['Nombre'])
        elif line['Sexe'] == 'M':
            prenoms[line['Annee']]['M'] += int(line['Nombre'])

print("Question 3")
print("Nombre de naissances par an et par sexe :")
for year in sorted(prenoms.keys()):
    print(f"{year} : ")
    for gender, nb in prenoms[year].items():
        print(f"\t{gender} : {nb}")
print("\n-----\n")

# Question 4 : Quels sont les prénoms masculins et féminins qui sont en baisse en 2017 et 2018 ?
# 'Clément_M': {'2016': 108, '2017': 88, '2018': 82}, 'Cléo_F': {'2016': 17, '2017': 16, '2018': 18}
prenoms = defaultdict(Counter)

for line in content:
    prenoms[line['Prenoms'] + '_' + line['Sexe']][line['Annee']] += int(line['Nombre'])

# on fait le choix de ne pas prendre en compte les prènoms qui n'apparaissent pas dans l'année 
## prénoms masculins en baisse en 2017
masc_2017 = [prenom[:-2] for prenom in prenoms if prenom.endswith('_M') and prenoms[prenom]['2017'] < prenoms[prenom]['2016'] and prenoms[prenom]['2017'] != 0]
print(f"prenoms masculins en baisse en 2017 : {', '.join(sorted(masc_2017))}")
print()

## prénoms masculins en baisse en 2018
masc_2018 = [prenom[:-2] for prenom in prenoms if prenom.endswith('_M') and prenoms[prenom]['2018'] < prenoms[prenom]['2017'] and prenoms[prenom]['2018'] != 0]
print(f"prenoms masculins en baisse en 2018 : {', '.join(sorted(masc_2018))}")
print()

## prénoms féminins en baisse en 2017
fem_2017 = [prenom[:-2] for prenom in prenoms if prenom.endswith('_F') and prenoms[prenom]['2017'] < prenoms[prenom]['2016'] and prenoms[prenom]['2017'] != 0]
print(f"prenoms féminins en baisse en 2017 : {', '.join(sorted(fem_2017))}")
print()

## prénoms masculins en baisse en 2017
fem_2018 = [prenom[:-2] for prenom in prenoms if prenom.endswith('_F') and prenoms[prenom]['2018'] < prenoms[prenom]['2017'] and prenoms[prenom]['2018'] != 0]
print(f"prenoms féminins en baisse en 2018 : {', '.join(sorted(fem_2018))}")
