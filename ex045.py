from random import randint
from time import sleep
itens = ["Pedra","Papél","Tesoura"]
computador = randint(1,3)
print('''Suas opções:
[0] Pedra
[2] Papel
[1] Tesoura''')
jogador = int(input("Qual é sua jogada: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
print("-=" * 20)
print(f" Computador jogou: {itens[computador]} ")
print(f"Jogador jogou: {itens[jogador]} ")
print("-=" * 20)
if computador == 0:
    if jogador == 0: # jogador jogou pedra
        print("EMPATE!")
    elif jogador == 1: # jogador jogou papel
       print("VITORIA do jogador!")
    else:
        print("VITORIA do computador!")
elif computador == 1:
     if jogador == 0:
         print("VITORIA do Computador!")
     elif jogador == 1:
         print("EMPATE!")
     else:
         print("VITORIA do Jogador!")
elif computador == 2:
    if jogador == 0:
        print("VITORIA do jogador!")
    elif jogador == 1:
        print("VITORIA do computador!")
    else:
        print("EMPATE!")
       



