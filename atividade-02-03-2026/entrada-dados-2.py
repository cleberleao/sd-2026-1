# O programa irá solicitar que o usuário insira um nome e um número. Verificar se o
# número digitado é par ou ímpar, validar se o nome contém mais de 3 caracteres. Se não, peça
# para o usuário digitar novamente.

nome = input("Digite seu nome: ")
numero =int(input("Digite um numero qualquer: "))

# todas estas formas de print funcionam
print(f"Seu nome é {nome}")
# print("Você digitou o nome", nome)
# print("Você digitou o nome "+ nome)

par_impar = numero % 2

if(par_impar == 0):
    print(f"Numero {numero} é par")
elif(par_impar !=0):
    print(f"Numero {numero} é Impar")

# print(len(nome[-1]))

if(len(nome)<4):
    print("Digite um nome com mais de 3 caracteres")
    nome = input("Digite seu nome: ")
else:
    print("Nome digitado corretamente")
