## Crear un archivo de texto .txt de notas de Windows, y guardar una palabra por lınea.
## Crear un programa que muestre en pantalla, una por una, las palabras que hay guardadas en ese archivo.
from distutils import extension


def archivo():# podriamos mandar un argumento pdre para que gobierne todas las funciones internas? Yes, you can!
    
        # crear un archivo de texto
    def crear_archivo(nombre):
        try:
            with open(nombre, "a") as archivo:
                return archivo
        except FileNotFoundError:
            print("No se pudo crear el archivo")
            return None

        # escribir en el archivo
    def escribir_archivo(nombre, texto):
        try:
           cantidad = int(input('Cuantas lineas deceas escribir: '))
           with open(nombre, "w+") as archivo:
               for i in range(cantidad):
                   archivo.write(f'LINEA:{i}: {texto}\n')
        except OSError :
            print("No se pudo escribir en el archivo")
            return None
            
        # mostrar y leer archivo              
    def mostrar_leer_archivo(archivo):
        with open(archivo, 'r') as f:
            lineas = f.readlines()   
        # mostrar lineas
        for linea in lineas:
            print(linea)
    def main_hijo():
        ingrese_nombre = input(f"Ingrese el nombre del archivo: ") 
        extencion = input(f"Ingrese la extencion del archivo: ")
        nombre = ingrese_nombre + "." + extencion
        crear_archivo(nombre) 
        texto = input(f"Ingrese el texto que desea guardar en el archivo: ")
        escribir_archivo(nombre, texto)       
        mostrar_leer_archivo(nombre)  
    main_hijo()        

    
# Crear un programa que genere un archivo de texto llamado numeros.txt con 10 numeros
# enteros guardados en el mismo, uno por lınea.

def archivo_numeros():
    try:
        def crea_archivo_algoritmen(nombre,cantidad):
            with open(nombre, 'a') as f:
                for i in range(cantidad):
                    f.write(f'{i}\n')
            return f
    except OSError:
        print("No se pudo crear el archivo")
        
    def leer_algoritmen(nombre):
        with open(nombre, 'r') as f:
            lineas = f.readlines()
        for linea in lineas:
            print(f'linea: {linea}')
    
    def main_hijo(nombre,cantidad,extension):
        
        nombre = nombre + "." + extension
        
        crea_archivo_algoritmen(nombre,cantidad)
        leer_algoritmen(nombre)
    main_hijo("numeros",10,"txt")
    
archivo_numeros()




    