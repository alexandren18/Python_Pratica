dia = int(input("Quantos dias o carro foi alugado: "))
km = float(input("Quantos km você rodou: "))
pagar = (dia * 60) + (km * 0.15)

print(f"O total a pagar é de {pagar:.2f}")