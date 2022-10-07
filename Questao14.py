positivo = 0
perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]

for pergunta in perguntas:
    print("Responda com sim ou não")
    resposta = input(pergunta + ": ")
    if resposta.lower() == "sim":
        positivo += 1

if positivo == 2:
    print("Suspeita")
elif positivo >= 3 and positivo <= 4:
    print("Cúmplice")
elif positivo == 5:
    print("Assassino")
else:
    print("Inocente")