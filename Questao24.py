import random
numeros = []
for i in range(7):
    numeros.insert(i,0)

for i in range(100):
    aleatorio = random.randint(1,6)
    numeros[aleatorio] += 1
    
for i in range(1,7):
    print("Numero %s -" % i,numeros[i])