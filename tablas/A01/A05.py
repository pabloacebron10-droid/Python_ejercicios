"""Escribir el método:
int[] rellenaPares(int longitud, int fin)
Que crea y devuelve una tabla ordenada de la longitud especificada, que se encuentra rellena con
números pares aleatorios comprendidos en el rango desde 2 hasta fin (inclusive)."""
import random

def rellenaPares(longitud,fin):
    tabla=[]
    for i in range(longitud):
        
        while True:
            num= random.randint(2,fin)
            if num % 2 ==0:
                break
        tabla.append(num)

    return tabla 

lenght= int(input("Introduce la longitud de la tabla: "))
end= int(input("Introduce el final del rango de números aleatorios: "))
print(rellenaPares(lenght,end))
