frase= input("Introduce tu frase y te la devuelvo sin máyusculas: ")
fraseMod=""

for i in range (len(frase)):
    if (frase[i].lower() in "aeiouáéíóúäëïöü"):
        fraseMod+=" "
    else:
        fraseMod+=frase[i]

print(fraseMod)


