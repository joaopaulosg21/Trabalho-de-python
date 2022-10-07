while True:
    nome = input("Digite o nome do atleta: ")
    distancias = []
    if nome == "":
        break
    for i in range(5):
        distancia = float(input("Digite a distancia: "))
        distancias.append(distancia)
    print("Atleta: %s" % nome)
    print("Saltos: ", end="")
    for i in distancias:
        print(i,end=" - ")
    print()
    print("Media dos saltos: %s m" % (sum(distancias)/5))