temperaturas = []
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
mediaAnual = 0
for i in range(12):
    temp = float(input("Digite a tempetura: "))
    temperaturas.append(temp)

for i in temperaturas:
    mediaAnual += i

mediaAnual = mediaAnual / 12
print("Media de temperatura anual: %s" % mediaAnual)
for i in range(len(temperaturas)):
    if temperaturas[i] > mediaAnual:
        print("%s - %s temperatura: %s" % ((i+1),meses[i],temperaturas[i]))