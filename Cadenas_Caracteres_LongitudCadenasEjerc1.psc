Proceso LongitudCadenas
	// Definimos tipo de variables.
	Definir i Como Entero;
	Definir MayorCadenas,longitudCadenas1,longitudCadena2 Como caracter;
	// Pedimos datos al usuario
	Escribir "Digite La primer cadena de texto: ";
	// Leemos los datos digitalizado por el usuario
	Leer longitudCadenas1;
	Escribir "Digite La Segunda Cadena: ";
	Leer longitudCadena2;
	// Definimos un condicional para asignar el mayor valor de longuitud a una variable denominada MayorCadenas
	Si longitud(longitudCadenas1)>longitud(longitudCadena2) Entonces
		MayorCadenas <-  longitudCadenas1;
	SiNo
		MayorCadenas <- longitudCadena2;
	FinSi
	// Por Ultimo mostramos la variable mas grande,osea la mayor cadena
	Escribir "Cadena mayor es igual ah:",MayorCadenas;
FinProceso
