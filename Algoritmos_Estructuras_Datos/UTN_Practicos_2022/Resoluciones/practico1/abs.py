def absoluto():
    try:
        numero=int(input("ingresa un Numero:"))
        return f" obsoluto: {abs(numero)} "
    except ValueError as error:
        return f"caracter incorrecto, ingrese un Numeros Real"