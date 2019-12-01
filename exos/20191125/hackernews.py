# -*- coding: utf-8 -*-

"""
Exo sur la page d'accueil de HackerNews
"""
import requests
import re

# Si utilisation du module requests pour récupérer la page d'accueuil
#r = requests.get('https://news.ycombinator.com/news')
#content = r.text

# Sinon en local
file = "hackernews.html"
content = ""
with open(file) as input:
    content = input.read()

domains = re.findall(r'<span class="sitestr">([^<]+?)</span>', content)
#print(domains)
comments = re.findall(r'([0-9]+)&nbsp;comments|discuss</a>', content)
#print(comments)

for domain, nb_comments in zip(domains, comments):
    print(f"{domain} : {nb_comments}")