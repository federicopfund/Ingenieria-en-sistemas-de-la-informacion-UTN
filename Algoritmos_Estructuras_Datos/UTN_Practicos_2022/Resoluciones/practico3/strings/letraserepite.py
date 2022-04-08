def letrasrepetidas(frase,letra):
    contador=0
    for i in frase:
        if i ==letra:
            contador+=1
            
    print(f"la cantidad de veces que se repite: {letra}, es: {contador}.")