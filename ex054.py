from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(0,7):
    nasc = int(input("Digite o ano que você nasceu: "))
    if ano - nasc >= 18 :
        maior += 1
    else:
        menor += 1

print(f"{maior} pessoas são maiores de idade e {menor} ainda não são .")
