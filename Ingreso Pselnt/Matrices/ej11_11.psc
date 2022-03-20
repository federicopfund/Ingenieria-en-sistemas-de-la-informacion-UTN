//matriz_transpuesta
// Realice un programa que lea una matriz de 3*3 y cree su matriz
// transpuesta. La matriz transpuesta es aquella que la columna
// era la fila i de la matriz.
Proceso ej11_11
	Definir i,j,matriz_transpuesta Como Entero;
	Dimension matriz_transpuesta[3,3];
	Para i <- 0 Hasta 2 Hacer
		Para j <- 0 Hasta 2 Hacer
			Escribir "Introduzca un número en la posición (",i,",",j,") " Sin Saltar;
			Leer matriz_transpuesta[j,i];
		FinPara
	FinPara
	Escribir " ";
	Escribir "La matriz transpuesta es:";
	Para i <- 0 Hasta 2 Hacer
		Para j <- 0 Hasta 2 Hacer
			Escribir Sin Saltar matriz_transpuesta[i,j]," ";
		FinPara
		Escribir "";
	FinPara
	Escribir " ";
FinProceso
