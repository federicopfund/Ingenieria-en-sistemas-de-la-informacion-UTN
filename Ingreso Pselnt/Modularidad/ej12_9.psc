//Implementar un subprograma recursivo que permita sumar los digitos de un número
SubProceso suma <- sum(num)
	Definir cad,car Como Caracter;
	Definir n,suma Como Entero;
	cad <- ConvertirATexto(num);
	Si Longitud(cad) > 1 Entonces
		car <- SubCadena(cad,0,0);
		n <- ConvertirANumero(car);
		suma <- n + sum(ConvertirANumero(Subcadena(cad,1,Longitud(cad)-1)));
	SiNo
		suma <- num;
	FinSi
FinSubProceso
Proceso ej12_9
	Definir n,resultado Como Entero;
	Escribir "ingrese un numero" Sin Saltar;
	Leer n;
	Escribir "el resultado de la suma de los digitos del número es: ",sum(n);
FinProceso
