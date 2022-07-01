import numpy as np

def pedir_numeros():
   
    """Diseñar un algoritmo que vaya pidiendo números enteros al usuario hasta que ingrese un número menor a 0,
        almacenar los números en un array. Mostrar por pantalla el número menor,
        el mayor y la diferencia entre ambos."""
    
    numeros = np.array([])
    numero = int(input('Ingrese un numero: '))
    while numero > 0:
        numeros = np.append(numeros, numero)
        numero = int(input('Ingrese un numero: '))
    print(f'El numero menor es: {np.min(numeros)}')
    print(f'El numero mayor es: {np.max(numeros)}')
    print(f'La diferencia entre ambos es: {np.max(numeros) - np.min(numeros)}')



def contador_aleatorio():
    """Crear un programa que genere 20 (veinte) números aleatorios ente 1 y 10 y
        los guarde uno por línea en un archivo llamado numeros.txt. 
        Posteriormente debe leer el archivo creado para mostrar el contenido por pantalla y determine 
        cuántos números iguales a 7 y a 3 hay en el archivo.
    """
    import random
    def crear_archivo_como(nombre,extension):
        nombre= nombre + "." + extension
        with open(nombre, "a") as numero:
            return numero
    ## llenamos  archivo con numeros random   
    def llenar_archivo(nombre,cantidad):
         with open(nombre, "w+") as f:
            
            for i in range(cantidad):
                numero = random.randint(1,10)
                f.write(f'{numero}\n')
    ## leemos archivo
    def leer_archivo_compara(nombre):
        contador7=0
        contador3=0
        with open(nombre, 'r') as f:
            lineas = f.readlines()
            for linea in lineas:
                if linea.strip() == '7':
                    contador7 += 1
                if linea.strip() == '3':
                    contador3 += 1
        print(f'Cantidad de numeros iguales a 7: {contador7}')
        print(f'Cantidad de numeros iguales a 3: {contador3}')
        
    def main_hijo():
        nombre = input('Ingrese el nombre del archivo: ')
        cantidad = int(input('Ingrese la cantidad de numeros a generar: '))
        extension = input('Ingrese la extencion del archivo: EJEM. txt, csv, json, etc: ')
        crear_archivo_como(nombre,extension)
        llenar_archivo(nombre,cantidad)
        leer_archivo_compara(nombre)
    main_hijo()  

def buscarvalor(vector,valor):
    """ Diseñar una función llamada BuscarValor, 
         cuyo propósito sea buscar un determinado valor dentro de un conjunto de valores. 
         Dicha función debe recibir como parámetros un vector  y una variable. 
         La función debe retornar 1 si el valor de la variable existe dentro del vector y en caso contrario -1.
    """
    for i in vector:
        if i == valor:
            return 1
    return -1   
          
def main():
    import numpy as np
    vector = np.array([1,2,3,4,5,6,7,8,9,10])
    valor = 4
    print(buscarvalor(vector,valor))
    valor = 0
    print(buscarvalor(vector,valor))
       
     
          
def main():
    import numpy as np
    pedir_numeros()
    contador_aleatorio()
    
    vector = np.array([1,2,3,4,5,6,7,8,9,10])
    valor = 4
    print(buscarvalor(vector,valor))
    valor = 0
    print(buscarvalor(vector,valor))
       
    
if __name__ == '__main__':
    main()