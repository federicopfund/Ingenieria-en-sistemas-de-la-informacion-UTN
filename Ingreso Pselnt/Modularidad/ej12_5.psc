// Diseñar un algoritmo que pida al usuario 5 apellidos, los almacene en un
//   arreglo y posteriormente muestre los apellidos ordenados alfabéticamente.



//Ordenación por metodo de burbuja
SubProceso ordenar_arreglo(arreglo)
	Definir i,j como Entero;
	Definir cadena_auxiliar Como Caracter;
	Para i<-0 Hasta 3 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			Si arreglo[j] > arreglo[j+1] Entonces
				cadena_auxiliar <- arreglo[j];
				arreglo[j] <- arreglo[j+1];
				arreglo[j+1] <- cadena_auxiliar;
			FinSi
		FinPara
	FinPara
	Para i <- 0 Hasta 4 Hacer
		Escribir arreglo[i],", " Sin Saltar;
	FinPara
	Escribir "";
	Escribir "";
FinSubProceso



Proceso ej12_5
	Definir i,j Como Entero;
	Definir arreglo,arreglo_ordenado Como Caracter;
	Dimension arreglo[5];
	Escribir "Crear arreglo";
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Escribir "Ingrese los apellios en el arreglo: ";
		Leer arreglo[i];
	FinPara

	ordenar_arreglo(arreglo);
	
FinProceso
