# -*- coding: utf-8 -*-

"""
Correction de l'examen Python du 18/11/2019
Deuxième partie sur le fichier 'lecun_pos.txt'
"""

import csv
from collections import Counter

def main():
    input_file = 'lecun-pos.txt'
    words = [] # structure de données principale
    # liste de mots, chaque élément est un tuple (forme, pos)
    with open(input_file) as input:
        for line in input:
            line = line.rstrip()
            line_words = line.split(' ')
            for item in line_words:
                # pour chaque mot de la ligne on crée un tuple
                words.append(tuple(item.split('/')))

    # question 1 : Lister les 20 mots les plus fréquents du texte
    counts = Counter()
    for word in words:
        counts[word[0]] += 1
    print(f"20 mots les plus fréquents")
    for w, c in counts.most_common(20):
        print(f"\t{w} : {c}")
    print('-' * 15)
    
    # question 2 : Lister les mots (mot : étiquette(s)) qui se terminent par « ment »
    print(f"Mots qui se terminent par « ment »")
    for w, pos in words:
        if w.endswith('ment'):
            print(f"\t{w} : {pos}")
    print('-' * 15)

    # question 3 : Lister les mots (mot : étiquette(s)) du texte qui peuvent recevoir
    # plus d’une étiquette POS
    # Création d'un dictionnaire avec en clé un mot (c-a-d la forme) et en valeur un ensemble (set)
    # contenant les étiquettes qu'il peut recevoir
    # ex: 'Internet': {'NPP', 'NC'}
    w_pos = dict()
    for w, pos in words:
        if not(w in w_pos): # si le mot courant 'w' n'est pas encore une clé, on la crée avec un set vide
            w_pos[w] = set()
        w_pos[w].add(pos)
    # on ne retient pour résultat que les mots qui ont plus de 1 étiquette
    res = [(w, pos) for w, pos in w_pos.items() if len(pos) > 1]  
    for w, pos in res:
        print(f"\t{w} : {', '.join(pos)}")
    print('-' * 15)
    
if __name__ == "__main__":
    main()