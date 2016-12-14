#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# examen python M2 - 07/12/2016

import re

def nb_emprunts(data):
    """
    calcule le nombre d'emprunts dans le jeu de données argument
    arg: data (list of lists)
    return: int
    """
    res = 0
    for item in data:
        res += int(item[-1])
    return res

def nb_emprunts_support(data):
    """
    calcule le nombre d'emprunts dans le jeu de données argument
    par type de support
    arg: data (list of lists)
    return: dict
    """
    dico = dict()
    for item in data:
        if not item[0] in dico:
            dico[item[0]] = int(item[-1])
        else:
            dico[item[0]] += int(item[-1])
    return dico

def exclam_interro(data):
    """
    trouve les titres contenant un point d'exclamation ou un point d'interrogation
    arg: data (list of lists)
    return: list of list
    """
    res = []
    pat = re.compile("(\?|!)")
    for item in data:
        if pat.search(item[2]):
            res.append(item)
    return res

def main():
    
    data = []

    with open("les-titres-les-plus-pretes.csv", "r") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith("Support;Auteur"):
                continue
            data.append(line.split(";"))

    print("Nombre d'emprunts total : ")
    nb = nb_emprunts(data)
    print(nb)
    print("\n---------------------------\n")

    print("Nombre d'emprunts par type de support : ")
    nb_support = nb_emprunts_support(data)
    for support in sorted(nb_support.keys(), key= lambda x: nb_support[x]):
        print("{} : {}".format(support, nb_support[support]))
    print("\n---------------------------\n")

    print("Titres avec un point d'exclamation ou un point d'interrogation : ")
    exclam = exclam_interro(data)
    nb_exclam = len(exclam)
    nb_exclam_jeunesse = 0
    nb_exclam_autre = 0
    for item in exclam:
        if "jeunesse" in item[0]:
            nb_exclam_jeunesse += 1
        else:
            nb_exclam_autre += 1
    print(nb_exclam)
    print("% jeunesse : {0:.2f}".format((nb_exclam_jeunesse / nb_exclam)*100))
    print("% autre : {0:.2f}".format((nb_exclam_autre / nb_exclam)*100))
            
if __name__ == '__main__':
    main()
