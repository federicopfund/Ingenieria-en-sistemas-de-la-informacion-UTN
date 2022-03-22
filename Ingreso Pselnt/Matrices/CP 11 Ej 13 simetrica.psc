//Ejercicio 13: Determinar si una matriz es simetrica
//Desarrollar una programam que determine su una matriz es simetrica
//o no. una matriz es simetrica si es cuadrada y si es igual a su
//matriz traspuesta, ejemplo: (pseudocodigo)

// 813		813
//174   -->  174 
//349		349

Proceso simetricaOno
	Definir i,j,matriz,matrizTraspuesta, fila,columna Como Entero;
	Definir simetrica Como logico;
	Dimension matriz[100,100],matrizTraspuesta[100,100];
	
	Escribir "ingrese la cantida de filas de la matriz: ";
	leer fila;
	Escribir "ingrese la cantida de columnas de la matriz: ";
	leer columna;
	
	si fila=columna entonces
		Para i<-0 Hasta fila-1 Hacer // llenando la matriz
			Para j<-0 Hasta columna-1 Hacer
				Escribir 'Digite un elemento[',i,'][',j,']: ' Sin Saltar;
				Leer matriz[i,j];
				matrizTraspuesta[j,i]<-matriz[i,j]; // Creamos una Traspuesta
			FinPara
		FinPara
		Escribir "";
		Para i<-0 Hasta fila-1 Hacer // mostramos la matriz
			Para j<-0 Hasta columna-1 Hacer
				Escribir matriz[i,j]," " Sin Saltar;			
			FinPara
			Escribir "";
		FinPara
		Escribir "";
		escribir "La matriz traspuesta es: ";
		Escribir "";
		Para i<-0 Hasta fila-1 Hacer // mostramos la matriz
			Para j<-0 Hasta columna-1 Hacer
				Escribir matrizTraspuesta[i,j]," " Sin Saltar;			
			FinPara
			Escribir "";
		FinPara
		Escribir "";
		simetrica<-Falso; //comprobamos si es simetrica
		Para i<-0 Hasta fila-1 Hacer
			Para j<-0 Hasta columna-1 Hacer
				si i <> j y matrizTraspuesta[i,j] = matriz[i,j] Entonces
					simetrica<- verdadero;
				FinSi
			FinPara
		FinPara
		escribir "";
		si simetrica=Verdadero Entonces
			Escribir  "la matriz es simetrica";
		SiNo
			Escribir "la matriz no es simetrica";
		FinSi
		Escribir "";
	sino 
		Escribir "La matriz no es cuadrado, por lo tanto NO es simetrica";
		
	FinSi
	Escribir "";
	
FinProceso
