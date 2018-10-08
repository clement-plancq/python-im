#-*- coding: utf-8 -*-
"""
Jeu du pendu en mode console, version simplifiée
On se sert de la fonction 'index' (https://docs.python.org/3.6/tutorial/datastructures.html)
pour trouver la position de la lettre proposée dans le mot à deviner
'index' ne renvoie que la position du premier item trouvé
pour 'assis' on ne trouvera que le premier 's' par exemple
"""
import random

def get_words(input_file):
    res_words = list()
    with open(input_file) as input_f:
        for line in input_f:
            res_words.append(line.rstrip())
    return res_words

words = get_words('lexique_fr.txt')
word = words[random.randint(0,len(words))]
user_word = list("_"*len(word))
user_tries = int(len(word) * 1.5)

print(f"Saurez-vous deviner ce mot ? vous avez {user_tries} chances")
print(" ".join(user_word))

while True:
    if not("_" in user_word):
        print(f"Gagné ! Le mot était bien {word}")
        break

    user_char = input("une proposition ? ")
    if user_char in word:
        print("Oui !")
        index = word.index(user_char)
        user_word[index] = user_char
    else:
        print('Raté !')
        user_tries -= 1
        if user_tries == 0:
            print(f"Vous avez perdu ! Le mot à deviner était {word}")
            break
    print(f"Il vous reste {user_tries} chances")
    print(" ".join(user_word))

