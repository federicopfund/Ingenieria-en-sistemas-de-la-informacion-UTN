Proceso Primer_Caracter
	// Definir tipos de Variables.
	Definir frase Como Caracter;
	Definir n,x,c Como Entero;
	// Ingresar un valor.
	Escribir 'Ingresa un Texto';
	// asignar el Valor ingresado
	Leer frase;
	// Asignar a la variable la frase ingresada
	n <- Longitud(frase);
	// Inicializar la variable en 0
	c <- 0;
	// Definimos un para para reccorre la frase caracteres por caracter.
	Para x<-0 Hasta n Hacer
		// Verificamos que x ==0 en caso de Verdad, Asigna una mayuscula a la primer cadena de la frase.
		Si x==0 Entonces
			Escribir Mayusculas(Subcadena(frase,x,x)) Sin Saltar;
		SiNo
			// En caso falso, Verificar que no sea un espacion.
			Si Subcadena(frase,x,x)==' ' Entonces
				// Si es verdad, sumamos un incremento a c
				c <- 1;
			SiNo
				// En caso de ser falso verificar que c==1
				Si c==1 Entonces
					// Asignar Mayuscula a la primer letra de una cadena.
					Escribir ' ',Mayusculas(Subcadena(frase,x,x)) Sin Saltar;
					// Asigacion de c en 0
					c <- 0;
				SiNo
					Escribir Subcadena(frase,x,x) Sin Saltar;
				FinSi
			FinSi
		FinSi
	FinPara
	Escribir '';
FinProceso
