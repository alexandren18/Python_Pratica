from datetime import date
ano = date.today().year
nascimento = int(input("Digite o seu ano de nascimento: "))
idade = ano - nascimento

if idade <= 9:
    print(f"O atleta tem {idade} anos")
    print(f"Classificação: Mirim")

elif idade > 9 and idade <= 14:
    print(f"O atleta tem {idade} anos")
    print(f"Classificação: Infantil")

elif idade > 14 and idade <=19:
    print(f"O atleta tem {idade} anos")
    print(f"Classificação: Junior")

elif idade > 19 and idade < 26:
    print(f"O atleta tem {idade} anos")
    print(f"Classificação: Senior")

else:
    print(f"O atleta tem {idade} anos")
    print(f"Classificação: Master")
