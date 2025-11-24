r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"OS segmentos acima podem formar um triangulo",end=" ")

    if r1 == r2 and r2 == r3:
        print(f"equilatero!")

    elif r1 != r2 and r2 != r3 and r3 != r1:
        print(f"escaleno")

    else:
        print(f"isósceles")


    

else:
    print("Os segmentos não podem formar triangulo")