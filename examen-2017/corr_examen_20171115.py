#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## correction de l'examen M2-IM du 15/11/2017

from collections import defaultdict
from collections import Counter
import re

def get_most_freq(data, n):
    """
    Finds the n most frequent items in data
    args: data (list of tuples (name, sex)), n
    returns: list of names (str)
    """
    data_dict = defaultdict(int)
    for name, sex in data:
        data_dict[name] += 1
    most_freq = sorted(data_dict, key=data_dict.get, reverse=True)
    return [(name, data_dict[name]) for name in most_freq[:n]]
    
def get_most_freq_c(data, n):
    """
    Finds the n most frequent items in data
    args: data (list of tuples (name, sex)), n
    returns: list of names (str)
    """
    cnt = Counter()
    for name, sex in data:
        cnt[name] += 1
    return cnt.most_common(n)

def main():
    file_name = "Equides_2016.csv"
    poneys = []
    autres = defaultdict(int)
    with open(file_name, "r", encoding="iso-8859-1") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) != 8:
                continue
            # uniquement les poneys
            if "PONEY" in cols[0]:
                #on conserve le noms et le sexe de chaque poney dans un tuple
                poneys.append((cols[5], cols[1])) 
                # uniquement les pas poneys nés en G-B
            elif "GRANDE-BRETAGNE" in cols[4]:
                autres[cols[0]] += 1

    # noms de poneys les + fréquents
    for poney in get_most_freq_c(poneys, 30):
        print("{} {}".format(poney[0], poney[1]))
    print("-"*30)
      
    # noms se terminant par 'a', 'ah' ou 'at'
    pat = re.compile("A[HT]?$")
    poneys_a = [poney for poney in poneys if pat.search(poney[0])]
    for poney in get_most_freq_c(poneys_a, 10):
        print("{} {}".format(poney[0], poney[1]))
    print("-"*30)
    
    # noms se terminant par une consonne suivie de "ine"
    pat = re.compile("[^AEIOUY]INE$")
    poneys_ine = [poney for poney in poneys if pat.search(poney[0])]
    for poney in get_most_freq_c(poneys_ine, 10):
        print("{} {}".format(poney[0], poney[1]))
    print("-"*30)
    
    # nom le plus fréquent pour un mâle
    poneys_m = [poney for poney in poneys if poney[1] == "M"]
    for poney in get_most_freq_c(poneys_m, 1):
        print("{} {}".format(poney[0], poney[1]))
    print("-"*30)
    
    # nom le plus fréquent pour une femelle
    poneys_f = [poney for poney in poneys if poney[1] == "F"]
    for poney in get_most_freq_c(poneys_f, 1):
        print("{} {}".format(poney[0], poney[1]))
    print("-"*30)

    # les chevaux nés en G-B par race en ordre décroissant
    most_freq = sorted(autres, key=autres.get, reverse=True)
    for autre in most_freq[:10]:
        print("{} : {}".format(autre, autres[autre]))
    
if __name__ == '__main__':
    main()
