Proceso Ciclos
	// Definimos Tipo de datos
	Definir j,i,Sumapares,Sumaimpares Como Entero;
	// declaramos variables de almacenamiento.
	Sumapares <- 0;
	Sumaimpares <- 0;
	// Definimos un bucle para que analice 50 veces
	Para i<-0 Hasta 50 Hacer
		Si i MOD 2==0 Entonces
			// suma valores pares
			Sumapares <- Sumapares+i;
		SiNo
			// suma deimpares
			Sumaimpares <- Sumaimpares+i;
		FinSi
	FinPara
	// Mostramos al usuario
	Escribir 'Sumas de Numeros Pares: ',Sumapares;
	Escribir 'Suamas de Numeros Impares:',Sumaimpares;
FinProceso
