#!/usr/bin/env python3

"""
Created on Mon Dec 16 16:56:52 2019

@author: renaudin
"""
import Bibliotheque_CV_PR  as BCP

#0.05 = 5km en lat
#lon [cuatro camino,La paz] -- [19.458454,-99.214643 // 19.35048513,-98.96061659]
#lat [Tlahuac,Ciudad azteca] -- [19.28680057,-99.01443243 // 19.53444312,-99.02711391]
#inter_lon=[-99.231,-98.942]
#inter_lat=[19.268,19.555]
print('\n')
print("respectez bien les intervalles pour la latitude et la longitude, sinon vous êtes en dehors de la ville et nous vous invitons à prendre un autre moyen de transport")
lat_dep=float(input("Rentrez la latitude de votre point de départ, elle doit appartenir à l'intervalle [19.268,19.555]: "))
while bool(19.268<=lat_dep<=19.555)!=True:
    lat_dep=float(input("Rentrez la latitude de votre point de départ elle doit appartenir à l'intervalle [19.268,19.555]: "))   
    
lon_dep=float(input("Rentrez la longitude de votre point de départ, elle doit appartenir à l'intervalle [-99.231,-98.942]: "))
while bool(-99.231<=lon_dep<=-98.942)!=True:
    lon_dep=float(input("Rentrez la longitude de votre point de départ [-99.231,-98.942]: "))   

lat_dest=float(input("Rentrez la latitude de votre point d'arrivée elle doit appartenir à l'intervalle [19.268,19.555]: "))
while bool(19.268<=lat_dep<=19.555)!=True:
        lat_dest=float(input("Rentrez la latitude de votre point d'arrivée elle doit appartenir à l'intervalle [19.268,19.555]]: ")) 
        
lon_dest=float(input("Rentrez la longitude de votre point d'arrivée elle doit appartenir à l'intervalle [-99.231,-98.942]: "))
while bool(-99.231<=lon_dep<=-98.942)!=True:
    lon_dest=float(input("Rentrez la longitude de votre point d'arrivée elle doit appartenir à l'intervalle [-99.231,-98.942]: ")) 
    
print('\n')
print("Merci de patientez, notre programme étant très complet, sa complexité l'handicape :(")
print('\n')

point_départ=BCP.CoordGPS(lat_dep,lon_dep)
point_arrivé=BCP.CoordGPS(lat_dest,lon_dest)
Mexico_subway=BCP.Réseau()

Mexico_subway.ordre_station(point_départ,point_arrivé)
print('\n')
print("Merci de patientez, le schéma est coinçé dans le métro ;)")


Mexico_subway.Trace(point_départ,point_arrivé)