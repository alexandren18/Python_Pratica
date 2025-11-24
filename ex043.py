peso = float(input("Qual é seu peso KG: "))
altura = float(input("Qual é sua altura: "))
imc = peso /(altura**2)

print(f"O IMC dessa pessoa é de {imc:.2f} ")

if imc < 18.5:
    print("Abaixo do peso")

elif imc > 18.5 and imc < 26:
    print("peso ideal")

elif imc > 25 and imc <= 30:
    print("Sobrepeso")

elif imc > 30 and imc <= 40:
    print("Obesidade")

else:
    print("Obesidade morbida")
