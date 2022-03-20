//Ejercicio 4: Hacer un algoritmo que llene una matriz de 3*4. Sumar las 
// columnas e imprimir que columna tuvo la máxima suma y la suma de esa columna.

Proceso principal
	Definir num,i,j como enteros; 
	Dimension num[3,4];
	Definir suma_col,columna,mayor como enteros;
	
	//Pedimos los elementos de la matriz
	Para i<-0 Hasta 2 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			Escribir Sin Saltar "Digite un numero[",i,"][",j,"]: ";
			Leer num[i,j];
		FinPara
	FinPara
	
	//Mostramos la matriz
	Escribir "";
	Para i<-0 Hasta 2 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			Escribir Sin Saltar num[i,j]," ";
		FinPara
		Escribir "";
	FinPara
	
	//Establecemos por el momento a mayor la suma de la primera columna
	suma_col <- 0;
	Para i<-0 Hasta 2 con paso 1 Hacer
		suma_col <- suma_col + num[i,0]; 
	FinPara
	
	//Mayor ya tiene la suma de la primera columna
	mayor <- suma_col;
	columna <- 0;
	
	//Recorremos las columnas que nos faltan y sumamos
	Para j<-1 Hasta 3 Con Paso 1 Hacer
		suma_col <- 0;
		Para i<-0 Hasta 2 Con Paso 1 Hacer
			suma_col <- suma_col + num[i,j];
		FinPara
		
		Si suma_col > mayor Entonces
			mayor <- suma_col;
			columna <- j;
		FinSi
	FinPara
	
	Escribir "";
	Escribir "La columna con mayor suma es: ",columna;
	Escribir "La suma de esa columna es: ",mayor;
	Escribir "";
FinProceso
