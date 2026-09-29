"""Realizar un programa que lea una frase del teclado y nos indique si es palíndroma, es decir, que la
frase sea igual leyendo de izquierda a derecha, que de derecha a izquierda, sin tener en cuenta los
espacios. Un ejemplo de frase palíndroma es: «Dábale arroz a la zorra el abad». Las vocales con tilde
hacen que los algoritmos consideren una frase palíndroma como si no lo fuese. Por esto,
supondremos que el usuario introduce la frase sin tildes."""

frase=input("Introduce tu frase y te digo si es un palíndroma: ")
fraseLimpia= "".join(frase.split()).lower()
if(frase==frase[::-1]):
    print("Es un palíndroma")
else:
    print("No es un palíndroma")