
SubProceso imprimirmatriz(matriz,n,m)
	Definir i,j Como Entero;
	Para i <- 0 Hasta n-1 Hacer
		Para j <- 0 Hasta m-1 Hacer
			Escribir matriz[i,j],"  "Sin Saltar;
		FinPara
		Escribir "";
	FinPara
FinSubProceso

SubProceso sumarmatriz(matriz,n,m)
	Definir i,j,resultado Como Entero;
	resultado <- 0;
	Para i<-0 Hasta n-1 Hacer
		Para j<-0 Hasta m-1 Hacer
			resultado <- resultado+matriz[i,j];
		FinPara
	FinPara
	Escribir "";
	Escribir "El resultado es: ",resultado;
	Escribir "";
FinSubProceso


Proceso ej12_6
	Definir matriz,i,j,selector Como Entero;
	Definir eligesalir Como Logico;
	eligesalir <- Falso;
	Repetir
		
		//Limpiar Pantalla;
		Escribir 'Elija una opción:';
		Escribir '  1 - Llenar una matriz 4*4';
		Escribir '  2 - Mostrar la matriz';
		Escribir '  3 - Sumar todos los elementos de la matriz';
		Escribir '  4 - Para salir';
		Leer selector;
		
		Segun selector Hacer
			1: 
				Dimension matriz[4,4];
				
				Para i <- 0 Hasta 3 Hacer
					Para j <- 0 Hasta 3 Hacer
						Escribir "Introduzca un número en la posicion (",i,",",j,"): " Sin Saltar;
						Leer matriz[i,j];
					FinPara
				FinPara
				Escribir "";
				
			2: 
				imprimirmatriz(matriz,4,4);
			3: 
				sumarmatriz(matriz,4,4);
			4:
				Escribir 'Fin del programa.';
				eligesalir <- Verdadero;
			De Otro Modo:
				Escribir 'eleccionción inválida!';
		FinSegun
		
	Hasta que EligeSalir = Verdadero
	
FinProceso
