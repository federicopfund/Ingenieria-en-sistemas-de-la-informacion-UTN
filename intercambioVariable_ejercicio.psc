Proceso Intercambio
	Definir Variable1, Variable2 Como Entero;
	Escribir "Digite una variable,Etiquetada como Variable n°1: ";
	Leer Variable1;
	Escribir "Digite una variable,Etiquetada como Variable n°1: ";
	leer Variable2;
	si Variable1 >= Variable2 Entonces
		Variable2 <- Variable1;
		Escribir "Intercambiamos Variables. n°1 por n° 2";
	SiNo
		Variable1 <- Variable2;
		Escribir "Intercambiamos Variables. n°2 por n°1";
	FinSi
	
FinProceso
