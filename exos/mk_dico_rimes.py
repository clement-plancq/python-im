#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pickle

def extract(filename):
    """ Extrait du fichier arguement les deux premiers champs
    arg : nom du fichier au format tsv
    return : list de tuples (ortho, phon)
    """
    words = []
    with open(filename, 'r') as f:
        f.readline() # première ligne
        for line in f:
            ortho, phon = line.split('\t')[0:2]
            words.append((ortho, phon))
    return words

def dico(lexique, n):
    """ Construit un dictionnaire de rimes de longueur n
    à partir d'un lexique phonétisé
    args : lexique [(ortho, phon)], n (int)
    return : dict { rime : [ortho1, ortho2, ...] } 
    """
    
    
def main():
    lexique = extract('noms-lexique.org.txt')
    try:
        f_lexique = open('lexique.pickle', 'wb')
    except:
        sys.exit('Error : cannot create lexique.pickle file')
    pickle.dump(lexique, f_lexique)

if __name__ == '__main__':
    main()
