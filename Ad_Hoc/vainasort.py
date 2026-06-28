from copy import deepcopy


def vainasort():
    """
    O Professor Odracir Snitram estudava vários métodos de ordenação,
    assim como as suas respectivas complexidades. Um dia, ele resolve
    fazer um teste, criando um método, com uma caixa e N pedras, numeradas
    de 1 a N. A ideia era sortear todas as pedras, uma de cada vez, de modo
    que a sequência de números sorteados fosse exatamente de 1 a N, ou seja,
    sorteando o número 1 primeiro, depois o número 2, depois o 3, e assim
    sucessivamente, até sortear o último, que seria N. Após sortear tudo,
    caso a tentativa não desse certo, todas as pedras eram devolvidas na
    caixa, e o sorteio recomeçava até dar certo. Esse método foi nomeado de
    VaiNaSort!

    Escreva um programa que, dada a quantidade de pedras, e de todas as tentativas
    até sortear corretamente, contabilize as tentativas.

    Entrada
    A entrada possui vários casos de teste. Cada um começa com um número inteiro N
    (2 ≤ N ≤ 10000), representando a quantidade de pedras na caixa. Em seguida, haverá
    algumas tentativas de sorteio, cada uma formada com os números de 1 a N, em uma ordem
    qualquer, até se conseguir a ordem esperada. A entrada finaliza com N = 0.

    Saída
    Para cada caso de teste, imprima o total de tentativas.
    :return:
    """
    while True:
        n = int(input())
        entradas, lista, cont = [], [], 1
        if n == 0:
            break
        else:
            entrada = list(map(int, input().split(" ")))
            lista = deepcopy(entrada)
            lista.sort()
            if entrada == lista:
                print(cont)
            else:
                while entrada != lista:
                    entrada = list(map(int, input().split(" ")))
                    cont += 1
                else:
                    print(cont)


vainasort()
