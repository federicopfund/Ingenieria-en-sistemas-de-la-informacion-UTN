# Supongamos tienes una lista con las alturas en cm de todos los miembros de tu familia,
# por ejemplo [181.5, 72., 34.7, 171.3, 160.1]. Crear un array y mostrar sus atributos, el tipo
# de datos, tanto del array como de sus elementos. Mostrar tambien el total de familiares
# cargados en el array.
import numpy as np

def familia():
    alturas = np.array([181.5, 72., 34.7, 171.3, 160.1])
    print(alturas)
    print(f'tipo de datos del array:{type(alturas)}')
    for altura in alturas:
        print(f'Ingresamos al elementos del array: {altura}')
        print(f'Tipo de datos del array: {type(altura)}')
    print(f'Total de familiares: {len(alturas)}')


def array3d(dimencion,filas,columnas):
    # crear un array de 3 dimensiones, que tenga 3 matrices de 2 filas por 4 columnas. Llenelo
    # con ceros.
    array=np.zeros((dimencion,filas,columnas))
    print(f'matriz de Zeros{array}')
    print(f'Tupla de {array.shape}')
    print(array.ndim)
  
    
def array(dimencion):
    array = []
    for i in range(dimencion):
        array.append([])
        for j in range(dimencion):
            array[i].append(0)
    print(array)
    for i in range(dimencion):
        for j in range(dimencion):
            print(f'Ingresamos al elementos del array: {array[i][j]}')
            print(f'Tipo de datos del array: {type(array[i][j])}')
    return array

# Crear una matriz de (4, 6) con valores al azar que pertenecen al intervalo [0, 1).
import numpy as np
import random
def matriz(a,b):
    matriz = np.random.rand(a,b)
    print(f'matrix azar: {matriz}')
    print(f'Tupla de {matriz.shape}')
    print(f'dimencion de la matriz: {matriz.ndim}')
    for i in range(a):
        for j in range(b):
            print(f'Ingresamos al elementos del array: {matriz[i][j]}')
            print(f'Tipo de datos del array: {type(matriz[i][j])}')
    return matriz

# Crear un vector con un total de 25 elementos equidistantes en el intervalo [1, 6].

def vector(a,b):
    vector = np.linspace(a,b,25)
    print(f'Vector: {vector}')
    print(f'Cantidad de Elementos: {len(vector)}')
    print(f'Tupla de {vector.shape}')
    print(f'dimencion de la matriz: {vector.ndim}')
    for i in range(25):
        print(f'Ingresamos al elementos del array: {vector[i]}')
        print(f'Tipo de datos del array: {type(vector[i])}')
    return vector
# Pedirle 6 numeros enteros al usuario y guardarlos en una lista. Crear un array de una
# dimension en base a dicha lista.

def numeros():
    lista = []
    for i in range(6):
        lista.append(int(input(f'Ingrese un numero: ')))
    print(lista)
    array = np.array(lista)
    print(array)
    print(f'Tupla de: {array.shape}')
    print(f'dimencion de la matriz: {array.ndim}')
    for i in range(6):
        print(f'Ingresamos al elementos del array: {array[i]}')
        print(f'Tipo de datos del array: {type(array[i])}')
    return array

# Crear un vector con numeros enteros al azar entre 0 y 5. Luego reemplazar los 0 con el valor -1.
import numpy as np
import random
def vector2():
    vector = np.random.randint(0,5,25)
    print(vector)
    for i in range(25):
        if vector[i] == 0:
            vector[i] = -1
    print(vector)
    print(f'Tupla de: {vector.shape}')
    print(f'dimencion de la matriz: {vector.ndim}')
    for i in range(25):
        print(f'Ingresamos al elementos del array: {vector[i]}')
        print(f'Tipo de datos del array: {type(vector[i])}')
    return vector

# Dada una lista de 3 numeros enteros cualesquiera, y un vector con 3 numeros enteros
# cualesquiera. ¿Que sucede si suma la lista a si misma, lista + lista, y si hace lo mismo
# con el vector? Haga la prueba y compare los resultados.

def listasyvectoressumas():
    lista = [1,2,3]
    vector = np.arange(5)
    # Suma de valores uno a uno con arreglos
    vectorA = np.arange(5)
    vectorB = np.arange(10) # este arreglo es mas grande que el anterios
    Suma_Vectores = vectorA+vectorB[:5] # deben tener el mismo tamaño para realizar la suma
    print(f'Suma de vectores: {Suma_Vectores}')
    print(f'Suma de listsa: {lista + lista}')
    print(f'vector{vector}')
    print(f'suma de vextores: {vector + vector}')
    print(lista + vector[:3])
    print(vector[:3] + lista)
    
# Crear una matriz de 3 x 3, con valores que van de 1 a 9.

def matriz3x3():
    matriz = np.arange(1,10,3).reshape(3,3)
    print(matriz)
    print(f'Tupla de {matriz.shape}')
    print(f'dimencion de la matriz: {matriz.ndim}')
    for i in range(3):
        for j in range(3):
            print(f'Ingresamos al elementos del array: {matriz[i][j]}')
            print(f'Tipo de datos del array: {type(matriz[i][j])}')
    return matriz

#  Crear una matriz de 16 x 20 con numeros al azar, de algun tipo que le guste, distinto al
#  tipo de dato por defecto float64.

def matriz16x20():
    matriz = np.ndarray(shape=(16,20), dtype="float64", order='F')

    print(matriz)
    print(f'Tupla de {matriz.shape}')
    print(f'dimencion de la matriz: {matriz.ndim}')
    
# Crear un array de 5 filas y 6 columnas, llenarlo con valores numericos enteros, al azar
# entre 1 y 6. Luego, reemplazar todos los valores en la fila 5, por el valor 0. 
def array():
    array = np.random.randint(1,6,(5,6))
    # Remplazamos la fila 5 por 0
    # comienza la indenzacion en 0 por eso en el indice 4 representa la fila 5
    array[4] = 0
    print(array)
    
    print(f'Tupla de {array.shape}')
    print(f'dimencion de la matriz: {array.ndim}')

 
# Crear una funcion que realice la suma de dos arrays de dimension 1 y devuelva el array
# resultante. Sin utilizar el operador + directamente, sino creando un algoritmo que hiciese
# la suma lugar a lugar.

def suma_array():
    array1 = np.random.randint(1,6,(5,))
    array2 = np.random.randint(1,6,(5,))
    array3 = np.zeros(5)
    for i in range(5):
        array3[i] = array1[i] + array2[i]
    print(f'primer array: {array1}')
    print(f'segundo aray: {array2}')
    print(f'suma de array: {array3}')
    print(f'Tupla de {array3.shape}')
    print(f'dimencion de la matriz: {array3.ndim}')
    
    
# Crear una funcion que realice un producto entre dos arrays de dimension 1 y devuelva el
# vector resultante. Sin utilizar el operador * directamente, sino creando un algoritmo que
# hiciese el producto lugar a lugar; sin considerar angulo alguno que hay en
# el producto vectorial o cruz de dos vectores, sino simplemente el producto de los valores
# lugar a lugar)   

def product_array():
    array1 = np.random.randint(1,6,(5,))
    array2 = np.random.randint(1,6,(5,))
    array3 = np.zeros(5)
    for i in range(5):
        array3[i] = array1[i] * array2[i]
    print(f'primer array: {array1}')
    print(f'segundo aray: {array2}')
    print(f'producto de array: {array3}')
    print(f'Tupla de {array3.shape}')
    print(f'dimencion de la matriz: {array3.ndim}')
    
# Extender ahora el ejercicio anterior, a otra funcion que permita realizar la suma de elementos lugar a lugar, de dos arrays de dimension 2.

def Suma_Array_d2():
    array1 = np.random.randint(1,6,(5,6))
    array2 = np.random.randint(1,6,(5,6))
    array3 = np.zeros((5,6))
    for i in range(5):
        for j in range(6):
            array3[i][j] = array1[i][j] + array2[i][j]
    print(f'primer array: {array1}')
    print(f'segundo aray: {array2}')
    print(f'suma de array: {array3}')
    print(f'Tupla de {array3.shape}')
    print(f'dimencion de la matriz: {array3.ndim}')
    
# Cree una matriz identidad de 6 x 6.
def identidad():
    matriz = np.identity(6)
    print(matriz)
    print(f'Tupla de {matriz.shape}')
    print(f'dimencion de la matriz: {matriz.ndim}') 
    
## genere una matriz 5 x 5  que tenga las filas intercaladad entre 0 y 1
def intercaladas_filas():
    matriz = np.zeros((5,5))
    for i in range(5):
        for j in range(5):
            if i % 2 == 0:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
    print(matriz)
    print(f'Tupla de {matriz.shape}')
    print(f'dimencion de la matriz: {matriz.ndim}')
## genere una matriz 5 x 5  que tenga las filas y columnas intercaladas entre 0 y 1
def intercaladas_filas_columnas():
    matriz = np.zeros((5,5))
    for i in range(5):
        for j in range(5):
            if i % 2 == 0:
                if j % 2 == 0:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 0
            else:
                if j % 2 == 0:
                    matriz[i][j] = 0
                else:
                    matriz[i][j] = 1
    print(matriz)
    print(f'Tupla de {matriz.shape}')
    print(f'dimencion de la matriz: {matriz.ndim}')
    
#. Crear un array (4, 3) de nombres inventados, determinar cuantos nombres en la segunda
# columna terminan con la letra s:

def array_nombre():
    nombres = np.array([['Juan', 'Pedro', 'Maria', 'Juan', 'Pedro', 'Maria'],
                        ['Luis', 'Gonzales', 'Gomez', 'Perez', 'Gonzalez', 'Gomez'],
                        ['Pepe', 'Gonzalez', 'Gomes', 'Peres', 'Gonzales', 'Gomez'],
                        ['Perez', 'Gonzale', 'Gomez', 'Perez', 'Gonzalez', 'Gomez']])
    contador=0
    for i in range(len(nombres)):
        for j in range(len(nombres)):
            if nombres[:,i][j][-1].strip()=='s':
                contador +=1
    
    print(f'Tupla de {nombres.shape}')
    print(f'dimencion de la matriz: {nombres.ndim}')
    print(f'Nombres que terminan con la letra s: {contador}')
    
#. Pedirle al usuario las notas de 3 examenes, para 8 alumnos diferentes. Utilizar todo
# lo aprendido hasta ahora, como archivos de texto, creacion de funciones propias, etc.
# Recuerde comentar el codigo y ser prolijo.

def notas():
    notas = np.zeros((8,3))
    for i in range(8):
        for j in range(3):
            notas[i][j] = int(input(f'Ingrese la nota {j+1} del alumno {i+1}: '))
    # Guardarlos en un archivo de texto llamado notas.txt.
    def guadar_notas():
        return np.savetxt('notas.txt', notas, fmt='%d')
    
    # Leer ese archivo de notas, y crear una matriz para guardar esas notas. Cada columna
    # seria una nota, cada fila representara un alumno.
    def leer_notas():
        notas_leidas = np.loadtxt('notas.txt')
        print(notas_leidas)
        print(f'Tupla de {notas_leidas.shape}')
        print(f'dimencion de la matriz: {notas_leidas.ndim}')
    #Calcular la nota promedio total, la nota promedio por alumno, y la nota promedio por examen
    def promedio_total():
        promedio_total = np.mean(notas)
        return promedio_total
    # Determinar la mejor nota de cada alumno.
    def mejor_nota():
        mejor_nota = np.max(notas, axis=1)
        return mejor_nota
    def menor_nota():
        menor_nota = np.min(notas, axis=1)
        return menor_nota
    # Determinar cual de los 3 examenes fue donde hubo la mejor nota.
    def examenes():
        examenes = np.argmax(notas, axis=1)
        return examenes
    # Determinar cual de los 3 examenes fue donde hubo la peor nota.
    def examenes_peor():
        examenes_peor = np.argmin(notas, axis=1)
        return examenes_peor
    
    def main_hijo():
       
        guadar_notas()
        leer_notas()
        print(f'El promedio total es: {promedio_total()}')
        print(f'La mejor nota es: {mejor_nota()}')
        print(f'La menor nota es: {menor_nota()}')
        print(f'El examen con la mejor nota es: {examenes()}')
        print(f'El examen con la peor nota es: {examenes_peor()}')
    main_hijo()  
def main():
    familia()
    array3d(3,2,3)
    array(3)
    matriz(4,6)
    vector(1,6)
    vector2()
    listasyvectoressumas()
    numeros()
    matriz3x3()
    matriz16x20()
    array()
    suma_array()
    product_array()
    Suma_Array_d2()
    identidad()
    intercaladas_filas()
    intercaladas_filas_columnas()
    array_nombre()
    array_1()
    array_2()
    array_3()
  
    notas()

if __name__ == '__main__':
    main() 