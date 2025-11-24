numero = int(input("Digita um numero inteiro: "))
print('''Escolha uma das bases para conversão:
[1] Para binario
[2] Para octal
[3] Para hexadecimal''')
opcao = int(input("Opção: "))

if opcao == 1:
    print(f"O numero {numero} convertido para binario  é igual a {bin(numero)[2:]}")

elif opcao == 2:
    print(f"O numero {numero} convertido para octal é igual a {oct(numero)[2:]}")

elif opcao == 3:
    print(f"O numero {numero} convertido para octal é igual a {hex(numero)[2:]}")

else:
    print(f"Essa opção não existe!")
    

