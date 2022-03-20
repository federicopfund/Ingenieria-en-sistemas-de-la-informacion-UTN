// Ejercicio 1: Hacer un algoritmo que almacene números en una matriz de 3*4. 
// Imprimir la suma de los números pares almacenados en la matriz.
Proceso principal
	Definir num,i,j,suma Como Entero;
	Dimension num[3,4];
	// Almacenamos los elementos en la matriz
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir 'Digite un numero[',i,'][',j,']: ' Sin Saltar;
			Leer num[i,j];
		FinPara
	FinPara
	// Mostramos la matriz
	Escribir '';
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir num[i,j],' ' Sin Saltar;
		FinPara
		Escribir '';
	FinPara
	// Ahora recorremos la matriz y sumamos los números pares
	suma <- 0;
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 3 Hacer
			// Si el número por el cual vamos es par
			Si num[i,j] MOD 2=0 Entonces
				suma <- suma+num[i,j];
			FinSi
		FinPara
	FinPara
	Escribir '';
	Escribir 'La suma de los números pares es: ',suma;
FinProceso
