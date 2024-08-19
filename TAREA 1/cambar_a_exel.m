data = readmatrix('id_coords.txt'); % Cambia 'archivo.txt' al nombre de tu archivo de texto
matrizDatos = data;
tablaDatos = array2table(data, 'VariableNames', data(1, :));
writetable(data, 'id_coords.xlsx'); % Cambia 'archivo.xlsx' al nombre que desees para el archivo de Excel


rot= readmatrix("resultados.txt")

tabla= table(rot(:,1), rot(:,2))
writetable(tabla, 'V_rot.xlsx')

﻿
vel= [24.8751,18.8457
19.5930,17.3199
13.0672,14.2817
22.4673,14.9318
24.0910,18.5538
14.9614,12.0179
23.1660,15.5854
12.1505,16.1298
12.1863,14.9917]

rot2= [1.10914860e+01 -2.01997505e+00 -8.88178420e-16
 1.10952527e+01 -2.16436181e+00  4.44089210e-16
 1.10782600e+01 -2.24570057e+00  8.88178420e-16
11.10183138 -2.06940835  0.        
11.10089258 -1.98472188  0.        
 1.10773128e+01 -2.24508772e+00  4.44089210e-16
 1.10961935e+01 -2.05518427e+00  4.44089210e-16
 1.11455729e+01 -2.21789757e+00 -4.44089210e-16
 1.10980742e+01 -2.26082800e+00 -4.44089210e-16]

tabla2= table(vel(:,1),vel(:,2))
writetable(tabla2, 'vel.xlsx')

for i=1:9
    vel_sin_rot(i,1)= vel(i,1) - rot2(i,1);
    vel_sin_rot(i,2)= vel(i,2) - rot2(i,2);
end
for i=1:9
    vel_sin_rot2(i,1)= vel(i,1) - rot2(i,2);
    vel_sin_rot2(i,2)= vel(i,2) - rot2(i,1);
end


estaciones= readmatrix("id_coords.txt")

vectores= [estaciones(:,2),estaciones(:,3),vel_sin_rot(:,1),vel_sin_rot(:,2),datos(:,7),datos(:,8)]
writematrix(vectores,'vectores.txt','Delimiter', '\t')

vectores2= [estaciones(:,2),estaciones(:,3),vel_sin_rot2(:,1),vel_sin_rot2(:,2),datos(:,7),datos(:,8)]
writematrix(vectores2,'vectores2.txt','Delimiter', '\t')

datos= readmatrix('datos.txt');
writematrix(datos,'datos.xlsx')
