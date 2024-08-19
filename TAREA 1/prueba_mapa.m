clc 
clear all

datos= readmatrix('id_coords.txt');
longitud = datos(:,2);
latitud = datos(:,3);
% Crear una figura
figure;
% Graficar puntos en el mapa
plot(longitud, latitud, 'r*', 'MarkerSize', 10);
grid on;
title('Puntos en el Mapa');
xlabel('Longitud');
ylabel('Latitud');

%% Cortando los datos

% Carpeta que contiene los archivos txt
carpeta = 'C:\Users\anton\Downloads\Geodesia\TAREA\pulled_data - copia'; 
% Reemplaza 'tu_ruta_de_carpeta' con la ruta de tu carpeta

% Intervalo de años que deseas conservar
ano_inicial = 2014;
ano_final = 2020;

% Lista de archivos en la carpeta
archivos = dir(fullfile(carpeta, '*.txt'));

% Bucle para procesar cada archivo
for i = 1:numel(archivos)
    nombre_archivo = archivos(i).name;
    archivo_completo = fullfile(carpeta, nombre_archivo);
    
    % Leer los datos del archivo
    datos = readmatrix(archivo_completo);
    
    % Obtener los años de los datos (suponiendo que los datos tienen una columna de años)
    anos = datos(:, 2);
    
    % Encontrar índices que están dentro del intervalo de años
    indices_intervalo = (anos >= ano_inicial) & (anos <= ano_final);
    
    % Recortar los datos según el intervalo de años
    datos_recortados = datos(indices_intervalo, :);
    
    % Guardar los datos recortados en un nuevo archivo
    nuevo_nombre_archivo = sprintf('%s_%d_%d.txt', nombre_archivo(1:end-4), ano_inicial, ano_final);
    nuevo_archivo_completo = fullfile(carpeta, nuevo_nombre_archivo);
    dlmwrite(nuevo_archivo_completo, datos_recortados, 'delimiter', '\t');
end


hola =readmatrix("AEDA.txt");