termo= int(input("Digite o primeiro termo de uma PA: "))
razao = int(input("Digite a razão da Pa: "))
decimo = termo + (10 - 1) * razao

for c in range(termo,decimo + razao,razao):
    
    print(f"{c}", end="->")
print("ACABOU!")
    









