# -*- coding: utf-8 -*-

# chifoumi tout nul fait en cours de Python

import random

def draw(coups):
    """
    Coup aléatoire au chifoumi 
    pas d'arguments
    """
    coup = random.choice(coups)
    return coup

def rules(player_1, player_2):
    """ 
    implémentation naïve des règles du chifoumi
    args: player_1 (str), player_2 (str)
    return: 0 if equality, 1 if player_1 wins, 2 if player_2 wins

    """
    if player_1 == player_2:
        return 0
    else:
        if player_1 == "pierre":
            if player_2 == "ciseaux":
                return 1
            else:
                return 2
        elif player_1 == "feuille":
            if player_2 == "pierre":
                return 1
            else:
                return 2
        else:
            if player_1 == "feuille":
                return 1
            else:
                return 2

coups = ["pierre", "feuille", "ciseaux"]
emojis = {'pierre': "\u270A", 'feuille': "\u270B", 'ciseaux': "\u270C"}
result = ['égalité', 'victoire', 'défaite']
final_result = {'égalité': 0, 'sarah': 0, 'skynet': 0}

for i in range(3):
    print("tour {}".format(i + 1))
    skynet = draw(coups)
    sarah = input("Vous êtes Sarah.\nÀ vous de jouer [pierre, feuille, ciseaux] : ")
    if not(sarah in coups):
        raise ValueError("Tricheur !")
    winner = rules(sarah, skynet)
    print(f"skynet : {skynet} {emojis[skynet]}, sarah : {sarah} {emojis[sarah]}, {result[winner]}")
    if winner == 0:
        final_result["égalité"] += 1
    elif winner == 1:
        final_result["sarah"] += 1
    else:
        final_result["skynet"] += 1
        
print("Victoire finale de {}".format(max(final_result, key=final_result.get)))
