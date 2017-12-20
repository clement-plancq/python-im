#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Comptes et vérifications de fichiers .conll
"""

import argparse
import glob
import os
from collections import defaultdict

class Word:
    """
    A word (i.e. a line of a conll file) with its features
    """
    def __init__(self, nid='_', token='_', lemma='_', pos='_', pos2='_', 
    feats='_', head='_', dep_rel='_', deps='_', misc='_'):
        self.nid = nid
        self.token = token
        self.lemma = lemma
        self.pos = pos
        self.pos2 = pos2
        self.feats = feats
        self.head = head
        self.dep_rel = dep_rel
        self.deps = deps
        self.misc = misc

    def __str__(self):
        text = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
            self.nid, self.token, self.lemma, self.pos, self.pos2, self.feats,
            self.head, self.dep_rel, self.deps, self.misc)
        return text

def file2sentences(file):
    """
    Turns a file into a list of sentences
    args: file
    return: list of lists (sents) of tuples (words)
    """
    sents = list()
    sents.append([])
    ln = 0
    with(open(file, 'r')) as f:
        for line in f:
            ln += 1
            if line.startswith('#'):
                continue
            line = line.rstrip()
            if line == "":
                sents.append([])
                continue
            sents[-1].append((ln, line))
    sents = [sent2words(sent) for sent in sents if len(sent) > 0]
    return sents

def sent2words(sentence):
    """ 
    Turns a sentence into a list of Word objects
    arg : sentence (list of tuples (line number, str))
    return : list of tuples (ln, Words objects)
    """
    words = []
    for ln, word in sentence:
        feats = word.split('\t')
        words.append((ln, Word(*feats)))
    return words

def check_deps(sent):
    """
    Checks that each dependency link refer to an existing word id
    Args: list of tuples (ln, word objs)
    Return: list of tuples (ln, word objs) with false head
    """
    headless_words = []
    ids = [word.nid for ln, word in sent]
    for ln, word in sent:
        # on zappe les contractés
        if "-" in word.nid:
            continue
        if not (word.head in ids) and word.head != '0':
            headless_words.append((ln, word)) 
    return headless_words

def check_token_nid(sent):
    """
    Makes sure that the tokens have correct nid
    Args: list of tuples (ln, word objs)
    Return: list of tuples (ln, word objs) with wrong ids
    """
    wrongs_nid = []
    i = 1
    for ln, word in sent:
        # on zappe les contractés
        if "-" in word.nid:
            continue
        if int(word.nid) != i:
            wrongs_nid.append((ln, word))
        i += 1
    return wrongs_nid    
        
def check_root(sent):
    """
    Makes sure that a root token has a 0 dep_rel attribute
    """
    wrong_roots = []
    wrong_roots.extend([(l, w) for l, w in sent if w.head == '0' and w.dep_rel != 'root'])
    wrong_roots.extend([(l, w) for l, w in sent if w.head != '0' and w.dep_rel == 'root'])
    return wrong_roots
    
def main():
    parser = argparse.ArgumentParser(description="comptes et vérifications de fichiers au format conll.")
    parser.add_argument('file', help='chemin du fichier')
    
    args = vars(parser.parse_args())

    
    orfeo_file = args['file']
    sents = file2sentences(orfeo_file)
    print("Nombre de phrases : {}".format(len(sents)))
    words = [word for sent in sents for word in sent if word[1].pos != "PUNCT"]
    print("Nombre de mots : {}".format(len(words)))
    print("Wrong deps : ")
    for ln, word in [word for sent in sents for word in check_deps(sent)]:
        print(ln, word)
    print("Wrongs nids : ")
    for ln, word in [word for sent in sents for word in check_token_nid(sent)]:
        print(ln, word)

    # Sujets par pos
    subjs_pos = defaultdict(int)
    subjs = [word for sent in sents for word in sent if word[1].dep_rel.startswith("nsubj")]
    print(len(subjs))
    for subj in subjs:
        subjs_pos[subj[1].pos] += 1
    print("\nSujets par pos :")
    for pos in subjs_pos.keys():
        print("{} : {}".format(pos, subjs_pos[pos]))

    # Têtes qui ont au moins deux dépendants 'adj'
    print("-"*30)
    print("Tête qui ont au moins deux dépendants 'ADJ'")
    for sent in sents:
        adjs_heads = [word.head for ln, word in sent if word.pos == "ADJ"]
        heads_2 = [head for head in adjs_heads if adjs_heads.count(head) > 1]
        heads_2_w = [word for ln, word in sent if word.nid in heads_2]
        for word in heads_2_w:
            print("{} ({})".format(word.token, ", ".join([word.token for ln, word in sent if word.head in heads_2 and word.pos == "ADJ"])))
        
if __name__ == "__main__":
    main()
