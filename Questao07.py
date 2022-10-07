soma = 0
mult = 1
numeros = []

for i in range(5):
    num = int(input("Digite um numero: "))
    numeros.append(num)

for i in numeros:
    soma += i
    mult *= i

print("Numeros: %s " % numeros)
print("Soma: %s" % soma)
print("Multiplicação: %s " % mult)