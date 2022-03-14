// Ejercicio 6: Calcular la siguiente sumatoria de los "N" elementos:
// S = 1 + 4 + 9 +...+ N (Diagrama N-S)
Proceso Sumatoria_de_serie
	Definir n_elementos como entero;
	Definir i,suma como enteros;
	Escribir "Digite la cantidad de elementos a sumarse: ";
	Leer n_elementos;
	i <- 1;
	suma <- 0;
	Mientras i<=n_elementos Hacer
		suma <- suma + i^2;
		i <- i + 1;
	FinMientras
	Escribir "La suma es: ",suma;
FinProceso
