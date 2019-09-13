import csv

from var_colunas import *
from src import gerador

'''
print(gerador.gerarNomeCompletoMasculino())
exit()
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
'''
db = open('src/avaliacoes.ldict', 'r')
users = eval(db.read())
'''
print(users[1][2])
print("user :", users[1][1] + '\n')
for key in users[1][2]:
    print(key, users[1][2][key])'''

for user in users:
    print(user)