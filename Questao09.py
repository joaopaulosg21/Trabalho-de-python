vetorA = []
for i in range(10):
    num = int(input("Digite um numero: "))
    vetorA.append(num)

total = 0
for i in vetorA:
    total += (i ** 2)

print("Soma dos quadrados: %s" % total)