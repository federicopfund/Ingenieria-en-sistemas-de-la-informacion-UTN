// Hacer un algoritmo que llene una matriz de 3*4. Sumar las columnas 
// e imprimir que columna tuvo la maxima suma y la suma de esa columna
Proceso ej11_4
	Definir num,i,j,sum_c,max,max_j Como Entero;
	Dimension num[3,4];
	Dimension sum_f[4];
	Dimension sum_c[4];
	//inicalizo el arreglo
	
	Para j <- 0 Hasta 3 Hacer
		sum_c[j] <- 0;
	FinPara
	//tomo los valores a almacenar en la matriz y los sumo
	//recorro las filas
	Para i <- 0 Hasta 2 Hacer
		// recorro las columnas
		Para j <- 0 Hasta 3 Hacer
			// pido que ingrese un numero y lo almaceno en la matriz
			Escribir "Ingrese un número entero en la matriz (posicion ",i,",",j,")";
			Leer num[i,j];
			//sumo los valores en su correspondiente arreglo y indice
			sum_c[j] <- sum_c[j] + num[i,j];
		FinPara
	FinPara
	max <- -1000000;
	// veo cual es la suma de columnas mayor
	Para j <- 0 Hasta 3 Hacer
		Si sum_c[j] > max Entonces
			max <- sum_c[j];
			max_j <- j;
		FinSi
	FinPara
	Escribir "La culumna que mayor da su suma es ",max_j," que da: ",max;
	
	
FinProceso
