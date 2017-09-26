# -*- coding: utf-8 -*-

# chifoumi tout nul fait en cours de Python

import random

def draw(coups):
    """
    Coup aléatoire au chifoumi 
    pas d'arguments
    """
    coup = coups[random.randint(0,2)]
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
final_result = {'égalité': 0, 'jeckel': 0, 'heckel': 0}

for i in range(3):
    print("tour {}".format(i + 1))
    heckel = draw(coups)
    jeckel = input("Vous êtes Jeckel.\nÀ vous de jouer [pierre, feuille, ciseaux] : ")
    if not(jeckel in coups):
        raise ValueError("Tricheur !")
    winner = rules(jeckel, heckel)
    print("Heckel : {} {}, Jeckel : {} {}, {}".format(heckel, emojis[heckel], jeckel, emojis[jeckel], result[winner]))
    if winner == 0:
        final_result["égalité"] += 1
    elif winner == 1:
        final_result["jeckel"] += 1
    else:
        final_result["heckel"] += 1
        
print("Victoire finale de {}".format(max(final_result, key=final_result.get)))
