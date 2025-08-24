"""
Exercício 8. Escreva um programa que possua as seguintes funções:
• media que recebe uma lista de floats e retorna a média deles;
• acima_da_media que recebe uma matriz n × 2, em que cada linha contém o nome
de um aluno (string) e sua respectiva nota (float). A função deve retornar uma nova
matriz contendo apenas os pares (nome, nota) dos alunos cuja nota seja estritamente
maior que a média de todas as notas presentes na matriz original. Essa função deve
usar a função media e não deve modificar a matriz original com as informações dos
alunos

O seu programa deve receber um inteiro n e, depois disso, o nome de n alunos juntamente
com as suas notas. Use a função acima_da_media para determinar quais foram os alunos
que possuem nota maior do que a média. O seu programa deve exibir na tela esses alunos,
sendo um por linha formatado da seguinte forma: “Nome - nota”.
"""

def media(lista):
    mediaDeLista = 0
    for i in range(0, len(lista)):
        mediaDeLista += lista[i]

    mediaDeLista = mediaDeLista / len(lista)
    return mediaDeLista

def acima_da_media(listaDeAlunos):
    listaDeNotas = []
    for i in range(0, len(listaDeAlunos)):
        listaDeNotas.append(listaDeAlunos[i][1])
    mediaNotasAlunos = media(listaDeNotas)

    alunosAcimaDaMedia = []
    for i in range (0, len(listaDeAlunos)):
        if listaDeAlunos[i][1] > mediaNotasAlunos:
            alunosAcimaDaMedia.append(listaDeAlunos[i])

    return mediaNotasAlunos, alunosAcimaDaMedia

n = int(input("Digite um número inteiro: "))
lista_alunosEnotas = [0]*n

for i in range(0, len(lista_alunosEnotas)):
    nomeAluno = input(f"Digite o nome do aluno ({i+1}): ")
    notaAluno = float(input(f"Digite o nota do aluno ({i+1}): "))
    lista_aluno = [nomeAluno, notaAluno]
    lista_alunosEnotas[i] = lista_aluno

# #Lista para teste de código
# listaAlunosTeste = [["aluno1", 7],
#                     ["aluno2", 7],
#                     ["aluno3", 7],
#                     ["aluno4", 7],
#                     ["aluno5", 3]]

print(f"Média dos alunos: {acima_da_media(lista_alunosEnotas)[0]}")
print(f"Lista de alunos acima da media:\n{acima_da_media(lista_alunosEnotas)[1]}")