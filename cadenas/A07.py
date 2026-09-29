""" /*Los habitantes de Javalandia tienen un idioma algo extraño; cuando hablan siempre comienzan sus
frases con «javalin, javalon», para después hacer una pausa más o menos larga (la pausa se
representa mediante espacios en blanco o tabuladores) y a continuación expresan el mensaje.
Existe un dialecto que no comienza sus frases con la muletilla anterior, pero siempre las terminan
con un silencio, más o menos prolongado y la coletilla «javalen, len, len».
Se pide diseñar un traductor que, en primer lugar, nos diga si la frase introducida está escrita en el
idioma de Javalandia (en cualquiera de sus dialectos), y en caso afirmativo, nos muestre solo el
mensaje sin muletillas. */"""


def idiomaJavalandia(cadena,dialecto1,dialecto2):
    if (cadena.startswith(dialecto1) or cadena.endswith(dialecto2)):
        print("La frase está escrita en el idioma de Javalandia")
        esJavanlandes= True
    else:
        print("La frase no está escrita en el idioma de Javalandia")
        esJavanlandes=False
    return esJavanlandes

def fraseTraducida(cadena,dialecto1,dialecto2):
    cadenaTraducida=cadena
    if(cadena.startswith(dialecto1)):
        cadenaTraducida= cadenaTraducida[len(dialecto1):].strip()
    if(cadena.endswith(dialecto2)):
        cadenaTraducida= cadenaTraducida[:len(cadenaTraducida)-len(dialecto2)].strip()
    return cadenaTraducida

dialecto1= "javalin, javalon  "
dialecto2= "javalen, len, len"
frase= input("Introduce una frase: ")

if(idiomaJavalandia(frase,dialecto1,dialecto2)):
    print(f"La frase traducida es \"{fraseTraducida(frase,dialecto1,dialecto2)}\"")


