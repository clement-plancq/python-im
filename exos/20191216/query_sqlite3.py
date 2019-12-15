# -*- coding: utf-8 -*-

"""
Python M1 – INALCO
16/12/2019
Exemple de requête sur base de données sqlite
"""

import sqlite3
import csv

DB_FILE = 'festival.db'
TABLE = 'festivals'

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
depts = ('75', '77', '78', '91', '92', '93', '94', '95')
query = f"SELECT nom, commune FROM {TABLE} WHERE departement IN ({', '.join(depts)})"
cursor.execute(query)
rows = cursor.fetchall()

print(rows)