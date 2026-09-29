""" /*Diseñar el método: int maximo (int t[]), que devuelva el máximo valor contenido en la tabla t. */"""

import random


tabla=[]
elementos=int(input("¿Cuántos elementos quieres que tenga la tabla?: "))
maximo=0

for i in range(elementos):
    num= random.randint(1,100)
    tabla.append(num)
    maximo= num if num>maximo else maximo

print("\nTabla:\n ", tabla)
print("\nEl máximo es: ", maximo)

# Sacando el máximo con método:

print("El máximo con método max es: ",max(tabla))
