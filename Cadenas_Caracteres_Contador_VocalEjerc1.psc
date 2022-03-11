Proceso Cadenas_Caracteres
	// Definir tipos de variables.
	Definir Caden,Vocales,Caract,Matriz,letra Como Caracter;
	Definir Cantidad,Contador_Vocal,i,j,Contador_consonante Como Entero;
	// pedimos valores al usuario.
	Escribir 'Introduce una cadena de Caracteres:';
	Leer Caract;
	// Asignamos una cadena de caracteres con las vocales a tener en cuenta.
	Vocales <- 'aeiou';
	Contador_Vocal <- 0;
	Contador_consonante <- 0;
	// Con un Para recorremos la cadena Podemos conciderar que en cada paso vamos a tomar una porcion de la cadena osea una subcadena y la guardamos en una matriz.
	Para i<-0 Hasta Longitud(Caract) Hacer
		letra <- Subcadena(Caract,i,i);
		Para j<-0 Hasta Longitud(Vocales)-1 Hacer
			// Condicional para generar un contador de vocales y no vocales
			Si Subcadena(Vocales,j,j)=letra Entonces
				Contador_Vocal <- Contador_Vocal+1;
			SiNo
				Contador_consonante <- Contador_consonante+1;
			FinSi
		FinPara
	FinPara
	Escribir 'La Cantidad de vocales es de: ',Contador_Vocal;
FinProceso
