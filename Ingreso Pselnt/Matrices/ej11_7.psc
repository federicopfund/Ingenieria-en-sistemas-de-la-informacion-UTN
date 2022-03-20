//  Rellenando una matriz
// Hacer un programa para rellenar una matriz pidiendo al usuario el 
// número de filas y columnas, posteriormente mostrar la matriz en pantalla
Proceso ej11_7
	Definir matriz,columnas,filas,i,j Como Entero;
	Dimension matriz[100,100];
	Escribir "Introduzca el número de filas de la matriz: " Sin Saltar; Leer filas;
	Escribir "Introduzca el número de columnas de la matriz: " Sin Saltar; Leer columnas;
	Para i <- 0 Hasta filas-1 Hacer
		Para j <- 0 Hasta columnas-1 Hacer
			Escribir "Introduzca un número en la posicion (",i,",",j,"): " Sin Saltar;
			Leer matriz[i,j];
		FinPara
	FinPara
	Escribir "";
	Para i <- 0 Hasta filas-1 Hacer
		Para j <- 0 Hasta columnas-1 Hacer
			Escribir matriz[i,j],"  "Sin Saltar;
		FinPara
		Escribir "";
	FinPara
	Escribir "";
FinProceso
