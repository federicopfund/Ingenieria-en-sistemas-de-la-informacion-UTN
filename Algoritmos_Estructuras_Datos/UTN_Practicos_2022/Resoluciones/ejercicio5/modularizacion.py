


def cuadrado(lado):
    """Crear una función que reciba un número como parámetro el cual representa el lado de
        un cuadrado y muestre en pantalla el perímetro y la superficie del mismo"""
    try:
        if type(lado) == int:
            perimetro = lado * 4
            superficie = lado * lado
            print(f"El perimetro del cuadrado es: {perimetro}")
            print(f"La superficie del cuadrado es: {superficie}")
        else:
            print("El valor ingresado no es un numero.")
    except TypeError:
        print(f"Error, ingresa un tipo de dato tipo Int.")


def escribir_tabla_multiplicar(numero):
    """Crear una función llamada escribir_tabla_ multiplicar, que reciba como parámetro un
         número entero, y escriba la tabla de multiplicar de ese número (por ejemplo, para el 3
         deberá mostrar desde 3x0=0 hasta 3x10=30)."""
    try:
        if type(numero) == int:
            for i in range(0, 11):
                resultado = numero * i
                print(f"{numero} x {i} = {resultado}")
        else:
            print("El valor ingresado no es un numero.")
    except TypeError:
        print("Ingresa un numero tipo int")



def cuadrante(x,y):
    """
     Escriba una función denominada cuadrante(x,y), dónde x e y son valores enteros
        recibidos como parámetros los cuales representan un punto, y que retorne un valor
        entre 1, 2, 3 o 4 de acuerdo al cuadrante que se encuentre el punto (x,y), ingresado
        como parámetro, en los ejes cartesianos.
    """
    try:
        if type(x) == int and type(y) == int:
            if x > 0 and y > 0:
                print("Primer Cuadrante.")
                return 1
            elif x < 0 and y > 0:
                print("Segundo Cuadrante.")
                return 2
            elif x < 0 and y < 0:
                print("Tercer Cuadrante.")
                return 3
            else:
                print("Cuarto Cuadrante.")
                return 4
        else:
            print("El valor ingresado no es un numero.")
    except TypeError:
        print("Ingresa un numero tipo int")



def potencia(base,exponente):
    """ Escriba una función que calcule la enésima potencia de un número, recibiendo
            como parámetro un número real base y otro entero llamado exponente.
            La definición de la función es: 
             y = xn
            donde x representa la base y n representa el exponente.
        Nota: tener en cuenta que n puede ser un número negativo.
        Ejemplo: 2^3 = 8 
        Ejemplo: 2^-3 = 1/8
    """
    try:
        if type(base) == float and type(exponente) == int:
            if exponente < 0:
                exponente = exponente * -1
                resultado = base ** exponente
                print(f"{base}^{exponente} = {resultado}")
            else:
                resultado = base ** exponente
                print(f"{base}^{exponente} = {resultado}")
        else:
            print(f"El valor ingresado no es un numero.")
    except TypeError:
        print(f"Ingresa un numero tipo float para la base y un numero tipo int para el exponente.")



def cadena_letra(cadena,letra):
    """Crear una función que reciba una cadena de caracteres y una letra como
        parámetros, y devuelva la cantidad de veces que dicha letra aparece en la
        cadena.Por ejemplo, si la cadena es "Barcelona" y la letra es 'a', debería devolver 2(aparece 2 veces).
    """
    try:
        if type(cadena) == str and type(letra) == str:
            contador = 0
            for i in cadena:
                if i == letra:
                    contador += 1
            print(f"La letra {letra} aparece {contador} veces en la cadena {cadena}")
        else:
            print("El valor ingresado no es una cadena de caracteres.")
    except TypeError:
        print("Ingresa una cadena de caracteres y una letra.")


def cadena_letra_10(caracter, lista):
    """ Con la función creada en el ejercicio anterior, elabore un programa en donde se ingresa un carácter y 10 palabras;
            y muestre la cantidad total de veces que apareció el carácter en las 10 palabras.
    """
   
    try:
        if type(caracter) == str and len(caracter) == 1:
            contador = 0
            for i in lista:
                if i == caracter:
                    contador += 1
            print(f"el caracter {caracter} aparece {contador} veces en la cadena {lista}")
        else:
            print(f"El valor ingresado no es un caracter o el has ingresado 2 caracter.")
    except TypeError:
        print(f"Ingresa un caracteres y una lista.")


def funcion_logica(numero):
    """ Crear una función lógica (función que retorna un valor lógico) que determine si es un  número entero  par o impar."""
    try:
        if numero % 2 == 0:
            print("El numero es par.")
            return True
        else:
            print("El numero es impar.")
            return False
    except TypeError:
        print("El valor ingresado no es un numero.")

"""
    Crear una función que reciba un carácter y un número como parámetros e
    imprima en pantalla un triángulo inverso formado por ese carácter que tenga como
    ancho inicial el número recibido como parámetro. Por ejemplo, si el carácter es * y
    el ancho es 4, debería escribir:

     ejemplo :  ****
                ***
                **
                *
"""
def trianguloinverso(caracter, base):
   
    try:
        if type(caracter) == str and type(base) == int:
            for i in range(base):
                for j in range(base-i):
                    print(" ",end="")
                for k in range(i+1):
                    print(caracter,end="")
                print("")
        else:
            print("El valor ingresado no es un caracter o el has ingresado un numero.")
    except TypeError:
        print("verifica el tipo de dato que has ingresado")
    


def es_primo(numero):
    """
    Crear una función es_ primo, que reciba un número entero como parámetro y
    devuelva verdadero si es un número primo o falso en caso contrario.
    """
    try:
        if type(numero) == int:
            if numero > 1:
                for i in range(2,numero):
                    if numero % i == 0:
                        print(f"{numero} no es primo.")
                        return False
                print(f"{numero} es primo.")
                return True
            else:
                print(f"{numero} no es primo.")
                return False
        else:
            print("El valor ingresado no es un numero.")
    except TypeError:
        print("Ingresa un numero tipo int.")



def dados(a,b):
    """ Crear una función que dados dos valores distintos, ingresados por parámetro,
         devuelva el mayor de ellos."""
    try:
        if type(a) == int and type(b) == int:
            if a > b:
                print(f"El mayor es {a}")
            elif a < b:
                print(f"El mayor es {b}")
            else:
                print(f"Los numeros son iguales.")
        else:
            print("El valor ingresado no es un numero.")
    except TypeError:
        print("Ingresa un numero tipo int.")



def promedio(a,b,c,d,e,f):
    """ Desarrollar una función que dados cinco números, recibidos por parámetro, devuelva el
         promedio de ellos. Se puede generalizar para n parámetros devolviendo el promedio
         de los mismos."""
    try:
        if type(a,b,c,d,f) == int:
            suma = a + b + c + d + e + f
            promedio = suma / 6
            print(f"El promedio es {promedio}")
        else:
            print("El valor ingresado no es un numero.")
    except TypeError:
        print("Ingresa un numero tipo int.")



def ceros_unos(numero):
    """ Dado un número entero formado sólo por los dígitos 0 (cero) y 1 (uno), diseñe una
        función que compruebe si el número tiene o no la misma cantidad de ceros que de unos."""
    try:
        if type(numero) == int:
            if numero > 0:
                contador_ceros = 0
                contador_unos = 0
                for i in str(numero):
                    if i == "0":
                        contador_ceros += 1
                    elif i == "1":
                        contador_unos += 1
                if contador_ceros == contador_unos:
                    print(f"El numero {numero} tiene la misma cantidad de ceros y unos.")
                else:
                    print(f"El numero {numero} no tiene la misma cantidad de ceros y unos.")
            else:
                print("El numero ingresado no es positivo.")
        else:
            print("El valor ingresado no es un numero.")
    except TypeError:
        print("Ingresa un numero tipo int.")



def caracterposicion(cadena,caracter):
    """Desarrollar una función que retorne la posición de un carácter la primera vez que
         aparezca dentro de la cadena de N caracteres de longitud, donde se reciben como
         parámetro la cadena y el carácter respectivamente."""
    try:
        if type(cadena,caracter) == str:
            contador = 0
            for i in cadena:
                if i == caracter:
                    print(f"El caracter {caracter} aparece en la posicion {contador+1}")
                    return contador+1
                contador += 1
            print(f"El caracter {caracter} no aparece en la cadena {cadena}")
        else:
            print(f"El valor ingresado no es un caracter o el has ingresado una cadena.")
    except TypeError:
        print(f"Ingresa un caracter y una cadena.")



def paga(monto,forma):
    """
        Diseñar un algoritmo que permita aplicar un descuento del 10% al monto total de una
        compra si la forma de pago empleada es mediante débito, 13% si la compra la realiza
        mediante pago contado-efectivo o aumente en un 4% (es un solo pago), si se realiza
        en pago con tarjeta. El usuario deberá ingresar el monto de la compra realizada y la
        forma de pago utilizada. Si es débito o efectivo, deberá aplicar el descuento, sino
        realizar el recargo correspondiente."""
    try:
        if type(monto) == int and type(forma) == str:
            if forma == "debito":
                descuento = monto * 0.10
                total = monto - descuento
                print(f"El monto total es {total}")
            elif forma == "contado efectivo":
                descuento = monto * 0.13
                total = monto - descuento
                print(f"El monto total es {total}")
            
            else:
                print("paga en efectivo")
                descuento = monto * 0.04
                total = monto - descuento
                print(f"El monto total es {total}")
        else:
            print("tipo de dato incorrecto")
    except TypeError:
        print(f"Ingresa un numero y una cadena para la forma de pago.")
        print(" ")
        print(f" ---------------------------------------------------")
        print(f"|                 Opciones:                         |")
        print(f" ---------------------------------------------------")
        print(f"|                   # debito.                       |")
        print(f"|                   # contado efectivo.             |")
        print(f"|                   # paga en efectivo.             |")
        print(f" ---------------------------------------------------")
        print(" ")
        print("Tipea la opcion correcta:")
        monto = int(input("ingrese el monto: "))
        forma = input("ingrese la forma de pago: ")
        paga(monto,forma)



def paga_tarjeta(monto,tipo_de_targeta):
    """ Realizar modificaciones para del ejercicio anterior para que permita variantes en las
        tarjetas de crédito ingresadas. Visa, Master, American Express con recargos en 5%, 
        7% ó 9% respectivamente sobre el valor de la compra."""
    try:
        if type(monto) == int and type(tipo_de_targeta) == str:
            if tipo_de_targeta == "visa":
                descuento = monto * 0.05
                total = monto - descuento
                print(f"El monto total es {total} pago con {tipo_de_targeta}")
            elif tipo_de_targeta == "master":
                descuento = monto * 0.07
                total = monto - descuento
                print(f"El monto total es {total} pago con {tipo_de_targeta}")
            elif tipo_de_targeta == "american express":
                descuento = monto * 0.09
                total = monto - descuento
                print(f"El monto total es {total} pago con {tipo_de_targeta}")
            else:
                print("tipo de tarjeta incorrecta")
        else:
            print("tipo de dato incorrecto")
    except TypeError:
        print(f"Ingresa un numero y una cadena para la forma de pago.")
        print(" ")
        print(f" ---------------------------------------------------")
        print(f"|                 Opciones:                         |")
        print(f" ---------------------------------------------------")
        print(f"|                   # visa.                        |")
        print(f"|                   # master.                       |")
        print(f"|                   # american express.             |")
        print(f" ---------------------------------------------------")
        print(" ")
        print("Tipea la opcion correcta:")
        monto = int(input("ingrese el monto: "))
        tipo_de_targeta = input("ingrese la forma de pago: ")
        paga_tarjeta(monto,tipo_de_targeta)


def personal_venta(monto,tipo_targeta,cuotas):
    """ Diseñar un algoritmo que ayude al personal de ventas a realizar el cálculo de los
    intereses sobre un producto, cuando un cliente intenta pagar en cuotas con alguna
    tarjeta que acepte el comercio.
    Las tarjetas aceptadas son 3 y con estas se pueden abonar en 3, 6 y 12 cuotas.
    Se aclaran los recargos para cada una de las opciones.
    Para la primer tarjeta 3 pagos con 4% mensual, 6 pagos 4,5% mensual y 12 pagos 5% mensual.
    Para la segunda tarjeta 3 pagos con 3% mensual, 6 pagos 4% mensual y 12 pagos 5% mensual.
    Para la tercer tarjeta 3 pagos con 3,8% mensual, 6 pagos 5% mensual y 12 pagos 5,3% mensual.
    Para el caso seleccionado, deberá mostrar la tasa de financiación mensual, 
    la tasa anual (tasa mensual x 12) y el valor del producto aplicado los intereses correspondientes.
    """
    try:
       
        if type(tipo_targeta) == str and type(cuotas) == int:
            if tipo_targeta == "visa":
                if cuotas == 3:
                    descuento = monto * 0.04
                    total = monto - descuento
                    print(f"El monto total es {total} pago con {tipo_targeta}")
                elif cuotas == 6:
                    descuento = monto * 0.045
                    total = monto - descuento
                    print(f"El monto total es {total} pago con {tipo_targeta}")
                elif cuotas == 12:
                    descuento = monto * 0.05
                    total = monto - descuento
                    print(f"El monto total es {total} pago con {tipo_targeta}")
                else:
                    print("coutas incorrectas")
            elif tipo_targeta == "master":
                if cuotas == 3:
                    descuento = monto * 0.03
                    total = monto - descuento
                    print(f"El monto total es {total} pago con {tipo_targeta}")
                elif cuotas == 6:
                    descuento = monto * 0.04
                    total = monto - descuento
                    print(f"El monto total es {total} pago con {tipo_targeta}")
                elif cuotas == 12:
                    descuento = monto * 0.05
                    total = monto - descuento
                    print(f"El monto total es {total} pago con {tipo_targeta}")
                else:
                    print("coutas incorrectas")
            elif tipo_targeta == "american express":
                if cuotas == 3:
                    descuento = monto * 0.038
                    total = monto - descuento
                    print(f"El monto total es {total} pago con {tipo_targeta}")
                elif cuotas == 6:
                    descuento = monto * 0.05
                    total = monto - descuento
                    print(f"El monto total es {total} pago con {tipo_targeta}")
                elif cuotas == 12:
                    descuento = monto * 0.053
                    total = monto - descuento
                    print(f"El monto total es {total} pago con {tipo_targeta}")
    except TypeError:
        
        print(f"Ingresa un numero para el monto a pagar y una cadena para la forma de pago y sus correspondientes cuotas que desea pagar.")
        print(" ")
        print(f" ---------------------------------------------------")
        print(f"|                 Opciones:            Cuotas:      |")
        print(f" ---------------------------------------------------")
        print(f"|                   # Visa.                         |")
        print(f"|                   # Master.                       |")
        print(f"|                   # American Express.             |")
        print(f" ---------------------------------------------------")
        print(" ")
        print("Tipea la opcion correcta:")
        monto = int(input("ingrese el monto: "))
        tipo_targeta = input("ingrese la forma de pago: ")
        cuotas = int(input("ingrese las cuotas: "))
        personal_venta(monto,tipo_targeta,cuotas)

def main():
    cuadrado(4)
    escribir_tabla_multiplicar(4)
    escribir_tabla_multiplicar(4)
    cuadrante(4,2)
    potencia(2,3)
    cadena_letra("adena","a")
    cadena_letra_10("caracter", [1,2,2])
    funcion_logica(3)
    trianguloinverso("er", 3)
    es_primo(3)
    promedio(3,2,2,3,2,1)
    caracterposicion("cadena","a")
    ceros_unos(2)
    paga(1200,"devito")
    paga_tarjeta(1200,"master")
    personal_venta(1233,"master",3)

if "__main__" == __name__:
    main()