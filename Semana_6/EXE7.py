"""
Exercício 7. Escreva um programa que recebe um inteiro positivo e imprime na tela quantos divisores ímpares ele tem.
"""

n = int(input("Digite um inteiro positivo: "))

if n > 0:
    divisores = 0
    for divisor in range(1, n+1, 2): #com o passo 2, divisor recebe valores impares
        if n % divisor == 0:
            divisores += 1

    print(divisores)

else:
    print(f"{n} nao é um inteiro positivo!")
