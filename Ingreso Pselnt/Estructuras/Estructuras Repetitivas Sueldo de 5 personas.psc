// Ejercicio 8: Dadas las horas trabajadas de 5 personas y la
// tarifa de pago, calcular el salario, y la sumatoria de 
// todos los salarios. (Diagrama de flujo)
Proceso ejercicio8
	// Definir tipos de variables.
	Definir i,horas Como Entero
	Definir tarifa,salario,suma Como Real
	// Inicializamos el Valor de la variable
	i <- 1
	suma <- 0
	// Definimos un Bucle, para que en cada pasada el usuario asigne el valor de cada sueldo.
	Mientras i<=5 Hacer
		// Si i es menor que 5 significa que le usuario va tener que cargar el valor de cada empleado.
		Escribir 'salario del empleado ',i,':'
		Escribir 'Digite las horas trabajadas: '
		Leer horas
		Escribir 'Digite la tarifa por hora'
		Leer tarifa
		// Luego hacemos la cuenta de la tarifa por el numero de horas.
		salario <- horas*tarifa
		Escribir 'El salario es: $',salario
		suma <- suma+salario
		i <- i+1
		Escribir ''
	FinMientras
	Escribir 'La suma de todos los salarios es: ',suma
FinProceso
