import csv
import os

from src import metrica
from var_colunas import *

def listarJogos():
    for jogo in jogos_nota:
        print(jogo)

def listarUsuarios():
    for user in users:
        print(user)

def detalharUsuarioNome(nome): #nota: dicionários não possuem ordem, então a ordem dos elementos podem diferir a cada print
    for user in users:
        if(user[1] == nome):
            print("Id do usuário:", user[0])
            print("Nome do usuário:", user[1])
            print("Avaliações:", user[2])
            return
    print("Usuário não encontrado")

def detalharUsuarioId(id):
    for user in users:
        if(user[0] == id):
            print("Id do usuário:", user[0])
            print("Nome do usuário:", user[1])
            print("Avaliações:", user[2])
            return
    print("Usuário não encontrado")

dados = open("data/vg.csv")
dados = csv.reader(dados)
db = open('avaliacoes.ldict', 'r')
users = eval(db.read())
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

#listarJogos()
#listarUsuarios()
#detalharUsuarioNome('Holly Martim')
#detalharUsuarioId(1497)

#todo métricas estão dando negativo pois não há jogos em comum, aumentar a qtd de avaliações ou diminuir qtd jogos
#print(metrica.distanciaEuclidiana(users[0][2], users[5][2]))
print(metrica.recommend(users[0][2], users))