Proceso ejercicio8
	definir i como entero;
	definir frase, frase2 como cadenas;
	definir letra Como Caracter;
	
	
	escribir Sin Saltar "Digite una cadena ";
	leer frase;
	
	
	frase2<- "";
	para i <- 0 hasta longitud(frase) con paso 1 Hacer
		letra <- subcadena(frase, i,i);
		
		si letra <> ' ' Entonces
			frase2<- concatenar(frase2, letra);
		SiNo
			frase2 <- concatenar(frase2, '*');
			
		FinSi
		escribir frase2;
		
		
	FinPara
	
	escribir frase2;
	escribir "";
FinProceso