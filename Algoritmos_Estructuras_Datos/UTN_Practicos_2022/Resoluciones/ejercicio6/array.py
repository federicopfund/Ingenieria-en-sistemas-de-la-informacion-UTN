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
array3d(3,2,3)   
    
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

