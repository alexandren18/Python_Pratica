from datetime import date
print(f"Descubra se você tem que se alistar!")
nascimento = int(input("Digite seu ano de nascimento: "))
ano = date.today().year
idade = ano - nascimento
print(f" você tem {idade} passou do tempo de você se alistar!")

if idade < 18:
    saldo = 18 - idade
    print(f" você tem {idade}  por tanto não pode se alistar ainda! faltam {saldo} anos")

elif idade == 18:
    print(f" você tem {idade} esta na hora de se alistar!")

else:
    saldo = idade - 18
    print(f" você tem {idade} passou do tempo, você tinha que se alistar a {saldo} anos atrás")