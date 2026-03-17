# Leia um parágrafo de texto do usuário e exiba:# 1. Quantidade de caracteres (com e sem espaços).# 2. Quantidade de palavras.# 3. Top 3 palavras mais frequentes (desconsiderando maiúsculas/minúsculas e pontuação # simples como , . ; : ! ?).# 4. Verificação se o texto começa e termina com uma palavra fornecida pelo usuário.# 5. Texto normalizado: sem espaços duplicados, sem pontuação básica, tudo em minúsculas.

texto = input("Digite um texto: ")

print("A quantidade de caracteres é: ", len(texto))
print("Letras Maiusculas ", texto.upper())
print("Letras minusculas ", texto.lower())
print("A quantidade de caracteres sem espaço em branco é: ", len(texto.split('.')))
print("Vamos trocar # por ? : \n", texto.replace('#', "?"))
