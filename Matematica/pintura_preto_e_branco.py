from math import ceil, floor


def pintura_preto_e_branco():
    """
    Você está visitando o Centro Pompidou que contém muitas pinturas
    modernas. Em particular você nota que uma pintura consiste somente
    em quadrados pretos e brancos, arranjados em linhas e colunas como
    em um tabuleiro de xadrez(sem que quadrados adjacentes tenham a mesma
     cor).

    Já que você está entediado, você se pergunta quantos tabuleiros de xadrez
    8 x 8 formam a pintura. O canto inferior direito do tabuleiro de xadrez
    tem que ser branco.

    Entrada
    A entrada contém vários casos de teste. Cada caso de teste consiste em uma
    linha com três inteiros n, m e c.(8 ≤ n, m ≤ 40000), onde n é o número de
    linhas do quadro, e m é o número de colunas do quadro. c é sempre 0 ou 1,
    onde 0 indica que o canto inferior da pintura é preto, e 1 indica que este
    canto é branco.

    O último caso de teste é seguido por uma linha composta por três zeros.

    Saída
    Para cada caso de teste, imprima o número de tabuleiros de xadrez contidos dentro
    da dada pintura.
    :return:
    """
    while True:
        n, m, c = map(int, input().split(" "))
        if n == m == c == 0:
            break
        else:
            if n == 8 and m == 8 and c == 0:
                print(0)
            elif n == 8 and m == 8 and c == 1:
                print(1)
            else:
                if n % 2 == 0 and m % 2 == 0:
                    if c == 1:
                        tabuleiros = ceil((n - 7) * (m - 7) / 2)
                        print(tabuleiros)
                    if c == 0:
                        tabuleiros = floor((n - 7) * (m - 7) / 2)
                        print(tabuleiros)
                else:
                    tabuleiros = int((n - 7) * (m - 7) / 2)
                    print(tabuleiros)


pintura_preto_e_branco()
