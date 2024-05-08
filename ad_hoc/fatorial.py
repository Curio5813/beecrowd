from math import factorial


def fatorial():
    """
    O fatorial de um número inteiro positivo N, denotado por N!, é
    definido como o produto dos inteiros positivos menores do que
    ou iguais a N. Por exemplo 4! = 4 × 3 × 2 × 1 = 24.

    Dado um inteiro positivo N, você deve escrever um programa para
    determinar o menor número k tal que N = a1! + a2! + ... + ak!,
    onde cada ai, para 1 ≤ i ≤ k, é um número inteiro positivo.

    Por exemplo, para N = 10 a resposta é 3, pois é possível escrever
    N como a soma de três números fatoriais: 10 = 3! + 2! + 2!. Para
    N = 25 a resposta é 2, pois é possível escrever N como a soma de
    dois números fatoriais: 25 = 4! + 1!.

    Entrada
    A entrada consiste de uma única linha que contém um inteiro N
    (1 ≤ N ≤ 105).

    Saída
    Seu programa deve produzir uma única linha com um inteiro representando
    a menor quantidade de números fatoriais cuja soma é igual ao valor de N.
    :return:
    """
    n = int(input())
    fatoriais, soma, cont = [], 0, 0
    for i in range(n + 1):
        fat = factorial(i)
        if fat >= n:
            break
        else:
            fatoriais.append(fat)
    fatoriais.reverse()
    for i in range(0, len(fatoriais)):
        while soma < n:
            soma += fatoriais[i]
            cont += 1
            if soma == n:
                return print(cont)
        else:
            soma -= fatoriais[i]
            cont -= 1


fatorial()
