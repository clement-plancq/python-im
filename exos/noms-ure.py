#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Exo cours Python IM - 2016/2017
## Recherche des noms en -ure dans lexique381.txt
## CP

import argparse
import re
import sys

def main():
    parser = argparse.ArgumentParser(description="Find noms ending with -ure in lexique.org csv file")
    parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
    parser.add_argument("file", help="lexique file (csv, utf8)")
    parser.add_argument("suff", help="suffix to look for")
    parser.add_argument("--phon", help="wether searchs on phonetic form or not", action="store_true")
    args = vars(parser.parse_args())


    res = []

    pat = re.compile("^.*" + args['suff']+ "$")


    ## extract
    try:
        with open(args['file'], 'r') as f:
            for line in f:
                line = line.rstrip()
                features = line.split("\t")
                if features[3] == "NOM": # On ne prend en compte que les noms
                    if(args['phon']): # recherche sur phon activée
                        if pat.search(features[1]):
                            res.append(tuple(features[0:6]))

                    else:
                        if pat.search(features[2]):
                            res.append(tuple(features[0:6]))
                else:
                    continue
    except IOError:
        print("Cannot read file {}".format(file_name), file=sys.stderr)
        sys.exit()

    ## report
    lemmes = set([word[2] for word in res])
    
    print("\n".join(sorted(lemmes)))
    
if __name__ == '__main__':
    main()
