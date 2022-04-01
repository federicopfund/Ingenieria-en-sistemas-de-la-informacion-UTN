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
from posixpath import split
import sys
from sodiaco import Sodiaco
from pip import main
from merge import merge_sort,merge
from rellenar_lista import rellena
from pares import elnumero_es_par
 

def main():
    parametro=int(input("ingrese un numero para verificar si es par: "))
    ##parametro = int(sys.argv[1])
    elnumero_es_par(parametro)
    nombre = input("Ingrese su fecha de Nacimiento:Ejem:(25/10/1996): ")
    Sodiaco(nombre)
    print("Lista a ordenar: [1,5,3,5] ")
    print(f"devolvera una lista ordenada:{merge_sort([1,5,3,5])[0]}, Cantida de comparaciones que hizo para lograrlo:{merge_sort([1,5,3,5])[1]}")
    lista=rellena()
    print("ordenacion por merge_sort: ")
    print(merge_sort(lista)[0])
    
    ##print(f"devolvera una lista ordenada:{merge_sort(lista)[0]}, Cantida de comparaciones que hizo para lograrlo:{merge_sort(lista)[1]}")
main()



## 11) Una ves que tengo los nombres imaginemos que se encuntran en una lista separados por ",".luego recorro la lista con un for "Para que pueda verificar todos los elementos de la lista" considerandolo que puedo seleccionar todos los nombres de la lista, en cada ciclo selecciono un elemento dela lista que corresponde a una nombre. dicho nombre podria comparar directamaente con un condicional si responde a que su inicio es con una M, ya que python
# #    por defoul compara el primer elemento del nombre, permitindome verificar que compla la condicion.
##      En caso de que el usuario ingrese  un argumento con un espacio antes del Nombre en si!! seeria necesario contemplar este error por lo que se supone que tendriamos que rediseñar el algoritmo para que tenga en cuenta este problema  de diseño y contemplar este caso, en el rediseño preguntaria "si" se se encuentra un espacio antes del alemento de interes en caso de ser si verificaria que se haga las comparaciones necesarias par 
##      lograr encontrar el argumento que necesito.

## 12) ordenacion:
## Ordenacion Alfabetiva: se necesita ordenar una lista alfavetica
## Ordenacion Numerica: se necesita ordenar una lista Numerica
## Ordenacion de Tareas: Tareas de un usuario
## ordenacion de Procesos: es posible se necesite ordenar procesos en programa para saber que es lo que va primero y lo siguiente
## Ordenacion Simbolica: es necesario saber cual es erden de los caracteres que tiene la sintaxis del habla. 
## Ordenacion de paquetes: es necesario tener un Orden claro de los package que lo compone de Sofware
## 13) Metodos de ordenacion:
## Bueno primero utilizacia los metodos desarrollado por Python "sort"
## Podria pensar en ordenacion por metodo burbuja 
##       Metodo                              ¿Cuanto Cuesta Ordenar por los difentes metodos?                                              Resumen             
## iterativo -->Ordenacion por seleccion                                    N^2      --> tiempo de Orden             El ordenamiento por selección es uno de los más sencillos, pero es bastante ineficiente: se basa en la idea de buscar el máximo en una secuencia, ubicarlo al final y seguir analizando la secuencia sin el último elemento. 
## iterativo -->Ordenamiento por inserción                                 (O(N^2))  --> tiempo de Orden             El ordenamiento por inserción es un algoritmo bastante intuitivo y se suele usar para ordenar en la vida real. Se basa en la idea de ir insertando ordenadamente: en cada paso se considera la inserción de un elemento más de secuencia y la inserción se empieza a hacer desde el final de los datos ya ordenados. 
## Recurrentes -->Ordenamiento merge sort                                  log2(N) --> tiempo de Orden                                                         Divide y reinarás es un paradigma de diseño de algoritmos recursivos que trabaja partiendo (dividiendo) el problema original en subproblemas del mismo tipo pero más sencillos de resolver. Las soluciones de estos subproblemas luego se combinan para obtener una solución del problema original.