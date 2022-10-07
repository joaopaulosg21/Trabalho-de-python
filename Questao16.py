vendedores = []
entre200E299 = 0
entre300E399 = 0
entre400E499 = 0
entre500E599 = 0
entre600E699 = 0
entre700E799 = 0
entre800E899 = 0
entre900E999 = 0 
maiorQue1000 = 0
while True:
    valor = 0
    vendasBrutas = float(input("Digite o valor das vendas brutas do funcionario ou -1 para sair: "))
    if vendasBrutas == -1:
        break
    valor = (vendasBrutas * 0.09)
    vendedores.append(valor + 200)

for i in vendedores:
    if i >= 200 and i <= 299:
        entre200E299 += 1
    elif i >= 300 and i <= 399:
        entre300E399 += 1
    elif i >= 400 and i <= 499:
        entre400E499 += 1
    elif i >= 500 and i <= 599:
        entre500E599 += 1
    elif i >= 600 and i <= 699:
        entre600E699 += 1
    elif i >= 700 and i <= 799:
        entre700E799 += 1
    elif i >= 800 and i <= 899:
        entre800E899 += 1
    elif i >= 900 and i <= 999:
        entre900E999 += 1
    else:
        maiorQue1000 += 1
    
print("$200 - $299: %s" % entre200E299)
print("$300 - $399: %s" % entre300E399)
print("$400 - $499: %s" % entre400E499)
print("$500 - $599: %s" % entre500E599)
print("$600 - $699: %s" % entre600E699)
print("$700 - $799: %s" % entre700E799)
print("$800 - $899: %s" % entre800E899)
print("$900 - $999: %s" % entre900E999)
print("Maior que $1000: %s" % maiorQue1000)


