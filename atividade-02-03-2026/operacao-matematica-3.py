#  Um programa que realiza operações matemáticas básicas (soma, subtração,
# multiplicação, divisão, raiz quadrada e logaritmo) entre dois números fornecidos pelo usuário.
import math

numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

resultado = numero1 + numero2
print(f"A soma dos numeros {numero1} + {numero2} é = {resultado}")
resultado = numero1 - numero2
print(f"A subtração dos numeros {numero1} - {numero2} é = {resultado}")
resultado = numero1 * numero2
print(f"A multiplicação dos numeros {numero1} * {numero2} é = {resultado}")
resultado = numero1 / numero2
print(f"A divisão dos numeros {numero1} / {numero2} é = {resultado}")

print(f"A Raiz dos numeros {numero1} e {numero2} é = {math.sqrt(numero1)} | {math.sqrt(numero2)}")
print(f"O Logaritmo dos numeros {numero1} e {numero2} é = {math.log(numero1)} | {math.log(numero2)}")
