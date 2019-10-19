#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## exo devinette

import random
import sys

print("Bonjour")
chiffre = random.randint(1,10)

i = 1
while(i <= 5):
    user = input("Essayez de trouver mon chiffre préféré [1-10]. Essai n° {} : ".format(i))
    try:
        user_int = int(user)
    except:
        sys.exit("Vous devez saisir un chiffre !")

    if not(1 <= user_int <= 10):
        raise ValueError("Entre 1 et 10 coco")
        
    if user_int == chiffre:
        print("Bravo ! Vous avez trouvé !")
        sys.exit()
    elif user_int < chiffre:
        print("Non. Trop petit.")
    elif user_int > chiffre:
        print("Non. Trop grand")
    i += 1

print("\nPerdu. Il fallait deviner {}".format(chiffre))
