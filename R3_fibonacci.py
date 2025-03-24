'''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 '''

def fibonacci(rango):
    numero = [0, 1, 1]
    for i in range(rango - 3):
        a = numero[-1] + numero[-2]
        numero.append(a)
    print(numero)

fibonacci(50)
input("Introduce algo para cerrar el programa.\n")