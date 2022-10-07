medias = []
for i in range(10):
    notas = []
    media = 0
    for x in range(4):
        nota = float(input("Digite a nota: "))
        media += nota
    medias.append((media/4))
    print(media/4)

alunos = 0
for i in medias:
    if i >= 7.0:
        alunos += 1

print("Medias: %s" % medias)
print("Quantidade de alunos com media maior ou igual a 7: %s" % alunos)
