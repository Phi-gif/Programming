#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:19:34 2019

@author: verron
"""


import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ast import literal_eval
import config as c


class CoordGPS:
    
    def __init__ (self, lat, lon):
	#Création d'une position GPS via ses coordonnées GPS
        self.lat = lat
        self.lon = lon


    def distance(self):
        Lat,Lon=(c.Solo['Lat']),(c.Solo['Lon'])
        Dist=pd.DataFrame(columns=['Distance'])
        for i in range(163):
            dist=0
            dist=100000*np.sqrt((self.lat-Lat[i])**2 + (self.lon-Lon[i])**2)
            Dist.loc[i,'Distance']=dist
        Tab=Dist.sort_values(by=['Distance']).reset_index(drop=False)           #On ne change pas l'index pour avoir accès au numéro des stations
        mask= Tab['Distance']<=Tab['Distance'][0]+175
        tableau=Tab[mask]
        if len(tableau)==0:
            return([Tab[0]])
        return(tableau)
   
    
    def temps_marche(self):
        distance=self.distance()
        liste_temps_marche=[int(i/c.vitesse_marche) for i in list(distance['Distance'])]
        return(liste_temps_marche)

class Fonctions:
    
    def EnsRes():
        Ligne=c.Metro['Ligne'] #récupère seulement les numeros de ligne
        Reseaux=[]
        LenRes=[]
        LenResSum=[]
        for i in range(1,13):
            Reseaux.append([ligne for ligne in Ligne if ligne==(i)])      
            LenRes.append(len(Reseaux[i-1])) 
        LenResSum=np.insert(np.cumsum(LenRes),0,0,axis=0) 
        Ensemble=12*[[]]
        for i in range(0,12):
            Ensemble[i]= c.Metro[LenResSum[i]:LenResSum[i+1]]
            Ensemble[i]=Ensemble[i].sort_values(by=['Sens']).reset_index(drop=True)
        return(Ensemble,LenResSum)
    
    
    def dessin(self):
        for ligne in Fonctions.EnsRes()[0]:
            plt.scatter(ligne['Lon'],ligne['Lat'],marker='.')
            plt.plot(ligne['Lon'],ligne['Lat'])
        

    def Tuple():
        liste_station=[]
        for df in Fonctions.EnsRes()[0]:
            for station in df["Station"]:
                liste_station.append(station)
        nom=12*[[]]
        liste_tuple=[]
        liste_tuple_rev=[]
        for k in range(0,12):
            nom[k]=liste_station[Fonctions.EnsRes()[1][k]:Fonctions.EnsRes()[1][k+1]]
        for camino in nom:
            for i in range(1,len(camino)):
                liste_tuple.append((camino[i-1],camino[i]))
                liste_tuple_rev.append((camino[i],camino[i-1]))
        return(liste_tuple+liste_tuple_rev)
        
        
    def adjency_matrix():
        Graphe_réseau=nx.DiGraph()
        Graphe_réseau.add_nodes_from(c.Metro['Station'].drop_duplicates(keep='first').reset_index(drop=True))
        Graphe_réseau.add_edges_from(Fonctions.Tuple())
        matrice_adjacence=nx.to_numpy_matrix(Graphe_réseau,nodelist=list(c.Metro['Station'].drop_duplicates(keep='first')))
        for i in range(len(matrice_adjacence)):
            for j in range(len(matrice_adjacence)):
                if i!=j and matrice_adjacence[i,j]==0:
                    matrice_adjacence[i,j]=float('inf')
        return(matrice_adjacence)
        
        
    def Floyd_Warshall():
        mat_adj=Fonctions.adjency_matrix() 
        (m,v)=np.shape(mat_adj)
        nxt=np.zeros([m,v])
        for i in range(m):
            for j in range(m):
                nxt[i][j]=i  # On crée une matrice de prédécesseur avec des nombres qui coorespondent à l'ordre des stations dans self.liste_station
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if mat_adj[i,j] > mat_adj[i,k] + mat_adj[k,j]:
                        mat_adj[i,j] = mat_adj[i,k] + mat_adj[k,j]
                        nxt[i][j] = nxt[k][j]
        return(mat_adj,nxt)     
    
    
    def ConstructPath(i,j):
        mat_pred=Fonctions.Floyd_Warshall()[1]
        if mat_pred[i,j] == float('inf'):
            return []
        path = [j]
        while i!=j :
            j = int(mat_pred[i,j])  
            path.append(j)
        return path

        
    def Shortest_path(départ,destination):
        liste_chemins=[]
        Temps=[]
        closest_stat_pt_dep=list(départ.distance()['index'])
        closest_stat_pt_arr=list(destination.distance()['index'])
        k=0
        tps_marche_dep=départ.temps_marche()
        tps_marche_arr=destination.temps_marche()
        for i in closest_stat_pt_dep:
            for j in closest_stat_pt_arr:
                liste_chemins.append(Fonctions.ConstructPath(i,j))
        for liste in liste_chemins:
            time=0
            if len(tps_marche_dep)==1 and len(tps_marche_arr)==1:
                time=c.tps_inter_stat*(len(liste)-1)+tps_marche_dep[0]+tps_marche_arr[0]
            elif len(tps_marche_dep)==1 and len(tps_marche_arr)>1:
                time=c.tps_inter_stat*(len(liste)-1)+tps_marche_dep[0]+tps_marche_arr[k]
            elif len(tps_marche_dep)>1 and len(tps_marche_arr)==1:
                time=c.tps_inter_stat*(len(liste)-1)+tps_marche_dep[k]+tps_marche_arr[0]
            else :
                time=c.tps_inter_stat*(len(liste)-1)+tps_marche_dep[k]+tps_marche_arr[k]
            for i in range(1,len(liste)-1):
                if liste[i] in list(c.Corres['index']) and c.Solo['Ligne'][liste[i-1]]==c.Solo['Ligne'][liste[i+1]]:
                    time+=c.tps_corres
            k+=1
            Temps.append(time)
        less_time = min(Temps)
        indice=Temps.index(less_time)
        return(liste_chemins[indice],less_time)
            
        
class Réseau(Fonctions):
    
    def __init__(self):
        self.liste_station=list(c.Metro['Station'].drop_duplicates(keep='first'))
        self.Geopoints=[]
        for coordonnées in list(c.Metro['Geopoint'].drop_duplicates(keep='first')):
            (x,y)=literal_eval(coordonnées)
            self.Geopoints.append(CoordGPS(x,y))
        
    
    def Trace(self,départ,destination):
        num_stat=Fonctions.Shortest_path(départ,destination)[0]
        liste_coord=[self.Geopoints[k] for k in num_stat]
        self.dessin()
        plt.scatter(départ.lon,départ.lat,marker='*',c='b',s=150, label='Départ')
        plt.scatter(destination.lon,destination.lat,marker='*',c='r',s=150, label='Arrivée')
        plt.scatter([coord.lon for coord in liste_coord],[coord.lat for coord in liste_coord],marker='.',c='black')
        plt.plot([coord.lon for coord in liste_coord],[coord.lat for coord in liste_coord],c='black',linewidth=2) 
        plt.plot([départ.lon,liste_coord[-1].lon],[départ.lat,liste_coord[-1].lat],linestyle='--',c='black')
        plt.plot([destination.lon,liste_coord[0].lon],[destination.lat,liste_coord[0].lat],linestyle='--',c='black')
        plt.legend()
        plt.axis('equal') 
        plt.show()
        
        
    def ordre_station(self,départ,destination):
        chemin,temps=Fonctions.Shortest_path(départ,destination)
        chemin_ord=[station for station in reversed(chemin)]
        ligne=[]
        for i in range(len(chemin_ord)-1):
            if c.Solo['Ligne'][chemin_ord[i]]==c.Solo['Ligne'][chemin_ord[i+1]]:
                ligne.append(c.Solo['Ligne'][chemin_ord[i]])
                
            if c.Solo['Ligne'][chemin_ord[i]]==c.Solo['Corresp. 1'][chemin_ord[i+1]]:
                ligne.append(c.Solo['Ligne'][chemin_ord[i]])
                
            if c.Solo['Corresp. 1'][chemin_ord[i]]==c.Solo['Ligne'][chemin_ord[i+1]]:
                ligne.append(c.Solo['Corresp. 1'][chemin_ord[i]])
                
            if c.Solo['Corresp. 2'][chemin_ord[i]]==c.Solo['Ligne'][chemin_ord[i+1]]:
                ligne.append(c.Solo['Corresp. 2'][chemin_ord[i]]) 
                
            if c.Solo['Corresp. 3'][chemin_ord[i]]==c.Solo['Ligne'][chemin_ord[i+1]]:
                ligne.append(c.Solo['Corresp. 3'][chemin_ord[i]])
                
            if c.Solo['Ligne'][chemin_ord[i]]==c.Solo['Corresp. 2'][chemin_ord[i+1]]:
                ligne.append(c.Solo['Ligne'][chemin_ord[i]])
                
            if c.Solo['Ligne'][chemin_ord[i]]==c.Solo['Corresp. 3'][chemin_ord[i+1]]:
                ligne.append(c.Solo['Ligne'][chemin_ord[i]])  
        
        if temps // 3600 == 0:
            print("En absence de grève, votre trajet devrait durer  ",temps//60," minute(s) et ", temps%60," seconde(s)")        
    
        else:
            print("En absence de grève, votre trajet devrait durer  ",temps//3600," heure(s), ", (temps%3600)//60," minutes et ",(temps%3600)%60," seconde(s)" )
        print(f"Marchez jusqu'à la station {self.liste_station[chemin_ord[0]]} et prenez la ligne {ligne[0]} en direction de {self.liste_station[chemin_ord[1]]}")
        for k in range(len(ligne)-1):
            if ligne[k]!=ligne[k+1]:
                print(f"Transférez vers la ligne {ligne[k+1]} à la station {self.liste_station[chemin_ord[k+1]]} direction {self.liste_station[chemin_ord[k+2]]}")
        print(f"Descendez à la station {self.liste_station[chemin_ord[-1]]} et marchez jusqu'à votre destination")
    



