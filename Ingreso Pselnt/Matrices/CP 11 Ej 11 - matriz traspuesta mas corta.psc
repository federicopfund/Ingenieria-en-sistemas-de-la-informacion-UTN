// Ejercicio 11 Matriz traspuesta
// Realice un programa que lea una matriz de 3*3 y cree su matriz
// traspuesta. La matriz traspuesta e aquella en la que la 
// columna i era la fila i de la matriz. (Diagrama de flujo)


Proceso traspuesta
	Definir i,j,matrix Como Entero;
	dimension matrix[3,3];
	//llenar la matriz
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir "Digite el numero que ira en la posicion [",i,",",j,"]" sin saltar;
			Leer matrix[i,j];
		FinPara
	FinPara
	Escribir "";
	Escribir "Esta es la matriz transpuesta:";
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Escribir sin saltar matrix[j,i], " ";
		FinPara
		Escribir "";
	FinPara
	Escribir "";
FinProceso
