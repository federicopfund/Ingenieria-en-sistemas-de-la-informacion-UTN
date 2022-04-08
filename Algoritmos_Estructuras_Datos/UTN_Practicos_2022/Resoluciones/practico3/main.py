from strings.iniciales import iniciales
from strings.pocisionpares import pocisionpar
from strings.letraserepite import letrasrepetidas
from strings.Simbolos import simbolos

def main():
    Nombre = input("ingrese su nombre: ")
    Apellido = input("ingrese su apellido: ")
    iniciales(Nombre,Apellido)
    frase = input("ingrese una frase: ")
    pocisionpar(frase)
    frase = input("ingresa una frase: ")
    letra = input("ingresa una letra: ")
    letrasrepetidas(frase,letra)
    frase = input("Ingrese una frase con Simbolos, mayusculas e numeros: ")
    simbolos(frase)
    
main()