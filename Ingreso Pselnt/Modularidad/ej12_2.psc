// Dise�e un algoritmo que muestre un men� al usuario con las siguientes
//opciones: potencici�n, ra�z cuadrada y terminar, que cada opci�n la realice
//una funci�n o procedimiento.
Funcion potencia <- potenciacion(base,exponente)
	Definir potencia Como Real;
	potencia <- base ^ exponente; 
FinFuncion
Funcion raiz_ <- raiz_cuadrada(subradical)
	Definir raiz_ Como Real;
	raiz_ <- raiz(subradical);
FinFuncion
Proceso ej12_2
	Definir selector,num2 Como Entero;
	Definir num1 Como Real;
	Escribir "Escriba 1 para clacular una potenciacion";
	Escribir "Escriba 2 para calcular una raiz cuadrada";
	Escribir "Escriba 3 para para termiar";
	Leer selector;
	Segun selector Hacer
		1:
			Escribir "Ingrese la base de una potenciaci�n: " Sin Saltar;
			Leer num1;
			Escribir "Ingrese el exponente de una potenciaci�n: " Sin Saltar;
			Leer num2;
			Escribir "El resultado es: ",potenciacion(num1,num2);
		2:
			Escribir "Ingrese el subradical de una ra�z: " Sin Saltar;
			Leer num1;
			Escribir "El resultado es: ",raiz_cuadrada(num1);
		3:
			Escribir "Fin del programa";
		De Otro Modo:
			Escribir "";
	FinSegun
FinProceso
