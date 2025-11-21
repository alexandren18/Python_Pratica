velocidade_carro = float(input("Qual sua velocidade: "))
multa = (velocidade_carro - 80) * 7

if velocidade_carro <= 80:
    print("Tenha um bom dia dirija com segurança!")
else:
    print(f" você ta em uma velocidade a cima da via de 80 KM/H foi multado em {multa}R$")