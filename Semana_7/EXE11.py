"""
Exercício 11. Faça um programa que recebe inteiros n e m e uma matriz n × m e imprime
a quantidade de linhas e colunas nulas. Obs: uma linha ou coluna de uma matriz é nula se
todos os seus elementos são iguais a zero.
"""

# matrizNula = [[1,0,0,0],
#                [0,0,1,0],
#                [0,0,0,1],
#                [0,1,0,0]]

n = int(input("Digite o número de linhas:\n"))
m = int(input("Digite o número de colunas:\n"))
colunaLinhaNulas = 0

#criando a matriz n x m
matriz = [0] * n
for i in range(0, n):
    matriz[i] = [0] * m

#recebe os valores da matriz
for i in range(0,n): #recebe os valores da matriz
    for j in range(0, n):
        matriz[i][j] = input(f"Digite o elemento [{i},{j}]: ")

#compara cada linha e verifica se é nula
linhaNula = True
for i in range(0, n):
    for j in range(0, m):
        if matriz[i][j] != 0:
            linhaNula = False
            break
    if linhaNula:
        colunaLinhaNulas += 1

#compara cada coluna e verifica se é nula
colunaNula = True
for i in range(0, m):
    for j in range(0, n):
        if matriz[j][i] != 0:
            colunaNula = False
            break
    if colunaNula:
        colunaLinhaNulas += 1

print(colunaLinhaNulas)