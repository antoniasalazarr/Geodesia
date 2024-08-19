# -*- coding: utf-8 -*-
import os
import numpy as np
from datetime import datetime
# importo el modelo de trayectoria y otras funciones
from trajectory import Trajectory as tj
from trajectory import toYearFraction

# Ruta de la carpeta que contiene los archivos .txt
carpeta = r'C:\Users\anton\Downloads\Geodesia\TAREA\estaciones cortadas' 
 # Reemplaza con la ruta de tu carpeta

# Lista para almacenar los nombres de archivos .txt
estaciones_txt = []

# Itera a través de los archivos en la carpeta
for estacion in os.listdir(carpeta):
    if estacion.endswith('.txt'):
       estaciones_txt.append(estacion)

# Imprime la lista de archivos .txt
print(estaciones_txt)

    
with open('id_coords.txt','r') as archivo:
    estaciones = archivo.readlines()
print(estaciones)


estaciones={}
t_eq_iq= toYearFraction(datetime(2014,4,1)) #Terremoto del 1 de abril del 2014
for estacion in estaciones_txt:
    param = tj(estacion, t_eq=t_eq_iq, t_at=False, Do_plot=True,  
				new_at=False,tau=None, t_cut=False)
    estaciones[estacion]= param
    
    

    