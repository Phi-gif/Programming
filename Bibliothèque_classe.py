# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:12:23 2019

@author: Philippine
"""

import networkx as nx
import numpy as np
import math as mt
import pandas as pd
import matplotlib.pyplot as plt 
from ast import literal_eval


#Metro = pd.read_excel("/Users/Philippine/Documents/Cours/Informatique/Programmation_Python/Projet/projet_poo/Data_treated.xlsx")
Metro = pd.read_excel("/users/mmath/renaudin/Documents/Programmation_python/Projet_progra/Data_treated.xlsx")

Lat=Metro['Lat'] #latitude des stations
Lon=Metro['Lon'] #longitude des stations
Stations=Metro['Station']
Geopoints=Metro['Geopoint']

vitesse_marche=4/3.6 #vitesse en m/s
durée_2_stations=143
    
class Réseau: 
            
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
            plt.plot(linea['Lon'],linea['Lat'])
        return(Ensemble,LenResSumBis)
        plt.axis('equal')
        plt.show()
         
        
    def Tuple():
        liste_station=[]
        for df in Réseau.EnsRes()[0]:
            for station in df["Station"]:
                liste_station.append(station)
        nom=12*[[]]
        liste_tuple=[]
        liste_tuple_rev=[]
        for k in range(0,12):
            nom[k]=liste_station[Réseau.EnsRes()[1][k]:Réseau.EnsRes()[1][k+1]]
        for camino in nom:
            for i in range(1,len(camino)):
                liste_tuple.append((camino[i-1],camino[i]))
                liste_tuple_rev.append((camino[i],camino[i-1]))
        return(liste_tuple+liste_tuple_rev)
    
    
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
            
class Graphe(Réseau):
    
    def __init__(self):
        self.sommets=[]
        self.aretes=[]

    def __str__(self):
        return f"Cet objet est un Graphe à {len(self.sommets)} sommets et {len(self.aretes)} arêtes"


    def add_sommet(self,s):
        if s not in self.sommets:
            self.sommets.append(s)

    def add_arete(self,s,t):
        self.add_sommet(s)
        self.add_sommet(t)
        if (s,t) not in self.aretes:
            self.aretes.append((s,t))

    def add_aretes_from(self,liste):
        for x in liste:
            if type(x) == tuple and len(x) == 2:
                self.add_arete(*x)

        
    def graphe_complet(liste_aretes):
        g=Graphe()
        g.add_aretes_from(liste_aretes)
        return(g)

class Parcours:
    
    def closest_station(geopoint):
        R=6373000
        (xp,yp)=geopoint
        liste_coordonnée_stations=[]
        liste_distances=[]
        liste_stations_proches=[]
        for coord in list(Geopoints):
            if literal_eval(coord) not in liste_coordonnée_stations:
                liste_coordonnée_stations.append(literal_eval(coord))
        for coordinates in liste_coordonnée_stations:
            (x,y)=coordinates
            dlon=np.radians(y)-np.radians(yp)
            dlat=np.radians(x)-np.radians(xp)
            a=mt.sin(dlat/2)**2+mt.cos(xp)*mt.cos(x)*mt.sin(dlon/2)**2
            c=2*mt.atan2(np.sqrt(a),np.sqrt(1-a))
            distance=R*c
            liste_distances.append(distance)
        for i,distance in enumerate(liste_distances):
            if distance < vitesse_marche*durée_2_stations:
                liste_stations_proches.append(list(Stations)[i])
                if len(liste_stations_proches)==0:
                    
        print(liste_stations_proches)
            
        
        
            
        
               
if __name__ == "__main__":
    
    Graphe_Réseau=Graphe.graphe_complet(Réseau.Tuple())
    print(Graphe_Réseau)
    
    
