//Escriba un subprograma nombrado cambio() que tenga un par�metro en n�mero entero y seis 
// par�metros de referencia en n�mero entero nombrados cien, cincuenta, veinte, diez,
//  cinco y uno, respectivamente. La funci�n tiene que considerar el valor entero
//  trasmitido como una cantidad en d�lares y convertir el valor en el n�mero
//  menor de billetes equivalentes.
SubProceso cambio(dolares)
	Definir cien,cincuenta,veinte,diez,cinco,uno Como Entero;
	Escribir "Billetes de 100: ",((dolares - (dolares mod 100))/100);
	dolares <- dolares mod 100;
	Escribir "Billetes de 50: ",((dolares - (dolares mod 50))/ 50);
	dolares <- dolares mod 50;
	Escribir "Billetes de 20: ",((dolares - (dolares mod 20))/ 20);
	dolares <- dolares mod 20;
	Escribir "Billetes de 10: ",((dolares - (dolares mod 10))/ 10);
	dolares <- dolares mod 10;
	Escribir "Billetes de 5: ",((dolares - (dolares mod 5))/ 5);
	dolares <- dolares mod 5;
	Escribir "Billetes de 1: ",(dolares / 1);
FinSubProceso

Proceso ej12_4
	Definir dolares Como entero;
	Escribir "Ingrese el monto de dolares" Sin Saltar;
	Leer dolares;
	cambio(dolares);	
FinProceso
