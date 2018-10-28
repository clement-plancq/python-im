# -*- coding: utf-8 -*- 

# À partir de l’export csv de https://opendata.paris.fr/explore/dataset/logements_sociaux_finances_a_paris/ 
# vous compterez le nombre de logements sociaux financés par arrondissement. 
# Pour les cinq arrondissements où l’on trouve le plus de logements financés vous afficherez l’évolution par année avec l’année 2001 et l’année précédente comme références. 

from collections import Counter
import csv

logements = {}
cnt = Counter()
sep = ';'
with open('logements_sociaux_finances_a_paris.csv') as f_logements:
    logements_reader = csv.reader(f_logements, delimiter=sep)
    for row in logements_reader:
        if row[0] == 'adresse':
            continue
        annee = row[1]
        arrondissement = row[10]
        nb_logements = row[3]
        if not arrondissement in logements:
            logements[arrondissement] = Counter()
        logements[arrondissement][annee] += int(nb_logements)
        cnt[arrondissement] += int(nb_logements)

# La fonction most_common renvoie la liste des tuples par ordre décroissant
# (https://docs.python.org/3.7/library/collections.html#collections.Counter.most_common)
print("Logements sociaux par arrondissement")
for arrondissement, nb_logements in cnt.most_common():
    print(f"{arrondissement} : {nb_logements} logements")

print("-"*20)
print("Évolution pour les 5 arrondissements avec le plus de logements sociaux")
top_five = [arr for arr, nb in cnt.most_common(5)]
for arr in top_five:
    print(f"{arr} (total : {cnt[arr]})")
    for annee in sorted(logements[arr].keys()):
        if annee == "2001":
            print(f"\t{annee}: {logements[arr][annee]}")
        else:
            cmp_2001 = logements[arr][annee] - logements[arr]["2001"]
            # ajout du signe '+' si évolution positive
            if cmp_2001 > 0:
                cmp_2001 = '+' + str(cmp_2001)
            # ajout du signe '+' si évolution positive
            cmp_precedente = logements[arr][annee] - logements[arr][str(int(annee) - 1)]
            if cmp_precedente > 0:
                cmp_precedente = '+' + str(cmp_precedente)
            print(f"\t{annee}: {logements[arr][annee]} (2001: {cmp_2001}, année précédente: {cmp_precedente})")
