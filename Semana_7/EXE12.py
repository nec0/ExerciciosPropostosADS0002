"""
Exercício 12. Faça um programa que recebe inteiros n e m e uma matriz n × m e imprime
se a matriz é de permutação ou não. Obs: uma matriz é de permutação se ela é uma
matriz quadrada e se cada linha e coluna é composta apenas por zeros, exceto por um único
elemento igual a 1.
"""
# matDePermutacao= [[1,0,0,0],
#                   [0,0,1,0],
#                   [0,0,0,1],
#                   [0,1,0,0]]

n = int(input("Digite o número de linhas:\n"))
m = int(input("Digite o número de colunas:\n"))

#criando a matriz n x m
matriz = [0] * n
for i in range(0, n):
    matriz[i] = [0] * m

#recebe os valores da matriz
for i in range(0,n): #recebe os valores da matriz
    for j in range(0, n):
        matriz[i][j] = input(f"Digite o elemento [{i},{j}]: ")

ehPermutacao = True
if n != m: #testa se a mariz é quadrada
    ehPermutacao = False

else:
    # compara cada linha e verifica se existe um elemento 1 e todos os outros são 0s
    linhaPermutavel = True
    for i in range(0, n):
        if linhaPermutavel: #controle para caso uma linha não seja permutavel o programa interrompe a estrutura de repetição
            temApenasUm1_linha = False
            for j in range(0, m):
                if matriz[i][j] == 1 and not temApenasUm1_linha: #o if pode ser verdadeiro apenas uma vez
                    temApenasUm1_linha = True
                elif matriz[i][j] != 0: #o restante tem que ser zero, caso seja diferente a linha não é permutavel
                    linhaPermutavel = False
                    break

    if linhaPermutavel: #se o teste da linha for False, a matriz não é permutável
        # compara cada coluna e verifica se existe um elemento 1 e todos os outros são 0s
        colunaPermutavel = True
        for i in range(0, m):
            if colunaPermutavel: #controle para caso uma linha não seja permutavel o programa interrompe a estrutura de repetição
                temApenasUm1_coluna = False
                for j in range(0, n):
                    if matriz[j][i] == 1 and not temApenasUm1_coluna: #o if pode ser verdadeiro apenas uma vez
                        temApenasUm1_coluna = True
                    elif matriz[j][i] != 0: #o restante tem que ser zero, caso seja diferente a linha não é permutavel
                        colunaPermutavel = False
                        break
    else:
        ehPermutacao = False

print(f"Matriz {n} x {m} é de permutação: {ehPermutacao}")