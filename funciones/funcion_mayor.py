numeros = [0,0,0]
numeros[0] = input("Escribe tres números.\nPrimer número: ")
numeros[1] = input("Segundo número: ")
numeros[2] = input("Tercer número: ")


def mayorIterativa(lista):
    mayor = lista[0]

    for numero in lista:
        if mayor < numero:
            mayor = numero

    return mayor


def mayorRecursiva(lista):
    #caso base
    if len(lista) == 1:
        return lista[0]

    #compuesto
    else:
        primero = lista[0]
        sublista = lista[1:]
        mayor_sub = mayorRecursiva(sublista)

        #casos
        if primero > mayor_sub:
            return primero
        else:
            return mayor_sub
    return 

print(mayorIterativa(numeros))
print(mayorRecursiva(numeros))



    