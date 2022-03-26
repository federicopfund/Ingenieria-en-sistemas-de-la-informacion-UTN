##Ejercicio numero 1
## un algoritmo es un conjunto de reglas 
## un programa es un conjunto de instrucciones
## Ejercicio numero 4
## A) es Falso porque no se puede combertir a entero un numero real.
## B) es Falso ya que no es necesario de convertir un str a un str osea son el mismo tipo.
## C) es falso ya que no se puede operar con distintos tipos de datos.
## D) es Verdadero lo que ocurrira sera que concatenara 2 str.

## 5) expresiones aritmeticas.
## a) ((3*23)-7+186)
## b) (185+(53/2) + 5)
## c) (314 + 21 - (117/2))
## d) (48 + (2*5) + (58/2) + 68)
 
## la correcta es (Los algoritmos deben ser descriptivos con precision y sin ambiguedad)
## 7) la apropiada en mi opinion es; Una secuencia de pasos que debe realizar para obtener un cierto resultado en un tiempo finito.
## 8)
##  a) Para numeros de dias desde el inicio del año. (tipo int) --> Unidad dimencionales Enteras.
##  b) Tiempo transcurrido desde el inicio del año hasta hoy,en dias. (tipo int) --> Unidad dimencional Enteras.
##  c) El numero serial de un celular o aparato electronico. (tipo float)--> Unidad dimencional Real.
##  d) La edad  de tu mascota.(tipo int)--> Unidad dimencional Entero.
##  e) La cantida actual de habitantes de una Ciudad.(tipo int)--> Unidad dimencional Entera.
##  f) El promedio temporal de habitantes en una ciudad.(tipo Float)--> Unidad dimencional Real.
##  g) Un numero de  telefono.(Tipo Int)--> unidad dimencional entera.
##  h) Cantidad de intentos permitidos para ingresar la contraseña.(tipo Int)-->unidad dimencional entera.
#%%
from ast import Num
import sys

from pip import main



def elnumero_es_par(Num):
    if Num % 2 == 0:
        print("Los Numeros son Pares")
    else:
        print("Los datos son Impares")    

def main(parametros):
    elnumero_es_par(parametros)

if __name__ == '__main__':
    
    import sys
    
    if len(sys.argv) != 2:
        main(int(sys.argv[0]))
    else:
        print("La Cantidad de algumento no es Correcta")