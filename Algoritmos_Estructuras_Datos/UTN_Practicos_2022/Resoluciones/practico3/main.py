
## Mentor: Lic. Carina Povarchik
## Ing. Fabian Talio
## Ing. Carolina Zapata
## Prof. Lucas Candia


from variados.variados import serie,cuentaregresiva, sumapositivosnegativos,nuemerosenteros,SupremeMachineComputing,ingresa,inverso, pucha, piramide
from pseudoAleatoridad.Aleatoridad import aleatoridad, veces2500,dados
from listas.listas import pedirnombre,nombre,frases, palabra,nombreapellido,promedioredondeo,cantidadpalabrasconlista,cantidaddepalabrassinlista,digitos
from strings.string import iniciales,pocisionpar,letrasrepetidas,simbolos,remplazo,remplazaarchivo,traducciondedigitoacaracter,mostrarfrase


def main():
    Nombre = input("ingrese su nombre: ")
    Apellido = input("ingrese su apellido: ")
    iniciales(Nombre,Apellido)
    frase = input("ingrese una frase: ")
    pocisionpar(frase)
    frase = input("ingresa una frase: ")
    letra = input("ingresa una letra: ")
    letrasrepetidas(frase,letra)
    frase = input("Ingrese una frase con Simbolos, mayusculas e numeros: ")
    simbolos(frase)
    frase = input("ingrese una frase: ")
    remplazo(frase)
    print("remplaza espacio por - y extencion por ## ")
    remplazaarchivo()
    print("traduccion de digito a caracter")
    traducciondedigitoacaracter()
    print("mostrar frase")
    mostrarfrase()
    print("fin String ")
    print("Comienza Listas")
    pedirnombre()
    print("Empieza con M ?")
    nombre()
    print("frase como elementos de una lista")
    frases()
    print("Lista letras de frases")
    palabra()
    print("Nombre lista")
    nombreapellido()
    print("promedio Redondeo")
    promedioredondeo()
    print("cantidad de palabra con lista: ")
    cantidadpalabrasconlista()
    print("cantidad de palabra sin lista: ")
    cantidaddepalabrassinlista()
    print("cantidad de digitos")
    digitos()
    print("fin Listas")
    print("comienzo Aleatoridad")
    print(" ")
    aleatoridad()
    print("2500 veces aleatorio")
    aleatoridad()
    print("diferencia entre 2500 y aleatorio")
    veces2500()
    print("randon marcas favoritas")
    dados()
    print("fin Aleatoridad")
    print("comienzo Varios")
    serie()
    print("Cuenta regresiva")
    cuentaregresiva()
    print("suma de numeros positivos y negativos")
    sumapositivosnegativos()
    print("letra s para salir, agrega numeros hasta que el usuario quiera")
    nuemerosenteros()
    print("Agarrese al disparar esta funcion")
    SupremeMachineComputing()## ojo con esta Funcion!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print("ingresa numeros")
    ingresa()
    print("invertir numeros")
    inverso()
    print("adivina")
    pucha()
    print("triangulo")
    piramide()
    print("Gracias por su tiempo, y gran dedicacion en su carrera de docencia.")
    print("fin")
main()