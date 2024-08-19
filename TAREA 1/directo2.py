import numpy as np
def directo(lat,lon,latp,lonp,omega):

  # Calcula el vector de velocidad de la placa local dados la posición y la posición y velocidad del Polo de Euler

    # ENTRADAS:
    # lat, lon -> posición del punto donde se desea calcular la velocidad
    # latp, lonp, omega -> posición y velocidad del Polo de Euler

    # Las latitudes y longitudes están en grados
    # Omega está en grados por millón de años

    # SALIDA:
    # v1 = [vn, ve, vd]' velocidad en las direcciones norte, este y vertical
    # (referido al punto p) en mm/año.


    RT = 6370*10**(6) # Radio de la tierra 
    
    # convertir de grados a radianes
    latr=np.deg2rad(lat)
    lonr=np.deg2rad(lon)
    latpr=np.deg2rad(latp)
    lonpr=np.deg2rad(lonp)
    
    omega = omega*10**(-6)*(np.pi/180) # convertir a radianes por año
    
    # Convertir a coordenadas cartesianas
    # Punto
    P = np.array([
    np.cos(latr) * np.cos(lonr),  # Componente X (Este)
    np.cos(latr) * np.sin(lonr),  # Componente Y (Norte)
    np.sin(latr)                 # Componente Z (Arriba y abajo)
    ]).T  # T para transponer el vector

    # Polo de Euler 
    EP = np.array([
    np.cos(latpr) * np.cos(lonpr),  # Componente X (Este)
    np.cos(latpr) * np.sin(lonpr),  # Componente Y (Norte)
    np.sin(latpr)                  # Componente Z (Arriba y abajo)
    ]).T *omega
    
    # R*p
    VC=RT*np.cross(EP,P)
    #rotate to local coordinate system
     
    T=np.zeros((3,3));
    T[0, 0] = -np.sin(latr) * np.cos(lonr)
    T[1, 0] = -np.sin(lonr)
    T[2, 0] = -np.cos(latr) * np.cos(lonr)
    T[0, 1] = -np.sin(latr) * np.sin(lonr)
    T[1, 1] = np.cos(lonr)
    T[2, 1] = -np.cos(latr) * np.sin(lonr)
    T[0, 2] = np.cos(latr)
    T[1, 2] = 0
    T[2, 2] = -np.sin(latr)

     
    v1=T.dot(VC)
    return v1

v = directo(-20.219, -70.153, -18.72, -134.22, 0.117)

resultados = np.array([-20.219, -70.153, v[0], v[1], v[2]]) 
                       
with open('resultados.txt', 'w') as archivo:
    archivo.write(' '.join(map(str, resultados)))
    
    
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