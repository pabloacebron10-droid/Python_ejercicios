import random

t= []
suma=0

for i in range (10):
    num= random.randint(1,100)
    t.append(num)
    print(num)
    suma+=num

print(t)
print(suma)



