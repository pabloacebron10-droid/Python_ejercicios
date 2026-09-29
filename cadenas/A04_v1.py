"""Diseñar el juego «Acierta la contraseña». La mecánica del juego es la siguiente: el primer jugador
introduce la contraseña; a continuación, el segundo jugador debe teclear palabras hasta que la
acierte.
(A04_V1.java) 4 v1 -> El programa indicará si la palabra introducida es mayor o menor
alfabéticamente que la contraseña."""

def pista(contraseña,intento):
    if(contraseña.lower()<intento.lower()):
        print("Pista: La contraseña está antes en el diccionario")
    if(contraseña.lower()>intento.lower()):
        print("Pista: la contraseña está después en el diccionario")

def validarContraseña(cadena):
    esInvalida= True
    if (not(cadena.isalpha())):
        esInvalida= False
        print("Clave inválida, solo letras, sin espacios")
    return esInvalida


print("=== ACIERTA LA CONTRASEÑA ===")

while True:
    contraseña= input("-- JUGADOR 1 -->  Introduce la contraseña: ")
    if(validarContraseña(contraseña)):
        break

while True:
    print(f"La contraseña tiene {len(contraseña)} caracteres")

    while True:
        intento= input("-- JUGADOR 2 --> Intenta adivinar la contraseña: ")
        if(validarContraseña(intento)):
            break
    pista(contraseña,intento)

    if(contraseña.lower()==intento.lower()):
            break

print("Enhorabuena J2, ¡Has acertado la contraseña!")