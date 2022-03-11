Proceso Espacios_Blanco
	// Definimos tipo de variables
	Definir EliminarEspacios,Espacio,Array Como Caracter;
	Definir i,j,ContadorDeEspacios Como Entero;
	// Definimos una variable para almacenar parte de la cadena de caracteres.
	Array <- ' ';
	// Pedir al usuario un breve texto .
	Escribir 'Escribe un texto breve: ';
	// Asignar un texto a la variable de asignacion.
	Leer EliminarEspacios;
	// Inicializamos un valor de variables
	ContadorDeEspacios <- 0;
	Para i<-0 Hasta Longitud(EliminarEspacios) Hacer
		// Dentro de un para de 0 hasta el tamaño de texto ingresado.
		// asignamos una subcadenas individual a una variable.
		Espacio <- Subcadena(EliminarEspacios,i,i);
		// Luego verificamos que ese caracter no sea un espacio.
		Si Espacio==' ' Entonces
			ContadorDeEspacios <- ContadorDeEspacios+1;
		SiNo
			// En Caso falso concatenaremos una cadena a lo ya teniamos
			Array <- Concatenar(Espacio,Array);
		FinSi
	FinPara
	Escribir Array;
FinProceso
