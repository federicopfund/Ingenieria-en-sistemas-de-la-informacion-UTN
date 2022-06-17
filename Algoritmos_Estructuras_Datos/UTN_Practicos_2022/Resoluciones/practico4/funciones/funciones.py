# Crear una funcion que tome un argumento numerico y devuelva ese numero elevado al
# cuadrado. Ejemplo: elevacuadrado(2) deberia devolver 4.
# Pedirle al usuario 5 numeros, de a uno, e ir
# mostrando cada numero elevado al cuadrado (utilizando dicha funcion).



from ast import Try


def elevacuadrado(numero):
    return numero**2

def pedirNumeros():
    ## pide numeros al usuario y los eleva al cuadrado
    for i in range(5):
        numero = int(input("ingrese un numero: "))
        print(elevacuadrado(numero))

## Crear una funcion llamada es positivo que tome un numero como argumento y devuelva
## verdadero o falso, como valores logicos, si el numero es positivo o no.

def espositivo(numero):
    
    if numero > 0:
        return True
    else:
        return False

##3. Crear una funcion llamada iguales, que tome dos palabras como parametros, y determine
## si son iguales o no. Devolviendo verdadero (true) si lo son, o falso (false) en caso contrario.

def iguales(palabrasq, palabrasw):
    return palabrasq == palabrasw

## Crear una funcion llamada signo, que tome un numero y devuelva 1 si este es positivo y
## -1 si este es negativo.

def signo(numero):
    try:
        if numero > 0:
            return 1
        else:
            return -1
    except TypeError:
        print("Error, el valor ingresado no es un numero")
## Crear una funcion llamada escalon, que tome un numero y devuelva 1 si este es positivo
## y 0 si este es negativo. considera las excepciones con try.

def escalon( numero ):
    try:
        if numero > 0:
            return 1
        else:
            return 0
    except TypeError:
        print(f"Error, el valor ingresado no es un numero, verifica el parametro: {numero}")

## desarrolla un tes para la funcion escalon, capturas las excepciones con try.
def tes():
    lista_tes_escalon=[escalon(1),
        escalon(-1),
        escalon("hola")]
    for i in lista_tes_escalon: 
        try:
            if type(i) == int:
                if i == 1:
                    print(f"el numero ingresado es positivo, parametro: {i}")
                else:
                    print(f"El numero ingresado es negativo, parametro: {i}")
        except TypeError:
            print(f"Error, el valor ingresado no es un numero, verifica el parametro: {i}")
    
## Crear una funcion llamada delta de dirac que tome dos numeros enteros y devuelva 1 si
## ambos numeros son iguales, y 0 sino.

def delta(numero1, numero2):
    if numero1 == numero2:
        return 1
    else:
        return 0

## Crear una funcion llamada raiz uno, que tome tres parametros: a, b, c. Y calcule solo la
# primera raız de la funcion cuadratica. ¿La funcion deberıa devolver un valor numerico
# entero o con decimales?
# camptura las excepciones con try.
def raiz(a,b,c):
    try:
        if a == 0:
            print("El valor de a no puede ser 0")
        else:
            x1 = ((-1*b) + (b**2 - (4*a*c))**0.5)/(2*a)
            x2 = ((-1*b) - (b**2 - (4*a*c))**0.5)/(2*a)
            print(f"Raices x1: {x1}, x2: {x2}")   
            return (x1, x2)
    except TypeError:
        print("Error, el valor ingresado no es un numero")
    except ValueError:
        print("Error, el valor ingresado no es un numero")

## Crear una funcion que tome tres numeros como parametros n, a, b, y devuelva verdadero
## o falso, segun n pertenece o no al intervalo cerrado [a, b].
# c
 
def tresnumero(n,a,b):
    try:
        if n >= a and n <= b:
            return True
        else:
            return False
    except TypeError:
        print("Error, el valor ingresado no es un numero")

## Crear una funcion que tome una palabra y devuelva la cantidad de vocales que tiene.Por
# ejemplo, si se le da el siguiente argumento a la funcion: ’hola’ la funcion deberıa devolver 2.
# camptura las excepciones con try.

def cantidadvocales(palabra):
    try:
        vocales = 0
        for i in palabra:
            if i in ["a","e","i","o","u"]:
                vocales += 1
        print(f"la cantidad de vocales es: {vocales}")
    except TypeError:
        print("Error, el valor ingresado no es una palabra")

## Crear una funcion que convierta una temperatura en Fahrenheit, en su temperatura equivalente, en grados Celsius.
# camptura las excepciones con try.
# Pedirle luego, al usuario temperaturas en Fahrenheit, unas 10 e ir mostrandole su conversion a grados centıgrados
def fahrenheit(grados):
    try:
        grados = (grados - 32) * 5/9
        print(grados)
    except TypeError:
        print("Error, el valor ingresado no es un numero")

## # Pedirle luego, al usuario unas 10  temperaturas en Fahrenheit,  e ir mostrandole su conversion a grados centıgrados

def muestrafahrenheit():
    for i in range(10):
        try:
            grados = int(input("Ingrese los grados en Fahrenheit: "))
            print(fahrenheit(grados))
        except ValueError:
            print("Error, el valor ingresado no es un numero")

## Crear una funcion que tome dos palabras como parametros, y devuelva el texto resultante
## de concatenar ambas palabras.

def concatenar(palabra1, palabra2):
    print(f"{palabra1 + palabra2}")

## Crear ahora una segunda funcion, que tome un tercer argumento extra, y haga lo mismo
## que la funcion del punto anterior, pero esta vez, utilizando el tercer argumento para saber
## si debe agregar o no un espacio entre medio de las dos palabras a concatenar. ¿Que tipo
## de dato utilizarıa para ese tercer argumento?

def concatenar1(palabra1, palabra2, espacio):
    if espacio == True:
        print(f"{palabra1}  {palabra2}")
    else:
        print(f"{palabra1}{palabra2}")

##. Crear una funcion que tome como argumentos una frase y una letra, y determine cuantas
## veces esta esa letra esta en dicha frase.
# Ejemplo: Si se le pasan los siguientes dos argumentos ’Joker’ y ’k’ la funcion deberıa
## devolver el valor numerico 1, si la funcion en cambio, recibe los valores ’Pedrito’ y ’a’
## deberıa devolver 0, y as´ı suc.

def letra(frase, letra):
    try:
        print(f"Aparece {frase.count(letra)} Veces la letra {letra} en la frase {frase}.")
    except TypeError:
        print("Error, el valor ingresado no es una palabra")

## Crear una funcion llamada capitalizar que tome una palabra como argumento y devuelva
## una palabra con la primer letra en mayusculas, y resto de las letras en minusculas, de la
## palabra original.

def capitalizar(palabra):
    try:
        print(f"{palabra.title()}")
    except TypeError:
        print("Error, el valor ingresado no es una palabra")

## . Crear una funcion que tome una lista de valores numericos como argumento, de dos
## elementos nada mas, y devuelva la lista ordenada. En el caso de Python, ¿Necesito utilizar
## una segunda lista, auxiliar para modificarla, o pudo devolver la lista original, el argumento
## que recibio, modificado y ordenado?

def ordenarlista(lista):
    try:
        lista.sort()
        print(f"La lista ordenada es: {lista}")
    except TypeError:
        print("Error, el valor ingresado no es una lista")

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comp = 0
    comparaciones = 0

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            comp = reubicar(lista, i + 1)
        comparaciones += comp
        # print("DEBUG: ", lista)
    
    return comparaciones
#%%
#< <------------------------ Reubicar Elemento ------------------------------>
def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    computer = 0

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        computer += 1

    lista[j] = v

    return computer

# Realizar una funcion que tome dos numeros: a, b y devuelva la cantidad de numeros pares
# que hay en el intervalo cerrado [a, b]. Controlar que a <= b.

def cantidadpares(a,b):
    try:
        if a <= b:
            contador = 0
            for i in range(a, b+1):
                if i % 2 == 0:
                    contador += 1
            print(contador)
        else:
            print("Error, el valor de a no es menor o igual que b")
    except TypeError:
        print("Error, el valor ingresado no es un numero")
