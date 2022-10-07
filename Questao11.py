vetorA = []
vetorB = []
vetorC = []
vetorD = []

for i in range(10):
    num = int(input("Digite um numero: "))
    vetorA.append(num)
    num2 = int(input("Digite outro numero: "))
    vetorB.append(num2)
    num3 = int(input("Digite outro numero: "))
    vetorC.append(num3)


for i in range(10):
    vetorD.append(vetorA[i])
    vetorD.append(vetorB[i])
    vetorD.append(vetorC[i])

print("Primeiro vetor: %s" % vetorA)
print("Segundo vetor: %s" % vetorB)
print("Terceiro vetor: %s" % vetorC)
print("Quarto vetor: %s" % vetorD)