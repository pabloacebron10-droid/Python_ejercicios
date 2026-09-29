"""Escribir una aplicación que solicite al usuario cuántos números desea introducir. A continuación,
introducir por teclado esa cantidad de números enteros, y por último, mostrar en el orden inverso al
introducido."""

vueltas= int(input("¿Cuántos números desea introducir?"))
tabla=[]

for i in range(vueltas):
    num=int(input(f"Introduce el elemento {i+1}: "))
    tabla.append(num)

print((tabla[::-1]))
    
    