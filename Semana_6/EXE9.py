"""
Exercício 9. Escreva um programa que recebe um inteiro positivo n e exibe, sem repetição,
todas as duplas de inteiros maiores ou iguais a 2 e menores ou iguais à n de números coprimos,
ou seja, duplas de números cujo único divisor em comum é o 1. Por exemplo, para n = 5,
temos 5 duplas: {2, 3}, {2, 5}, {3, 4}, {3, 5} e {4, 5}. Note que, por exemplo, a dupla de
coprimos {2, 3} e {3, 2} são a mesma e, portanto, apenas uma das duas pode ser exibida
"""

n = int(input("Digite um inteiro positivo: "))

if n > 0:
    for n1 in range(2, n + 1):
        for n2 in range(n1+1, n + 1): #n2 sempre maior que n1 para que não tenha duplas repetiras {2, 3} e {3, 2} por exemplo
            coPrimos = True
            for i in range(2, n1 + 1): #verifica se são coprimos, dividindo n1 e n2 por todos os divisores até n1
                if (n1 % i == 0) and (n2 % i == 0):
                    coPrimos = False #nao sao coprimos, pois i é divisor de n1 e n2
                    break #sai da estrutura de repetição do laço que ele está imediatamente
            if coPrimos:
                print(f"{n1}, {n2}")

else:
    print(f"{n} nao é um inteiro positivo!")