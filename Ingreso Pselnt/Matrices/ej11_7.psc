//  Rellenando una matriz
// Hacer un programa para rellenar una matriz pidiendo al usuario el 
// n�mero de filas y columnas, posteriormente mostrar la matriz en pantalla
Proceso ej11_7
	Definir matriz,columnas,filas,i,j Como Entero;
	Dimension matriz[100,100];
	Escribir "Introduzca el n�mero de filas de la matriz: " Sin Saltar; Leer filas;
	Escribir "Introduzca el n�mero de columnas de la matriz: " Sin Saltar; Leer columnas;
	Para i <- 0 Hasta filas-1 Hacer
		Para j <- 0 Hasta columnas-1 Hacer
			Escribir "Introduzca un n�mero en la posicion (",i,",",j,"): " Sin Saltar;
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
