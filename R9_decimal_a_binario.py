'''/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */'''

def decimal_a_binario(decimal):
    if decimal < 0:
        print("No gracias")
        return

    resultado = 0
    i = 0
    while decimal > 1:
        resto = decimal % 2

        decimal //= 2
        resultado += resto * 10**i
        i += 1
    resultado += decimal * 10 **i
    print("El resultado es: " + str(resultado))

while True:
    try:
        numero = int(input("Introduce un número decimal y te lo paso a binario:\n"))
        decimal_a_binario(numero)
    except ValueError:
        print("Un entero, por favor")

