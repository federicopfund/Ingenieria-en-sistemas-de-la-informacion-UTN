// Ejercicio 2: Hacer un algoritmo que llene una matriz de 4*4 y determine
// la posición [fila, columna] del número mayor almacenado en la matriz.
Proceso principal
	Definir num,i,j,mayor,posFila,posCol como enteros;
	Dimension num[4,4];
	
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir Sin saltar "Digite un numero[",i,"][",j,"]: ";
			Leer num[i,j];
		FinPara
	FinPara
	
	Escribir "";
	
	// Mostramos la matriz
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir Sin saltar num[i,j]," ";
		FinPara
		Escribir "";
	FinPara
	
	// Ahora, recorremos la matriz buscando el mayor
	mayor <- num[0,0];
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Si num[i,j] > mayor Entonces
				mayor <- num[i,j];
				posFila <- i;
				posCol <- j;
			FinSi
		FinPara
	FinPara
	
	Escribir "";
	Escribir "El numero mayor es: ",mayor;
	Escribir "Se encuentra en la fila: ",posFila,", Columna: ",posCol;
FinProceso

