// Ejercicio 5: Calcular el factorial de un número mayor o igual a 0.
// (Diagrama de flujo)
Proceso Factorial
	// Definimos Tipos de Variable.
	Definir num,n,r,f Como Entero
	Definir i,fact Como Entero
	// Pedimos el valor para calcualrle el factorial
	Escribir 'Ingrese el Valor del Numero para encontrar el factorial:'
	// Asignamos el Valor de la variable deceada
	Leer n
	// Verificamos que el valor es entero.
	Si n<>Trunc(n) Entonces
		Escribir 'El numero debe ser entero!'
	SiNo
		// Verificamos que el valor al cual le podemos calcular el factorial es muy grande.
		Si abs(n)>50 Entonces
			Escribir 'Resultado muy grande!'
		SiNo
			// Inicializamos los valores en 1.
			r <- 1; f <- 1
			// Verificamos que el usuario ingreso el factorial de 1, en caso de ser asi devolvemos el valor asignado de r.
			Mientras f<=abs(n) Hacer
				// en caso que se quiera calcuñar el factorial de un numero distinto de 1
				Si n<0 Entonces
					r <- (-f)*r
				SiNo
					r <- f*r
				FinSi
				// Incrmentamos f en una unidada.
				f <- f+1
			FinMientras
			Escribir 'Factorial:',r
		FinSi
	FinSi
FinProceso
