'''/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */'''

def inversor(cadena):
    resultado = ""
    for c in cadena[::-1]:
        resultado += c
    print(resultado)

while True:
    texto = input("Introduce un texto y te lo inverto:\n")
    inversor(str(texto))