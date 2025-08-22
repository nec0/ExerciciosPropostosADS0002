"""
Exercício 10. Faça um programa que recebe inteiros n e uma matriz n × n e verifica se
os elementos na diagonal principal são iguais aos elementos da diagonal secundária. Obs:
A diagonal principal de uma matriz quadrada (número de linhas é igual ao de colunas)
consiste nos elementos partindo do elemento superior esquerdo ao elemento inferior direito.
A diagonal secundária de uma matriz quadrada consiste nos elementos partindo do elemento
superior direito ao elemento inferior esquerdo.
"""

n = int(input("Digite um valor inteiro positivo"))
matriz = [0]*n

for i in range(0, n): #cria a matriz quadrada
    matriz[i] = [0]*n

for i in range(0,n): #recebe os valores da matriz
    for j in range(0, n):
        matriz[i][j] = input(f"Digite o elemento [{i},{j}]: ")

diagonalPrincipal = [0]*n
diagonalSecundaria = [0]*n
for i in range(0, n): #retorna os valores de cada diagonal para sua respectiva lista
    diagonalPrincipal[i] = matriz[i][i]
    diagonalSecundaria[i] = matriz[i][n - 1 - i]

print(diagonalPrincipal == diagonalSecundaria)