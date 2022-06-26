Proceso ejercicio4
	Definir num1,num2,resultado Como Real;
	Escribir 'Digite dos numeros: ';
	Leer num1,num2;
	Si num1=num2 Entonces
		resultado<- num1*num2;
	SiNo
		Si num1>num2 Entonces
			resultado<- num1-num2;
		SiNo
			resultado<-num1*num2;
		FinSi
	FinSi
	Escribir 'El resultado es: ',resultado;
FinProceso
