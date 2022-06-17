## Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas.
import random


def aleatoridad():
    lista = [] 
    global promedio1
    for i in range(20):
        numero = random.randint(1,6)
        lista.append(numero)

    print(lista)
    promedio1 = sum(lista)/len(lista)
    print(f"El promedio es: {round(promedio1,2)}")

    ## Tirar ahora, 2500 veces un dado de 6 caras. Mostrar el promedio de esas tiradas. Comparar
    ## con el promedio del ejercicio anterior. ¿Nota una diferencia sustancial habiendo cambiado
    ## la cantidad de tiradas?
 



def veces2500():
        lista = []
        for i in range(2500):
            numero = random.randint(1,6)
            lista.append(numero)
        print(lista)
        promedio2 = sum(lista)/len(lista)
        print(f"El promedio es: {round(promedio2,2)}")
        print(f"La diferencia es: {round(promedio2-promedio1,2)}")
        print(f"La diferencia es de: {round(promedio1-promedio2,2)}")

## Pedirle al usuario sus 10 marcas favoritas. Mostrar una marca al azar de la lista


def dados():
    lista = []
    for i in range(10):
        marca = input("Ingrese una marca: ")
        lista.append(marca)
    print(lista)
    marca = random.choice(lista)
    print(marca)
    