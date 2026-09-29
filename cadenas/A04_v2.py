"""El programa mostrará la longitud de la contraseña y una cadena con los
caracteres acertados en sus lugares respectivos y asteriscos en los no acertados."""

def validarContraseña(cadena):
    esInvalida= True
    if (not(cadena.isalpha())):
        esInvalida= False
        print("Clave inválida, solo letras, sin espacios")
    return esInvalida


def pista(contraseña,intento):
    longitudMinuma= min(len(contraseña),len(intento))
    pista=""

    for i in range (longitudMinuma):
        if(contraseña[i]==intento[i]):
            pista+=contraseña[i]
        else:
            pista+="*"

    if(len(intento)<len(contraseña)):
        diferencia= len(contraseña)-len(intento)
        for i in range (diferencia):
            pista+="*"

    return pista
           
       
       
print("=== ACIERTA LA CONTRASEÑA ===")
while True:
    contraseña= input("-- JUGADOR 1 -->  Introduce la contraseña: ")
    if(validarContraseña(contraseña)):
        break

intento=""
while True:
    print(f"La contraseña tiene {len(contraseña)} caracteres")
    print(pista(contraseña,intento))
    while True:
        intento= input("-- JUGADOR 2 --> Intenta adivinar la contraseña: ")
        if(validarContraseña(intento)):
            break
    if(contraseña.lower()==intento.lower()):
            break
    
    print("Enhorabuena J2, ¡Has acertado la contraseña!")