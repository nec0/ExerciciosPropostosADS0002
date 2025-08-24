"""
Exercício 10. Escreva um programa que receba do usuário um inteiro e exiba na tela o seu
último dígito. O programa deve tratar o possível erro de o usuário não digitar um inteiro,
exibindo a mensagem “Entrada inválida” e finalizando.
"""

try:
    n = int(input("Digite um inteiro: "))
    numero = str(n)
    print(numero[len(numero) - 1])

except ValueError:
    print("Entrada inválida")