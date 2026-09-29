n = input("Introduce un numero")

def es_par(n):
    if n == 0:
        return True
    elif n== 1:
        return False
    else:
        return es_par(n-2)

print(es_par(n))