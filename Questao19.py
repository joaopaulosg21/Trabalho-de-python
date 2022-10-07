sistemasOperacionais = []
nomes = [0,"Windows Server","Unix","Linux","Netware","Mac OS","Outro"]
for i in range(7):
    sistemasOperacionais.insert(i,0)

total = 0
while True:
    opcao = int(input("Escolha um numero de 1 a 5 ou 0 para sair!: "))
    if opcao == 0:
        break
    sistemasOperacionais[opcao] += 1
    total += 1

print("Sistema operacional","       ","Votos","         ","%")
print("-------------------","----")
for i in range(1,7):
    print(nomes[i],"               ",sistemasOperacionais[i],"         %.2f" % ((sistemasOperacionais[i]/total)*100),"%")
print("-------------------     -----")
print("Total","     ",total)


maior = 0
maisVotos = ""
indice = 0
for i in range(len(sistemasOperacionais)):
    if sistemasOperacionais[i] > maior:
        maior = sistemasOperacionais[i]
        maisVotos = nomes[i]
        indice = i


print("O Sistema Operacional mais votado foi o %s, com %s votos, correspondendo a %s" % (maisVotos,maior,((sistemasOperacionais[indice]/total)*100)),"% dos votos.")
