def festa_no_polo_norte():
    """
    Esta função calcula o coprimos dos duendes inumerados
    para saber onde será a festa sem que o Grinch saiba.
    Como o Grinch é tão ruim com números a ponto de nem
    saber que dois números só são chamados de coprimos se
    o MDC (máximo divisor comum) entre eles é 1, Giovana
    simplesmente envia uma carta para o polo norte com os
    números dos duendes que devem levar as comidas, e com
    isso, os duendes já conseguem descobrir onde será a festa
    de aniversário, mas o Grinch não. Dada a carta que os
    duendes receberam, determine na casa de qual Duende será
    a festa de aniversário de Giovana. A entrada a primeira
    linha contém um inteiro N (1 ≤ N ≤ 104) o qual representa
    a quantidade de números escritos na carta de Giovana. A
    segunda linha da entrada possui N números inteiros Ai (1 ≤ Ai ≤ 105)
    representando os identificadores dos duendes escritos na carta.
    A saída consiste de uma única linha contendo o número do duende que
    sediará a festa de Giovana em sua casa.
    :return:
    """
    n = int(input())
    a = map(int, input().split(" "))
    d = max(a) + 1
    print(d)


festa_no_polo_norte()
