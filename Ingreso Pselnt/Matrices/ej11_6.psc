//Hacer un algoritmo que llene una matriz de 5*5 y que almacene en la 
//  diagonal principal unos y en las demas posiciones ceros.
Proceso ej11_6
	Definir num,i,j Como Entero;
	Dimension num[5,5];
	Para i <- 0 Hasta 4 Hacer
		Para j <- 0 Hasta 4 Hacer
			Si i = j Entonces //lleno con unos la diagonal 
				num[i,j] <- 1;
			SiNo  // lleno con ceros el resto
				num[i,j] <- 0;
			FinSi
		FinPara
	FinPara
FinProceso
