// Hacer un algoritmo que llene una mtriz de 4*4 y determine la posicion 
// [fila,columna] del numero mayor almacenado en la matriz
Proceso ej11_2
	Definir num,i,j,p_i,p_j,max Como Entero;
	Dimension num[4,4];
	max <- -1000000;
	//recorro las filas	
	Para i <- 0 Hasta 3 Hacer
		// recorro las columnas
		Para j <- 0 Hasta 3 Hacer
			// pido que ingrese un numero y lo almaceno en la matriz
			Escribir "Ingrese un número entero en la matriz (posicion ",i+1,",",j+1,")";
			Leer num[i,j];
			// Si el numero alctual es mayor que max, guardo su posicion y remplazo max
			Si num[i,j] > max Entonces
				max <- num[i,j];
				p_i <- i;
				p_j <- j;
			FinSi
		FinPara
	FinPara
	Escribir "El numero mayor de la matriz es: ",max," se encuentra en la posicion (",p_i+1,",",p_j+1,")"; 
FinProceso
