lista = [1,2,10,3,4,5,6,7,8,8,-1,-2,-3,-4,-5]
segundoMax = -100000000
max= -100000000
contador = 0

for elemento in lista:
    if max < elemento:
        segundoMax = max
        max = elemento
    elif elemento > segundoMax and elemento != max:
        segundoMax = elemento
print(segundoMax)