from random import shuffle
aluno1 = str(input('digite o nome:'))
aluno2 = str(input('digite o nome:'))
aluno3 = str(input('digite o nome:'))
aluno4 = str(input('digite o nome:'))

lista = [aluno1, aluno2, aluno3, aluno4]
ordem = shuffle(lista)

print(lista)
