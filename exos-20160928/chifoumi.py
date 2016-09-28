# -*- coding: utf-8 -*-

# chifoumi tout nul fait en cours de Python
# 21/09/2016

import random

coups = ["pierre", "feuille", "ciseaux"]
emojis = {'pierre': "\u270A", 'feuille': "\u270B", 'ciseaux': "\u270C"}

def draw():
    """
    Coup aléatoire au chifoumi 
    pas d'arguments
    """
    coup = coups[random.randint(0,2)]
    return coup

def rules(heckel, jeckel):
    """ 
    implémentation naïve des règles du chifoumi
    args : heckel (str), jeckel (str)
    """
    if heckel == jeckel:
        return("Égalité")
    else:
        if heckel == "pierre":
            if jeckel == "ciseaux":
                return("Heckel a gagné")
            else:
                return("Jeckel a gagné")
        elif heckel == "feuille":
            if jeckel == "pierre":
                return("Heckel a gagné")
            else:
                return("Jeckel a gagné")
        else:
            if jeckel == "feuille":
                return("Heckel a gagné")
            else:
                return("Jeckel a gagné")

            
heckel = draw()
jeckel = input("Vous êtes Jeckel.\nÀ vous de jouer [pierre, feuille, ciseaux] : ")
if not(jeckel in coups):
    raise ValueError("Tricheur !")
result = rules(heckel, jeckel)
print("Heckel : {} {}, Jeckel : {} {}, {}".format(heckel, emojis[heckel], jeckel, emojis[jeckel], result))
