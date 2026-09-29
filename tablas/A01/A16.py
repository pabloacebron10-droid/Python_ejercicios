"""16) Desarrollar el juego «la cámara secreta», que consiste en abrir una cámara mediante su combinación
secreta, que está formado por una combinación de dígitos del 1 al 5:
• El jugador especificará cuál es la longitud de la combinación; a mayor longitud, mayor será la
dificultad del juego.
• La aplicación genera, de forma aleatoria, una combinación secreta que el usuario tendrá que
acertar.
• En cada intento se muestra como pista, para cada dígito de la combinación introducido por el
jugador (si es mayor, menor o igual que el correspondiente en la combinación secreta)."""

import random


def dificultad(numero_menu):
    match(numero_menu):
        case 1: longitud= random.randint(2,5)
        case 2: longitud= random.randint(5,8)
        case 3: longitud= random.randint(8,12)
    return longitud

def clave_secreta(longitud):
    tabla_secreta=[]
    for i in range (longitud):
        num=random.randint(1,5)
        tabla_secreta.append(num)
    return tabla_secreta

def clave_usuario(longitud,tabla_secreta,tabla_usuario):
    for i in range (longitud):
        if tabla_usuario[i]!=tabla_secreta[i]:
            while True:
                num= int(input(f"Escribe la posición {i+1}: "))
                tabla_usuario[i]=(num)
                if num <1 or num>5:
                    print("Valor no válido (Introduce un número del 1 al 5)")
                else:
                    break
        else:
            tabla_usuario[i]=(tabla_secreta[i])
    return tabla_usuario

def comparar_tablas(tabla1,tabla2):
    sonIguales=(tabla1==tabla2)
    return sonIguales
    
def pista(tabla_secreta,tabla_usuario,length):
    for i in range(length):
        if tabla_secreta[i]> tabla_usuario[i]:
            print(f"Pista: La posición {i+1} es mayor que ",tabla_usuario[i])
        if tabla_secreta[i]< tabla_usuario[i]:
            print(f"Pista: La posición {i+1} es menor que ",tabla_usuario[i])
        
            

    
def candado(tabla_secreta, tabla_usuario, length):

    tabla_candado=tabla_usuario
    for i in range(length):
        if tabla_secreta[i]!=tabla_candado[i]:
            tabla_candado[i]= "*" 
    print(tabla_candado)
    return tabla_usuario

def menu():
    while True:
        print("==== LA CÁMARA SECRETA ====")
        print("\n Elige la dificultad: ")
        opcion=int(input("1. Fácil\n2. Intermedio\n3. Dificil\n0. Salir\n"))
        if opcion <0 or opcion >3:
            print("Opción no válida")
        else:
            break
    return opcion


while True:
    opcion=menu()

    if opcion!=0:
        length= dificultad(opcion)
        tabla_secreta=clave_secreta(length)
        tabla_usuario=[0]*length
        while True:
            tabla_usuario=clave_usuario(length,tabla_secreta,tabla_usuario)
            print("")
            pista(tabla_secreta,tabla_usuario,length)
            print("")
            candado(tabla_secreta,tabla_usuario,length)
            print("")
            if comparar_tablas(tabla_secreta,tabla_usuario):
                break
        print("¡Click! Has abierto la cámara secreta!")
    if opcion==0:
        print("Saliendo...")
        break


