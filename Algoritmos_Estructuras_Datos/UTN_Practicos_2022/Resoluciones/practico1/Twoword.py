def twoword():
    lista=[]
    for i in range(2):
        palabra=input("ingresa una palabra:")
        lista.append(palabra)
    
    if len(lista[0]) <= len(lista[1]):
       print( f"la palabra mas larga es{lista[1]} por {len(lista[1])-len(lista[0])} caracteres de diferencias.")
    else:
        print(f"la palabra mas grande es {lista[0]}, por {len(lista[0])-len(lista[1])}, caracteres de diferencias.")
