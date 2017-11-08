#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Exo http://www.pythonchallenge.com/pc/def/map.html
## k -> m, o -> q, e -> g (on avance de deux lettres pour déchiffrer)
## CP

letters = list("abcdefghijklmnopqrstuvwxyz")
letters_2 = list(letters[2:] + letters[:2])
# on aurait aussi pu faire chr(ord(c) + 2) mais on a un résultat faux pour y et z
table = {i:j for i, j in zip(letters, letters_2)}
msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
res = msg.translate(str.maketrans(table))
print(res)
