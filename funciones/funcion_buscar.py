lista = ["a",4,5,7,"loco", 55, 33]

def buscar(elemento, lista):
    if len(lista) == 0:
        return False
    else:
        primero = lista[0]
        sublista = lista[1:]
        if primero == elemento:
            return True
        else:
            return buscar(elemento, sublista)

print(buscar("e",lista))
