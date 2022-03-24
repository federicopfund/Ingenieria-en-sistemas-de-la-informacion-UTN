Funcion suma <- serie_f(n) 
	Definir suma Como Entero;
	
	Si n = 1 o n = 0 Entonces
		suma <- n;
		
	SiNo
		suma <- serie_f(n-1) + serie_f(n-2);
	FinSi
FinFuncion

Proceso ej12_8
    Definir resultado,n,i Como Entero;
	Escribir "n de la serie fibonachi";
	Leer n;
	Escribir serie_f(n);	
FinProceso