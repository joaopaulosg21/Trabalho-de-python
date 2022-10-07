idades = [10,13,15,17,18,20,12,11,15,13,14,18,19,21,20,15,16,17,19,18,14,15,21,23,15,18,18,19,11,12]
alturas = [1.6,1.5,1.3,1.8,1.4,1.6,1.5,1.8,1.9,2.0,1.2,1.4,1.8,1.9,1.6,1.5,1.3,1.8,1.4,1.6,1.5,1.8,1.9,2.0,1.2,1.4,1.8,1.9,2.0,1.1]

mediaAltura = sum(alturas) / len(idades)
total = 0
for i in range(len(idades)):
    if idades[i] > 13 and alturas[i] < mediaAltura:
        total += 1
print("Total de alunos com a altura inferior a media: %s" % total)