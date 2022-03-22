Proceso SimetricaMatriz
	//determinar si una matriz es simetricaldesarrollados un programa que determine si una matriz es simetrica o no, una matriz es simetrica si es cuadradrada y si es igual a su matriz traspuesta, 
	//813 -->
	Definir Matris Como Entero;
	Dimension  Matris[3,3];
	Booleano <-Verdadero;
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta  2 Hacer
			Matris[i,j]<- Azar(100);
		FinPara
	FinPara
	
	Para  i<-0 Hasta  2 Hacer
		Para  j<-0 Hasta 2 Hacer
			si Matris[i,j] <> Matris[j,i] Entonces
				Booleano<-Falso;
				j<-1;
				i<-1;
			FinSi
		FinPara
	FinPara
	
	si Booleano== Verdadero Entonces
		Escribir "La matriz es simetrica";
	SiNo
		Escribir "La Matriz no es simetrica";
	FinSi
FinProceso
