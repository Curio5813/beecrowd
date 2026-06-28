from math import sqrt, floor


def musica_alta():
    """
    Marcelo Freitas de Jesus, mais conhecido como Fredinho gosta
    muito do carnaval. Durante o feriado ele pretende ouvir sua
    musica no volume mais alto possível. Entretanto, para poder
    saber qual volume ele deve levar em conta a localização da
    residência de seu vizinho Josué Braulio Petiz, que mantêm
    sempre por perto um audiodosímetro ( aparelho utilizado para
    medir a intensidade sonora em decibéis ) e chamará a policia
    caso o som passe um centésimo sequer do máximo permitido pela
    lei de Babanua. Dado o mapa simplificado da vizinhança onde F
    representa a casa de Fredinho, J a de Josué , X representa uma
    casa aleatória e cada caractere representa 10 metros (considere
    que a casa de Fredinho emite o som do centro de seu terreno e que
    Josué captura o áudio também do centro de seu terreno), o som máximo
    permitido em Babanua e considerando que o som propaga-se com perda
    de 1 % a cada metro e que o som mantêm sua intensidade nesse metro
    ( as leis da física em Babanua são diferentes, por decreto do
    presidente R.Rey) informe o volume máximo que Fredinho pode ouvir
    sua musica.

    Para calcular o valor, deve-se dividir o valor máximo permitido por
    0.99 no expoente de quantas vezes o som será reduzido. Por exemplo, no
    caso de um som máximo de 110Dbs e uma distância de 14,1421 teremos que
    o som máximo é de 110/0.9914, ou seja, 126.619.

    Entrada
    A entrada consiste de um inteiro N (0 < N < 51) indicando o número de casos,
    cada caso de testes é constituído por dois inteiros K (0< K < 201 ) e J
    ( 0 < J < 30 ) que indica a máxima intensidade sonora permitida e a quantidade
    de linhas usada no mapa. Após isso seguem J linhas (com no máximo 30 caracteres)
    representando o mapa.

    Saída
    Para cada caso de teste imprimir a intensidade máxima do som que Fredinho pode
    ouvir em sua casa sem nenhuma casa decimal , arredondando para baixo ,seguido
    de "dBs".
    :return:
    """
    n = int(input())
    while n > 0:
        k, j = map(int, input().split(" "))
        mapa = []
        for i in range(j):
            colunas = list(input())
            mapa.append(colunas)
        dist = 10
        temp, mapa_dist = [], []
        for i in range(len(mapa)):
            for m in range(len(mapa[i])):
                temp.append(dist)
                dist += 10
            dist = 10
            mapa_dist.append(temp)
            temp = []
        coord, altura, flag = [], 0, False
        for i in range(len(mapa)):
            for m in range(len(mapa[i])):
                if mapa[i][m] == 'F' or mapa[i][m] == 'J':
                    coord.append(mapa_dist[i][m])
                    flag = True
            if len(coord) == 2:
                break
            if flag:
                altura += 10
        dist_fj = int(sqrt(abs(coord[0] - coord[1]) ** 2 + altura ** 2))
        altura_maxima = floor(k / 0.99 ** dist_fj)
        print(f"{altura_maxima} dBs")
        n -= 1


if __name__ == '__main__':
    musica_alta()
