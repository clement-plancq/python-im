#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Exo POO, classe Word
## CP

import re

class Word:
    """ Classe Word : définit un mot simple de la langue """

    type = "simple"

    def __init__(self, *args):
        if len(args) == 1:
            self.form, self.lemma, self.pos = self.__import__(args[0])
        
        elif len(args) == 3:
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

    def __import__(self, formatted_str):
        """
        import a formatted_str in treetagger or brown format
        return a tuple (form, lemma, pos)

        arg : str
        return : tuple
        """
        pattern = re.compile("(.+)[/\t](.+)[/\t](.+)")
        res = pattern.search(formatted_str)
        if res:
            assert len(res.groups()) == 3
            return res.groups()
        else:
            None

    def __str__(self):
        return " ".join((self.form, self.lemma, self.pos))
            
def main():
    #obj = Word("été", "être", "V")
    #obj2 = Word("été", "été", "NOM")
    #print(obj.magic_compare(obj2))
    obj3 = Word("percolais/percoler/V")
    print(obj3)
    obj4 = Word("percolais	percoler")
    print(obj4)

if __name__ == '__main__':
    main()
