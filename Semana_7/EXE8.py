"""
Exercício 8. Faça um programa que recebe uma sequência de inteiros até que receba o
inteiro zero (zero não faz parte da sequência), e exiba na tela a maior distância dentre todas
as distâncias entre cada número da sequência e o último número da sequência.
Por exemplo, suponha que a sequência foi: [2, 10, 9, 5, 7]. Temos que 2 está a distância 5 de
7; 10 está a distância 3 de 7; 9 está a distância 2 de 7; 5 está a distância 2 de 7; e 7 está a
distância 0 de 7. Dentre todas essas distâncias, a maior distância é 5. Portanto, o programa
deve exibir 5 na tela.
"""

continuar = True
lista = []
while continuar:
    n = int(input("Digite um inteiro:\n"))

    if n == 0:
        continuar = False
        break
    else:
        lista.append(n)
print(lista)

maior = 0
for i in range(0, len(lista)):
    diferenca = abs(lista[i] - lista[len(lista) - 1])
    if diferenca > maior:
        maior = diferenca

print(maior)


