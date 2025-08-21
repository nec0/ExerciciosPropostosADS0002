"""
Exercício 7. Faça um programa que recebe inteiros n e, depois disso, uma lista com n
inteiros. Por fim, exibe todas as posições em que o último inteiro da lista aparece. Obs:
Esse exercício é parecido com o Exercício 3, porém, tendo que exibir todas as posições e não
apenas a quantidade de vezes.
"""

n = int(input("Digite um inteiro positivo (tamanho da lista):\n"))
lista = [0] * n

for i in range(0,n):
    lista[i] = int(input(f"Digite um inteiro positivo (lista[{i}])\n"))

posicoes = []
for j in range(0,n):
    if lista[j] == lista[n-1]:
        posicoes.append(j)

print(posicoes)