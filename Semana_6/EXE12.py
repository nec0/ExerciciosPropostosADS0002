"""
Exercício 12. Escreva um programa que recebe um inteiro positivo n e exibe na tela
todas as triplas pitagóricas (a, b, c) tais que a, b, c ≤ n, ou seja, todas as triplas ordenadas
de inteiros positivos (a, b, c) tais que a**2 + b**2 = c**2, onde a, b, c ≤ n. Note que as triplas são
ordenadas e, portanto, a tripla pitagórica (3, 4, 5) é diferente da tripla pitagórica (4, 3, 5).
"""

n = int(input("Digite um inteiro positivo: "))

if n > 0:
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if ((a ** 2) + (b ** 2) == (c ** 2)):
                    print(f"({a}, {b}, {c})")

else:
    print(f"{n} nao é um inteiro positivo!")