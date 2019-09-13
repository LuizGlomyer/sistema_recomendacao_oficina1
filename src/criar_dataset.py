import csv
import random

from var_colunas import *
from src import gerador



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

print(random.choice(jogos_nota))


lista_usuarios = []
id = 0
for i in range(1500):
    usuario = []
    nome = ""
    notas = {} #todo
    id += 1
    num = random.randint(0, 10)
    genero = "m" if num%2 == 0 else "f" # gênero da pessoa
    if genero == "m":
        nome = gerador.gerarNomeCompletoMasculino()
    else:
        nome = gerador.gerarNomeCompletoFeminino()

    if(num in range(0, 4)):
        intervalo = random.randint(1, 9)
        for j in range(intervalo): # aqui são avaliados de 1 até 8 itens
            jogo = random.choice(jogos_nota)
            while(jogo[Name] in notas):
                jogo = random.choice(jogos_nota)
            nota = random.random() * 100
            nota = int(nota) / 10
            notas[jogo[Name]] = nota

    if(num in range(4, 8)): # de 8 até 15
        intervalo = random.randint(8, 16)
        for j in range(intervalo):
            jogo = random.choice(jogos_nota)
            while (jogo[Name] in notas):
                jogo = random.choice(jogos_nota)
            nota = random.random() * 100
            nota = int(nota) / 10
            notas[jogo[Name]] = nota

    if(num in range(8, 11)): # de 20 a 30
        intervalo = random.randint(20, 31)
        for j in range(intervalo):
            jogo = random.choice(jogos_nota)
            while (jogo[Name] in notas):
                jogo = random.choice(jogos_nota)
            nota = random.random() * 100
            nota = int(nota) / 10
            notas[jogo[Name]] = nota
    if(notas == {}): # rand int vai até o número b informado
        print(num)
        exit()

    usuario.append(id)
    usuario.append(nome)
    usuario.append(notas)
    lista_usuarios.append(usuario)

arquivo = open("avaliacoes.ldict", "w") #lista com dicionario dentro
arquivo.write(str(lista_usuarios))
arquivo.close()
print(str(lista_usuarios))