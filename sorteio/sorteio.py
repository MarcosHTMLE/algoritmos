from random import choice

aluno1 = str(input('digite o nome de um aluno:'))
aluno2 = str(input('digite o nome de um aluno:'))
aluno3 = str(input('digite o nome de um aluno:'))
aluno4 = str(input('digite o nome de um aluno:'))

lista = [aluno1, aluno2, aluno3, aluno4]
sortear = choice(lista)

print('{}'.format(sortear))
