
"""
trabajo practico N° 4 

contruccion de funciones 

@author: federico pfund 
"""
#-ejercicio N°1
#-. Crear una funcion llamada signo que tome un numero como argumento y devuelva 1 si es positivo o cero y -1 si es negativo.
def signo(numero):
    num=int(numero)
    if num>=0:
        return 1
    else: 
        return -1
signo(-1)
#-ejercicio N°2
#-. Crear una funcion llamada en rango que tome 3 numeros: n, a y b y devuelva True si n pertenece al rango [a, b] y False sino.
                
def rango(n1,a,b):

    numero_1 = int(a)
    numero_2 = int(b)
    n=int(n1)
 
    if (n in list(range(numero_1 , numero_2 +1))) or (n in list(range(numero_2 , numero_1 +1))):
        return True
    elif(n not in list(range(numero_1 , numero_2 +1))) or (n not in list(range(numero_2 , numero_1 +1))):
        return False
        
#- ejercicio N°3

#-Crear una funcion llamada farenheit to celcius que tome una temperatura en Farenheit como argumento y devuelva como resultado la temperatura convertida a grados Celsius.Redondear a 2 decimales
def faranheit_to_celcius(tf):
 
    tc = (5/9)*(tf-32)
    return tc

#-ejercicio N°4 

#-Crear una funcion llamada suma que tome dos numeros a y b. Y devuelva la suma al cuadrado, es decir (a + b)°2
def suma(a,b):
    c=(a+b)**2
    return c
#-ejercicio N°5
#- Crear una funcion llamada cuenta palabras que tome una frase y devuelva la cantidad de palabras que tiene.
def cuenta_palabras(frase1):
    frase=str(frase1) 
    
    lista=frase.split()
    cantidad=0
    
    for i in lista:
        cantidad=cantidad + 1 
    return cantidad

cuenta_palabras("dnasld asdasd asdas")

#-ejercicio N°6
#-Crear una funcion llamada promedio que tome una lista y devuelva el promedio de sus valores.
def promedio(*lista):#modificado *para ingresar cantidad de parametros indefinidos
        
    tamaño=len(lista)
 
    p= sum(lista)/tamaño
    
    return p

promedio([2,1,2,1,1])

#def promedio(lista):# codigo viejo 
   # print("seleccione el tamaño  de su lista:")
    #tamaño=int(input("numero:"))
    #lista=[]
    #p= sum(lista)/tamaño
   # for i in range(tamaño):
        #numero=int(input("ingrese el valor deceado para su lista: "))
        #lista.append(numero)
      #  print(lista)
    #return p
    
#-ejercicio N°7

#-Crear una funcion llamada replace with que tome una frase y un caracter y devuelva la frase donde cambio los espacios por dicho caracter.
def replace_with(frase,caracter):
    nueva=frase.replace(" ",caracter)
    return nueva

replace_with("hola ","o")


#def replace_with():
  #  frase=input("ingrese una frase: ")
    #caracter=input("ingrese un caracter: ")
    #nueva=frase.replace(" ",caracter)
    #print(nueva)
    
#-ejercicio N°8

#-8. Crear una funcion llamada sin repetidos que tome una lista y que devuelva la lista sin elementos repetidos.

def sin_repetidos():
    tamaño=int(input("numero:"))
    lista=[]
    for i in range(tamaño):
        elemento=input("ingrese el elemento deceado para su lista: ")
        if elemento in lista:
            lista.remove(elemento)  
        lista.append(elemento)    
    return lista
    

#-ejercicio N°9

#- . Escribir una funcion llamada letras pares que tome una frase y devuelva un texto nuevo donde se han tomado solo los caracteres en las posiciones pares de la misma. Ejemplo: para ’patio’ se devolverıa la nueva palabra ’ai’  
def letras_pares(frase):
    frases=" "
    for i in range(0,len(frase),2):
        frases= frases + frase[i]
    return frases
frase="hola mundo"
letras_pares(frase)
#-ejercicio N°10
#-. Realizar una funcion llamada max_pal que tome una frase, y determine la longitud de la mayor palabra. (mostrar la longitud, no la palabra)
def max_pal(frase):
    suma = 0
    suma1 = 0
    #en el bloque siguiente nos guardara en la variable suma1 me guarde la loguitud de la palabra mas larga.
    for i in frase: 
        if i==" " and suma>suma1:#cuando encuentre un espacio analiza si suma es suma>suma1 en caso de True guardala en la variable suma la loguitud mayor. 
            suma1=suma
            suma=0
        elif i == " " :
            suma=0
        else:
            suma=suma + 1
    return suma1
max_pal("rcuerdo de constatinopla mundual ")
#-ejercicio N°11
#-Crear una funcion llamada algo en comun que tome dos listas y determine si tienen algun elemento en comun, devolviendo True en ese caso, y False sino.
def algo_en_comun(lista,lista1):

    for i in lista:
        if i in lista1:
            return True
            break
    return False 

algo_en_comun([1,2,3],[7,8,0])


#-ejercicio N°12
#-Crear una funcion llamada cuenta digitos que tome un n entero como argumento y devuelva la cantidad total de dıgitos que tiene. Por ejemplo, si se le da el numero 86253 dara como resultado 5.
def cuenta_digitos(numero):
    
    cuenta=0
    for i in numero:
        cuenta = cuenta + 1
    return cuenta
cuenta_digitos("3456") 
#otra estructura pero no cumple con lo de str
def cuenta_digitos(b):
    a=str(b)
    cuenta=0
    for i in a:
        cuenta = cuenta + 1
    print("contiene ",cuenta," digitos ")

 
#-ejercicio N°13
#- Crear una funcion llamada swap name que tome un str conteniendo nombre y apellido, y lo devuelva intercambiados. Ejemplo, si se le da ”Bilbo Bols´on” devolver´a ”Bols´on Bilbo” y vice versa.
def swap_name(nombre):
    
    i=0
    pa = " "
    for i in range(-1,1-len(nombre),-1):
        if nombre[i] == " ":
            pa=nombre[i+1:] +" "+ nombre[:i]
    return pa               
swap_name("federico pfund")
#-ejercicio N°14
#-Crear una funcion llamada inversa que tome una frase y la devuelva invertida. Les recuerdo que no se pueden utilizar ni los metodos de los str, salvo len() ni listas para resolverlo.
def inversa(frase):
   
    i=0
    alreves = ""
    j= len(frase)-1
    while(i <= j):
        alreves = alreves + frase[j]
        j=j-1
    return alreves
inversa("hola mundo como esta")

#-ejercicio N°15
#-Crear una funcion llamada cosquin que tome una palabra y la devuelva habiendo repetido cada vocal una vez. Ejemplo hola ⇒ hoolaa.
def cosquin(palabra):
   
    s= "" #las cadenas son inmutables es necesario hacer una copia modificada de la cadena.
    i=0
    for i in palabra:
        s=s + i
        if i =="a" or i=="e"or i=="i" or i=="o" or i=="u":
            s = s + i 
    return s
cosquin("palabras")   

#-ejercicio N°16
#-. Crear una funcion llamada pedacito que tome una frase y dos numeros, inicio y fin, y devuelva la subfrase que inicia en la posicion inicio y termina en la posicion fin de la frase original. No utilizar listas. Y solo usar len() de los metodos de str. Ademas se debe controlar que inicio sea menor o igual que fin, y que inicio sea mayor o igual a 1 y que fin sea menor o igual que la cantidad total de caracteres de la frase. Ejemplo, para una frase ”hola que tal”se tendrıa que pedacito(frase,5,7) darıa ”que”
def pedacito(frase,inicio,fin):
 
  
    if 1 <=inicio <= fin and len(frase)-1>=fin:
        return frase[inicio:fin]
    else:
        print("verifique los parametros que ingreso de inicio y fin ")
pedacito("hola mundo",4,8)
#-ejercicio N°17
#-Crear una funcion llamada iguales que tome dos palabras, y controlando tengan la misma longitud, chequee si son iguales o no, devolviendo True o False segun corresponda.
def iguales(palabra1,palabra2):
       
    if len(palabra1)==len(palabra2):
       for i in range(0,len(palabra1),1):
           if palabra1[i]==palabra2[i]:
               return True
           else:
               return False 
    else:
        print("False las palabras no tienen el mismo tamaño")
        
iguales("fede","fede")
iguales("no","si")
 