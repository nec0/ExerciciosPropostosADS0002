"""
Exercício 11. Escreva um programa que recebe um inteiro positivo par n maior ou igual
a 4 e exibe na tela dois números primos cuja soma é igual a n.
"""

n = int(input())
n1EhPrimo = False
n2EhPrimo = False
n1 = 1
n2 = 1

while (not n1EhPrimo) or (not n2EhPrimo):
    n1 += 1
    n1EhPrimo = True
    for i in range(2, n1): #testa se n1 é primo
        if n1 % i == 0:
            n1EhPrimo = False
            break
    if not n1EhPrimo:
        continue #retorna para o inicio do while n += 1

    n2 = n - n1 #n1 + n2 = n
    n2EhPrimo = True
    for i in range(2, n2): #testa se n2 é primo
        if n2 % i == 0:
            n2EhPrimo = False
            break

print(f"{n1} e {n2} são primos, e n1 + n2 = {n1 + n2}")


