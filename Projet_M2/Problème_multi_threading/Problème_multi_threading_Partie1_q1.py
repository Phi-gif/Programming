
#Parie 1 : Monotâche

#Question 1

import numpy.random as npr

liste_instruction = ["1+1","7+2","3*3","f(2)"]

def f(x):
    return(3*x)

def simulateur(instructions):
    n = len(instructions)
    dico = {}                                           #structure de sonnées chosie pour garder les résultats en mémoire
    while n!=0:
        ins_choisie = npr.choice(instructions)
        i = instructions.index(ins_choisie)
        instructions.pop(i)
        dico[ins_choisie]=eval(ins_choisie)             # à l'air de marcher aussi pour des fonctions
        n = len(instructions)
    return(dico)                                        #return ou print ?
        