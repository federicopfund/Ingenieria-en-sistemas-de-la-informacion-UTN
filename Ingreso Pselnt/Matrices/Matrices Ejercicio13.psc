//Ejercicio 13: Determinar si una matriz es simetrica, 
//Desarrollar un programa que determine si una matriz es simetrica
//o no. Una matriz es simetrica si es cuadrada y si es igual a su
//matriz transpuesta, ejemplo:    (Pseudocódigo)
//
//  8 1 3            8 1 3
//  1 7 4     -->    1 7 4
//  3 4 9            3 4 9
Proceso Matrices
	Definir matriz1,i,j,filas,columnas,matriz2 Como Entero;
	Dimension matriz1[100,100],matriz2[100,100];
	Definir band Como Caracter; //Es una bandera
	
	band <- "F";
	
	Escribir "Digite el numero de filas: ";
	Leer filas;
	Escribir "Digite el numero de columnas: ";
	Leer columnas;
	//Llenamos la matriz
	Para i<-0 Hasta filas-1 Con Paso 1 Hacer
		Para j<-0 Hasta columnas-1 Con Paso 1 Hacer
			Escribir Sin Saltar "Digite un numero[",i,"][",j,"]: ";
			Leer matriz1[i,j];
			matriz2[j,i] <- matriz1[i,j];
		FinPara
	FinPara
	Escribir "";
	Para i<-0 Hasta filas-1 Con Paso 1 Hacer
		Para j<-0 Hasta columnas-1 Con Paso 1 Hacer
			Escribir Sin Saltar matriz2[i,j]," ";
		FinPara
		Escribir "";
	FinPara
	//Vemos si la matriz es cuadrada
	Si filas = columnas Entonces
		Para i<-0 Hasta filas-1 Con Paso 1 Hacer
			Para j<-0 Hasta columnas-1 Con Paso 1 Hacer
				Si i <> j y matriz1[i,j] = matriz1[j,i] Entonces
					band <- "V";
				FinSi
			FinPara
		FinPara
	FinSi
	Escribir "";
	Si band = "V" Entonces
		Escribir "La matriz es simetrica";
	SiNo
		Escribir "La matriz No es simetrica";
	FinSi
	
FinProceso
