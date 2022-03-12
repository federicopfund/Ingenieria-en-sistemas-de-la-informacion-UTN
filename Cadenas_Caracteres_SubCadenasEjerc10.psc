Proceso ej10_10
    Definir frase,subfrase Como Caracter;
    Definir i,n_subfrase Como Entero;
    //pido la frase y la subfrase, y las paso a minusculas
    Escribir "Ingrese una frase";
    Leer frase;
    frase <- Minusculas(frase);
    Escribir "Ingrese una sub-frase, que quiera contabilizar cuantas veces se repite";
    Leer subfrase;
    subfrase <- Minusculas(subfrase);
    n_subfrase <- 0;
    // Deberia completarlo eliminando los espacios en blanco
    
    // Variando la posicion evaluo cuantas veces se repite la sub frase
    Para i <- 0 hasta Longitud(frase)-1 Hacer
        Si Subcadena(frase,i,Longitud(subfrase)+i-1) = subfrase Entonces
            n_subfrase <- n_subfrase + 1;
        FinSi
    FinPara
    Escribir "La sub-frase se repite ",n_subfrase," veces.";
    
FinProceso