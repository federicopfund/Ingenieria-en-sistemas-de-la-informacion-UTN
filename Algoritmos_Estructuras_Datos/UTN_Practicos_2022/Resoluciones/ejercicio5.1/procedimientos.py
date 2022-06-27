# -*- coding: utf-8 -*-

def numerales(nombre,longitud,caracter):
    def crear_archivo_como(nombre):
        with open(nombre, "a") as rectangulo:
            return rectangulo
    ## llenamos  archivo con numeros random   
    def llenar_archivo(nombre,longitud,caracter):
         with open(nombre, "w+") as f:
            for i in range(longitud):
                if i == 0 or i == longitud-1:          
                    f.write(f'{caracter*(longitud+2)}\n')
                else:
                    
                    espacios =' '*longitud
                    f.write(f'{caracter}{espacios}{caracter}\n')
            return f
    ## leemos archivo
    def leer_archivo_compara(nombre):
        contador=0
        with open(nombre, 'r') as f:
            lineas = f.readlines()
            for linea in lineas:
                print(linea)
                    
    def main_hijo(nombre,longitud,caracter):
        crear_archivo_como(nombre)
        llenar_archivo(nombre,longitud,caracter)
        leer_archivo_compara(nombre)
        
    main_hijo(nombre,longitud,caracter)
numerales("numeros.txt",6,"*")
from archivo import archivo_numeros,archivo_numeros_con_argumentos

def main_hijos_procedimientos():
    print(""" 
          Crear un procedimiento que se encargue de crear un archivo de texto, con el nombre que
          se le de como argumento. Y que lo llene con 250 numeros al azar entre 1 y 100.
          """)
    archivo_numeros()
    print(""" 
          Crear una segunda version del procedimiento anterior, que ahora tome dos parametros
           extras, a y b para poder indicarle el intervalo de valores que se desean para los numeros
           al azar. O sea, ahora el procedimiento generara un archivo de texto, del nombre que se le
           de, con valores al azar en [a, b].
           """)
    archivo_numeros_con_argumentos(nombre="numeros.txt",cantidad=250,inicio=1,fin=100)
    print("""
           Realizar un procedimiento que tome como parametro una longitud e imprima en pantalla
             un rectangulo de numerales, hueco por dentro. Por ejemplo, si se ingreso 4, se vera en
             pantalla: Tip: Puede ser util pensarlo por lınea horizontal
             Generalizarlo, luego, en una version 2, para un parametro extra: el caracter que se usara
             para dibujar el rectangulo, en vez de usar siempre un numeral.
          """)
    numerales("numeros.txt",6,"*")
if __name__ == "__main_hijos_procedimientos__":
    main_hijos_procedimientos()