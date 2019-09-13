import csv
from var_colunas import *
print(Critic_Score)


dados = open("data/vg.csv")
dados = csv.reader(dados)
jogos_nota = []
qtd = 0
for linha in dados:
    if linha[Critic_Score] != '':
        jogos_nota.append(linha)
        qtd += 1
jogos_nota.pop(0)
jogos_nota.sort()
jogos_nota[0][Name] = jogos_nota[0][Name].lstrip(" ")
jogos_nota.sort()
a = jogos_nota[0]
b = jogos_nota[1]
for jogo in jogos_nota:
    print(jogo)


