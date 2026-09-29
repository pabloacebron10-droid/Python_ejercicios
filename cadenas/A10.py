"""Un anagrama es una palabra que resulta del cambio del orden de los caracteres de otra. Ejemplos de
anagramas para la palabra roma son: amor, ramo o mora. Construir un programa que solicite al
usuario dos palabras e indique si son anagramas una de otra."""

  
NUMERO_DE_PALABRAS=2
palabras=[0]*NUMERO_DE_PALABRAS

import unicodedata
import re

def normalizarPalabras(palabras):
    
    for i in range (NUMERO_DE_PALABRAS):
        # Pasar a minúsculas
        palabrasLimpias[i] = palabrasLimpias[i].lower()

        # Normalizar (separar letras de tildes)
        palabrasLimpias[i] = unicodedata.normalize('NFD', palabrasLimpias[i])

        # Eliminar tildes / marcas diacríticas
        palabrasLimpias[i] = ''.join(
            c for c in [palabrasLimpias[i]]
            if unicodedata.category(c) != 'Mn'
        )

        # Dejar solo letras a-z
        palabrasLimpias[i] = re.sub(r'[^a-z]', '', palabrasLimpias[i])

    return palabrasLimpias


def esAnagrama(palabrasLimpias):
    # Contador base con la primera palabra
    contador_base = [0] * 26
    for c in palabrasLimpias[0]:
        contador_base[ord(c) - ord('a')] += 1

    # Comparar el resto de palabras contra la base
    for palabra in palabrasLimpias[1:]:
        contador = [0] * 26
        for c in palabra:
            contador[ord(c) - ord('a')] += 1

        if contador != contador_base:
            return False

    return True



print(f"Dame {NUMERO_DE_PALABRAS} palabras y te indico si son un anagrama.")

for i in range (NUMERO_DE_PALABRAS):
    palabras[i]=input(f"Introduce la palabra nº {i+1}: ")

palabrasLimpias= normalizarPalabras(palabras)
if(esAnagrama(palabrasLimpias)):
    print("Las palabras:")
    for i in range (NUMERO_DE_PALABRAS):
        if i<NUMERO_DE_PALABRAS-1:
            print(f"\" {palabras[i]}\",")
        else:
            print(f"\" {palabras[i]}\"")

    print(" son un anagrama.")




