## Pedir el nombre al usuario, y corroborar si ese nombre existe entre los nombres de usuarios
## validos guardados en una lista.
def pedirnombre():
    nombre = input("Ingrese su nombre: ")
    lista = ["Juan","Pedro","Miguel","Ana","Sofia","Jorge","Maria","Carmen","Julieta","Pablo","Rosa","Lucia","Luis","Ricardo","Lorena","Juan","Pedro","Miguel","Ana","Sofia","Jorge","Maria","Carmen","Julieta","Pablo","Rosa","Lucia","Luis","Ricardo","Lorena"]
    if nombre in lista:
        print(f"El nombre {nombre} ya esta registrado")
    else:
        print(f"El nombre {nombre} no esta registrado")

## Implemente el programa que pide la usuario 8 nombres del algoritmo del practico anterior.
## En ese ejercicio tenıa que intentar disenar un algoritmo que seleccionase los nombres que
## empiezan con la letra M de una serie de nombres otorgados por el usuario. Utilice para
## resolverlo los tipos de datos y comandos que le parezcan mas apropiados.

def nombre():
    lista = []
    for i in range(8):
        nombre = input("Ingrese su nombre: ")
        lista.append(nombre)
    print(lista)
    lista2 = []
    for i in lista:
        if i[0]=="M":
            lista2.append(i)
    print(lista2)

## Realizar un programita que le pida ingresar una frase al usuario y coloque cada palabra
## de la misma como elemento de una lista.

def frases():
    frase = input("Ingrese una frase: ")
    lista = frase.split(" ")
    print(lista)

## Realizar un programita que le pida ingresar una frase al usuario y coloque cada letra
## como elemento de una lista

def palabra():
    frase = input("Ingrese una frase: ")
    lista = []
    for i in frase:
        lista.append(i)
    print(lista)

## El usuario debera poder ingresar varios nombres completos. El
## programa debera luego, colocar los nombres en una lista y los apellidos en otra.
## ejemplo: Luis Perez -> [“Luis”, “Perez”]
def nombreapellido():
    lista = []
    lista2 = []
    for i in range(5):
        nombre = input("Ingrese su nombre: ")
        lista.append(nombre)
    for i in lista:
        lista2.append(i.split(" "))
    print(lista2)

## Se deberan ingresar 8 numeros. Se mostrara el promedio, redondeado a 2 decimales.

def promedioredondeo():
    lista = []
    for i in range(8):
        numero = int(input("Ingrese una nota: "))
        lista.append(numero)
    print(lista)
    promedio = sum(lista)/len(lista)
    print(f"El promedio es: {round(promedio,2)}")
## Pedir al usuario una frase. Determinar de al menos dos modos diferentes con y sin listas
# la cantidad de palabras que hay en dicha frase.
## con lista
def cantidadpalabrasconlista():
    lista = []
    frase = input("Ingrese una frase: ")
    for i in frase:
        lista.append(i)
    print(lista)
    print(f"La cantidad de palabras es: {len(lista)}")
## sin lista
def cantidaddepalabrassinlista():
    frase = input("Ingrese una frase: ")
    cantidad = len(frase.split(" "))
    print(f"La cantidad de palabras es: {cantidad} ")
## Dada una lista de numeros, ingresada por el usuario o inventada por usted, cree otra lista
## con la cantidad de dıgitos de cada numero de la misma.

def digitos():
    lista = []
    for i in range(5):
        numero = int(input("Ingrese un numero: "))
        lista.append(numero)
    print(lista)
    lista2 = []
    for i in lista:
        lista2.append(len(str(i)))
    print(lista2)