def iniciales(nombre,apellido):
    print (f" {nombre.capitalize()} {apellido.capitalize()}")
    

def letrasrepetidas(frase,letra):
    contador=0
    for i in frase:
        if i ==letra:
            contador+=1
            
    print(f"la cantidad de veces que se repite: {letra}, es: {contador}.")


def pocisionpar(frase):  
    for i in range(0,len(frase),2):
       print(f"Pocision: {i}, letra: {frase[i]}")
        
def remplazo(frase):
    lista= list(frase)
    for i in range(len(lista)):
        if lista[i] =="a":
            lista.insert(i,4)
        if lista[i] == "e":
            lista.insert(i,3)
    print(frase)

def simbolos(frase):
    contador=0
    for i in frase:
        if i == " ":
            contador +=1
    print(f"Cantida de Caracteres de la frase: {len(frase)-contador}, Cantidad de espacios: {contador} ")
## Permita al usuario ingresar el nombre de un archivo, genere un nuevo nombre donde los
## espacios sean reemplazados por guion bajo y la extension por numerales.
##  archivo nuevo.txt -> archivo-nuevo.#####

def remplazaarchivo():
    nombre = input("ingrese el nombre del archivo: ")
    nuevonombre = nombre.replace(" ","-")
    nuevonombre = nuevonombre.replace(".txt",".#####")
    print(nuevonombre)

## Permitir ingresar al usuario un numero de un dıgito. Controlando se haya ingresado dicho
## numero de no mas de 1 dıgito de longitud, pasarlo a letras y mostrarlo en pantalla.
## Ejemplo: Si ingresa 3, se vera como resultado ”tres”

def traducciondedigitoacaracter():
    numero = int(input("Ingrese un numero: "))
    if numero>0 and numero<10:
        print(f"El numero {numero} es: {str(numero)}")
    else:
        print("El numero ingresado no es valido")

##Se le pedira al usuario una frase. Se mostraran en pantalla, una palabra por lınea de la
## misma frase. no usar listas en este ejercicio
def mostrarfrase():
    frase = input("Ingrese una frase: ")
    for i in frase:
        print(i)