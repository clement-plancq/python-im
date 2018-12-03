# -*- coding: utf-8 -*-

"""
Helps parsing a conllu file into sentences and words
See http://universaldependencies.org/format.html 
"""
class Word:
    """
    A word (i.e. a line of a conll file) with its features
    """
    def __init__(self, nid='_', form='_', lemma='_', upos='_', xpos='_', 
    feats='_', head='_', dep_rel='_', deps='_', misc='_'):
        self.nid = nid
        self.form = form
        self.lemma = lemma
        self.upos = upos
        self.xpos = xpos
        self.feats = feats
        self.head = head
        self.dep_rel = dep_rel
        self.deps = deps
        self.misc = misc
        
    def __str__(self):
        text = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
            self.nid, self.token, self.lemma, self.upos, self.xpos, self.feats,
            self.head, self.dep_rel, self.deps, self.misc)
        return text

class Sentence:
    """
    A sentence is composed of a list of Word objects and a list of comments (str)
    """
    def __init__(self):
        self.words = list()
        self.sent_id = ""
        self.text = ""

    def __str__(self):
        lines = ""
        lines += "# sent_id = "
        lines += self.sent_id + "\n"
        lines += "# text = "
        lines += self.text + "\n"
        for word in self.words:
            lines += str(word)
            lines += "\n"
        return lines
    
    def add_word(self, line):
        """
        Add a Word to the words list
        Args:
            line (str): a line of an orfeo file with a word informations
        """
        features = line.split('\t')
        if features:
            self.words.append(Word(*features))

    def length(self, with_punct=True):
        if with_punct:
            return len(self.words)
        else:
            return len([word for word in self.words if word.upos != 'PUNC'])

def parse_file(file):
    """
    Turns a file into a list of sentences
    Args: 
        file (str): the file path
    Return:
        list of dicts (sents) of tuples (words)
    """
    sents = list()
    sent = Sentence()
    with(open(file, 'r')) as f:
        for line in f:
            line = line.rstrip()
            if line == "":
                if sent.length() > 0:
                    sents.append(sent)
                    sent = Sentence()
            elif line[0] == "#":
                if 'sent_id' in line:
                    meta, meta_value = line.split('=')
                    sent.sent_id = meta_value.strip()
                elif 'text' in line:
                    meta, meta_value = line.split('=')
                    sent.text = meta_value.strip()
            else:
                sent.add_word(line)
        # au cas où le fichier se termine sans ligne vide        
        if sent.length() > 0:
            sents.append(sent)
            sent = Sentence()   
    return sents