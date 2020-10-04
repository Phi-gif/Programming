# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:37:47 2020

@author: Philippine
"""
import pandas as pd

#Data

Metro = pd.read_excel("Data_treated.xlsx") #insert the right path here
Solo = Metro.drop_duplicates(keep='first',subset='Station').reset_index(drop=True)
Corres = Solo[Solo['Corresp. 1'] != 0].reset_index(drop=False)

#Values
vitesse_marche=1.1 #m/s
tps_inter_stat=143 #s
tps_corres=240     #s
