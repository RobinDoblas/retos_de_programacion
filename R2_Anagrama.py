'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

def anagrama_comprobator(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    if len(palabra1) != len(palabra2):
        return False
    for i in range(len(palabra1)):
        if palabra1[i] not in palabra2:
            return False
        elif palabra2.count(palabra1[i]) != palabra1.count(palabra1[i]):
            return False
        elif palabra2.count(palabra1[i]) <= 1 and palabra2.find(palabra1[i]) == i:
            return False
    return True

while True:
    enunciado = input("Introduce dos palabras separadas por un espacio y te compruebo si son un anagrama\n")
    entrada1 = str(enunciado.split(" ")[0])
    entrada2 = str(enunciado.split(" ")[1])
    if anagrama_comprobator(entrada1, entrada2):
        print("Estas dos palabras son un anagrama")
    else:
        print("Estas dos palabras NO son un anagrama")