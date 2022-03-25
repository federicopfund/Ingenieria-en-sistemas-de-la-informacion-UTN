# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 12:07:52 2020

@author: federico pfund
"""

import random 


#Pedir una frase al usuario y mostrarla en mayusculas y en minusculas.
#ejercicio n°1
frase=input("ingrese una frase: ")
print(frase.lower())
print(frase.upper())
#ejercicio n°2
#Pedir una frase al usuario y si se encuentra en mayusculas devolverla en minusculas, y vice versa
frase1=input("ingrese una frase: ")

if frase1==frase1.lower():
    print(frase1.upper())
else:
    print(frase1.lower())
#ejercicion n°3
#Pedir una frase y una palabra al usuario. Determinar si la palabra se encuentra en la frase. *Utilizar in    
unafrase=input("ingrese una frase:")
unapalabra=input("ingrese una palabra:")

if unapalabra in unafrase:
    print("la palabra se encuentra en la frase")
    
else:
    print("la palabra no se encuentra en la frase")
#ejercicio n°4    
#Pedir una palabra al usuario y determinar si ingreso todos numeros o una palabra cualquiera.

unapalabra=input("ingrese una palabra:")

if unapalabra==str(unapalabra):
    print("es una palabra")
else:
    print("son todos numeros")
#ejercicio n°5
#Pedir una frase al usuario y una palabra. Determinar si esa frase empieza o termina condicha palabra.
unafrase=input("ingrese una frase:")
unapalabra=input("ingrese una palabra:")

if unafrase.startswith(unapalabra):
    print("la frase comienza con la palabra",unapalabra)
elif unafrase.endswith(unapalabra):
    print("la frase termina con la palabra",unapalabra)
    
else:
    print("la palabra no se encuentra en la frase")
#ejercicio n°6    
#Realizar un programa que pida una frase y una letra. Y determine la cantidad de ocurrencias de esa letra en dicha frase.
unafrase=input("ingrese una frase:")
unaletra=input("ingrese una letra:")
cantidad=0

for i in range(len(unafrase)):
    if unafrase[i]==unaletra:
        cantidad=cantidad + 1
print("la cantidad de letras es",cantidad)
#ejercicio n°7
#Realizar un programita que tome una frase y devuelva la misma frase con guiones intercalados. (hola → h-o-l-a) Tip: utilizar los metodos split y join: Googlear sobre ellos.
frase=input("ingrede una frase: ")
lt= "-".join(frase)
print(lt)
 #ejercicio n°8
#. Realizar un programita que dada la frase ”23, 6, 82, 5, 123, 65”devuelva la lista [23,6,82,5,123,65]. Tip: utilizar el metodo 
lista="23,6,82,5,123,65"
lt=lista.split()
print(lt)
#ejercicio n°9
#¿Como puedo acceder al ultimo elemento de una lista, siempre, sin saber a priori cuantos elementos tiene ni utlizando len() a tal fin?
"""la manera de extraer al ultimo elemento de la es analizando que hay en dicho lugar ejem:"""
lista=[1,2,3,4,5,6,7,87,98]
print(lista[-1])
#ejercicio n°10
#Dada una lista de 10 frutas cualesquiera, realizar las siguientes operaciones: (Utilizar los metodos de las listas en este punto)
lista=["anana","durazno","naranja","manzana","pera","damasco","frutilla","melon","kiwi","cereza"]
#Determinar si la fruta cereza se encuentra en dicha lista.
for x in lista:
    if (x=="cereza"):
        print("cereza se encuentra en la lista")
li=input("puede ingresar una fruta que te guste?") #Pedirle una fruta al usuario, y agregarla a la lista.
lista.insert(-1,li)
print(lista)
print("eliminamos la fruta durazno de la lista")
lista.remove("durazno") #Si se encuentra la fruta durazno, eliminarla de la lista.
print(lista)
print("Mostrar las primeras 5 frutas de la lista.")
print(lista[0:5])#imprimir las primeras 5 frutas.
print("total de elemntos que compone la lista:")
print(len(lista))#mostrar el total de elementos que compone la lista.
lis=[] #ingresamos 5 frutas y las guardamos en una lista.
print("Ingresa 5 frutas") 
for x in range(5):
    ingresado = input("Ingrese:")  # Capturamos lo ingresado por teclado
    lis.append(ingresado)
print(lis)
listanueva=lis + lista  #concatenacion de listas.
print(listanueva)
print("ordenamos la lista nueva:")
listanueva.sort()
print(listanueva)

# EJERCICIO N°11

palabra=input("ingrese una palabra:")#Pedir al usuario una palabra e imprimirla en vertical, una letra por l´ınea.

for i in palabra:
    print(i)

# Pedir al usuario una palabra e imprimirla en vertical, pero en orden inverso, es decir,la primer letra a imprimir, sera la  ultima de la palabra.
palabra=input("ingrese una palabra: ")
palabra.split()
l=''.join(reversed(palabra))
for i in l:
    print(i)
#sumatoria
print("sumatoria:")
suma=0
for J in range(1,51):
    suma=suma + (J**2+3*J)
print(suma)
#Pedir al usuario dos numeros enteros a, b y calcular 
a=int(input("ingrese un numero: "))
b=int(input("ingrese otro numero: "))
c=int(input("ingrese otro numero: ")) 
suma=0
for i in range(1,46):
    suma= suma + (i+((a+b)/a**2+b**2+i**2))
print(suma) 
#ejercicio n°12
#Pedir al usuario 10 numeros enteros y guardarlos en una lista. Ordenar la lista, y mostrarla en pantalla. Mostrar ademas, el valor maximo y mınimo de la misma. Utilizar los metodos de la lista, ademas de las funciones max() y min()
lis=[] #ingresamos 10 numeros y las guardamos en una lista.
print("Ingresa 10 numeros") 
for x in range(10):
    ingresado = int(input("Ingrese numero n°:"))  # Capturamos lo ingresado por teclado
    lis.append(ingresado)# agregamos el valor seleccionado por el usuario a la lista.
lis.sort()#ordenamos los valores de mayor a menor.
    
print("lista :",lis)
print("valor maximo de la lista: ",max(lis))
print("valor minimo de la lista:",min(lis))
#ejercicio n°13
#. Realizar un programa que permita al usuario ingresar una longitud e imprima en pantalla un rectangulo de numerales, hueco por dentro. Por ejemplo, si se ingreso 4, se vera en pantalla: Tip: Puede ser util pensarlo por lınea horizontal
anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))

for i in range(anchura):#la primera y la ultima linea se generan mediante un bucle simple.
    print("* ", end="")
print()
#las lineas centrales requieren un bucle anidado. por un lado,cada linea de la figura esta formadad por dos estrellas y varios espacios en blanco.eso nos dice que tendremos que escribir un bucle como este (se ha redeado con un borde el codigo qque separa el dibujo rodeado por el mismo borde)..
for i in range(altura - 2):
    print("* ", end="")
    for j in range(anchura - 2):
        print("  ", end="")
    print("*")
#finalmente,para generar la figura completa,hay que es escribir un bucle detras del otro()primero el bucle simple que genera una linea de estrellas ,depues el bucle anidado que genera lineas centrales y por ultimo otro bucle simple que genera una lista de estrellas.
for i in range(anchura):
    print("* ", end="")

print("NUMEROS ALEATORIOS:")
#ejercicio n°14
#NUMEROS SEUDO-ALEATORIO RANDON
# Dada una frase ingresada por el usuario, devolver en pantalla una letra de la misma,al azar.
frase=input("ingrese una: ")
lista=list(frase)
p=random.choice(lista)
print(p)
#Pedir un numero al usuario, y determinar si este es mayor o menor que un numero aleatorio entre 1 y 100.
num=int(input("ingrese un numero entero: " ))
num1=random.randint(1,100)
if num>=num1:
    print("el numero ingresado por el usuario es mayor que el numero seudo-aleatorio entre 1 a 100",num)
else:
    print("el numero seudo-aleatorio es mayor que el numero ingresado por el usuario: ",num1)
#ejercicio n°15
#. Dada una lista de colores inventada, devolver un color al azar y mostrarlo en pantalla.
lista=["rojo","azul","violeta","naranja","verde","marron"]
r=random.choice(lista)
print(r)
# ejercicio n°16
#Llenar una lista con 50 numeros enteros aleatorios entre 1 y 10.
lista=[]
for i in range(51):
    nu=random.randint(1,10)
    lista.append(nu)
print(lista)
#ejercicio n°17
# Llenar una lista con 10 numeros con decimales aleatorios entre 0 y 1.
lista=[]
for i in range(11):
    fl=random.random()
    lista.append(fl)
print(lista)
#ejercicio n° 18
#. Determine que hace el siguiente codigo, en palabras simples, para que sirve este programita:
    #el codigo cuenta los espacio, de la cual no funciona porque no reconoce los apostrofes (’ ’).
    #en lugar de los apostrofes van (" ").
frase = input("Ingrese una frase:")
frase = frase.strip ()
c = 0
for i in range(len(frase)):
       # if (frase[i] == ’ ’ ):
            c = c + 1
print(c+1)
# ejercicio n°19
#. Realizar un programa que permita al usuario ingresar una frase y determine la cantidad de vocales que hay en la misma.
frase=input("ingrese una frase: ")
lista=list(frase)
cantidad=0# variable que acumula las cantidad de vocales de una frase.
cant=0#variable que acumula la cantidad de consonantes de la frase.
for i in lista:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        cantidad=cantidad + 1 
    else:
        cant=cant + 1
print("cantidad de vocales de la frase:",cantidad)
print("cantidad de consonantes en la frase:",cant)
#ejercicio n°20
#. Pedirle una frase al usuario y una letra, determinar cuantas veces esta esa letra en la frase.
frase=input("ingrese una frase: ")
letra=input("ingrese una letra:")
lista=list(frase)
cantidad=0

for i in lista:
    if i==letra:
        cantidad=cantidad + 1 
print("cantidad de veces que aparece la letra seleccionada:",cantidad)  
#ejercicio n°21  
#. Realizar un programa que permita al usuario ingresar una frase y determine la cantidad de palabras que hay en la misma.
frase=input("ingrese una frase: ")
lista=frase.split()
cantidad=0
for i in lista:
    cantidad=cantidad + 1 
print("cantidad de palabras en la frase:",cantidad) 
#ejercicio n°22
#. Realizar un programa que permita al usuario ingresar una palabra e imprima en pantalla la palabra resultante de haberle quitado todas las vocales.
frase=input("ingrese una palbra: ")
lista=list(frase.lower())

for i in lista:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        lista.remove(i)
lt=" ".join(lista)
print("frase sin vocales:",lt)
#ejercicio n°23
#Pedirle al usuario dos palabras. Determinar si una es la inversa de la otra.
palabra1=input("ingrese una palabra:")
palabra2=input("ingrese una palabra:")

if palabra1==''.join(reversed(palabra2)):
    print("la palabra 1 es la inversa de la palabra 2")
else:
    print("la palabras no coinciden con su inversa")
#ejercicio n°24
#Pedirle una palabra al usuario y determinar si es palındrome o no. (si se lee igual del derecho que del reves)
palabra3=input("ingrese una palabra:")

if palabra1==''.join(reversed(palabra2)):
    print("la palabra es polindromica")
else:
    print("la palabra no es polindromica")