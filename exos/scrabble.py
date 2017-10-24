import sys
import math

# https://www.codingame.com/ide/puzzle/scrabble
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def find_best_word(word_list):
    """
    Finds and returns the best word in a list
    according to his score
    """
    scores = {'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 
    'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1, 
    'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 
    'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 
    'y': 4, 'k': 5, 'j': 8, 'x': 8, 'q': 10,
    'z': 10}
    best = (0, "")
    for word in word_list:
        score = 0
        for c in word:
            score += scores[c]
        if score > best[0]:
            best = (score, word)
    return best[1]
    
    
def is_candidate(word, letters):
    """
    Checks wether a word can be written
    with the given set of letters
    """
    letters_ls = list(letters)
    #Mot trop long
    if len(word) > len(letters):
        return False
    for c in word:
        if not(c in letters_ls):
            return False
        else:
            letters_ls.pop(letters_ls.index(c))
    return True
        
        
words = []
n = int(input())
for i in range(n):
    w = input()
    words.append(w)
letters = input()

candidates_words = [word for word in words if is_candidate(word, letters)]
best_word = find_best_word(candidates_words)
print(best_word)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

