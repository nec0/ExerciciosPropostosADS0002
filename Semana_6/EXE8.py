"""
Exercício 8. Escreva um programa que recebe um inteiro positivo n e imprime todas as
somas iguais a n de 2 números inteiros positivos distintos sem repetição. Por exemplo, se
n = 4, há somente 2 somas: 1 + 3, 3 + 1, pois 2 + 2 seria a soma de dois números iguais; e,
se n = 5, há 4 somas: 1 + 4, 2 + 3, 3 + 2 e 4 + 1.
"""

n = int(input("Digite um inteiro positivo: "))

if n > 0:
    for x in range(1, n):
        for y in range(1, n):
            if x != y and x + y == n:
                print(f"{x} + {y} = {n}")

else:
    print(f"{n} nao é um inteiro positivo!")