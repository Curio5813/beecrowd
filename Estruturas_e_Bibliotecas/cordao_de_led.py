def cordao_de_led():
    """
    Mariazinha quer montar sua árvore de Natal com os cordões de led
    comprados no ano passado. O problema é que sua irmã caçula acabou
    cortando estes cordões em vários pedaços.

    Mariazinha quer saber se após unir estes pedaços (enumerados com uma
    etiqueta por ela de 1 até N) o cordão está totalmente unido ou não,
    pois se faltar unir algum dos segmentos, as luzes do cordão de led
    não irão funcionar.

    Escreva um programa que, dada uma série de ligações entre segmentos de
    cordões de led, indique se o cordão estará Completo ou Incompleto.

    Entrada
    A primeira linha da entrada contém dois inteiros N e L, indicando o número
    de segmentos de cordão de Led e o número de ligações efetuadas (1 ≤ N ≤ 100,
    1 ≤ L ≤ 100). Os números de cada um dos N segmentos, inicialmente, são os
    inteiros de 1 até N.

    Cada uma das L linhas seguintes irá conter 2 números X e Y, indicando que
    Mariazinha está ligando estes 2 segmentos (X e Y). As ligações serão sempre
    realizadas entre pedaços de cordões de led diferentes.

    Saída
    Seu programa deve imprimir a mensagem 'COMPLETO' indicando que os segmentos
    de cordão de led foram todos unidos ou ou 'INCOMPLETO' no caso de algum segmento
    daquele cordão não ter sido ligado.
    :return:
    """
    n, l = map(int, input().split())
    pedacos = []
    for i in range(l):
        pedaco = sorted(list(map(int, input().split())))
        pedacos.append(pedaco)
    flag = False
    i, j = 0, 1,
    while True:
        while i < len(pedacos):
            # print(pedacos)
            if pedacos[i][1] == pedacos[j][0] and pedacos[j][1] != n:
                pedacos[i] = pedacos[j]
                # print(pedacos)
                i = 0
                j = 1
                continue
            elif pedacos[i][1] == pedacos[j][0] and pedacos[j][1] == n:
                # print(pedacos)
                flag = True
                break
            j += 1
            if j > len(pedacos) - 1:
                break
        i += 1
        if flag:
            print("COMPLETO")
            break
        if j > len(pedacos) - 1:
            break
    if not flag:
        print("INCOMPLETO")


if __name__ == '__main__':
    cordao_de_led()

"""
4 3
1 2
1 3
2 4

6 4
1 2
3 4
5 6
2 3
"""
