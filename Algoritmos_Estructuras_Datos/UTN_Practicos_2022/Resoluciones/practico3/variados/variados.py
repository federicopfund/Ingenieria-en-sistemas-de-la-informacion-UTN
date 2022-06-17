## Pedirle al usuario la cantidad de notas que desea ingresar. Luego pedir cada nota, y
## guardarlas

import random
from turtle import delay


def cantidadenotas():
    lista = []
    for i in range(8):
        numero = int(input("Ingrese una nota: "))
        lista.append(numero)
    print(lista)
    promedio = sum(lista)/len(lista)
    print(f"El promedio es: {round(promedio,2)}")

## Dado un n ingresado por el usuario, realizar la suma de los n primeros terminos de la
## serie a continuacion. Mostrar el resultado.
## 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + 1/8 + 1/9 + 1/10

def serie():
    n = int(input("Ingrese un n: "))
    suma = 0
    if n == 0:
        print(suma)
    else:
        for i in range(1,n+1):
            suma += 1/i
        print(suma)
## Cuenta Regresiva: Se requiere un programa que permita el ingreso de un numero positivo
## y muestre en pantalla la cuenta regresiva desde el numero ingresado hasta llegar a 0.
## Realizar diferentes versiones del programa, utilizando en cada una, una estructura de
## bucle diferente de las que tiene disponibles en Python.
## versio 1
def cuentaregresiva():
    n = int(input("Ingrese un n: "))
    if n == 0:
        print(n)
    else:
        for i in range(n,0,-1):
            print(i)
            delay(5)

# version 2

def cuentaregresiva2():
    n = int(input("Ingrese un n: "))
    if n > 0:
        for i in range(n,0,-1):
            print(i)
            delay(5)
    else:
        print("Ingrese un n positivo")

## version 3

def cuentaregresiva3():
    n = int(input("Ingrese un n: "))
    if n < 0:
        print("Ingrese un n positivo")
    else:
        for i in range(n,0,-1):
            print(i)
            delay(5)

## version 4

def cuentaregresiva4():
    n = int(input("Ingrese un n: "))
    if n < 0:
        print("El numero debe ser positivo")
    else:
        for i in range(n,0,-1):
            print(i)
            delay(5)
## version 5
def cuentaregresiva5():
    n = int(input("Ingrese un n: "))
    if n <= 0:
        print("Ingrese un n positivo")
    else:
        for i in range(n,0,-1):
            print(i)
            delay(5)


##Suma de Numeros Positivos y Negativos: Se requiere un programa que permita el ingreso
## de 10 numeros y al finalizar muestre en pantalla la cantidad numeros positivos y por otra
## parte la cantidad de numeros negativos que fueron ingresados.

def sumapositivosnegativos():
    lista = []
    for i in range(10):
        numero = int(input("Ingrese un numero: "))
        lista.append(numero)
    print(lista)
    positivos = 0
    negativos = 0
    for i in lista:
        if i > 0:
            positivos += 1
        else:
            negativos += 1
    print(f"La cantidad de numeros positivos es: {positivos}")
    print(f"La cantidad de numeros negativos es: {negativos}")

 ##   Permitir ingresar numeros enteros hasta que se ingrese la opcion ”s” de salir. Plantee
## primero el diseno en pseudocodigo del algoritmo e implemente luego dos versiones.
## a) La primer implementacion funcionarıa en cualquier lenguaje.
def nuemerosenteros():
    lista = []
    while True:
        numero = int(input("Ingrese un numero: "))
        lista.append(numero)
        if numero == "s":
            break
    print(lista)

## b) La segunda implementacion debera aprovechar que Python es un lenguaje dinamicamente tipado
## respuesta de b):no se tiene que preocupar por el tipo de dato de los valores que se van a almacenar.
def nuemerosenteros1():
    lista = []
    while True:
        numero = input("Ingrese un numero: ")
        if numero == "s":
            break
        else:
            lista.append(numero)


##. Disenar e implementar un algoritmo que permita ingresar una serie de numeros, sumar
## todos los pares y al terminar la serie mostrar dicha suma. Si se ingreso algun impar,
## mostrar un mensaje Se ingresaron impares. Para finalizar el ingreso, indicar la cantidad
## de numeros a ingresar al principio del programa, o interrumpir la carga cuando se ingrese
## el numero 99.

def SupremeMachineComputing():## paa que nombre le pongo?
    lista = []
    suma = 0
    while True:
        numero = int(input("Ingrese un numero: "))
        if numero == 99:
            break
        lista.append(numero)
    print(lista)
    for i in lista:
        if i % 2 == 0:
            suma += i
## Permitir ingresar 10 numeros al usuario. Determinar y mostrar el menor y el mayor.

def ingresa():
    lista = []
    for i in range(10):
        numero = int(input("Ingrese un numero: "))
        lista.append(numero)
    print(f"numero minimo ingresado: {min(lista)}, numero maximo ingresado: {max(lista)}")

## Numero Invertido: Se requiere mostrar en pantalla un numero invertido de 6 cifras, al
## que fuera ingresado por teclado. 
## Ejemplo: en pantalla se vera: “El numero ingresado es 140975, invertido es: 579041”
def inverso():
    ## no se puede como tipo int deviuelve TypeError solo funciona como string
    ## buen hecho
    numero = input("Ingrese un numero: ")
    ## Mal hecho 
    ## - output = TypeError: 'str' object cannot be interpreted as an integer
    ## numero = int(input("Ingrese un numero: "))
    print(f"El numero ingresado es: {numero}, invertido es: {numero[::-1]}")

## Pedirle al usuario dos numeros positivos, a y b. Controlar que a < b. Mostrar en pantalla
## los numeros del intervalo cerrado [a, b] La computadora debera ahora seleccionar al azar
# un numero de ese intervalo. Y el usuario debera adivinar cual numero ha sido seleccionado
## por la computadora, obteniendo un mensaje de exito en caso de acertar. El usuario solo
## tendra 10 vidas (numero de intentos) y en caso de no acertar, debera obtener un mensaje
# de pucha.

def pucha():
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un numero: "))
    if a > b:
        print("Ingrese un numero menor para a")
        a = int(input("Ingrese un numero: "))
    else:
        for i in range(a,b):
            print(i)
        numero = random.randint(a,b)
        seleccion = int(input(f"Adivina que numero salio:"))
        while intentos < 10:
            if seleccion == numero:
                print("Felicidades, adivinaste")
                break
            else:
                intentos += 1
                seleccion = int(input(f"Adivina que numero salio:")) 
        print("Pucha, no adivinastes")
    
## El problema es el siguiente, el usuario debera poder ingresar la longitud de la base de
## una piramide y el algoritmo debera imprimir en pantalla una piramide de numerales. Por
## ejemplo, si se ingresa 7, se deberıa ver en pantalla:
##a) Disene el algoritmo que imprima ese triangulo, en pseudocodigo.
##b) Determine que restricciones deberıa contemplar para que el triangulo quede bien
## formado. ¿Cualquier valor para la longitud de la base servira?
##c) Implemente el programa en Python a partir del pseudocodigo creado.
## triangulo de pascal con *
def piramide():
    base = int(input("Ingrese la base de la piramide: "))
    for i in range(base):
        for j in range(base):
            if j < base - i :
                print(" ", end="")
            else:
                print("*", end="")
        print()
