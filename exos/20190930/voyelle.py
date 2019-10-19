#-*- coding: utf-8 -*-

"""
Reçoit un mot de l'utilisateur, compte le nombre de voyelles et de consonnes
"""

nb_voyelles = 0
nb_consonnes = 0
voyelles = ['a', 'à', 'â', 'e', 'é', 'è', 'ê', 'i', 'ï', 'o', 'ô', 'u', 'ù']

mot = input("Quel est votre mot ? ")

for char in mot:
    if char.isalnum():
        if char in voyelles:
            nb_voyelles += 1
        else:
            nb_consonnes += 1

print(f"Le mot {mot} contient {nb_voyelles} voyelles et {nb_consonnes} consonnes.")