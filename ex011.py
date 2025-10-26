altura = float(input("Qual é a altura da parede em metros: "))
largura = float(input("Qual é a largura da parede em metros: "))
area = altura * largura
tinta = area/2

print(f"sua parede tem {altura} de altura e {largura} largura então sua area é de {area:.2f}m²")
print(f"para pintar sua parede de {area}m² você vai precisar de {tinta} litros de tinta")