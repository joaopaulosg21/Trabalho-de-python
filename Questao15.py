
notas = []
out = ","
while True:
    valor = float(input("Digite uma nota ou -1 para sair: "))
    if(valor == -1):
        break
    notas.append(valor)

print("Quantidade: %s " % len(notas))

for i in notas:
    print(i,end=" ")
print()

qtdNotas = len(notas) - 1
while qtdNotas >= 0:
    print(notas[qtdNotas],end=" ")
    qtdNotas -= 1
print()
print("Soma dos valores: %s " % sum(notas))
media = sum(notas)/len(notas)
print("Media %.2f " % media)

maiorQueMedia = []
menorQue7 = []
for nota in notas:
    if nota > media:
        maiorQueMedia.append(nota)
    if nota < 7:
        menorQue7.append(nota)
print("Maior que media: ",end=" ")
for nota in maiorQueMedia:
    print(nota,end=" ")
print()

print("Menor que 7: ",end=" ")
for nota in menorQue7:
    print(nota,end=" ")
print()
print("Programa encerrado")

