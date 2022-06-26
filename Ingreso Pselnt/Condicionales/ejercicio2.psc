Proceso ejercicio2
	Definir nota1,nota2,nota3 Como Real;
	Definir promedio Como Real;
	Escribir 'digite las 3 calificaciones: ';
	Leer nata1,nota2,nota3;
	promedio <- (nota1+nota2+nota3)/3;
	Si promedio>=70 Entonces
		Escribir 'El alumno esta aprobado con: ',promedio;
	SiNo
		Escribir 'El alumno esta desaprobado con: ',promedio;
	FinSi
FinProceso
