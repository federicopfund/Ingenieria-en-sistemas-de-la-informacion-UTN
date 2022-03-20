// Hacer un algoritmo que llene una matriz de 4*4 y que almacene la diagonal
// principal en un arreglo. Imprimir el arreglo resultante
Proceso ej11_5
	Definir num,i,j,diag Como Entero;
	Dimension num[4,4];
	Dimension diag[4];
	Para i <- 0 Hasta 3 Hacer
		Para j <- 0 Hasta 3 Hacer
			Escribir Sin Saltar "Introduzca un valor en la posicion (",i,",",j,"):";
			Leer num[i,j];
			Si i = j Entonces
				diag[i] <- num[i,j];
			FinSi
		FinPara
	FinPara
	//devuelvo la diagonal
	Escribir "La diagonal principal es";
	Para i <- 0 Hasta 3 Hacer
		Escribir "(",i,",",i,"): ",diag[i];
	FinPara
FinProceso
