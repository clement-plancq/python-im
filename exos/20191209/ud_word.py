
# -*- coding: utf-8 -*-

"""
Classe Word écrite pendant la séance du 9 décembre 2019 avec les étudiantes
Et oui seules les filles ont bravé les pbs de transport
"""

class Word():
    """
    Un mot au format UD
    On ne conserve que les infos : id, form, lemma, pos
    """
    def __init__(self, id, form, lemma, pos):
        self.id = id
        self.form = form
        self.lemma = lemma
        self.pos = pos

    def tostring(self):
        res = "/".join((self.form, self.lemma, self.pos))
        #res = f"{self.form}/{self.lemma}/{self.pos}"
        return res
    
    def is_inflected(self):
        """
        Vérifie si la forme du mot est fléchie ou non
        i.e form != lemma
        Returns:
            bool: True or False
        """
        if self.form == self.lemma:
            return True
        else:
            return False

def main():
    w = Word('1', 'cela', 'cela', 'PRON')
    print(w.tostring())

if __name__ == "__main__":
    main()