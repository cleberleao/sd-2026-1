# Solicite ao usuário um número-base e um intervalo (por ex. de 1 a 10) e exiba a tabuada
# multiplicativa nesse intervalo. Permita repetir o processo até o usuário decidir sair.

numero_base = int(input("Digite o numero base para tabuada: "))
inicio_tabuada = int(input("Digite o inicio do intervalo maior que 0: "))
fim_tabuada = int(input("Digite o ultimo numero do intervalo da tabuada: "))

print(f"Tabuada do numero {numero_base}")

for i in range (inicio_tabuada, fim_tabuada):
    print(f"{numero_base} x {i} = ",numero_base * i)