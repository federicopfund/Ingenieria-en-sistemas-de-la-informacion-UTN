// Implementación del cálculo de una potencia mediante una función recursiva

SubProceso resultado <- Potencia(base, exponente)
    Definir resultado como Entero;
    Si exponente=0 Entonces
        resultado <- 1;
    SiNo 
        resultado <- base*Potencia(base,exponente-1); 
    FinSi
FinSubProceso

Proceso ej12_7
    Definir base,exponente como Entero;
    Escribir "Ingrese Base";
    Leer base;
    Escribir "Ingrese Exponente";
    Leer exponente;
	base <- potencia(base,exponente);
    Escribir "El resultado es ",base;
FinProceso
