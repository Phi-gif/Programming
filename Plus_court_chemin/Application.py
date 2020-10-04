#!/usr/bin/env python3

"""
Created on Mon Dec 16 16:56:52 2019

@author: renaudin
"""
import Bibliotheque_CV_PR  as BCP

print('\n')
print("Merci de bien respecter les intervalles pour la latitude et la longitude, sinon vous serez en dehors de la ville et nous vous invitons donc à prendre un autre moyen de transport")

lat_dep=float(input("Rentrez la latitude de votre point de départ, elle doit appartenir à l'intervalle [19.268,19.555]: "))
while bool(19.268<=lat_dep<=19.555)!=True:
    lat_dep=float(input("Rentrez la latitude de votre point de départ, elle doit appartenir à l'intervalle [19.268,19.555]: ")) 
    
    
lon_dep=float(input("Rentrez la longitude de votre point de départ, elle doit appartenir à l'intervalle [-99.231,-98.942]: "))
while bool(-99.231<=lon_dep<=-98.942)!=True:
    lon_dep=float(input("Rentrez la longitude de votre point de départ, elle doit appartenir à l'intervalle [-99.231,-98.942]: "))   
    

lat_dest=float(input("Rentrez la latitude de votre point d'arrivée, elle doit appartenir à l'intervalle [19.268,19.555]: "))
while bool(19.268<=lat_dep<=19.555)!=True:
        lat_dest=float(input("Rentrez la latitude de votre point d'arrivée, elle doit appartenir à l'intervalle [19.268,19.555]]: ")) 
    
        
lon_dest=float(input("Rentrez la longitude de votre point d'arrivée, elle doit appartenir à l'intervalle [-99.231,-98.942]: "))
while bool(-99.231<=lon_dep<=-98.942)!=True:
    lon_dest=float(input("Rentrez la longitude de votre point d'arrivée, elle doit appartenir à l'intervalle [-99.231,-98.942]: ")) 
    
print('\n')
print("Merci de patienter, notre programme étant très complet, sa complexité l'handicape :(")
print('\n')

point_départ=BCP.CoordGPS(lat_dep,lon_dep)
point_arrivé=BCP.CoordGPS(lat_dest,lon_dest)
Mexico_subway=BCP.Réseau()

Mexico_subway.ordre_station(point_départ,point_arrivé)
print('\n')
print("Merci de patienter, l'acheminement du plan est en cours ...")


Mexico_subway.Trace(point_départ,point_arrivé)