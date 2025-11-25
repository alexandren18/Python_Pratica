contador = 0
soma = 0

for c in range(0,6):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        contador += 1
        soma += n
print(f"Dos 6 numeros somente {contador} são pares e a soma deles deu {soma}")