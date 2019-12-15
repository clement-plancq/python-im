# -*- coding: utf-8 -*-

"""
Python M1 – INALCO
16/12/2019
Création et ajout de données dans la bd festivals.db
Attention la base de données doit exister avant le lancement du script
"""

import sqlite3
import csv

DB_FILE = 'festival.db'
TABLE = 'festivals'


def get_csv_data(input_file, sep=';'):
    """
    Read the given csv file with csv.DictReader
    Returns content in a list of dict
    """
    data = []
    with open(input_file) as input:
        reader = csv.DictReader(input, delimiter=sep)
        for row in reader:
            data.append(row)
    return data


def populate_db(data, db_file, table, init=True):
    """
    Populate table in sqlite db file with the given data
    Args:
        data (list of dict): the data
        db_file (str): the db_file path
        table (str): the table to be populated
        init (bool): wether the table should be dropped before being populated
    """
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    conn.execute(f"drop table if exists {table}")
    conn.commit()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS `{table}` (\
  `nom` varchar(50) NOT NULL,\
  `region` varchar(50) NOT NULL,\
  `domaine` varchar(250) NOT NULL DEFAULT '',\
  `complement_domaine`  varchar(250) NOT NULL DEFAULT '',\
  `departement` varchar(5) DEFAULT NULL,\
  `commune` varchar(5) DEFAULT NULL);")

    for item in data:
        cursor.execute(f"insert into {table} values (?, ?, ?, ?, ?, ?)", item)
    conn.commit()
    conn.close()

def main():
    data = get_csv_data('panorama-des-festivals.csv')
    selected_keys = ['Nom de la manifestation','Région','Domaine','Complément domaine','Département','Commune principale']
    filtered_data = []
    for row in data:
        tmp = []
        for key, value in row.items():
            if key in selected_keys:
                tmp.append(value)
        filtered_data.append(tmp)
    populate_db(filtered_data, DB_FILE, TABLE)

if __name__ == "__main__":
    main()
