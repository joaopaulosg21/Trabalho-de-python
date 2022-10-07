carros = []
consumoDosCarros = []
consumoEm1000 = []

for i in range(5):
    carro = input("Digite o carro: ")
    consumo = float(input("Digite o consumo do veiculo: "))
    carros.append(carro)
    consumoDosCarros.append(consumo)

print("Relatorio Final")
for i in range(len(carros)):
    print((i+1),carros[i],"-",consumoDosCarros[i],"- %.2f litros" % (1000/consumoDosCarros[i]),"- R$ %.2f" % ((1000/consumoDosCarros[i])*2.25))
    consumoEm1000.append(1000/consumoDosCarros[i])

menor = consumoEm1000[0]
menorConsumo = ""
for i in range(len(consumoEm1000)):
    if consumoEm1000[i] < menor:
        menor = consumoEm1000[i]
        menorConsumo = carros[i]

print("O menor consumo é do %s" % menorConsumo)