salario = float(input("Qual seu salaíro: "))

if salario <= 1250:
    aumento = (salario * 15)/100
    print(f"voce teve um aumento de {aumento:.2f}R$ seu salario ficou {salario + aumento:.2f}R$")

else:
    aumento = (salario * 10)/100
    
    print(f"voce teve um aumento de {aumento:.2f}R$ seu salario ficou {salario + aumento:.2f}R$")