lista = [1,2,3,4,5,6,3,8,9,0,4,12]

def devuelve_suma(lista):
    if len(lista) == 0:
        return 0
    else:
        sublista = lista[1:]
        return lista[0] + devuelve_suma(sublista)

print(devuelve_suma(lista))