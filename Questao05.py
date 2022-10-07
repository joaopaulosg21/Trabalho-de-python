numeros = []
par = []
impar = []

for i in range(20):
    num = int(input("Digite um numero: "))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print("Numeros: %s" % numeros)
print("Numeros pares: %s" % par)
print("Numeros impares: %s" % impar)
