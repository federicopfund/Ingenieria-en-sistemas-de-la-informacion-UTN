
## Mentor: Lic. Carina Povarchik
## Ing. Fabian Talio
## Ing. Carolina Zapata
## Prof. Lucas Candia
from funciones import elevacuadrado,pedirNumeros,espositivo,iguales,signo,escalon,tes,delta, raiz,tresnumero,cantidadvocales, fahrenheit, muestrafahrenheit,concatenar,concatenar1,letra, capitalizar,ord_insercion, reubicar,cantidadpares,ordenarlista
def main():
    numero = int(input("ingrese un numero: "))
    elevacuadrado(numero)
    pedirNumeros()
    espositivo(numero)
    iguales("hola","hola")
    
    signo(numero)
    escalon( numero )
    tes()
    delta(1,1)
    raiz(9,4,7)
    tresnumero(1,2,3)
    cantidadvocales("hola")
    fahrenheit(32)
    muestrafahrenheit()
    concatenar("hola","mundo")
    concatenar1("hola","mundo",True)
    letra("hola","a")
    capitalizar("hola")
    ord_insercion([1,5,3,1,6,9,4,4])
    reubicar([1,5,3,1,6,9,4,4],3)
    ordenarlista([1,5,3,1,6,9,4,4])
    cantidadpares([1,5,3,1,6,9,4,4])
if __name__ == '__main__':
    main()


