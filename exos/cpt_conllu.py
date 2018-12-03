# -*- coding: utf-8 -*-

"""
Parse un fichier conll-u et propose des informations sur le contenu :
nombre de phrases, nombre de mots, nombre d'items par POS
"""

def parse_file(file_path):
    """
    Parses input file and returns a list of list of tuples.
    Each sentence is a list of tuples, one tuple per token
    """
    sentences = list()
    with open(file_path, 'r') as input_f:
        sentence = list()
        for line in input_f:
            line = line.rstrip()
            # commentaire (sent_id ou text) 
            if line.startswith('#'):
                next
            # nouvelle phrase
            elif line == "":
                sentences.append(sentence)
                sentence = list()
            # token
            else:
                items = line.split('\t')
                sentence.append(tuple(items))
    return sentences

def cpt_tokens(sentences):
    """
    Counts and returns the number of tokens and words in a list of sentences (list of tuples)
    A word is a token which is not a punctuation
    Args:
        sentences: The list of sentences (list of tuples)
    Returns:
        nb of tokens, nb of words (tuple)
    """
    tokens = [tok for sentence in sentences for tok in sentence]
    words = [tok for sentence in sentences for tok in sentence if tok[3] != "PUNCT"]
    return len(tokens), len(words)

def cpt_tokens_pos(sentences, pos):
    """
    Counts and returns the number of tokens of a given POS
    Args:
        sentences: The list of sentences (list of tuples)
        pos: The POS tag (string)
    Returns:
        nb of tokens
    """
    tokens = [tok for sentence in sentences for tok in sentence if tok[3] == pos]
    return len(tokens)
    
def main():
    sentences = parse_file('../python-im/fr_gsd-ud-test.conllu')
    print(f"Le fichier contient {len(sentences)} phrases.")
    nb_tokens, nb_words = cpt_tokens(sentences)
    print(f"Le fichier contient {nb_tokens} tokens et {nb_words} mots.")
    pos = input(f"\n\nLes tokens de quel POS voulez-vous compter ? ")
    nb_tokens = cpt_tokens_pos(sentences, pos)
    print(f"Le fichier contient {nb_tokens} tokens annotés {pos}.")

    ment = [token for sentence in sentences for token in sentence if token[2][-4:] == 'ment' and token[3] != 'ADV']
    print(ment)

if __name__ == "__main__":
    main()