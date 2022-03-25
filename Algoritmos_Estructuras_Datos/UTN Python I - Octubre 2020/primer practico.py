# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 02:25:49 2020

@author: federico cristian pfund
"""

#PRIMER PRACTICO:

#EJERCICIO N°1:
    
#1)Calcule la raíz cuadrada del numero 458. Muestre el resultado completo con decimales,y luego muestre lo truncado

import math

a=458
p=math.sqrt(a)
print("numero con decimales:",p)
#numero truncado
r1=math.trunc(p)
print("numero truncado:",r1)

#EJERCICIO N°2:
    
#2)Realizar el programa que calcule cada una de las siguientes expresiones: (*La sumatoria y la productoria de los puntos e, f desarróllelas primero en papel para calcular dicha expresión numérica)

w1=(3+8)*(2-26)
print("a)el producto de dos binomios es:",w1)
x=34
n=3
w2=math.pow(x,n) 
print("b)la potencia cubica de 34 es:",w2)

w3=(2*(10-2))/(-1*(8-12))
print("c)resultado del cociente:",w3)

w4=3*math.sqrt(9)
print("d)constante multiplica a una raiz:",w4)

    
#se especificara una "n" para que el usuario seleccione el extremo final de la sumatoria  "eleccion de usuario".
print("e)sumatoria: ")
n= int(input("cargue un valor de n: "))
i=1 # extremo inicial de la sumatoria.
sumatoria=0 #variable para almacenar la operacion "sumatoria" inicia en 0..
 
while i <= n:     #contruimos  nuestro ciclo.
    sumatoria += i  # condicion de nuestro ciclo.
    i += 1        #avance de nuestro ciclo.
print("el valor de sumatoria es:"+str(sumatoria))  # imprimir el valor de sumatoria.
  #se especificara una "n" para que el usuario seleccione el extremo final de la productoria  "eleccion de usuario".
print("f)productoria: ")
n= int(input("cargue un valor de n: ")) 
j=2 # extremo inicial de la productoria.
productoria=1 #variable para almacenar la operacion "productoria" inicia en 0..
 
while j <= n:     #contruimos  nuestro ciclo.
    productoria *= j+1 # condicion de nuestro ciclo.
    j += 1        #avance de nuestro ciclo.
print("el valor de productoria es:"+str(productoria))  # imprimir el valor de productoria.
  
w7=(1/2)+(2/3)+(3/4)+(4/5)
print("g)valor de los cocientes es:",w7)

w8=(-8+math.sqrt(8**2-4*3*2))/(2*3)
print("h)valor de bhaskara es:",w8)

#EJERCICIO N°3:
    
#Realizar un programa que calcule para una temperatura ingresada por el usuario en Fahrenheit, su temperatura equivalente, en grados Celsius. Recordar que la relacion entre ambas cantidades es: Tc = (5/9)*(Tf-32).

print("programa de temperatura")

Tf=int(input("ingrese la temperatura en Fahrenheit Tf:"))
Tc = (5/9)*(Tf-32)
print("temperatura en centigrados tc:",Tc)

#EJERCICIO N°4:
    
#Escribir un programita que permita convertir una medida en pulgadas, a una medida en metros. *Una pulgada es 0.0254 mtrs.

pulgadas=int(input("ingrese el valor en pulgas p:"))
cm=pulgadas*2.54
print("medida en centimetros cm:",cm)

#EJERCICIO °5:
    
#Realizar un programita que pida un nombre al usuario e imprima en pantalla un saludo de bienvenida junto al nombre ingresado. (”Hola Pepe!”por ejemplo, si el usuario ingreso Pepe.

nombre=input("ingrese su nombre:")
print("hola "+str(nombre))

#EJERCICIO N°6:
    
#Realizar un programita que pida un numero y determine si es par o impar.

n=int(input("ingrese un numero:"))

if n % 2==0:
    print("el numero es par")
else:      
    n % 2 !=0
    print("el numero es impar")
    
#EJERCICIO N°7:
    
#Realizar un programita que pida un numero, controlando que haya ingresado un numero entre 1 y 10, determinar si es menor a 5 o mayor o igual a 5.

n=int(input("ingrese un numero entre 1 y 10 n:"))

if n>=1 and n<=10:
    print("entra en el rango")
    if n<5 and n>=1:
        print("es menor a cinco")
    elif n>=5 and n<10:
        print("es mayor o igual a cinco")      
else:
    n<=1 and n>=10
    print("no entra en el rango ")
    
#EJERCICIO N°8:
    
#Realizar un programita que pida un numero y devuelva +1 si este es positivo y -1 si este es negativo.

n=int(input("ingrese un numero n:"))
a=-1
b=1
if n<0:
    print("el numero es negativo:",a)
elif n>0:
    print("el numero es positivo:",b)
else:
    n=0
    print("ingrese otro numero ERROR")

#EJERCICIO N°9:
    
#Realizar un programita que pida un numero y devuelva +1 si este es positivo y 0 si este es negativo.

n=int(input("ingrese un numero por favor n:"))
a=0
b=+1
if n<0:
    print("el numero es negativo:",a)
elif n>0:
    print("el numero es positivo:",b)
else:
    n=0
    print("ingrese otro numero ERROR")
    
#EJERCICIO N°10:
    
#Realizar un programita que pida dos numeros enteros y devuelva 1 si ambos numeros son iguales, y 0 sino.
n1=float(input("ingrese un numero entero n1:"))
n2=float(input("ingrese un numero entero n2:"))
a=1
b=0
if n1%1==0 and n2%1==0:
    print("los numero ingresado son entero")
    if n1==n2:
        print("los nuemeros ingresado son iguales N:",a)
    elif n1!=n2:
        print("los numero ingresado son distintos N:",b)
else:
    n1%1 !=0 and n2%1 !=0
    print(" ERROR los numeros ingresados no son enteros")
    
#EJERCICIO N°11:
    
#Realizar un programita que pida dos numeros enteros y devuelva true si ambos numeros son iguales, y false sino.

n1=float(input("ingrese un numero entero n1:"))
n2=float(input("ingrese un numero entero n2:"))

if n1%1==0 and n2%1==0:
    print(n1==n2)
    
else:
    n1%1 !=0 and n2%1 !=0
    print(" ERROR los numeros ingresados no son enteros")
    
    #EJERCICIO N°12:
        
#Realizar un programita que pida dos palabras al usuario y determine si son iguales o no, devolviendo true (verdadero) si lo son."""

n3=str(input("ingrese una palabra:"))
n4=str(input("ingrese otra palabra:"))

print(n3==n4)

#EJERCICIO N°13:
    
#Realizar un programita que pida dos palabras al usuario y muestre la palabra que resulta de concatenar (sumar) ambas.
n5=str(input("ingrese una palabra:"))
n6=str(input("ingrese otra palabra:"))

print(str(n5)+" "+str(n6))

#EJERCICIO N°14:
    
#Realizar un programita que pida una contraseña al usuario y determine si es la contraseña correcta, dando un mensaje de error cuando no lo sea."""

n7=str(input("ingrese su contraseña:"))

validar=False #que se vayan cumpliendo los requisitos uno a uno.
long=len(n7) #Calcula la longitud de la contraseña
espacio=False  #variable para identificar espacios
mayuscula=False #variable para identificar letras mayúsculas
minuscula=False #variable para contar identificar letras minúsculas
numeros=False #variable para identificar números
y=n7.isalnum()#si es alfanumérica retona True
correcto=True #verifica que hayan mayuscula, minuscula, numeros y no alfanuméricos
        
for carac in n7: #ciclo for que recorre caracter por caracter en la contraseña

    if carac.isspace()==True: #Saber si el caracter es un espacio
        espacio=True #si encuentra un espacio se cambia el valor user

    if carac.isupper()== True: #saber si hay mayuscula
        mayuscula=True #acumulador o contador de mayusculas
                
    if carac.islower()== True: #saber si hay minúsculas
        minuscula=True #acumulador o contador de minúsculas
                
    if carac.isdigit()== True: #saber si hay números
        numeros=True #acumulador o contador de numeros
                            
if espacio==True: #hay espacios en blanco
    print("La contraseña no puede contener espacios")
else:
    validar=True #se cumple el primer requisito que no hayan espacios
                       
if long <8 and validar==True:
    print("Mínimo 8 caracteres")
    validar=False #cambia a Flase si no se cumple el requisito minimo de caracteres

if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
    validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
else:
    correcto=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
           
if validar == True and correcto==False:
    print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")
        

if validar == True and correcto == True:

    correcto=True
    

while correcto==True:
    n8=input("repita su contraseña: ")
    if n7 == n8:
        print("Contraseña creada exitosamente")
        break
    else:
        n7!=n8
        print("error de validacion vuelva a intentarlo")
   
    #EJERCICIO N°15:
        
#Realizar un programita que pida 3 numeros enteros al usuario, y determine el orden creciente de los mismos, es decir, los muestre en pantalla de menor a mayor.

a=int(input("ingrese un numero entero a:"))
b=int(input("ingrese otro numero entero b:"))
c=int(input("ingrese otro numero entero c:"))

if (a>=c) and (a>=b):
    maximo=a
if(a<=c) and (a<=b):
    minimo=a
else:
    medio=a
if (b>=c) and (b>=a):
    maximo=b
if(b<=c) and (b<=a):
    minimo=b
else:
    medio=b
if (c>=a) and (c>=b):
    maximo=c
if(c<=a) and (c<=b):
    minimo=c
else:
    medio=c
    
print(minimo)
print(medio)
print(maximo)

#otra manera de hacelo
num = []  # Contendrá los numeros

print("Ingresa 3 Numeros")
for x in range(3):
    ingresado = input("Ingrese:")  # Capturamos lo ingresado por teclado
    num.append(ingresado)  # Agregamos al arreglo lo ingresado

num.sort() #Ordenamos el arreglo
mayor = num[2]
medio = num[1]
menor = num[0]
print("menor:",menor)
print("medio:",medio)
print("Mayor:", mayor)

#EJERCICIO N°16:
    
#Realizar un programita que pida 2 datos: el valor del dolar actual, y la cantidad de pesos que posee el usuario, y determine cuantos dolares tendrıa el usuario entonces.
n8=float(input("ingrese el valor actual de 1 dolar:"))
n9=float(input("ingrese la cantidad de pesos que posee:"))
cambio= n9/n8
print("dolares que tendria:",cambio)

#EJERCICIO N°17:
    
#Realizar un programita Convertir a Pesos: que pida 2 datos, el valor del dolar actual, y el precio en dolares de un producto. Calcular y mostrar en pantalla cuanto cuesta en pesos ese producto.

n1=float(input("ingrese el valor actual de un dolar:"))
n2=float(input("ingrese el precio del producto en dolares:"))

cambio=n1*n2

print("el precio del producto en pesos argentino es:",cambio)

#EJERCICIO N°18:
    
#Realizar un programita que pida una nota de un alumno, y devuelva Aprobado si la nota esta entre 6 y 8. Desaprobado, si la nota es menor que 6, y Promocionado si la nota es mayor o igual a 9. (*ademas se debera controlar que la nota ingresada es una nota valida entre 1 y 10 previo a clasificarla)

n2=float(input("igrese una su nota:"))
n3=round(n2) #redondeamos al extremo mas cercano.
#CONDICIONES

if n3>=1 and n3<=10:
    if n3>=6 and n3<8:
        print("aprobado con:",n3)
    elif n3>=8 and n3<=10:
        print("promocionado con:",n3)
    else:
        print("desaprobado con:",n3)
else:
    print("nota invalida")
    
#EJERCICIO N°19:
    
#Determinar si el siguiente codigo tiene algun tipo de error, ya sea de sintaxis o de logica. Sugerir correccion si ası fuese"""       
 #codigo incorrecto
 #a = input("Ingrese un numero:")
 #b = input(’Ingrese otro numero:")
#if (b − a = 0):
#print(’a y b son distintos’)

a =input("Ingrese un numero:")
b =input("Ingrese otro numero:")
c=input("Ingrese otro numero:")
if a+b==c:
   print("a y b son distintos")
   
 #EJERCICIO N°20:
     
#¿Que imprimira en pantalla el siguiente codigo?   
n = 5
m = 1
o = 8
if ((n != m) and (o > m)) or (m == 1):
    if (n + m == o):
        print("m y n son iguales")
    
    else:
        print("listo")
    print("tal vez")
    
    #EJERCICIO N°21:
        
#Escribir un programita que pida el dıa de nacimiento (no la fecha, solo el dıa, controlando que este entre 1 y 31) y el mes de nacimiento (como texto, enero, febrero, etc) al usuario. Determinar el signo astrologico del usuario

dia=int(input("intrudusca el dia de su nacimiento: "))
mes=int(input("introdusca el mes de su nacimiento en numero: "))
enero=1
febrero=2
marzo=3
abril=4
mayo=5
junio=6
julio=7
agosto=8
septiembre=9
octubre=10
noviembre=11
diciembre=12
  
if dia>=1 and dia<=31:
    if((mes==1) and (dia>=20)) or ((mes==2) and (dia<=18)):
        print(("su signo es Acuario"))
    if ((mes==2) and (dia>=19)) or ((mes==3) and (dia<=20)):
        print("su signo es Piscis")
    if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=19)):
        print("su signo es Aries")
    if ((mes==4) and (dia>=20)) or ((mes==5) and (dia<=20)):
        print("su signo es Tauro")
    if ((mes==5) and (dia>=21)) or ((mes==6) and (dia<=20)):
        print("su signo es Geminis")
    if ((mes==6) and (dia>=21)) or ((mes==7) and (dia<=22)):
        print("su signo es Cancer")
    if ((mes==7) and (dia>=23)) or ((mes==8) and (dia<=22)):
        print("su signo es Leo")
    if ((mes==8) and (dia>=23)) or ((mes==9) and (dia<=22)):
        print("su signo es Virgo")
    if ((mes==9) and (dia>=23)) or ((mes==10) and (dia<=22)):
        print("su signo es Libra")
    if ((mes==10) and (dia>=23)) or ((mes==11) and (dia<=21)):
        print("su signo es Escorpio")
    if ((mes==11) and (dia>=22)) or ((mes==12) and (dia<=21)):
        print("su signo es Sagitario")
    if ((mes==12) and (dia>=22)) or ((mes==1) and (dia<=19)):
        print("su signo es Capricornio")
else:
    print("fecha invalida vuelva a intentarlo")
   
    #EJERCICIO N°22:
        
#Realizar un programita que pida 4 numeros y los muestre ordenados en pantalla en orden decreciente.2"""

num = []  # Contendrá los numeros

print("Ingresa 4 Numeros")
for x in range(4):
    ingresado = input("Ingrese:")  # Capturamos lo ingresado por teclado
    num.append(ingresado)  # Agregamos al arreglo lo ingresado

num.sort() #Ordenamos el arreglo
m1= num[3]
m2 = num[2]
m3 = num[1]
m4 = num[0]
print(m1)
print(m2)
print(m3)
print(m4)


# codigo con if y else:
    
a=int(input("ingreasa un numero entero:"))
b=int(input("ingreasa un numero entero:"))
c=int(input("ingreasa un numero entero:"))
d=int(input("ingreasa un numero entero:"))

#encuentra el mayor de los 4 numeros.

if(a>=b) and (a>=c) and (a>=d):
    maximo = a
    if (b >=c) and (b>=d):
        mayor = b
    else:
        if (c>=d):
            mayor = c
        else:
            mayor = d
    if (b <=c) and (b<=d):
        menor = b
    else:
        if (c<=d):
            menor = c
        else:
            menor = d
    medio=(b+c+d)-menor-mayor
else:
    if (b>=c) and (b>=d):
         maximo = b
         if (a >=c) and (a>=d):
             mayor = a
         else:
            if (c>=d):
                mayor = c
            else:
                mayor = d
         if (a <=c) and (a<=d):
            menor = a
         else:
            if (c>=d):
                menor = c
            else:
                menor = d
         medio=(a+c+d)-menor-mayor
    else:
       if (c>=d):
            maximo=c
            if (a >=b) and (a>=d):
                mayor = a
            else:
                 if (b>=d):
                     mayor = b
                 else:
                     mayor = d
            if (a <=b) and (a<=d):
                 menor = a
            else:
                if (b<=d):
                    menor = b
                else:    
                    menor = d
            medio=(a+b+d)-menor- mayor
       else:
            maximo=d
            if (a >=b) and (a>=c):
                mayor = a
            else:
                 if (b>=c):
                     mayor = b
                 else:
                     mayor = c
            if (a <=b) and (a<=c):
                 menor = a
            else:
                if (b<=c):
                    menor = b
                else:    
                    menor = c
            medio=(a+b+c)-menor- mayor
print(maximo)
print(mayor)
print(medio)
print(menor)

    #EJERCICIO N°23:
    
#Realizar un programita que permita determinar si un triangulo es equilatero, isosceleso escaleno. Al usuario le debera pedir 3 numeros. Nota: Equilatero es cuando sus tres lados son iguales. Escaleno cuando sus tres lados son distintos entre si. Isosceles cuando al menos dos de sus lados son iguales."""

print("clasificador de triangulos")

l1=float(input("ingrese un lado del triangulo l1:"))
l2=float(input("ingrese otro lado del triangulo l2:"))
l3=float(input("ingrese otro lado del triangulo l3:"))

if (l1==l2) and (l1==l3):   #condicion implicita
    print("su triangulo es Equilatero")
elif (l1!=l2) and (l1!=l3) and (l2!=l3):   #condicion implicita
    print("su triangulo es Escaleno")
else:
    print("su triangulo es isosceles")
    
    #EJERCICIO N°24:
        
#Escribir un programita que permita calcular la edad de un perro equivalente en años humanos. Tip: Los dos primeros años de un perro equivalen a 10.5 años de un humano. Despues cada año del perro equivalen a 4 años de un humano.

print("calcularemos la edad de su mascota")

ap=float(input("ingrese la edad de su perro:"))

if ap>=1 and ap<=2:
    años=ap*10.5
    print("la edad de su perro equivalente a los años del humano es:",años)
elif ap>2 and ap<=12:
    años=ap*4
    print("la edad de su perro equivalente a los años del humano es:",años)
else:
    print("su perro es inmortal")
    
    #EJERCICIO N°25:
        
#Escribir un programita que permita ingresar una letra y determine si es una consonante o una vocal.

n=input("ingrese una letra")


if (n=="a") or (n=="e") or (n=="i") or (n=="o") or (n=="u"):
        print("la letra ingresada es una vocal")
else:
        print("es una consonante")     
