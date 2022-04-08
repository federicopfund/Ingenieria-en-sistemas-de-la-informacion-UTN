def simbolos(frase):
    contador=0
    for i in frase:
        if i == " ":
            contador +=1
    print(f"Cantida de Caracteres de la frase: {len(frase)}, Cantidad de espacios: {contador} ")