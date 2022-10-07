jogadores = []
totalDeVotos = 0
for i in range(0,23):
    jogadores.insert(i,0)

while True:
    numero = int(input("Informe um valor entre 1 e 23 ou 0 para sair!: "))
    if numero == 0:
        break
    if numero > 23 or numero < 0:
        print("Numero invalido")
        continue
    totalDeVotos += 1
    jogadores[numero -1] += 1

print("Resultado da votação:")
print("Foram computados %s votos" % totalDeVotos)
print("Jogador      Votos       %")
for i in range(len(jogadores)):
    if(jogadores[i] > 0):
        print((i+1),"           ",jogadores[i],"        %.1f" % ((jogadores[i]/totalDeVotos)*100),"%")

maior = 0
numMelhorJogador = 0
for i in range(len(jogadores)):
    if(jogadores[i] > 0):
        if maior < jogadores[i]:
            maior = jogadores[i]
            numMelhorJogador = i+1
print("O melhor jogador foi o número %s, com %s votos, correspondendo a %.2f" % (numMelhorJogador,jogadores[numMelhorJogador-1],((jogadores[numMelhorJogador-1]/totalDeVotos)*100)),"% do total de votos.")
