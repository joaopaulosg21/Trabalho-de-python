valorMinimo = 0
maiorValor = 0
valorDoSalario = []
valorDoAbono = []
while True:
    salario = float(input("Digite o valor do salario ou 0 para sair: "))
    if salario == 0:
        break
    valorDoSalario.append(salario)
    if (salario * 0.2) <= 100:
        valorMinimo += 1
        valorDoAbono.append(100)
    else:
        valorDoAbono.append(salario*0.2)

maiorValor = max(valorDoAbono,key=int)

print("Salario","-","Abono")
for i in range(len(valorDoSalario)):
    print("R$",valorDoSalario[i],"-","R$",valorDoAbono[i])

print("Foram processados %s colaboradores" % len(valorDoSalario))
print("Total gasto com abonos: R$ %.2f" % sum(valorDoAbono))
print("Valor mínimo pago a %s colaboradores" % valorMinimo)
print("Maior valor de abono pago: R$ %.2f" % maiorValor)
