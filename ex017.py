from math import hypot

ca = float(input("Digita o adjacente: "))
co = float(input("Digite o cateto oposto: "))
h = hypot(ca,co)

print(f"a hipotenusa dos catetos {co:.2f} e {ca:.2f} é {h:.2f}")