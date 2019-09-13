from random import randint, choice
import os


dir = os.path.abspath(__file__).rstrip("gerador.py") # local do arquivo
print(dir)

#retorna um numero no formato XXXX-XXXX. Se o parâmetro for True, retorna um número no formato (XX) XXXX-XXXX
def gerarTelefoneFixo(temDDD = False):
    parte1 = str(randint(2, 5))
    if temDDD:
        f = open("DDDs.txt", "r")
        listaDDDs = f.read().split(" ")
        parte1 = "(" + str(choice(listaDDDs)).rstrip('\n') + ") " + parte1
        f.close()

    parte2 = randint(0, 999)
    parte3 = randint(0, 9999)

    return parte1 + "{:03d}-{:04d}".format(parte2, parte3)
    return parte1 + parte2 + "-" + parte3

def gerarNumeroCelular(temDDD = False):
    parte1 = "9"
    if temDDD:
        f = open("DDDs.txt", "r")
        listaDDDs = f.read().split(" ")
        parte1 = "(" + str(choice(listaDDDs)).rstrip('\n') + ") " + parte1
        f.close()

    parte2 = randint(0, 9999)
    parte3 = randint(0, 9999)

    return parte1 + "{:04d}-{:04d}".format(parte2, parte3)

def gerarSobrenome():
    f = open("data/sobrenomes.txt", 'r')
    lista_sobrenomes = f.readlines()
    f.close()
    qtd_nomes = randint(2, 3) #de 2 a 3 sobrenomes
    sobrenome = ""
    if randint(1, 10) > 8: #20% para cair no caso onde há apenas 1 ou 4 sobrenomes
        qtd_nomes = choice([1, 4])

    for i in range(qtd_nomes):
        sobrenome += choice(lista_sobrenomes).rstrip('\n')
        sobrenome += " " if i != qtd_nomes-1 else "" #não pode concatenar espaço em branco na última iteração
    return sobrenome

def gerarNomeMasculino():
    f = open("data/nomes_masculinos.txt", 'r')
    lista_nomes = f.readlines()
    f.close()
    nome = choice(lista_nomes).rstrip('\n')

    return nome

def gerarNomeCompletoMasculino():
    return gerarNomeMasculino() + " " + gerarSobrenome()

def gerarNomeFeminino():
    f = open("data/nomes_femininos.txt", 'r')
    lista_nomes = f.readlines()
    f.close()
    nome = choice(lista_nomes).rstrip('\n')

    return nome

def gerarNomeCompletoFeminino():
    return gerarNomeFeminino() + " " + gerarSobrenome()

def gerarCpfFantasioso(): #não necessáriamente é um cpf válido
    parte1 = randint(0,999)
    parte2 = randint(0,999)
    parte3 = randint(0,999)
    parte4 = randint(0,99)

    return "{:03d}.{:03d}.{:03d}-{:02d}".format(parte1, parte2, parte3, parte4)

def gerarData(doisDigitos = False): #não necessariamente é uma data válida #True para gerar anos com apenas 2 caracteres
    ano = str(randint(1900, 2020))
    mes = randint(1, 12)
    if mes == 2:
        dia = str(randint(1, 29))
        dia = "0" + dia if len(dia) < 2 else dia
        return "{}/{:02d}/{}".format(dia, mes, ano if not doisDigitos else ano[2:])
    else:
        dia = str(randint(1, 31))
        dia = "0" + dia if len(dia) < 2 else dia
        return "{}/{:02d}/{}".format(dia, mes, ano if not doisDigitos else ano[2:])

def gerarHorario():
    segundos = randint(0, 59)
    minutos = randint(0, 59)
    horas = randint(0, 23)

    return "{:02d}:{:02d}:{:02d}".format(horas, segundos, minutos)

#print(gerarNomeCompletoFeminino())