# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:00:28 2020

@author: federrico pfund
"""
import random

#ejercicio n°1  
#.Imprimir en pantalla todos los numeros enteros entre 1 y un numero N ingresado por el usuario.
n=int(input("ingrese un numero:"))
x=1
while x<=n:
    print(x)
    x += 1
print("programa terminado")

#ejercicio n°2
#Imprima en pantalla el siguiente esquema, segun un numero n ingresado por el usuario.Ejemplo a continuacion, para un n ingresado igual a 5.
n=int(input("ingrese un numero :"))
s=1
for i in  range(n,0,-1):
    while i>=s:
        print(i,end=" ")
        i-=1
    print()# despues de mucho tiempo me salio vamos noma jaja!!
print("programa terminado")     
    
# ejercicio n°3
# . Pedirle numeros enteros al usuario y guardarlos en una lista, hasta que el usuario ingrese la letra s en cuyo caso, muestre la lista final y deje de pedir mas numeros.
# metodo centinela
def mi_funci():
    x=input("ingrese un numero:")
    lis=[]
    while x!="s":
        x=int(x)
        lis.append(x)
        x=input("ingrese otro numero:")
    print("programa terminado")
    print("lista:",lis)
    
#ejercicion n°4
#  Imprimir un menu de opciones para el usuario:
 #1. Sumar dos numeros
 #2. Restar dos numeros
 #3. Multiplicar dos numeros
 #4. Dividir dos numeros
 #5. Salir
#definimos nuestras funciones
def suma():
    a=int(input("seleccione un numero para la operacion:"))
    b=int(input("seleccione otro numero para la operacion:"))
    return a+b
def resta():
    a=int(input("seleccione un numero para la operacion:"))
    b=int(input("seleccione otro numero para la operacion:"))
    return a-b
def multiplicacion():
    a=int(input("seleccione un numero para la operacion:"))
    b=int(input("seleccione otro numero para la operacion:"))
    return a*b
def divicion():
    a=int(input("seleccione un numero para la operacion:"))
    b=int(input("seleccione otro numero para la operacion:"))
    return a/b
#funcion para mostrar el menu
def mostrar_menu():
    print("menu de opciones")
    print()
    print('1. sumar')
    print('2. restar')    
    print('3. multiplicar')
    print('4. dividir')
    print('5. salir')
#ejercicion n°5
#funcion para tomar datos de la eleccion del usuario y convocar la operacion correspondiente.
def main():
    while True:#ciclo indefinido.
        while True:#para dar otra oportunidad en caso de que el usuario no ingrese un numero entero.
            try:
                mostrar_menu()
                opcion = int(input("digite la opcion: "))
                if 0<opcion<=5:
                    if opcion==1:
                        return suma()
                        break
                    elif opcion==2:
                        return resta()
                        break
                    elif opcion==3:
                        return multiplicacion()
                        break
                    elif opcion==4:
                        return divicion()
                        break
                    elif opcion==5:
                        break
                else:
                    print("MENSAJE: debe digitar algunas de las opciones propuestas")
            except ValueError:
                    print("ERROR: debe digitar un numero entero valido.")
#ejercicion n°6
#. Escribir una funcion que tome dos numeros, inicio y fin, e imprima en pantalla la secuenciades de inicio hasta fin en la izquierda, y a su lado la secuencia inversa fin hasta inicio.Ejemplo, supongase se le da inicio = 1 y fin = 99, entonces se vera en pantalla:     
def sec():
    inicio=int(input("inicio de la secuencia: "))
    final=int(input("final de la secuencia: "))
    
    while True:
        try:
            inicio +=1
            final -=1
            print(inicio,"---------",final)
            if final==1:
                break
        except ValueError:
            print("ERROR: debe digitar un numero entero valido.")
    #ejercicion n°7        
#. Pedirle numeros enteros al usuario y si son numeros impares guardarlos en una lista llamada impares y a los que sean pares, guardarlos en otra lista llamada pares. Se podran seguir ingresando numeros hasta que el usuario ingrese la letra q en cuyo caso, muestre ambas listas y deje de pedir mas numeros.

def datos():
     listapar=[]
     lisimpar=[]    
     numero = input("ingrese un numero entero:")
     while numero != 'q':
          try:
              n=int(numero)
              if n % 2==0:
                  listapar.append(n)
                                         
              elif n % 2 !=0:            
                    lisimpar.append(n)
              numero = input("ingrese un numero entero:")
              
          except ValueError:
              print("ERROR: debe digitar un numero entero.")
     print("lista par: ",listapar)
     print("lista impar: ",lisimpar)
     
   #ejercicion n°8           
#. Escribir un programita que dada dos listas, que pueden ser de diferentes longitudes, haga una lista nueva que contenga solo los elementos en comun entre ambas. Un ejemplo a continuacion, darıa la lista [1, 2, 3, 5, 8]:
lis=[41,1,2,3,5,8,13,21,34,82,89]
lia=[1,2,3,4,5,6,7,8,9,20,12,11,16]
lisnueva=[]
for i in lis:
    if i in lia:
        lisnueva.append(i)
print("lista  nueva:",lisnueva)
#Crear una funcion que tome una longitud y un caracter e imprima en pantalla la mitadde una piramide, con ese caracter. Ejemplo de lo que imprimira en pantalla si el usuario ingreso 6 y el caracter @ No utilizar metodos de str (excepto len()) ni listas para resolverlo.
def fun():
    n=int(input("ingrese un numero: "))
    sim=input("ingrese un caracter: ")
    
    for i in range(n):
        print(sim*i)
        
#ejercicion n°9
#. Crear un programita para el juego Adivina mi numero. Se debe generar un numero al azar entre 1 y 9 (que los incluya). Pedirle al usuario que lo adivine. Luego decirle si estuvo muy abajo, muy alto o le acerto justo. Seguir preguntandole que adivine hasta que, o bien el usuario quiera salir o bien le haya acertado. El usuario podra salir del todo del juego si ingresa una letra ’s’ (utilizar break como comando para salir del bucle.

intentosRealizados = 0
print('¡Hola! ¿Cómo te llamas?')
miNombre = input() 
número = random.randint(1, 9)
print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 9.')
while intentosRealizados < 6:
    print('Intenta adivinar.') # Hay cuatro espacios delante de print.
    estimación = input("propone un numero:")
    estimación = int(estimación)
    intentosRealizados = intentosRealizados + 1
    if estimación < número:
        print('Tu estimación es muy baja!! sin miedo al exito ' + miNombre + ' vamos animo!!') # Hay ocho espacios delante de print.
    if estimación > número:
         print('Tu estimación es muy alta.')
    if estimación == número:
        break
if estimación == número:
     intentosRealizados = str(intentosRealizados)
     print('¡Buen hecho, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos, ' + ' tu CI es extremadamente alto!! ')


if estimación != número:
     número = str(número)

     print('Pues no. El número que estaba pensando era ' + número)