from random import randint
from time import sleep
computador = randint(0,5)

print("-=-"*20)
print("Vou pensar em um numero de 0 a 5 tente adivinhar...")
print("-=-"*20)
jogador = int(input("Digite uum numero: "))
print("processando...")
sleep(2)

if computador == jogador:
    print(f"Parabens você ganhou eu pensei no numero {computador}")

else:
    print(f"Você perdeu eu pensei no numero {computador}")


print("FIM DO JOGO!")