% Lee el archivo de texto
nombreArchivoTexto = 'id_coords.txt'; % Reemplaza con el nombre de tu archivo TXT
datos = readtable(nombreArchivoTexto, 'Delimiter', '\t'); % Ajusta el delimitador si es necesario

% Especifica el nombre del archivo de Excel
nombreArchivoExcel = 'id_coords.xlsx'; % Puedes cambiar el nombre si lo deseas

% Escribe los datos en un archivo de Excel
writetable(datos, nombreArchivoExcel, 'Sheet', 'Hoja1'); % Cambia 'Hoja1' al nombre de la hoja que desees

disp(['Se ha creado el archivo Excel: ' nombreArchivoExcel]);
