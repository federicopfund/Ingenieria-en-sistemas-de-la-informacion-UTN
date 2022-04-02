## python trabaja con datos dinamicamente tipado por lo que no es necesario definir el tipo de varibles ah usar.
##Variables tipos str 
## Practico N°1 
#%% Practico N°1 
##hola="hola mundo"
##print(hola)
##Ejercicio 2
##Varibles tipo enteras.
##numero= 30
##print(numero)
##Ejercicio 3

##ombre=input(str("Ingresa tu Nombre:"))
##print(f"Hola Mucho gusto de Conocerte!!, {nombre}")
## ejercicio 4
##numero1= int(input((f"Ingresa un valor Numerico:")))
##numero2= int(input((f"Ingresa un valor Numerico:")))
##print(f"Segundo Valor: {numero2}.")
##print(f"Primer Valor: {numero1}")
# %%
##Ejercico N°5

##ingrso=int(input(f"Ingresa un Valor:"))
##print(f"Has introducido el Numero: {ingrso}")
#%%
##Ejercicio N°6

from cmath import sqrt


number1= int(input((f"Ingresa un valor Numerico:")))
number2= int(input((f"Ingresa un valor Numerico:")))

print(f"Suma: {number1+number2}")
print(f"Resta: {number1-number2}")
print(f"Multiplicacion: {number1*number2}")

try:
    if type(number1)==int:
        if number2!=0:
            print(f"Divicion es igual ah: {number1/number2}")
        else:
            print(f"NO PUEDE DIVIDIR POR 0")
       
except ValueError:
    print(f"Usted debe ingresar un valor Entero.")
#%%    
##Ejercicio N°7
def Function(a,b):
    print(f"Ingresa el valor de las Constante a Operar")
    
    return 5*a +10*b
print("A):")
print(f"Valor de la operacio a): {Function(3,4)}")
 
def FunctionAlCuadrado(b):
     print("Ejercicio Potencia")
     return b**2
print("b):")
print(f"Valor de la operacio b): {FunctionAlCuadrado(3)}")

def FunctionDenominador(n):
     print("Ejercicio Denominador")
     return (2*n-1)/(2*n+1)
print("d):")
print(f"Valor de la operacio c): {FunctionDenominador(3)}")
def FunctionRaiz(b):
     print("Ejercicio Raiz")
     return sqrt(b)
print("e):")
print(f"Valor de la operacio d): {FunctionRaiz(3)}")
def FunctionMultiVariable(x,y):
     print("Ejercicio Multivariable")
     return 2*x-y
print("e):")
print(f"Valor de la operacio e): {FunctionMultiVariable(3,3)}")
def FunctionMultiVariables(x,y):
     print("Ejercicio Multivariables")
     return (x-y)/(x+y)
print("f):")
print(f"Valor de la operacio f): {FunctionMultiVariables(3,3)}")
#%%

## Ejercicio N°8
try:
    Numer_Real= float(input("Ingrese el primer Valor Real: "))
    Numer_Real_dos= float(input("Ingrese le Segundo Valor Numerico: "))
    if type(Numer_Real_dos)!=0:
        print(f"El Valor de la Operacion{round(Numer_Real/Numer_Real_dos,2)}")
    else:
        print(f"Deve ingresar un Numero distinto de 0")
except:
    print(f"Deves Ingresar un Valor Numerico.")
#%%
##Ejercicio N°9
try:
    numero1= int(input("Ingresa un Numero: "))
    numero2= int(input("Ingresar un Numero:"))

    if numero1 == numero2 :
        print("Numero iguales")
    else:
        print("Numeros Desiguales")
except ValueError as err:
    print("ingrese un caracter correcto")
#%%
##Ejercisio N°10
try:
    numero1= int(input("Ingresa un Numero: "))
    numero2= int(input("Ingresar un Numero:"))

    if numero1 > numero2 :
        print(f"Numero iguales")
    else:
        print("Numeros Desiguales")
except ValueError as err:
    print("ingrese un caracter correcto")
    
##Ejercico N°11
