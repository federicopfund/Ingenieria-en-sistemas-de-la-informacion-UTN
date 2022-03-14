// Ejercicio 4: Suponga que se tiene un conjunto de calificaciones de un
// grupo de 10 alumnos. Realizar un algoritmo para calcular la
// calificación promedio y la calificación más baja de todo el
// grupo. (Pseudocódigo)
Proceso ejercicio4
	// Definimos Variables.
	Definir calificacion_promedio,calificacion_baja Como Real;
	Definir calificacion,suma Como Real;
	Definir i Como Entero;
	// Declaramos Valor  de Variable en 0.
	suma <- 0;
	calificacion_baja <- 99999;
	// Hacemos el proceso por 10 veces la cantidad de alumnos que queremos calcuar las Notas
	Para i<-1 Hasta 10 Hacer
		Escribir i,'. Digite una calificación: ';
		// En cada ciclo le pedimos al usaria que ingrese un Valor
		Leer calificacion;
		// Suma interactiva de las calificaciones
		suma <- suma+calificacion;
		// Calcular la menor calificacion
		Si calificacion<calificacion_baja Entonces
			calificacion_baja <- calificacion;
		FinSi
	FinPara
	// Sacamos el promedio de las Notas.
	calificacion_promedio <- suma/10;
	// Mostramos el valor promedia al usuario.
	Escribir 'La calificacion promedio es: ',calificacion_promedio;
	Escribir 'La calificacion mas baja es: ',calificacion_baja;
FinProceso
