"""
Exercício 10. Escreva um programa que recebe dois inteiros maiores do que 1, a e b, e
imprime na tela todos os números primos entre a e b (incluindo a e b se forem primos).
"""

a = int(input("Digite um inteiro positivo maior do que 1: "))
b = int(input("Digite um inteiro positivo maior do que 1: "))

if a > 1 and b > 1:
    for numero in range(a, b + 1):  # percorre todos os numeros no intervalo (a <= numero <= b)
        ehPrimo = True
        for divisor in range(2, numero): #testa se o numero é primo, dividindo por todos os numeros entre "2" até o próprio "numero"
            if numero % divisor == 0:
                ehPrimo = False
                break
        if ehPrimo:
            print(f"{numero} é primo!")

else:
    print("Algum dos dois números não seguem o critério de entrada!")