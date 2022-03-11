// Ejercicio 3: Leer 10 números e imprimir cuantos son poritivos
// cuantos negativos y cuantos neutros. (Diagrama N-S)
Proceso ejercicio3
	Definir num,i Como Entero;
	Definir conteo_positivos,conteo_negativos,conteo_neutros Como Entero;
	// Inicializamos el valor de las variable que almacenaran Valores de Variable.
	conteo_positivos <- 0;
	conteo_negativos <- 0;
	conteo_neutros <- 0;
	// Iniciamos un bucle.
	Para i<-1 Hasta 10 Hacer
		// Pedimos un valor para cada Ciclo.
		Escribir i,'Digite un numero: ';
		// Leemos el Valor de la Variable.
		Leer num;
		// Condicioneales Simple
		Si num=0 Entonces
			conteo_neutros <- conteo_neutros+1;
		SiNo
			// Condicional Doble
			Si num>0 Entonces
				conteo_positivos <- conteo_positivos+1;
			SiNo
				conteo_negativos <- conteo_negativos+1;
			FinSi
		FinSi
	FinPara
	// Mostramso resultado al uduario.
	Escribir 'La cantidad de positivos es: ',conteo_positivos;
	Escribir 'La cantidad de negativos es: ',conteo_negativos;
	Escribir 'La cantidad de neutros es: ',conteo_neutros;
FinProceso
