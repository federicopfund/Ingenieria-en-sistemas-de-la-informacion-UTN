Proceso ejercicio3
	Definir compra Como Real;
	Definir descuento,precio_final Como Real;
	Escribir 'Digite la cantidad a pagar: ';
	Leer compra;
	Si compra>100 Entonces
		descuento <- compra*0.2;
	SiNo
		descuento<-0;
	FinSi
	precio_final <- compra - descuento;
	Escribir 'El precio a pagar es: ',precio_final;
	
FinProceso
