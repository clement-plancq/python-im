# -*- coding: utf-8 -*-

"""
Dans le texte ventre de Paris, trouvez tous les mots commençant par une majuscule.
Générez un fichier csv avec 3 colonnes : contexte gauche (5 mots), mot, contexte droit (5 mots).
"""
import csv

def file2tokens(filename):
    """
    Lit et découpe le fichier argument en tokens.
    Split sur l'espace
    Args:
        filename (str): le nom du fichier à traiter
    Returns:
        list: les tokens
    """
    tokens = []
    with open(filename) as input:
        for line in input:
            content = line.rstrip()
            tokens.extend(content.split())
    return tokens

def find_l_context(tokens, i, n=5):
    """
    Trouve et renvoie le contexte gauche d'un mot d'indice i
    dans la liste tokens
    Args:
        tokens (list): liste des tokens
        i (int): indice du mot pivot dans tokens
        n (int): longueur du contexte
    Returns:
        str: les n tokens à gauche du mot pivot
    """
    context = ""
    left_i = i-n
    # version améliorée si on veut récupérer le contexte gauche
    # même s'il est de longueur inférieure à n
    #while left_i < 0 and left_i <= i:
    #    left_i += 1
    if left_i >= 0:
        context_list = tokens[left_i:i]
        context = " ".join(context_list)
    return context

def find_r_context(tokens, i, n=5):
    """
    Trouve et renvoie le contexte droit d'un mot d'indice i
    dans la liste tokens
    Args:
        tokens (list): liste des tokens
        i (int): indice du mot pivot dans tokens
        n (int): longueur du contexte
    Returns:
        str: les n tokens à gauche du mot pivot
    """
    context = ""
    right_i = i+n+1 # la borne droite n'est pas renvoyée dans une tranche. Pour renvoyer le 5e mot on ajoute 1
    context_list = tokens[i+1:right_i] # i+1 pour ne pas renvoyer le token pivot
    context = " ".join(context_list)
    return context

def main():
    n = 10
    tokens = file2tokens('zola_ventre-de-paris.txt')
    writer = csv.writer(open('concordance.csv', 'w'), delimiter=',')
    for i in range(len(tokens)):
        token = tokens[i]
        if token[0].isupper():
            l_context = find_l_context(tokens, i, n)
            r_context = find_r_context(tokens, i, n)
            writer.writerow((l_context, token, r_context))

if __name__ == "__main__":
    main()