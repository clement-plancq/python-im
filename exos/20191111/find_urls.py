# -*- coding: utf-8 -*- 

"""
À l'aide du module requests trouver les liens hypertextes présents dans la page 
https://www.reddit.com/r/Python/ et les afficher sous la forme ancre: url.

La page d'accueil de Hacker News se prête mieux à cet exercice : https://news.ycombinator.com/news
"""

import requests
import re

#r = requests.get('https://www.reddit.com/r/Python/')
r = requests.get('https://news.ycombinator.com/news')
content = r.text
urls = re.findall(r'href="([^"]+?)".*?>(.+?)</a>', content)
for url in urls:
    print(f"{url[1]} : {url[0]}")
