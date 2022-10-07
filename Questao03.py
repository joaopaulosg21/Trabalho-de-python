notas = []
media = 0

for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    media += nota
print("notas: %s " % notas)
print("media: %s" % (media/4))