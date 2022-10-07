idades = []
alturas = []

for i in range(5):
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    idades.append(idade)
    alturas.append(altura)

count = 4
idade_inversa = []
altura_inversa = []
while count >= 0:
    idade_inversa.append(idades[count])
    altura_inversa.append(alturas[count])
    count -= 1


print(idade_inversa)
print(altura_inversa)