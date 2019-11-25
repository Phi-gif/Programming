#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:17:23 2019

@author: verron
"""
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from ast import literal_eval

Metro = pd.read_excel("/Users/Philippine/Documents/Cours/Informatique/Programmation_Python/Projet/projet_poo/Data_treated.xlsx")
##Metro = pd.read_excel("/users/mmath/renaudin/Documents/Programmation_python/Projet_progra/Data_treated.xlsx")

Lat=Metro['Lat'] #latitude des stations
Lon=Metro['Lon'] #longitude des stations
Stations=Metro['Station']
Geopoints=Metro['Geopoint']

########################################################
#Premier schéma représentant l'emplacement des stations #
########################################################

plt.scatter(Lon,Lat,marker='.')
plt.axis('equal')
plt.show()

#import Data

"""
Ligne = Df des numeros de ligne
Reseaux = liste de liste des numero de ligne
LenRes = liste de la ongeur de chaque ligne en nombre de station
LenResSum = somme cumulé de chaque station

Ensemble=[Ligne1,Ligne2,Ligne3,Ligne4,Ligne5,Ligne6,
          Ligne7,Ligne8,Ligne9,Ligne10,Ligne11,Ligne12]
"""
####################
#Création du Réseau#
##################
    
def EnsRes():
    Ligne=Metro['Ligne'] #récupère seulement les numeros de ligne
    Reseaux=[]
    LenRes=[]
    LenResSum=[]
    for i in range(1,13):
        Line=[]
        for ligne in Ligne:
            if ligne==i:
                Line.append(ligne) #récupere dans une liste chaque ligne
        Reseaux.append(Line)       #liste de liste par ligne
        LenRes.append(len(Reseaux[i-1])) #liste du nb de station par ligne
    LenResSum=np.cumsum(LenRes)
    LenResSumBis=np.insert(LenResSum,0,0,axis=0) #rajoute un zero au debut
    Ensemble=12*[[]]
    for i in range(0,12):
        Ensemble[i]= Metro[LenResSumBis[i]:LenResSumBis[i+1]]
    for i in range(0,12):
        Ensemble[i]=Ensemble[i].sort_values(by=['Sens'])
    for linea in Ensemble:
        linea=linea.reset_index(drop=True,inplace=True)
    for linea in Ensemble:
        plt.scatter(linea['Lon'],linea['Lat'],marker='.')
    for linea in Ensemble:
        plt.plot(linea['Lon'],linea['Lat'])
    return(Ensemble,LenResSumBis)
    plt.axis('equal')
    plt.show()
     
    
def Tuple():
    liste_station=[]
    for df in EnsRes()[0]:
        for station in df["Station"]:
            liste_station.append(station)
    nom=12*[[]]
    liste_tuple=[]
    liste_tuple_rev=[]
    for k in range(0,12):
        nom[k]=liste_station[EnsRes()[1][k]:EnsRes()[1][k+1]]
    for camino in nom:
        for i in range(1,len(camino)):
            liste_tuple.append((camino[i-1],camino[i]))
            liste_tuple_rev.append((camino[i],camino[i-1]))
    return(liste_tuple+liste_tuple_rev)

Liste_Tuple=Tuple()

###########################################
#Création du Graphe représentant le réseau #
##########################################

def position():
    pos={}
    Coordonnées=[]
    i=0
    for points in Geopoints:
        Coordonnées.append(points)
    for station in Stations:
        pos[station]=literal_eval(Coordonnées[i])
        i+=1
    return(pos)
    
pos=position()
    
Graphe_reseau=nx.MultiDiGraph()
Graphe_reseau.add_nodes_from(Metro['Station'])
Graphe_reseau.add_edges_from(Liste_Tuple)
    
nx.draw(Graphe_reseau,pos,node_size=40,linewidths=[0.1],arrowsize=5,with_labels=True) 
#Dessine le graphe du réseau en positionnant les stations selon leurs coordonnées géographiques

