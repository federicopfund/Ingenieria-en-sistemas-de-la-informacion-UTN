Proceso Alreves
	// Definimos Tipos de Variables.
	Definir Caden,NuevaCadena,Matrix Como Caracter;
	Definir i,Aqui,j Como Entero;
	// Pedimos datos al usuario
	Escribir 'Digite una Cadena de caracter: ';
	// Leemos los datos ingresado por el usuario
	Leer Caden;
	// Asignamos una cadena vacia a una variable 
	NuevaCadena <- '';
	// Definimos Aqui la longuitud de la cadena
	Aqui <- longitud(Caden);
	// inicializamos un iterador en 0
	j <- 0;
	Para i<-0 Hasta Aqui Hacer
		// Dentro de un para, Asignamos una pocion de cadena dentro de una una variable vacia
		NuevaCadena <- SubCadena(Caden,Aqui-i,Aqui-j);
		j <- j+1;
		// Mostramos la nueva cadena
		Escribir NuevaCadena;
	FinPara
FinProceso
