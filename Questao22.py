defeitos = []
total = 0
nomesDefeitos = [0,"necessita da esfera","necessita de limpeza","necessita troca do cabo ou conector","quebrado ou inutilizado"]
for i in range(5):
    defeitos.insert(i,0)
while True:
    numero = int(input("Digite o numero de identificação do mouse: "))
    if numero == 0:
        break
    defeito = int(input("Digite o problema \n1-necessita da esfera\n2- necessita de limpeza\n3- necessita troca do cabo ou conector\n4- quebrado ou inutilizado\n"))
    defeitos[defeito] += 1
    total += 1

print("Quantidade de mouses: %s" % total)

print("Situação\tQuantidade\tPercentual")
for i in range(1,5):
    print(nomesDefeitos[i],"\t",defeitos[i],"\t%.2f" % ((defeitos[i]/total)*100),"%")
