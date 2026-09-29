"""Diseñar un programa que solicite al usuario que introduzca por teclado 5 números decimales. A
continuación, mostrar los números en el mismo orden que se han introducido."""

print("Introduce 5 números por teclado:")
numeros=[]

for i in range(5):
    num=int(input(f"Introduce el elemento número {i+1}: "))
    numeros.append(num)

print(numeros)
    

     
