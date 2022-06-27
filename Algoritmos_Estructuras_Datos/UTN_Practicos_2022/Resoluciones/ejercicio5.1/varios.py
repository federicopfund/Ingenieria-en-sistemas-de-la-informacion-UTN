# Crear un programa que permita al usuario ingresar un numero en base 10 y lo devuelva en base binaria
def base10_a_binaria(numero):
    if numero == 0:
        return 0
    else:
        return (numero % 2) + 10 * base_binaria(numero // 2)
# Crear un programa que permita al usuario ingresar un numero en base 10 y la base a
# la cual desea convertirlo. Mostrar el resultado de la conversion. Siempre que la base sea
# menor a 10.

def decimal_a_base(numero_decimal, base):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal != 0:
        # dividimos por la base indicada
        numero_binario = numero_binario + numero_decimal % base * multiplicador
        numero_decimal //= base
        multiplicador *= 10

    return numero_binario
## forma recursiva de decimal a base
def decimal_a_base(numero,base):
    if numero == 0:
        return 0
    else:
        return (numero % base) + 10 * base_a(numero // base,base)
    
# Crear un programa que permita ingresar un numero en base 2, y lo convierta a base 10

def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal

def main_hijos_varios():
    numero_decimal = input("Ingrese un numero en base 10: ")
    print(f'el numero {numero_decimal} convertido a binario es: {base10_a_binaria(numero_decimal)}')
    base = input("Ingrese la base a la cual desea convertir: ")
    print(f'El numero {numero_decimal} en base {base},es:  {decimal_a_base(numero_decimal,base)}')
    numero_binario = input("Ingrese un numero en base 2: ")
    print(f'El numero  binario {numero_binario} convertido a decimal es:{binario_a_decimal(numero_binario)}')

if __name__ == '__main_hijos_varios__':
    main_hijos_varios()    