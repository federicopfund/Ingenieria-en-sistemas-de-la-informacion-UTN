def treanuameros():
    lista=[]   
    a=int(input("ingrese un numero entero a:"))
    lista.append(a)
    b=int(input("ingrese otro numero entero b:"))
    lista.append(b)
    c=int(input("ingrese otro numero entero c:"))
    lista.append(c)
    lista.sort()
    
    print("Numero Maximo: ",lista[-1])
    print("Numero Medio: ",lista[-2])
    print("Numero Minimo: ",lista[-3])