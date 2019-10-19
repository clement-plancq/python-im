#-*- coding: utf-8 -*-

"""
Détermine si un nombre donné par l'utilisateur est pair ou impair
"""

nombre = input("Tapez un nombre svp : ")

if int(nombre) % 2 == 0:
    print("C'est  un nombre pair !")
else:
    print("C'est un nombre impair !")

print("Au revoir")