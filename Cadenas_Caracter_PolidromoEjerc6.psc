Proceso Polidromo
	// Definir Variables
	Definir Palabra Como Caracter;
	Definir b,a,x Como Entero;
	// Pedir una Palabra al usuario
	Escribir 'Escribe una Palabra';
	// Leer la palabra que ingresa el usuario
	Leer Palabra;
	// Asignar a una variable la longuitud de la cadena -1.
	b <- Longitud(Palabra)-1;
	a <- 0;
	x <- 0;
	// Verificamos que sea Polidromo.
	// Mientras a sea menor que b se ejecura un mientras.
	Mientras a<b Hacer
		// Comparamos porciones de cadena 
		Si Subcadena(Palabra,a,a)<>Subcadena(Palabra,b,b) Entonces
			x <- x+1;
		FinSi
		// Incrementamos la variable con un contador.
		a <- a+1;
		b <- b-1;
	FinMientras
	// Si x nunca fue incrementada osea que tiene el mismo valor de asignacion.
	Si x==0 Entonces
		Escribir 'La Palabra ',Palabra,' Es un Polidromo';
	SiNo
		Escribir 'La Palabra ',Palabra,' No es Polidromo';
	FinSi
FinProceso
