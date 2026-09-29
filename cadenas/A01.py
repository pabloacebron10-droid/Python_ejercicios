"""*Introducir por teclado dos frases e indicar cuál de ellas es la más corta, es decir, la que
contiene menos caracteres."""

frase1= input("Introduce la frase 1: ")
frase2= input("Introduce la frase 2: ")

if(len(frase1) < len(frase2)):
    print(f"La frase 1: \""+frase1+"\" es la más corta")
elif(len(frase1) > len(frase2)):
    print(f"La frase 2: \""+frase2+"\" es la más corta")
else:
    print("Son de la misma longitud")
