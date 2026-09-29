"""Crear un programa que solicite palabras una a una. Terminar cuando alguna de las palabras
introducidas sea la cadena «fin» escrita con cualquier combinación de mayúsculas y minúsculas.
Mostrar la frase completa con todas las palabras introducidas separando las palabras introducidas
con espacios en blanco. La cadena «fin» no aparecerá en la frase final."""

frase=""
palabraFin="fin"

while True:
    palabra=input("Introduce una palabra: ")
    if(palabra.lower()==palabraFin):
        break
    frase+= palabra+" "

print(frase)
