"""
Exercício 9. Faça um programa que recebe um inteiro n ≥ 2 e, após isso, uma sequência
de n inteiros, e exibe na tela a quantidade de inversões da lista. Obs: uma inversão de uma
lista são dois índices da lista (i, j) tal que i < j e o valor no índice i é maior do que o valor
no índice j.
Por exemplo, suponha que a lista é: [9, 2, 9, 5, 7]. Temos as seguintes inversões (lembrando
que o índice do primeiro elemento é 0): (0, 1),(0, 3),(0, 4),(2, 3) e (2, 4). Portanto, como são
5 inversões ao Tod0 o programa deve exibir o valor 5.
"""

n = int(input("Digite um inteiro (tamanho da sequência) positivo maior ou igual a 2:\n"))
lista = []

for i in range(0, n):
    numero = int(input("Digite um inteiro: "))
    lista.append(numero)

inversoes = 0
for i in range(0, len(lista) - 1):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            inversoes += 1

print(inversoes)