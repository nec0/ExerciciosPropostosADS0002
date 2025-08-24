"""
Exercício 9. Crie um programa que receba um texto do usuário e aplique uma compactação
simples. Ele deve possuir as seguintes funções:
• remover_espacos que recebe uma string e retorna outra igual a que recebeu, mas
sem os espaços em branco;
• remover_vogais que recebe uma string e retorna outra igual a que recebeu, mas sem
as suas vogais (maiúsculas e minúsculas);
• compactar que recebe uma string e retorna outra igual a que recebeu porém sem
espaços e nem vogais. Essa função deve usar as funções remover_espacos e remover_vogais.
Usando essas três funções, o seu programa deve receber uma string do usuário e exibir na
tela a string sem espaços na primeira linha, sem vogais na segunda linha e completamente
compactada na terceira linha.
"""

def remover_espacos(s):
    texto = s.replace(" ", "")
    return texto

def remover_vogais(s):
    texto = s
    texto_semvogais = ""
    for i in range(0, len(texto)):
        if texto[i] in "aAáÁàÀãÃâÂeEéÉiIíÍoOóOõÕôÔuUúÚ":
            continue
        else:
            texto_semvogais += texto[i]
    return texto_semvogais

def compactar(s):
    return remover_espacos(remover_vogais(s))

# string_teste = "  Para remover um item com valor especificado, use o metodo  "

texto = input("Digite um texto:\n")
print(f"{remover_espacos(texto)}\n{remover_vogais(texto)}\n{compactar(texto)}")