"""Diseñar un algoritmo que lea del teclado una frase e indique, para cada letra que aparece en la
frase, cuántas veces se repite. Se consideran iguales las letras mayúsculas y las minúsculas para
realizar la cuenta."""

import unicodedata
import re

def normalizar_frase(frase):
    frase = frase.lower()

    # Separar letras de tildes (á -> a + ´)
    frase = unicodedata.normalize('NFD', frase)

    # Eliminar marcas diacríticas (acentos)
    frase = ''.join(
        c for c in frase
        if unicodedata.category(c) != 'Mn'
    )

    # Dejar solo letras a-z
    frase = re.sub(r'[^a-z]', '', frase)

    return frase

def recorreryContar(fraseNormalizada):
    contador=[0]*26
    for c in fraseNormalizada:
        contador [ord(c) - ord('a')]+=1
    return contador

def imprimeRespuesta(contador):
    print("Resultado: ")
    for i in range (len(contador)):
        if contador[i]>0:
            letra= chr(i + ord('a'))
            veces= "veces" if contador[i]>1 else "vez"
            print(f"\t{letra}: {contador[i]} {veces}")



frase= input("Introduce una frase y para cada letra que aparece en la frase, te digo cuántas veces se repite: \n")
fraseNormalizada= normalizar_frase(frase)
contador=recorreryContar(fraseNormalizada)
imprimeRespuesta(contador)


