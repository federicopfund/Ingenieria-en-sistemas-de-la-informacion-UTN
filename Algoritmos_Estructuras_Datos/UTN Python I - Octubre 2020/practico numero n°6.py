# -*- coding: utf-8 -*-
"""


@author: federico pfund
"""
import random


#Ejercicio numero n°1

miarch = open('.txt','r')

with miarch:
    condicion= miarch.readlines()
    for linea in condicion:
        print(linea)

#otra forma de hacerlo.
archivo = open(".txt",'r')
i = 1
for linea in archivo:
    linea = linea.rstrip("\n")
    print("{}: {}".format(i, linea))
    i += 1
archivo.close()

#Ejercicio numero n°2


with open("numero.txt", "w+") as numero:
    numero.write("Este programa fue generado para producir un archivo con numeros aleatorio!\n")
    for i in range(50):
        a =int(random.randint(1,50))
        numero.write('numero aleatorio: % s'% a+'\n')
    
archivo = open("numero.txt",'r')
i = 1
for linea in archivo:
    print("{}: {}".format(i-1, linea))
    i += 1
archivo.close()

#Ejercicio N°3

cantida=int(input("ingrese la cantida de colores que desea para su lista: "))
lista=[]
with open("colores.txt","w+") as colores:
    colores.write("lista de colores del usuario: \n")
    for i in range(cantida):
        ingrese=input("color deceado: ")
        lista.append(ingrese)
        colores.write(f'{i+1}: % s'%ingrese+"\n")
    
#ejercicio N° 4


import random


with open("color.txt","r+") as color:
    linea=color.readlines()
for i in range(len(linea)):
    linea[i]=linea[i].rstrip("\n")
a=random.randint(1,8)
print("lista de colores azar!!")
print()
print("color al azar: {}".format(linea[a]))

#ejercicio N°5

try:
    with open ('datos.txt','r') as datos:
        linea=datos.readlines()
    cuenta=0
    for i in range(len(linea)):
        linea[i]=int(linea[i].rstrip("\n"))
        cuenta = linea[i] + cuenta
    print("suma de los caracteres del archivo datos: ",cuenta)    
except ValueError:
    print("Se aplicó una operación con un parámetro de tipo apropiado pero no así su valor revice su archivo")
        
#ejercicio N°6

with open ('promedio.txt','r+') as promedio:
    linea=promedio.readlines()
cuenta=0
for i in range(len(linea)):
    linea[i]=int(linea[i].rstrip("\n"))
    cuenta = linea[i] + cuenta
promedio=cuenta/len(linea)
print("promedio de archivos: ",promedio)

#ejercicio N° 7

import csv, os

ARCHIVO = "agenda.csv"
CAMPOS = ("Nombre", "Apellido", "Telefono", "Cumpleaños")

def cargar_agenda(archivo):
#"""Carga todos los datos del archivo en una lista y la devuelve."""
    agenda = []
    if not os.path.exists(archivo):
        return agenda
    with open(archivo) as f:
        datos_csv = csv.reader(f)
        encabezado = next(datos_csv)
        for item in datos_csv:
            agenda.append(item)
    return agenda

def guardar_agenda(agenda, archivo):
#"""Guarda la agenda en el archivo."""
    with open(archivo, "a") as f:
        datos_csv = csv.writer(f)
        datos_csv.writerow(CAMPOS)
        datos_csv.writerows(agenda)

def leer_busqueda():
#"""Solicita al usuario nombre y apellido y los devuelve."""
    nombre = input("Nombre: ")  
    apellido = input("Apellido: ")
    return nombre, apellido

def buscar(nombre, apellido, agenda):
#"""Busca el primer item que coincida con nombre y con apellido."""
    for item in agenda:
        if nombre in item[0] and apellido in item[1]:
            return item
    return None
def menu_alta(nombre, apellido, agenda):
#"""Pregunta si se desea ingresar un nombre y apellido y de ser así, pide los datos al usuario."""
    print("No se encuentra {} {} en la agenda.".format(nombre, apellido))
    confirmacion = input("¿Desea ingresarlo? (s/n): ")
    if confirmacion.lower() != "s":
        return
    telefono = input("Telefono: ")
    cumple = input("Cumpleaños: ")
    agenda.append([nombre, apellido, telefono, cumple])

def mostrar_item(item):
#"""Muestra por pantalla un item en particular."""
    nombre, apellido, telefono, cumple = item
    print()
    print("{} {}".format(nombre, apellido))
    print("Telefono: {}".format(telefono))
    print("Cumpleaños: {}".format(cumple))
    print()

def menu_item():
 #"""Muestra por pantalla las opciones disponibles para un item existente."""
     o = input("b: borrar, m: modificar, ENTER para continuar (b/m): ")
     return o.lower()

def modificar(viejo, nuevo, agenda):
#"""Reemplaza el item viejo con el nuevo, en la lista datos."""
    indice = agenda.index(viejo)
    agenda[indice] = nuevo

def menu_modificacion(item, agenda):
#"""Solicita al usuario los datos para modificar una entrada."""
    nombre = input("Nuevo nombre: ")
    apellido = input("Nuevo apellido: ")
    telefono = input("Nuevo teléfono: ")
    cumple = input("Nuevo cumpleaños: ")
    modificar(item, [nombre, apellido, telefono, cumple], agenda)

def baja(item, agenda):
#"""Elimina un item de la lista."""
     agenda.remove(item)

def confirmar_salida():
#"""Solicita confirmación para salir"""
    confirmacion = input("¿Desea salir? (s/n): ")
    return confirmacion.lower() == "s"

def agenda():
#"""Función principal de la agenda.Carga los datos del archivo, permite hacer búsquedas, modificar borrar, y al salir guarda. """
    agenda = cargar_agenda(ARCHIVO)
    while True:
        nombre, apellido = leer_busqueda()
        if nombre + apellido == "":
            if confirmar_salida():
                break
        item = buscar(nombre, apellido, agenda)
        if not item:
            menu_alta(nombre, apellido, agenda)
            continue
        mostrar_item(item)
        opcion = menu_item()
        if opcion == "m":
            menu_modificacion(item, agenda)
        elif opcion == "b":
            baja(item, agenda)
    guardar_agenda(agenda, ARCHIVO)

agenda()

#Ejercicio N°8

with open("agenda.csv","r+") as agenda:
    lista=agenda.readlines()       
    for linea in lista:
        if linea == "\n":
            lista.remove("\n")
        
        
    print("la cantidad de amigos en su lista es de: ",len(lista)-1)
    print(lista)
    
#Ejercicio N°9

numerador=int(input("ingrese el dividendo: "))
denominador=int(input("ingrse el divisor: "))
try:
    divicion = numerador/denominador
    print("el resultado de la divicion es: ",divicion)
    
except:
    print('no se puede dividir por cero')
    
#Ejercicio N°10

def pedir_entero():
#Solicita un valor entero y lo devuelve.Mientras el valor ingresado no sea entero, vuelve a solicitarlo.
    while True:
        valor = input("Ingrese un número entero: ")
        try:
            return int(valor)
        except ValueError:
            print("'{}' no es un número entero.".format(valor))
pedir_entero()

#Ejercicio n°11

def abrir_archivo(archivo,modo):
    try:
        with open(archivo,modo): 
            condicion=open(archivo,modo).readlines()
            for linea in condicion:
                print(linea)
    except FileNotFoundError:
        print("no se encuentra la ruta del archivo especificado,verificar: ")
    except: 
        print("ingreso un modo no adecuado;solo lectura")
abrir_archivo(".txt","r")

#Ejercicio N°13

"""Tipo Significado Exception Excepción genérica.
 Todas las excepciones son de tipo Exception:
     
AssertionError Una instrucción assert falló.

IndexError Se intentó acceder a una secuencia con un índice fuera de rango.

KeyError Se intentó acceder a un diccionario con una clave inexistente.

TypeError Se aplicó una operación a un valor de tipo inapropiado.

ValueError Se aplicó una operación con un parámetro de tipo apropiado pero no así su valor.

ZeroDivisionError Se intentó dividir un número por 0.

IOError Error de entrada / salida (por ejemplo al intentar acceder
a un archivo)"""
