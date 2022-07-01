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

def main():
    pedir_numeros()
    
if __name__ == '__main__':
    main()