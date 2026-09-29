palabras_total = 0
caracteres = 0

def cantidadLineas(nombre_fichero):
    with open(nombre_fichero + "txt", "r") as fichero:
        lineas = len(fichero.readlines)
        return lineas

def cantidadPalabras(nombre_fichero):
    with open(nombre_fichero + ".txt", "r") as fichero:
        for linea in fichero:
            palabras_total += len(linea.split(" "))
        return palabras_total

def cantidadCaracteres(nombre_fichero):
    with open(nombre_fichero + ".txt", "r") as fichero:
        for linea in fichero:
            caracteres += len(linea)
    return caracteres