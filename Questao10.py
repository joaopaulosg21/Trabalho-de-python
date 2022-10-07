vetorA = []
vetorB = []
vetorC = []

for i in range(10):
    num = int(input("Digite um numero: "))
    vetorA.append(num)
    num2 = int(input("Digite outro numero: "))
    vetorB.append(num2)

for i in range(10):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])

print("Primeiro vetor: %s" % vetorA)
print("Segundo vetor: %s" % vetorB)
print("Terceiro vetor: %s" % vetorC)