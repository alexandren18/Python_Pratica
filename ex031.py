viagem_km = float(input("Quantos kms são a sua viagem : "))
print(f"Você vai comeeçar uma viagem de {viagem_km}Km/h")
if viagem_km <= 200:
    preco =viagem_km * 0.50
    print(f"O valor da sua passagem é de {preco}")

else:
    preco = viagem_km * 0.45
    print(f"Valor da sua passagem é de {preco}")