% Especifica la carpeta que contiene los archivos de texto
carpeta = 'C:\Users\anton\Downloads\Geodesia\TAREA\pulled_data'; % Cambia 'ruta_a_tu_carpeta' a la ubicación de tus archivos

% Lista todos los archivos de texto en la carpeta
archivos = dir(fullfile(carpeta, '*.txt'));

% Define el rango de años que deseas extraer
ano_inicio = 2014;
ano_fin = 2020;

% Itera a través de los archivos
for i = 1:length(archivos)
    archivo = archivos(i).name;
    ruta_completa = fullfile(carpeta, archivo);
    
    % Lee el archivo de texto
    archivo_datos = dlmread(ruta_completa); % Supongo que los datos son números
    
    % Filtra los datos basados en la segunda columna (asumiendo que la segunda columna contiene años)
    datos_ano = archivo_datos(archivo_datos(:, 2) >= ano_inicio & archivo_datos(:, 2) <= ano_fin, :);
    
    % Extrae el nombre del archivo (sin extensión) para crear un nombre de archivo de salida
    [nombre, ~, ~] = fileparts(archivo);
    
    % Genera el nombre del archivo de salida
    nombre_salida = fullfile('C:\Users\anton\Downloads\Geodesia\TAREA\pulled_data\cortadas', [nombre '_filtrado.txt']); % Cambia 'ruta_de_salida' según tu preferencia
    
    % Guarda los datos filtrados en un archivo de texto separado
    dlmwrite(nombre_salida, datos_ano, ' ');
end
