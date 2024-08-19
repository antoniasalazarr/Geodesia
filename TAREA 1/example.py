# -*- coding: utf-8 -*
# -*- coding: utf-8 -*-
"""
Trayectory model. Bevis & Brown (2014)
Joaquín Hormazabal M.
2021
"""

import numpy as np
from datetime import datetime
# importo el modelo de trayectoria y otras funciones
from trajectory import Trajectory as tj
from trajectory import toYearFraction

# Estación que quiero correr
sta = 'AEDA.txt'

# corro el modelo de trayectoria
# tiene estos inputs (solo es necesario el txt de la estación)
# ts_file: ruta a la estación
# t_eq = None : si quieres ingresar un terremoto
# el formato del tiempo del terremoto es en fracción de año
# usar: "t_eq_pisagua = toYearFraction(datetime(2014,4,1))" # fecha es año mes dia
# tau = None # para los postsismicos, se ingresan en dias
# t_at = False  
# en caso de querer usar saltos (estos se guardan en un .pickle y hay que crear el directorio)
# new_at = False 
# para agregar cambios de antena (hay que dejar el Do_plot = True para esto), se abrira al figura y uno pincha donde los quiere
# Do_plot = False
# para plotear las series de tiempo con el modelo
# t_cut = False
# para cortar las series de tiempo desde un ti

t_eq_iquique = toYearFraction(datetime(2014,4,1))
param = tj(sta,  t_eq=[t_eq_iquique], t_at=False, Do_plot=True, 
				new_at=False,tau = 15, t_cut=False)


ew = (param['Param_ew']) # muestra los diccionarios que devuelve el modelo
ewm = (ew['m'])
ewm = ewm[1]
lon = 45.6789  # Reemplaza con el valor de longitud que desees
lat = -123.4567  # Reemplaza con el valor de latitud que desees

with open("datos.txt", "w") as archivo:
    archivo.write(f"{lon} {lat} {ewm}\n")
    
# Param tiene los "m" y "Cm"
# fg_all tiene la matriz G
# fg tiene todas las funciones bases separadas
# data tiene los datos (tiempo, ew, ns, up, sigm_Ew, sigm_ns, sigm_up)
# wrms son los errores cuadraticos medio con pesos respectivos
