#Descrição: Crie um programa que demonstra o uso de variáveis básicas (inteiros, floats,
# strings e booleanos). Após entender como funciona, modifique o programa para incluir mais
# dois tipos de variáveis: uma lista e um dicionário.

inteiro = 10
real = 10.1
caractere = "Aula 02-03-2026"
v_ou_f = True
# Comentado, para teste tire o comentário e veja o tipo de dado de cada variável
# print(type(inteiro))
# print(type(real))
# print(type(caractere))
# print(type(v_ou_f))

lista = [10,15,25,30, "A", True, 15.8]
# Comentado, para teste tire o comentário e veja o tipo de dado de cada posição da lista
# print(type(lista))
# print(type(lista[4]))
# print(type(lista[1]))
# print(type(lista[5]))
# print(type(lista[6]))

dicionario = {"nome": "Cleber", "aula": "Sistemas Distribuidos", "ativo": False, "valor_a1": 30}
print(type(dicionario))
print(type(dicionario["ativo"]))
print(dicionario["ativo"])

status = dicionario["ativo"]
print(status)
