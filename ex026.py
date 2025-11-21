frase = str(input("digite uma frase: ")).strip().upper()

print(f"sua frase tem a palavra A {frase.count("A")}")
print(f"A letra a aparece a primeira vez na posição {frase.find("A")}")
print(f"A letra a aparece a ultima vez na posição {frase.rfind("A")}")