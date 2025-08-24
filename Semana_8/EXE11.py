"""
Exercício 11. Implemente uma função de leitura de inteiros positivos robusta. Ela deve se
charmar ler_positivo e deve:
• Solicitar um número inteiro positivo do usuário;
• Se o número não for inteiro, ou não for positivo, a função deve exibir uma mensagem
de erro específica para cada um desses dois casos e pedir novamente o dado ao usuário;
• Se o usuário digitar um inteiro positivo, a função deve retorná-lo.
Escreva um programa que use a função ler_positivo para retornar a soma de dois inteiros
positivos.
"""

def ler_positivo():
    while True:
        try:
            n = int(input("Digite um inteiro positivo: "))
            if type(n) == int and n >= 0:
                print(n)
                break
            elif n < 0:
                print("O número não é positivo")
        except ValueError:
            print("Valor inválido (não é um inteiro positivo)!\n")

ler_positivo()