def rellena(lista):
    lista=[]
    cantidad= int(input("ingresa la cantidad de numeros que tiene tu lista:"))
    for i in range(cantidad):
        ingresa= int(input("ingresa un numero:"))
        lista.append(ingresa)
    return lista