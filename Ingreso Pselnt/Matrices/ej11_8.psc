// Mostrar la diagonal principal de una matriz
// Realizar un programa que defina una matriz de 3*3 y escriba un ciclo
// para que muestre la diagonal principal de la matriz.
Proceso ej11_8
	Definir matriz,i,j,n Como Entero;
	Dimension matriz[3,3];
	n <- 1;
	Para i <- 0 Hasta 2 Hacer
		Para j <- 0 Hasta 2 Hacer
			matriz[i,j] <- n;
			Si i = j Entonces
				Escribir matriz[i,j]," "Sin Saltar;
			SiNo
				Escribir "  "Sin Saltar;
			FinSi
			n <- n + 1;
		FinPara
		Escribir "";
	FinPara
	Escribir "";
FinProceso
