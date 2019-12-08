# -*- coding: utf-8 -*-

"""
tests des fonctions utilisées dans concordance_zola.py
"""

import concordance_zola

def test_right_context():
    """
    Test contexte droit
    """
    sent = "Imagine un monde où les animaux nous mangeraient Ils feraient des ragoûts de nous, des soupes de nous, des burgers de nous"
    tokens = sent.split()
    r_context = concordance_zola.find_r_context(tokens, 6, 5)
    assert r_context == "mangeraient Ils feraient des ragoûts"

def test_left_context_easy():
    """
    Test contexte gauche sans difficulté
    """
    sent = "Imagine un monde où les animaux nous mangeraient Ils feraient des ragoûts de nous, des soupes de nous, des burgers de nous"
    tokens = sent.split()
    l_context = concordance_zola.find_l_context(tokens, 12, 5)
    assert l_context == "mangeraient Ils feraient des ragoûts"

def test_left_context_sixth_w():
    """
    Test contexte gauche avec mot pivot en 6e position
    Le contexte doit débuter par le premier token
    """
    sent = "Imagine un monde où les animaux nous mangeraient Ils feraient des ragoûts de nous, des soupes de nous, des burgers de nous"
    tokens = sent.split()
    l_context = concordance_zola.find_l_context(tokens, 5, 5)
    assert l_context == "Imagine un monde où les"

def test_left_context_first_w():
    """
    Test contexte gauche avec mot pivot en première position
    Résultat vide
    """
    sent = "Imagine un monde où les animaux nous mangeraient Ils feraient des ragoûts de nous, des soupes de nous, des burgers de nous"
    tokens = sent.split()
    l_context = concordance_zola.find_l_context(tokens, 0, 5)
    assert l_context == ""

def test_left_context_third_w():
    """
    Test contexte gauche avec mot pivot en 3e position
    Résultat chaîne de 2 tokens
    """
    sent = "Imagine un monde où les animaux nous mangeraient Ils feraient des ragoûts de nous, des soupes de nous, des burgers de nous"
    tokens = sent.split()
    l_context = concordance_zola.find_l_context(tokens, 2, 5)
    assert l_context == "Imagine un"
