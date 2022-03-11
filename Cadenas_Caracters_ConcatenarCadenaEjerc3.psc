Proceso ConcatenarCadena
	// Definir Tipos de variables.
	Definir Cadena_tex,Concatena Como Caracter;
	Definir Numer,i Como Entero;
	// Pedimos datos al usuario.
	Escribir 'Digite un Valor para una cadena de texto';
	// Leemos el valor que digito el usuario.
	Leer Cadena_tex;
	Escribir 'Digite un numero: ';
	Leer Numer;
	// Inicialisamos una variable como una cadena vacia.
	Concatena <- '';
	// Repetimos el para por el numero que ingreso, en esa medida vamos a concatenar cadenas. 
	Para i<-0 Hasta Numer-1 Hacer
		Concatena <- Concatenar(Cadena_tex,Concatena);
	FinPara
	Escribir Concatena;
FinProceso
