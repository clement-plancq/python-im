#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Exo POO, classe Word
## CP

import re

class Word:
    """ Classe Word : définit un mot simple de la langue """

    type = "simple"

    def __init__(self, *args):
            self.form, self.lemma, self.pos = args

    def is_inflected(self):
        if self.form != self.lemma:
            return True
        else:
            return False

    def magic_compare(self, other_word):
        diff = []
        for key in self.__dict__.keys():
            if self.__dict__[key] != other_word.__dict__[key]:
                diff.append(key)
        return diff

    def __str__(self):
        return " ".join((self.form, self.lemma, self.pos))

class WordTreeTagger(Word):
    def __init__(self, formatted_str):
        """
        import a formatted_str in treetagger format
        """
        self.form, self.lemma, self.pos = formatted_str.split("\t")

class WordBrown(Word):
    def __init__(self, formatted_str):
        """
        import a formatted_str in brown format
        """
        self.form, self.lemma, self.pos = formatted_str.split("/")

class WordSem(Word):
    def __init__(self, formatted_str):
        """
        import a formatted_str in sem format (brown with no lemmas
        """
        self.form, self.pos = formatted_str.split("/")
        self.lemma = ""

        
def main():
    #obj = Word("été", "être", "V")
    #obj2 = Word("été", "été", "NOM")
    #print(obj.magic_compare(obj2))
    obj3 = WordBrown("percolais/percoler/V")
    print(obj3)
    obj4 = WordTreeTagger("claques	claque	NOM")
    print(obj4)
    print(obj3.magic_compare(obj4))
    obj5 = WordSem("le/DET")
    
if __name__ == '__main__':
    main()
