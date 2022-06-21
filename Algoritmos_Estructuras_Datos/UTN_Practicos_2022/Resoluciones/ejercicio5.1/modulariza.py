## Crear un procedimiento llamado cuadrado que tome un numero como parametro e imprima en pantalla dicho numero al cuadrado. *A fines pedagogicos, no a fines de elegancia
## de codigo, haremos un procedimiento en este caso y no una funcion como corresponderıa.
## a)Imprimir, desde dentro del procedimiento, las variables locales que este posea.¿Que
##   se imprime? * utilizar locals()

## b)Agregar dos o tres variables extras con valores inventados, y volver a mostrar todas
##   las variables locales. ¿Hubo cambio alguno?






from ast import Global
from threading import local


def cuadradolocals(numero):
    ##numero = globals
    numero = locals()["numero"]
    ## ingresar datos, captar exepciones con try
          
    def elevar(numero):
        return numero ** 2
 
    def imprime(numero): 
        print(f"El {numero} al cuadrado es: {elevar(numero)}") 
        
    imprime(numero)
    ## verificar como ingresar al valor de numero que esta guardado en memoria.
    



##Crear una variable llamada n, que sera global, en el codigo del ejercicio anterior y asignarle
## un valor inventado. Realizar las siguientes acciones:

## Mostrar el valor de n, elevado al cuadrado desde dentro del procedimiento.
## Modificar el valor de n, dentro del procedimiento. ¿Que ocurre?
## Si necesitase modificar el valor de n, que es una variable global, dentro del procedimiento cuadrado, ¿Que deberıa hacer?


def cuadradoglobal():
    # creamos una variable global
    global n
    
    ## acceder a la variable global y cambiar el valor de la misma
    globals()["n"] =6
   
    cuadradolocals(n)
    ## para modificar el valor de n, dentro del procedimiento, se debe utilizar el nombre de la variable
    globals()['n'] = 30  #modificamos el valor de la variable a través del diccionario
    cuadradolocals(n)
   

## ¿Que imprimira en pantalla el siguiente codigo?
# Output :"Es un lindo dia"
#  ¿Cual es el alcance de la variable frase?
## el alcance de la variable frase es local, porque esta dentro del procedimiento f().
## tan local  que si imprimo el nombre de la variable frase antes de la asignacion dentro del proceso 
#   el papu no save la asignacion que tiene frase y su Output dira : "UnboundLocalError" claro que si el no 
## entiende nada sobre lo que le estampos pidiendo pero la raza humana se encargara de ayudarlo
#  podriamos darle una mano y explicarle que es una variable local.
frase = "Hola"

def f():
    try:
        print(frase)
        frase = "Es un lindo dia"
        print(frase)
    except UnboundLocalError as error:
        print("Su variable no esta definida dentro del procedimiento")
        frase = "Es un lindo dia"
        f() 


## ¿Que imprimira en pantalla el siguiente codigo? 
## Output: "3" "4" "1"
# Determine el alcance de cada variable.
# alcance de x: global
# alcance de y: local pero bueno porque esta dentro de la funcion f() definida.
# osea que x es mas global que y.
# en todo caso sera y global en todo el procedimiento.

x = 3

def f():
    
    y = x + 1
    ## nuuuu encontro el valor de x el manija, la verdad que no se porque pense que no se puede acceder a x desde esta anidacion.
    print(x)
    def g():
        x = 1
        print(y)
        print(x)
        def h():
            z = y + 1
            print(z)
            print(y)
        h()
        # print(z) aca si no entiende y no sabe que es z, ya que z es local re contra local.
    g()
f()

