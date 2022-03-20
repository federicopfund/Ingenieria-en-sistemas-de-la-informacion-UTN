Proceso ej11_10
	Definir i,j,filas,columnas,matriz_original,matriz_copia Como Entero;
	Dimension matriz_original[100,100], matriz_copia[100,100];
	Escribir "Ingrese el número de columnas que tendra la matriz" Sin Saltar;
	Leer columnas;
	Escribir "Ingrese el número de filas que tendra la matriz" Sin Saltar;
	Leer filas;
	Escribir "";
	Para i <- 0 Hasta filas-1 Hacer
		Para j <- 0 Hasta columnas-1 Hacer
			matriz_original[i,j] <- azar(999);
			matriz_copia[i,j] <- matriz_original[i,j];
			Escribir Sin Saltar matriz_copia[i,j], "  ";
		FinPara
		Escribir " ";
	FinPara
	Escribir "";
FinProceso