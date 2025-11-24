nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2)/2
 
if media < 5.0:
    print(f"Sua média final foi {media:.2f} , reprovado!")

elif media >= 5.0 and media <= 6.9:
    print(f"Sua média final foi {media:.2f}, recuperação!")

else:
    print(f"Sua média final foi {media:.2f}, Parabéns passou!")