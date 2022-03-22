Proceso SimetricaMatriz
	// determinar si una matriz es simetrica,desarrollandos un programa que determine si una matriz es simetrica o no,
	// una matriz es simetrica si es cuadradrada y si es igual a su matriz traspuesta. 
	// 813 -->
	Definir Matris,i,j Como Entero;
	Definir Booleano Como Logico;
	Dimension Matris[3,3];
	Booleano <- Verdadero;
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 2 Hacer
			Matris[i,j]<-Azar(100);
		FinPara
	FinPara
	si filas= columna Entonces
		Para i<-0 Hasta filas-1 Hacer
			Para j<-0 Hasta columna-1 Hacer
				Si i <> j  Y MatRis[i,j] = Matris[j,i] Entonces
					Booleano <- Falso;
				
				FinSi
			FinPara
		FinPara
		Escribir "";
		Si Booleano==Verdadero Entonces
			Escribir 'La matriz es simetrica';
		SiNo
			Escribir 'La Matriz no es simetrica';
		FinSi
	FinSi
	
FinProceso
