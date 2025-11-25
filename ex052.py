num = int(input("Digita um numero: "))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
        tot += 1
        print("\033[31m",end=" ")
    else:
        print("\033[33m",end=" ")
    print(f"{c}", end=" ")

print(f"O numero {num} foi divisivel {tot} vezes")
if tot == 2:
    print("Ele é primo")
else:
    print("Ele não é primo")
    