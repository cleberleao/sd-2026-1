# imc = peso / (altura * altura)
# Abaixo de 18.5: Abaixo do peso
# 18.5 a 24.9: Peso normal
# 25.0 a 29.9: Sobrepeso
# 30.0 ou mais: Obesidade

# Duas funções separadas: uma para o cálculo e outra para a classificação.

def calcular_imc(peso, altura):
    return peso / (altura * altura)

def classificacao_imc(imc):
    if imc <= 18.5:
        print("Você está abaixo do peso ideal")
    elif imc > 18.5 and imc < 24.9:
        print("Seu peso está normal")
    elif imc > 25.0 and imc < 29.9:
        print("Você está com sobrepeso")
    elif imc >= 30.0:
        print("Você está obesidade")

while True:
    print("\n-- Calculadora de IMC --")
    opcao = int(input("Digite 1 para calcular e 0 para sair: "))
    if opcao == 1:
        peso = float(input("Digite o peso em KG ex: 58.700= "))
        altura = float(input("Digite a altura em metros ex: 1.75= "))
        imc = calcular_imc(peso, altura)
        classificacao_imc(imc)
    elif opcao == 0:
        break
    else:
        print("Dados invalidos")
