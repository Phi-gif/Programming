#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:35:29 2019

@author: renaudin
"""

from fonctions import readconf
import fonctions

conf_file = "minmax.conf"

config = readconf(conf_file)
print(config)
if config["read"]=="keyboard":
    print("lecture des données depuis le clavier")
    L=fonctions.read_from_keyboard()
elif config["read"]=="arg":
    print("lecture des données depuis la ligne de commande")
    L=fonctions.read_from_cmdline()
elif config["read"]=="file":
    print("lecture des données depuis file")
    if "datafile" in config:
        filename = config["datafile"]
        print(filename)             
    else:
        filename = input("Entrer le nom de ce fichier:")
    L = fonctions.read_from_file(filename)
    ...

if (config["search"]=="min"):
    print(f"le min est {min(L)}")
elif (config["search"]=="max"):
    print(f"le max est {max(L)}")
else:
    print("valeur inconnue pour search")