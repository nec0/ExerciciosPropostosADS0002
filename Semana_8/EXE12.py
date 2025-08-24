"""
Exercício 12. Escreva um programa que possui a função tamanho, a qual recebe uma
lista e retorna o seu tamanho sem utilizar a função len(). O seu programa deve receber
um vetor de strings do usuário, recebendo valores até que seja digitado a string vazia. O
programa deve guardar as strings em uma lista (a string vazia não deve fazer parte da lista),
e, usando a função tamanho, determinar quantos valores foram digitados.
"""

def tamanho(lista):
    tamanho = 0
    for i in lista:
        tamanho += 1
    print(tamanho)

vetorStrings = []
while True:
    txt = str(input("Digite uma string: "))
    if txt == "":
        tamanho(vetorStrings)
        break
    else:
        vetorStrings.append(txt)
        print(vetorStrings)