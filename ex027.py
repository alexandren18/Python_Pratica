nome = str(input("Digite seu nome completo: ")).strip()
lista_nome = nome.split()
print(f"Seu primeiro nome é {lista_nome[0]}")
print(f"Seu ultimo nome é {lista_nome[len(lista_nome)-1]}")