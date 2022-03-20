Proceso ej11_9
	// Definimos iteradores i y j, definimos matriz ortiginal y matriz copiada 
	Definir i,j,matriz_original,matriz_copia Como Entero;
	Dimension matriz_original[2,2];
	Dimension matriz_copia[2,2];
	// Pedimos al usuario que ingrese los valores en la matriz
	Para i<-0 Hasta 1 Hacer
		Para j<-0 Hasta 1 Hacer
			Escribir "Introduzca un numero entero, en la posicion (",i,",",j,")";
			Leer matriz_original[i,j];
		FinPara
	FinPara
	// Ahora vamos a copiar los datos en la matriz copia
	Escribir " ";
	Escribir "La matriz copia es:";
	Para i<-0 Hasta 1 Hacer
		Para j<-0 Hasta 1 Hacer
			matriz_copia[i,j] <- matriz_original[i,j] ;
			Escribir Sin Saltar matriz_copia[i,j]," ";
		FinPara
		Escribir " ";
	FinPara
FinProceso
