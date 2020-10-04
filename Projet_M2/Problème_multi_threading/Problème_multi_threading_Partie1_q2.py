# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:01:04 2020

@author: Philippine
"""
import numpy.random as npr
import sys 

#Côté fichier
def f(x):
    return(3*x)

liste_instruction = ["1+1","7+2","3*3","f(2)"]


#Création du fichier de donées externes
with open('fichier_data.txt','w') as file:
    for instruction in liste_instruction:
        file.write(str(instruction) + "\n")
        
        
        
#Redéfinition du simulateur 
        
def simulateur(fichier):
    instructions =[]
    with open(fichier,'r') as file:
        for line in file:
            instru = line.rstrip("\n")
            instructions.append(instru)
    n = len(instructions)
    dico = {}
    while n!=0:
        ins_choisie = npr.choice(instructions)
        i = instructions.index(ins_choisie)
        instructions.pop(i)
        dico[ins_choisie]=eval(ins_choisie)             
        n = len(instructions)
    return(dico)         
    
test = simulateur('fichier_data.txt')
print(test)

'A tester sur les ordi de la fac'
#if __name__ == "__main__":
#    fichier = sys.argv[1:]  
#    res = simulateur(fichier)