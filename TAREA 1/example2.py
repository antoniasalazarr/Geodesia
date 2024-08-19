# -*- coding: utf-8 -*
# -*- coding: utf-8 -*-
"""
Trayectory model. Bevis & Brown (2014)
Joaquín Hormazabal M.
2021
"""
from inverso import polo_euler
from directo2 import directo
import numpy as np
import pandas as pd
from datetime import datetime
# importo el modelo de trayectoria y otras funciones
from trajectory import Trajectory as tj
from trajectory import toYearFraction

# Estaciones que quiero correr
estaciones = ['AEDA.txt', 'ATJN.txt','BN15.txt','CGTC.txt','CRSC.txt','IAC1.txt','IQQE.txt','MNMI.txt','PCCL.txt']  

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

t_eq_pisagua = toYearFraction(datetime(2014, 4, 1))
resultados = pd.DataFrame(columns=['param_ew', 'param_ns', 'param_up', 'wrms_ew','wrms_ns','wrms_up'])

# Cargar id_coords
with open('id_coords.txt', 'r') as file:
    lines = file.readlines()
    data = [line.strip().split() for line in lines]

# Crea un Dataframe con los datos
coordenadas = pd.DataFrame(data, columns=['Nombre', 'Longitud', 'Latitud'])

# Convierte la longitud y latitud a números
coordenadas['Longitud'] = coordenadas['Longitud'].astype(float)
coordenadas['Latitud'] = coordenadas['Latitud'].astype(float)
# print(coordenadas)

# Iterar sobre las estaciones
for estacion in estaciones:
    param = tj(estacion, t_eq=[t_eq_pisagua], t_at=False, Do_plot=True, new_at=False, tau=15, t_cut=False)
    
    # Extraer los valores de interés
    param_ew = param['Param_ew']
    param_ew = param_ew['m'][1]
    param_ns = param['Param_ns']
    param_ns = param_ns['m'][1]
    param_up = param['Param_up']
    param_up = param_up['m'][1]
    wrms_n = param['wrms_n']
    wrms_e = param['wrms_e']
    wrms_u = param['wrms_u']
    extraccion = {'param_ew': param_ew, 'param_ns': param_ns, 'param_up': param_up, 'wrms_ew': wrms_e, 'wrms_ns': wrms_n, 'wrms_up': wrms_u} #diccionario con las variables
    resultados = pd.concat([resultados, pd.DataFrame([extraccion])], ignore_index=True)  

# Unir coordenadas y resultados
resultados = pd.concat([coordenadas, resultados], axis=1)

# Guardar en un archivo de texto
resultados.to_csv('datos.txt', index=False, sep='\t', float_format='%.4f')

# Param tiene los "m" y "Cm"
# fg_all tiene la matriz G
# fg tiene todas las funciones bases separadas
# data tiene los datos (tiempo, ew, ns, up, sigm_Ew, sigm_ns, sigm_up)
# wrms son los errores cuadraticos medio con pesos respectivos

long_polo= -1.69185668e+02 
lat_polo= -1.03614390e+01
omega=  1.51969360e-01

long_estacion=[]
lat_estacion=[]

## DIRECTO

# Abre el archivo de coordenadas
with open("id_coords.txt", "r") as archivo_coords:
    # Abre el archivo de resultados en modo escritura
    with open("resultados.txt", "w") as archivo_resultados:
        for linea in archivo_coords:
            partes = linea.split()
            estacion = partes[0]
            longitud = float(partes[1])
            latitud = float(partes[2])
            lat_estacion.append(latitud)
            long_estacion.append(longitud)

           # Calcula la velocidad llamando a la función
            velocidad = directo(latitud, longitud, lat_polo, long_polo, omega)

            #Guarda el resultado en el archivo de resultados
            archivo_resultados.write(f"{estacion}\t{velocidad}\n")

#aqui me hizo el archivo resultados con las velocidades de rotacion de cada estacion  
velocidad1 = directo(-20.55 , -70.18, -1.87244450e+01, -1.34223527e+02, 1.17157028e-01)
velocidad2 = directo(-19.30 , -70.14, -1.87244450e+01, -1.34223527e+02, 1.17157028e-01)
velocidad3 = directo(-18.48  , -70.32, -1.87244450e+01, -1.34223527e+02, 1.17157028e-01)
velocidad4 = directo(-20.18  , -70.07, -1.87244450e+01, -1.34223527e+02, 1.17157028e-01)
velocidad5 = directo(-20.92 , -70.08, -1.87244450e+01, -1.34223527e+02, 1.17157028e-01)
velocidad6 = directo(-18.48  , -70.33, -1.87244450e+01, -1.34223527e+02, 1.17157028e-01)
velocidad7 = directo(-20.27 , -70.13, -1.87244450e+01, -1.34223527e+02, 1.17157028e-01)
velocidad8 = directo(-19.13 , -69.60, -1.87244450e+01, -1.34223527e+02, 1.17157028e-01)
velocidad9 = directo(-18.46 , -70.11, -1.87244450e+01, -1.34223527e+02, 1.17157028e-01)
print(velocidad1)
print(velocidad2)
print(velocidad3)
print(velocidad4)
print(velocidad5)
print(velocidad6)
print(velocidad7)
print(velocidad8)
print(velocidad9)

#AHORA HAY QUE HACER LA RESTA
