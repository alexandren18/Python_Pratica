from random import choice
a1 = str(input("Nome do aluno 1: "))
a2 = str(input("Nome do aluno 2: "))
a3 = str(input("Nome do aluno 3: "))
a4 = str(input("Nome do aluno 4: "))
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print(f"O aluno escolhido foi o {escolhido}")