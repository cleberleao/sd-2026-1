# Leia uma quantidade n de notas (0 a 10) informada pelo usuário, armazene em uma lista e:
# 1. Ordene as notas em ordem crescente e exiba.
# 2. Mostre maior, menor, média e mediana.
# 3. Pergunte se deseja ordenar decrescente e exibir novamente.

qtde = int(input("Quantas notas deseja entrar no sistema: "))
notas = []

for i in range(qtde):
    notas.append(float(input("Digite a nota: ")))

print("Notas na ordem de digitação", notas)
notas.sort()
print("Notas ordenadas crescente", notas)
notas.sort(reverse = True)
print("Notas ordenadas decrescente", notas)