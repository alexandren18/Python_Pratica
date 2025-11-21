nome = str(input("Digita seu nome completo: ")).strip()

print(f"Seu nome com letras maiusculas é {nome.upper()}")
print(f"Seu nome com letras minusculas é {nome.lower()}")
print(f"Seu nome tem {len(nome.replace(" ",""))}")
print(f"Seu primeiro nome tem {nome.find(" ")} letras")