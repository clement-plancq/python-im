#-*- coding: utf-8 -*-
"""
Jeu du pendu en mode console, version un peu améliorée
Cette fois le programme est capable de remplacer toutes
les occurrences d'un caractère dans la chaîne de car.
"""

def gen_user_word(word, user_word, user_char, sep="_"):
    """
    for each occurrences of user_char in word, replace '_' by
    user_char in user_word
    returns the new user_word
    """
    indexes = [i for i, letter in enumerate(word) if letter == user_char]
    for i in indexes:
        user_word[i] = user_char
    return user_word

def gen_user_word_2(word, user_word, user_char, sep="_"):
    """
    Same as gen_user_word with 'index' in a loop
    for each occurrences of user_char in word, replace '_' by
    user_char in user_word
    returns the new user_word
    """
    moving_index = 0
    while True:
        try:
          char_index = word.index(user_char, moving_index)
          user_word[char_index] = user_char
          moving_index = char_index + 1
          print(moving_index)
        except ValueError:
            break
    return user_word

sep = "_"
word = "assise"
user_word = list(sep*len(word))
user_tries = int(len(word) * 1.5)

print(f"Saurez-vous deviner ce mot ? vous avez {user_tries} chances")
print(" ".join(user_word))

while True:
    if not(sep in user_word):
        print(f"Gagné ! Le mot était bien {word}")
        break

    user_char = input("une proposition ? ")
    if user_char in word:
        print("Oui !")
        user_word = gen_user_word(word, user_word, user_char)
    else:
        print('Raté !')
        user_tries -= 1
        if user_tries == 0:
            print(f"Vous avez perdu ! Le mot à deviner était {word}")
            break
    print(f"Il vous reste {user_tries} chances")
    print(" ".join(user_word))

