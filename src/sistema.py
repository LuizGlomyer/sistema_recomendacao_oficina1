import csv
import os
from src import criar_dataset

from src import metrica
from var_colunas import *


def listarJogos():
    lista_jogos = getDataset()
    for jogo in lista_jogos:
        print(jogo)

def listarUsuarios():
    for user in lista_usuarios:
        print(user)

def detalharUsuarioNome(nome): #nota: dicionários não possuem ordem, então a ordem dos elementos podem diferir a cada print
    for user in lista_usuarios:
        if user[1] == nome:
            print("Id do usuário:", user[0])
            print("Nome do usuário:", user[1])
            print("=" * 50)
            for key in user[2]:
                print(key + " -", user[2][key])
            print("=" * 50)
            return
    print("Usuário não encontrado")

def detalharUsuarioId(id):
    for user in lista_usuarios:
        if(user[0] == id):
            print("Id do usuário:", user[0])
            print("Nome do usuário:", user[1])
            print("=" * 50)
            for key in user[2]:
                print(key + " -", user[2][key])
            print("=" * 50)
            return
    print("Usuário não encontrado")

def getTamanhoDatasetCompleto(dados):
    tam = 0
    for linha in dados:
        tam += 1
    return tam

def getTamanhoDatasetUsados(dados): # apenas os jogos que estão sendo usados
    tam = 0
    for linha in dados:
        tam += 1
    return tam

#criar_dataset.criar()

def getDataset():
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
    return jogos_nota

def getAvaliacoes():
    db = open('avaliacoes.ldict', 'r')
    lista_usuarios = eval(db.read())
    return lista_usuarios


lista_usuarios = getAvaliacoes()


#listarUsuarios()
#detalharUsuarioNome('Holly Martim')
#detalharUsuarioId(1497)

#print(metrica.distanciaEuclidiana(users[0][2], users[5][2]))
#print(users[0][2])

print(metrica.recommend(lista_usuarios[0][2], lista_usuarios, "cosseno")) # refazer esse [0][2]
#print(lista_usuarios[0])