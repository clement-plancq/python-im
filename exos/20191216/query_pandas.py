# -*- coding: utf-8 -*-

"""
Python M1 – INALCO
16/12/2019
Exemple de requête avec pandas
"""

import pandas

df = pandas.read_csv(open('panorama-des-festivals.csv'), sep=';')
rows = df.loc[df.Département.isin(['75', '77', '78', '91', '92', '93', '94', '95']), ['Nom de la manifestation', 'Commune principale']] 
print(rows.values)
