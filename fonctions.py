#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:14:34 2019

@author: renaudin
"""
def readconf(filename):
    """
    Cette fonction lit un fichier de configuration
    contenant des lignes de la forme variable=valeur.
    Le caractère # est la marque d'un début de commentaire.
    Il peut y avoir des lignes vides dans ce fichier.

    La fonction reçoit en paramètre le nom du fichier.
    Elle renvoie un dictionnaire dont les clés sont les variables
    définies dans le fichier, et les valeurs leurs valeurs.
    """
    ...
    table = {}
    il=1
    with open(filename, "r") as f:
      for line in f:
          line = line.strip()       # supprimer le saut de ligne
          if line=="": continue     # c'est une ligne vide
          elif line[0]=="#": continue # c'est un commentaire
          elif not "=" in line:       # cas non prévu
              raise Exception(f"erreur de syntaxe en ligne {il}: {line}")
          L = line.split('=')
          table[L[0]] = L[1]
          il += 1
    return table

def read_from_keyboard():
    """
    Renvoie des entiers lus au clavier
    """
    l=int(input('Combien de nombres allez-vous saisir ?'))
    L =[]
    n=0
    while len(L)!=l:
        n=int(input('Saisissez les nombres'))
        L+=[n]
    return(L)
    
import sys
def read_from_cmdline():
    """
    Renvoie des entiers lus sur la ligne de commande
    """
    return(sys.argv[1:])

def read_from_file(filename):
    """
    Renvoie des entiers lus dans le fichier dont le nom est contenu dans filename
    """
    l =[]
    with open(filename, "r") as f:
        for line in f:
            i = int(line)
            l+=[i]
    return(l)

if __name__=="__main__":
  print("""
  ...
  """)
