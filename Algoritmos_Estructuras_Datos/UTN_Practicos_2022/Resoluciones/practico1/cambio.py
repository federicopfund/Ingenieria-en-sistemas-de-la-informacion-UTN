
def Cambio():
    precio_dolar = float(input("Ingresa el precio del dólar en pesos: "))
    dolares = float(input("Ingresa la cantidad de dólares: "))
    tasa =0.04
    pesos= precio_dolar*dolares
    costo_transaccion = dolares * precio_dolar * tasa
    print(f"Los $${dolares} dólares equivalen a ${pesos} pesos,La trasaccion cuenta ${costo_transaccion} pesos")
  
    

    
    