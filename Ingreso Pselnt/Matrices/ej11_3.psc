// Hacer un algoritmo que llene una matriz de 4*4. Calcular la suma de 
// cada fila y almacenarla en un arreglo, la suma de cada columna y
// almacenarla en otro arreglo.

Proceso ej11_3
	Definir num,i,j,sum_f,sum_c Como Entero;
	Dimension num[4,4];
	Dimension sum_f[4];
	Dimension sum_c[4];
	//inicalizo el arreglo
	Para i <- 0 Hasta 3 Hacer
		sum_f[i] <- 0;
	FinPara
	Para j <- 0 Hasta 3 Hacer
		sum_c[j] <- 0;
	FinPara
	//tomo los valores a almacenar en la matriz y los sumo
	//recorro las filas
	Para i <- 0 Hasta 3 Hacer
		// recorro las columnas
		Para j <- 0 Hasta 3 Hacer
			// pido que ingrese un numero y lo almaceno en la matriz
			Escribir "Ingrese un número entero en la matriz (posicion ",i,",",j,")";
			Leer num[i,j];
			//sumo los valores en su correspondiente arreglo y indice
			sum_f[i] <- sum_f[i] + num[i,j];
			sum_c[j] <- sum_c[j] + num[i,j];
		FinPara
	FinPara
	// devuelvo los resulatdos al usuarios
	Para i <- 0 Hasta 3 Hacer
		Escribir "El resultado de la fila ",i," es: ",sum_f[i];
	FinPara
	Para j <- 0 Hasta 3 Hacer
		Escribir "El resultado de la columna ",j," es: ",sum_c[j];
	FinPara
FinProceso
