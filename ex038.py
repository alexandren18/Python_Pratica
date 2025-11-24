numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))

if numero1 > numero2:
    print(f"O numero {numero1:.2f} é maior que {numero2:.2f}")

elif numero2 > numero1:
    print(f"O numero {numero2:.2f} é maior que o numero {numero1:.2f}")

else:
    print(f"Os numeros são iguais")