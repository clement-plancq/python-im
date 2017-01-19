#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Extract examples from the input html file
## Creates a json file with all the examples and a minified html file

from bs4 import BeautifulSoup
import sys
import json
import logging
import argparse




def main():

    ## argparse
    parser = argparse.ArgumentParser(description="Extract examples from partitif html file")
    parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
    parser.add_argument("file", help="html file")
    parser.add_argument("--json-file", help="json file with examples", default="examples.json")
    parser.add_argument("--min-file", help="minified html file", default="index-min.html")
    args = vars(parser.parse_args())
    verbose = args['verbose']



    soup = BeautifulSoup(open(args['file']), 'html.parser')
    divs = soup.find_all('div', class_="structure")
    if verbose: print("{} structure divs found".format(len(divs)), file=sys.stderr)
    
    verbs = dict()
    for div in divs:                                  
        verbs[div['id']] = list()               
        examples = div.find_all('div', class_="exemple")
        if verbose: print("{} examples divs found for verb {}".format(len(examples), div['id']), file=sys.stderr)
        for example in examples:
            tmp = dict()
            tmp['sp'] = example.find('div', class_="sp").string
            tmp['phrase'] = example.find('div', class_="phrase").string
            verbs[div['id']].append(tmp.copy())
            example.decompose()
            
    with open(args['json_file'], "w") as f:
        json.dump(verbs, f, ensure_ascii=False)
                
    with open(args['min_file'], "w") as out:
        out.write(soup.prettify())
                
    
    

if __name__ == '__main__':
    main()
