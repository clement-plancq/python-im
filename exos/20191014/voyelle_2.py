#-*- coding: utf-8 -*-

"""
Reçoit un mot de l'utilisateur, compte le nombre d'occurrences de chaque voyelle et chaque consonne
"""

from collections import Counter

cnt_voyelles = Counter()
cnt_consonnes = Counter()
voyelles = ['a', 'à', 'â', 'e', 'é', 'è', 'ê', 'i', 'ï', 'o', 'ô', 'u', 'ù']

mot = input("Quel est votre mot ? ")

for char in mot:
    if char.isalnum():
        if char in voyelles:
            cnt_voyelles[char] += 1
        else:
            cnt_consonnes[char] += 1

print(f"Le mot {mot} contient {len(cnt_voyelles)} voyelles et {len(cnt_consonnes)} consonnes.")
print("Voyelles : ")
for item in cnt_voyelles:
    print(f"\t{item} : {cnt_voyelles[item]}")

print("Consonnes : ")
for consonne, occ in cnt_consonnes.items():
    print(f"\t{consonne} : {occ}")