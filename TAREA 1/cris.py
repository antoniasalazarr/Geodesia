# -*- coding: utf-8 -*-
import os
import numpy as np
from datetime import datetime
# importo el modelo de trayectoria y otras funciones
from trajectory import Trajectory as tj
from trajectory import toYearFraction
# Ruta de la carpeta que contiene los archivos de texto
sta = r'C:\Users\anton\Downloads\Geodesia\TAREA\estaciones cortadas'   # Reemplaza con la ruta de tu carpeta

# Lista para almacenar los nombres de archivos .txt
estaciones_txt = []
Vew = []

# Itera a través de los archivos en la carpeta y realiza el resto del proceso para cada archivo
for estacion in os.listdir(sta):
    if estacion.endswith('.txt'):
        estaciones_txt.append(estacion)

        # Procesar para cada archivo de texto encontrado
        # Correr el modelo de trayectoria
        # Aquí puedes ajustar los valores de t_eq, tau, t_at, new_at, Do_plot, t_cut según sea necesario

        # ejemplo de uso de la variable 'estacion' dentro del ciclo for
        ts_file = os.path.join(sta, estacion)  # ruta al archivo de estación actual
        t_eq_iq= toYearFraction(datetime(2014,4,1)) #Terremoto del 1 de abril del 2014
        # corro el modelo de trayectoria con los parámetros actualizados para cada archivo
        param = tj(ts_file,  t_eq=[t_eq_iq], t_at=False, Do_plot=True, new_at=False, tau=15, t_cut=False)

        print(param.keys())
        ew = (param['Param_ew'])  # muestra los diccionarios que devuelve el modelo
        ewm = (ew['m'])
        ewm = ewm[1]
        Vew.append(ewm)
        ems = (param['Param_ns'])
        ems = (ems['m'])
        ems = ems[1]
        lon = 45.6789  # Reemplaza con el valor de longitud que desees
        lat = -123.4567  # Reemplaza con el valor de latitud que desees

        with open("datos.txt", "a") as archivo:
             archivo.write(f"{lon} {lat} {ewm} {ems}\n")
                          
                        

        # Param tiene los "m" y "Cm"
        # fg_all tiene la matriz G
        # fg tiene todas las funciones bases separadas
        # data tiene los datos (tiempo, ew, ns, up, sigm_Ew, sigm_ns, sigm_up)
        # wrms son los errores cuadraticos medio con pesos respectivos