'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 '''

n = 33
primos = [1]

def localizar_primos(rango):
    for i in range(rango + 1):
        #primero compruebo k no es uno y vuelvo a la siguiente iteración
        if i <= 1:
            continue
        elif any(i % primo == 0 for primo in primos[1:]) and len(primos) > 1:
            #no primo
            continue
        else: 
            #primo
            primos.append(i)

def ejercicio():
    while True:
        try:
            entrada = int(input("Escribe un número y te diré si es primo\n"))
            break
        except ValueError:
            print("Introduce un entero")

    localizar_primos(entrada)
    if entrada in primos:
        print("El " + str(entrada) + " es primo")
    else:
        print("El " + str(entrada) + " NO es primo")
    primos.clear
    localizar_primos(100)
    print("Los primos del 1 al 100 son:")
    print(primos)

def explotar_portatil():
    while True:
        try:
            entrada = int(input("Escribe el límite de los primos a comprobar\n"))
            break
        except ValueError:
            print("Introduce un entero")
    primos.clear
    localizar_primos(entrada)
    print(primos)

while True:
    eleccion = input("¿Qué quieres hacer? (Comprobar) si un número es primo. (Imprimir) numeros primos\n")
    match eleccion:
        case "Comprobar":
            ejercicio()
        case "Imprimir":
            explotar_portatil()
