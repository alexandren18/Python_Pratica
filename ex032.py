from datetime import date
ano = int(input("digite algum ano se o ano for 0 é o atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é bisexto")

else:
    print(f"O ano de {ano} não é bisexto")