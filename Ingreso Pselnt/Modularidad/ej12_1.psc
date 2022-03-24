// diseñar un algoritmo que pinda un nombre al usuario y que despliegue
// en pantalla entre asteriscos. La cantidad de asteriscos debe ser 
// la misma que carcteres en el nombre incluidos espacios.
SubAlgoritmo asteriscos(caden) 
	Definir n_caracteres,i Como Entero;
	Definir frase Como Caracter;
	n_caracteres <- Longitud(caden);
	frase <- "";
	Para i <- 0 Hasta n_caracteres-1 Hacer
		frase <- Concatenar(frase,"*");
	FinPara
	Escribir frase,caden,frase;
FinSubAlgoritmo
Proceso ej12_1
	Definir cadena_1 Como Caracter;
	Escribir "Introduzca una cadena: " Sin Saltar;
	Leer cadena_1;
	asteriscos(cadena_1);
FinProceso
