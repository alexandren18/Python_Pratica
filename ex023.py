numero = int(input("Digita um numero: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milha = numero // 1000 % 10

print("ANALISANDO NUMERO")
print(f"unidade {unidade}")
print(f"dezena {dezena}")
print(f"centena {centena}")
print(f" milha {milha}")