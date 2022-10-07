numeros = []
for i in range(10):
    num = int(input("Digite um numero "))
    numeros.append(num)

j = len(numeros) - 1
reversa = []
while j >= 0:
    reversa.append(numeros[j])
    j -= 1

print(reversa)