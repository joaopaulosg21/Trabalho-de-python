consoantes = []
letras = []
for i in range(10):
    letra = input("Digite um caractere: ")
    letras.append(letra)


for i in letras:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        continue
    else:
        consoantes.append(i)

print("Quantidade de consoantes: %s" % len(consoantes))
print("Consoantes: %s" % consoantes)
