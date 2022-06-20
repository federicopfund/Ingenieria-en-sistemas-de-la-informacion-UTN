## Crear un procedimiento llamado cuadrado que tome un numero como parametro e imprima en pantalla dicho numero al cuadrado. *A fines pedagogicos, no a fines de elegancia
## de codigo, haremos un procedimiento en este caso y no una funcion como corresponderıa.
## a)Imprimir, desde dentro del procedimiento, las variables locales que este posea.¿Que
##   se imprime? * utilizar locals()

## b)Agregar dos o tres variables extras con valores inventados, y volver a mostrar todas
##   las variables locales. ¿Hubo cambio alguno?



def cuadradolocals( numero):
    
    ## ingresar datos, captar exepciones con try
    def cargar_numero():
        nonlocal numero
        try:
            numero = int(input("Ingrese un numero: "))
            return numero
        except ValueError:
            print("Error, no es un numero")
            cargar_numero()
       
    def elevar(numero):
        return numero ** 2
 
    def imprime(numero):
        print(f"El {numero} al cuadrado es: {elevar(cargar_numero())}") 
    ## verificar como ingresar al valor de numero que esta guardado en memoria.
    imprime(cargar_numero())



##Crear una variable llamada n, que sera global, en el codigo del ejercicio anterior y asignarle
## un valor inventado. Realizar las siguientes acciones:

## Mostrar el valor de n, elevado al cuadrado desde dentro del procedimiento.
## Modificar el valor de n, dentro del procedimiento. ¿Que ocurre?
## Si necesitase modificar el valor de n, que es una variable global, dentro del procedimiento cuadrado, ¿Que deberıa hacer?
globals()['valor'] = 30 #modificamos el valor de la variable a través del diccionario
def cuadradoglobal():
    global n
    cuadradolocals(n)
    ## para modificar el valor de n, dentro del procedimiento, se debe utilizar el nombre de la variable
    globals()['n'] = 30 
    cuadradolocals(n)
cuadradoglobal()