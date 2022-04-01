def rellena():
    lista=[]
    cantidad= input("ingresa la cantidad de numeros que tiene tu lista:")
    for i in range(int(cantidad)):
        ingresa= int(input("ingresa un numero:"))
        lista.append(ingresa)
    return lista


