// Ejercicio 7: Ingresar "N" enteros, visualizar la suma de los
// números pares de la lista, cuántos números pares
// existen y cuál es el promedio de los números
// impares. (Pseudocódigo)
Proceso Numeros_pares
	// Definimos Tipo de variable.
	Definir n_elementos,i,num Como Entero
	Definir suma_pares,conteo_pares Como Entero
	Definir suma_impares,conteo_impares Como Entero
	Definir promedio_impares Como Real
	// Pedimos un digito al usuario.
	Escribir 'Digite la cantidad de elementos a ingresar: '
	// Leemos el valor ingresado por el usuario.
	Leer n_elementos
	// Inicializamos los Valores de las Variables.
	i <- 1
	suma_pares <- 0
	conteo_pares <- 0
	suma_impares <- 0
	conteo_impares <- 0
	// Iniciamos primer Condicional.
	Mientras i<=n_elementos Hacer
		// Digite un Numero 
		Escribir i,'. Digite un número: '
		Leer num
		Si num MOD 2=0 Entonces
			// El num es Para 
			// Suma interactiva de pares
			suma_pares <- suma_pares+num
			// Conteo de pares
			conteo_pares <- conteo_pares+1
		SiNo
			// El número es impar
			// Suma interactiva de impares
			suma_impares <- suma_impares+num
			// Conteo de impares
			conteo_impares <- conteo_impares+1
		FinSi
		i <- i+1
	FinMientras
	Si conteo_pares=0 Entonces
		Escribir 'No se han digitado número pares: '
	SiNo
		Escribir 'La suma de los números pares es: ',suma_pares
		Escribir 'El conteo de los números pares es: ',conteo_pares
	FinSi
	Si conteo_impares=0 Entonces
		Escribir 'No se han digitado números impares'
	SiNo
		promedio_impares <- suma_impares/conteo_impares
		Escribir 'El promedio de impares es: ',promedio_impares
	FinSi
FinProceso
