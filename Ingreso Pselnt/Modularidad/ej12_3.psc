// Desarrollar un programa que pueda calcular el valor del tipo de cambio de moneda
// (de tu moneda a dolar y viceversa)
Funcion dolar <- peso_a_dolar(peso,cotizacion_dolar)
	Definir dolar Como Real;
	dolar <- peso * cotizacion_dolar;
FinFuncion
Funcion peso <- dolar_a_peso(dolar,cotizacion_peso)
	peso <- dolar * cotizacion_peso;
FinFuncion
Proceso ej12_3
	Definir n_peso,n_dolar,cotizacion_dolar,cotizacion_peso Como Real;
	Definir selector Como Entero;
	cotizacion_dolar <- 114.75;
	cotizacion_peso <- 0.00871459;
	Escribir "Ingrese 1 para pasar de pesos a dolares o 2 para pasar dolares a pesos: " Sin Saltar;
	Leer selector;
	Segun selector Hacer
		1:
			Escribir "Ingrese la suma de pesos a convertir a dolares: " Sin Saltar;
			Leer n_peso;
			Escribir "ARS$ ",n_peso," = U$D ",peso_a_dolar(n_peso,cotizacion_dolar);
		2:
			Escribir "Ingrese la suma de dolares a convertir a pesos: " Sin Saltar;
			Leer n_dolar;
			Escribir "U$D ",n_dolar," = ARS$ ",dolar_a_peso(n_dolar,cotizacion_dolar);
		De Otro Modo:
			Escribir "";
	FinSegun
	
FinProceso
