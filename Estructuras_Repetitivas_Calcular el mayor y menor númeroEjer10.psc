//Ejercicio 10: Ingresa "N" números, calcular el maximo y minimo de ellos.
Proceso ejercicio10
	Definir n_elementos,i como enteros;
	Definir num,mayor,menor como reales;
	
	Repetir
		Escribir "Digite el número de elementos: ";
		Leer n_elementos;
	Hasta Que n_elementos>0
	//El paso anterior significa que el usiario no puede ingresar
	//un número menor a cero, ni negativo
	Escribir "1. Digite un numero: ";
	leer num;
	
	mayor <- num;
	menor <- num;
	//Le ponemos 2 al interador porque el usuario pidio 2 elementos
	i <- 2;
	
	//Determinar el mayor de los números
	Repetir
		Escribir i,". Digite un número: ";
		Leer num;
		Si num > mayor Entonces
			mayor <- num;
		SiNo
			//Determinar el número menor
			Si num < menor Entonces
				menor <- num;
				
			FinSi
		FinSi
		
		i <- i + 1;
	Hasta Que i>n_elementos;
	
	Escribir "El mayor de los números es: ",mayor;
	Escribir "El menor de los números es: ",menor;
	
FinProceso
