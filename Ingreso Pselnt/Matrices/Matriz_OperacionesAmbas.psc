Proceso sin_titulo
	Definir matriz1,matriz2,matrizResultado,i,j Como Entero;
	Dimension matriz1[3,3],matriz2[3,3],matrizResultado[3,3];
	Escribir 'Escribir la primera matriz en orden ascendente: ' Sin Saltar;
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			// Pedimos datos al usuario.
			Escribir 'Digite los datos para llenar la matriz';
			Leer matriz1[i,j];
		FinPara
	FinPara
	Escribir "Escribir la matriz decendente";
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir '[',i,':',j,']';
			Leer matriz2[i,j];
		FinPara
	FinPara
	Escribir '';
	// mostramos la matriz
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir matriz2[i,j],' ';
		FinPara
		Escribir '';
	FinPara
	Escribir '';
	// mostrar las dos matrices
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir matriz2[i,j] + matriz1[i,j];
		FinPara
	FinPara
FinProceso
