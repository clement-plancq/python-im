#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

file_handler = logging.FileHandler(filename="partitif.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(stream_handler)


soup = BeautifulSoup(open('index.html'), 'html.parser')
divs = soup.find_all('div', class_="structure")
logger.info("{} structure divs found".format(len(divs)))

verbs = dict()
for div in divs:                                  
    verbs[div['id']] = list()               
    examples = div.find_all('div', class_="exemple")
    logger.info("{} examples divs found for verb {}".format(len(examples), div['id']))
    for example in examples:
        tmp = dict()
        tmp['sp'] = example.find('div', class_="sp").string
        logger.debug(example.find('div', class_="sp").string)
        tmp['phrase'] = example.find('div', class_="phrase").string
        verbs[div['id']].append(tmp.copy())
        #example.decompose()
        
with open("verbs.json", "w") as f:
    json.dump(verbs, f, ensure_ascii=False)

#with open("out.html", "w") as out:
#    out.write(soup.prettify())
