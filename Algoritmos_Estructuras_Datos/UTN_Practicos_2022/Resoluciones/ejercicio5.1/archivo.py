
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
    def escribir_archivo(nombre):
        try:
           cantidad = int(input('Cuantas lineas deceas escribir: '))
           with open(nombre, "w+") as archivo:
               for i in range(cantidad-1):
                   texto = input(f'Ingrese un {nombre.strip("s.txt")}: ')
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
        escribir_archivo(nombre)       
        mostrar_leer_archivo(nombre)  
    main_hijo()        

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

def archivo_colores():
    ## reutilizamos codigo.
    archivo()

def archivo_numeros():
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
        contador=0
        with open(nombre, 'r') as f:
            lineas = f.readlines()
            for linea in lineas:
                if linea.strip() == '5':
                    contador += 1
        print(f'Cantidad de numeros iguales a 5: {contador}')
        
    def main_hijo():
        nombre = input("Ingrese el nombre del archivo: ")
        extension = input("Ingrese la extencion del archivo: ")    
        nombre = nombre + "." + extension
        crear_archivo_como(nombre,extension)
        cantidad = int(input("Ingrese la cantidad de numeros que desea guardar: "))
        llenar_archivo(nombre,cantidad)
        leer_archivo_compara(nombre)
    main_hijo()


def archivo_promedio(nombre):
    cuenta=0
    
    with open (nombre,'r+') as promedio:
        linea=promedio.readlines()

        for i in range(len(linea)):
            linea[i]=int(linea[i].rstrip("\n"))
            cuenta = linea[i] + cuenta
        promedio=cuenta/len(linea)
    print(f'promedio de archivos: {round(promedio,2)}.')
    


def main():
    print("""Crear un archivo de texto .txt de notas de Windows, y guardar una palabra por lınea.
            Crear un programa que muestre en pantalla,una por una, 
            las palabras que hay guardadas en ese archivo.""")
    archivo()
    print("""Crear un programa que genere un archivo de texto llamado numeros.txt con 10 numeros
            enteros guardados en el mismo, uno por lınea.""")
    archivo_numeros()
    print("""Crear un programa que le pida al usuario 5 colores, y los guarde en un archivo de texto
            llamado colores.txt""")
    archivo_colores()
    print(""" Crear un programa que dado un archivo de numeros con valores entre 1 y 10 (lo puede generar como ud. desee)
                determine cuantos numeros iguales a 5 hay en el archivo.""")
    archivo_promedio('numeros.txt')


if __name__ == "__main__":
    main()