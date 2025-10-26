preco = float(input("Qual é o preço do produto: "))
desconto =(preco * 5)/100
valor = preco - desconto

print(f"O produto vale {preco:.2f} mas com o desconto de 5% fica {valor:.2f}")