//Hacer un algoritmo que almacene n�meros en una matriz de 3*4. Imprimir la suma 
// de los n�meros pares almacenados en la matriz.
Proceso ej11_1
	Definir num,i,j,suma Como Entero;
	Dimension num[3,4];
	// inicializo la variable suma que va a contener la suma de los n�meros pares
	suma <- 0;
	// recorro las filas
	Para i <- 0 Hasta 2 Hacer
		// recorro las columnas
		Para j <- 0 Hasta 3 Hacer
			// pido que ingrese un numero y lo almaceno en la matriz
			Escribir "Ingrese un n�mero entero en la matriz (posicion ",i,",",j,")";
			Leer num[i,j];
			// si el n�mero ingresado es par pido que lo sume a "suma"
			Si (num[i,j] mod 2) = 0 Entonces
				suma <- suma + num[i,j];
			FinSi
		FinPara
	FinPara
	Escribir "El resultado de la suma de los n�meros pares de la matriz es: ",suma;
FinProceso
