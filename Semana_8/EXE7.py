"""
Exercício 7. Escreva um programa que possua uma função conta_vogais que receba uma
string e retorne o número de vogais nela. Considere apenas as vogais a, e, i, o, u (maiúsculas
ou minúsculas). Use a função para calcular a quantidade de vogais de uma string digitada
pelo usuário.
"""

def conta_vogais(s):
    vogais = 0
    for i in range(0, len(s)):
        if s[i] in "aAáÁàÀãÃâÂeEéÉiIíÍoOóOõÕôÔuUúÚ":
            vogais += 1

    return vogais

st = input("Digite uma string: ")
print(f"Quantidade de vogais na string digitada: {conta_vogais(st)}")