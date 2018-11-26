# -*- coding: utf-8 -*-

""" conseillers de Paris -- préparation de l'examen Python1 du 19/11/2018 """

from collections import Counter
import re

def read_csv_file(csv_file, sep=";"):
    """
    Read the csv file and return the content as a list of tuples
    """
    data = list()
    with open(csv_file) as csv_input:
        csv_input.readline()
        for line in csv_input:
            line = line.rstrip()
            data.append(tuple(line.split(sep)))
    return data

def count_m_w(data):
    """
    Count men and women in the given data (list of tuples)
    Sex is in the 3rd column
    """
    men = [item for item in data if item[2] == "M."]
    women = [item for item in data if item[2] == "Mme"]
    return len(men), len(women)

def filter_by_date(data, year):
    """
    Filter the given data (list of tuples) before the given year
    Date is in the first columm
    """
    res_data = list()
    for item in data:
        date = item[0]
        b_date, e_date = date.split('-')
        if int(b_date) < int(year):
            res_data.append(item)
    return res_data

def data2counter(data):
    """
    Turn data (list of tuples) into a Counter object based on the name (column 4-5)
    """
    cpt = Counter()
    for item in data:
        name = item[3] + " " + item[4]
        cpt[name] += 1
    return cpt

def main():
    conseillers = read_csv_file("les-conseillers-de-paris-de-1977-a-2014.csv")    
    # question 1 : combien de conseillers
    print("Question 1")
    print(f"Il y a {len(conseillers)} conseillers dans le fichier")
    print("-"*50)

    # question 2 : combien de femmes, combien d'hommes
    print("Question 2")
    count_conseillers_m, count_conseillers_w = count_m_w(conseillers)
    print(f"Il y a {count_conseillers_w} femmes et {count_conseillers_m} hommes")
    print("-"*50)

    # question 3 : combien de femmes, combien d'hommes avant 1995
    print("Question 3")
    conseillers_before_95 = filter_by_date(conseillers, '1995')
    count_conseillers_m, count_conseillers_w = count_m_w(conseillers_before_95)
    print(f"Il y a {count_conseillers_w} femmes et {count_conseillers_m} hommes avant 1995")
    print("-"*50)

    # question 4 : combien de conseiller avec un nom à particule
    print("Question 4")
    cons_particules = [(cons[3], cons[4]) for cons in conseillers if re.search(r'[( ]d[uei\'][) ]',cons[4])]
    for name in set(cons_particules):
        print(name[0], name[1])
    print("-"*50)

    # question 5 : compter le nb de conseillers ayant 1 mandat, 2 mandats, 3 mandats, …, 6 mandats
    print("Question 5")
    cpt_conseillers = data2counter(conseillers)
    for value in range(1, 7):
        cons = [cons for cons in cpt_conseillers.keys() if cpt_conseillers[cons] == value]
        print(f"{len(cons)} conseillers avec {value} mandat(s)")
    print("-"*50)


if __name__ == "__main__":
    main()