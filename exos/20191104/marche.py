# -*- coding: utf-8 -*-

"""
Python M1 2019-2020. 04/11/2019

Exo sur dictionnaires
"""

prix = {'bananes': 2,
        'clementine': 3.25,
        'pommes': 3,
        'poires': 3.5,
        'mangues': 3
        }

prix['raisin blanc'] = 4
prix['oranges'] = 2.5

panier = {'bananes': 2, 'raisin blanc': 1.5, 'pommes': 2, 'mangues': 3}
prix_panier = 0
for item, nb in panier.items():
    print(f"bananes : {prix[item] * nb}")
    prix_panier += prix[item] * nb

print(f"Prix total : {prix_panier}")

