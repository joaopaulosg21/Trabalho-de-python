usuarios = ["alexandre","anderson","antonio","carlos","cesar","rosemary"]
espaco = [456123789,1245698456,123456456,91257581,987458,789456125]
totalOcupado = (sum(espaco)/1024)/1024

print("ACME Inc.       Uso do espaço em disco pelos usuários")
print("------------------------------------------------------------------------")
print("Nr.  Usuário        Espaço utilizado     % do uso")
for i in range(len(usuarios)):
    espacoOcupadoUsuario = ((espaco[i]/1024)/1024)
    print(usuarios[i],"             %.2f MB" % espacoOcupadoUsuario,"\t %.2f" % ((espacoOcupadoUsuario/totalOcupado)*100),"%")
print("Espaço total ocupado: %.2f MB" % totalOcupado)
print("Espaço médio ocupado: %.2f MB" % (totalOcupado/len(usuarios)))