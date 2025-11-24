valor = float(input("Valor do produto: "))


print("FORMAS DE PAGAMENTO")
print('''
[1] A vista dinheiro/cheque
[2] A vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
forma_pagamanento = int(input("Qual é opção: "))

if forma_pagamanento == 1:
    desconto = valor * 10 / 100
    print(f"Sua compra de {valor:.2f} vai ficar no valor de {valor - desconto:.2f}")

elif forma_pagamanento == 2:
    desconto = valor * 5 / 100
    print(f"Sua compra de {valor:.2f} vai ficar no valor de {valor - desconto:.2f}")

elif forma_pagamanento == 3:
    print(f"sua compra será parcelada em 2x de {valor:.2f}")
    
elif forma_pagamanento == 4:
    juros = valor + (valor * 20 / 100)
    parcela = int(input("Quantas parcelas: "))
    print(f"Sua compra sera parcelada em {parcela}x de {juros/parcela:.2f} COM JUROS! ")
    print(f"Sua compra de {valor:.2f} vai custar {juros:.2f} no final.")

else:
    print("Essa opção não existe!")


