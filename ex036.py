valor_casa = float(input("Qual é o valor da casa que você quer comprar: "))
salario = float(input("Qual seu salário: "))
anos = int(input("Em quantos anos você vai pagar :"))
prestacao = valor_casa/(anos*12)
minimo = salario * 30 / 100

if prestacao> minimo:
    print(f"Emprestimo negado pois a parcela de {prestacao:.2f} é maior que 30% do seu salario de {salario:.2f}")

else:
    print(f"Emprestimo aprovado em {anos*12} parcelas de {prestacao:.2f}")