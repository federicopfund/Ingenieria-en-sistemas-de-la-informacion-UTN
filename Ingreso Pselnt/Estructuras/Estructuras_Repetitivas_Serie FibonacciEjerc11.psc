// Ejercicio 11: Imprimir la serie de los "N" términos de la serie Fibonacci.
// 0 1 1 2 3 5 8 13 21...
Proceso ejercicio11
	// Definimos Tipos de Variables. 
	Definir n_elementos Como Entero;
	Definir a,b,c,i Como Entero;
	// Pedimos datos al usuario.
	Repetir
		Escribir 'Digite la cantidad de elementos';
		// Leemos los datos ingresados.
		Leer n_elementos;
		// Primer condicional para verificar que sea mayor a 2.
	Hasta Que n_elementos>2
	// Inicializamos el valor de variables en 0.
	a <- 0;
	b <- 1;
	c <- 1;
	Escribir '0';
	Escribir '1';
	i <- 3;
	Repetir
		c <- a+b;
		Escribir c;
		a <- b;
		b <- c;
		i <- i+1;
	Hasta Que i>n_elementos
FinProceso
