# importar biblioteca nomes
import random

print(random.randint(0,9))

lista_usuarios = []
for i in range(1500):
    usuario = []
    nome = "" #todo
    notas = {} #todo

    num = random.randint(10)
    if(num in range(0, 4)):
        pass # aqui são avaliados de 1 até 8 itens
    if(num in range(4, 8)):
        pass # de 8 até 15
    if(num in range(8, 11)):
        pass # de 20 a 30

    usuario.append(nome)
    usuario.append(notas)
    lista_usuarios.append(usuario)

arquivo = open("avaliacoes")