Proceso SubCadenas
	// Definir tipo de datos 
	Definir Caden,letra Como Caracter;
	Definir i,ContadorA,Contadorb,largoCadena,j Como Entero;
	// Pedeir una letra al usuuaruna
	Escribir 'Digite una cadena de Caracteres';
	// Asignar lo que ingresa el usuario
	Leer Caden;
	// Asignar un comtador en 0
	ContadorA <-0;
	// Asignar a una variable el largo de un la longitud de teto que
	largoCadena <- Longitud(Caden);
	Para i<-0 Hasta ((largoCadena/2)-1) Hacer
		letra <- Subcadena(Caden,i,i);
		Para j<-0 Hasta Longitud(Caden)/2 Hacer
			Si Subcadena(Caden,j,j)==letra Entonces
				ContadorA<- ContadorA + 1;
				Escribir ContadorA;
			FinSi
		FinPara
		
	FinPara
FinProceso
