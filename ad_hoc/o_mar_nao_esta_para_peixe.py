from math import floor


def o_mar_nao_esta_para_peixe():
    """
    Em um arquipélago no meio do Oceano Pacífico a economia
    é regida pela pesca, pois o peixe é o principal alimento
    disponível. Ultimamente, a população desse arquipélago tem
    aumentado drasticamente, o que levou a um grande aumento
    da pesca, e, consequentemente, a problemas.

    Neste arquipélago, cada pescador vai diariamente ao alto mar
    com a intenção de conseguir trazer o maior número de peixes para
    o seu vilarejo. Com a expansão da pesca, os pescadores estão começando
    a jogar suas redes de pesca por cima das de outros pescadores.
    Com isso, os pescadores perdem, pois apenas o primeiro pescador
    pega os peixes da intersecção entre as redes.

    A Associação dos Pescadores da ilha decidiu fazer um levantamento
    para descobrir quanto do mar está de fato sendo aproveitado, ou seja,
    qual a área do mar que está coberta por pelo menos uma rede de pesca.

    Como há muitas intersecções entre as redes de pesca, é muito difícil
    para a associação calcular a área total da região coberta pelas redes.
    Por este motivo, eles pediram para que você escrevesse um programa para
    resolver este problema.

    Como é muito difícil navegar pelo mar, os pescadores sempre jogam as redes
    de forma que as regiões cobertas por cada rede são sempre retângulos com
    lados paralelos aos eixos, se imaginarmos o mar como um plano cartesiano.

    Entrada
    A primeira linha da entrada possui um inteiro N (1 ≤ N ≤ 100)indicando o número
    de redes que foram lançadas. As próximas N linhas descrevem as regiões cobertas
    pelas redes: cada uma contém quatro inteiros Xi e Xf , Yi e Yf  (1 ≤ Xi ≤ Xf ≤100)
    e (1 ≤ Yi ≤ Yf ≤ 100). A região coberta pela rede em questão contém todo ponto (X,Y)
    tal que Xi ≤ X ≤ Xf e Yi ≤ Y ≤ Yf.

    Saída
    A saída deve conter apenas uma linha contendo a área da região do mar realmente
    aproveitada pelos pescadores, ou seja, a área total da região do mar coberta por
    pelo menos uma rede de pesca.
    :return:
    """
    n = int(input())
    coordenadas_x, coordenadas_y, area = [], [], 0
    for i in range(n):
        x1, x2, y1, y2 = map(int, input().split(" "))
        coordenadas_x.append(x1)
        coordenadas_x.append(x2)
        coordenadas_y.append(y1)
        coordenadas_y.append(y2)
    coordenadas_x.sort()
    coordenadas_y.sort()
    base = coordenadas_x[-1] - coordenadas_x[0]
    altura_menor = coordenadas_y[1] - coordenadas_y[0]
    altura_maior = coordenadas_y[-1] - coordenadas_y[0]
    base_maior = coordenadas_x[-1] - coordenadas_x[0]
    base_menor = coordenadas_x[1] - coordenadas_x[0]
    print(altura_maior)
    print(altura_menor)
    print(base_maior)
    print(base_menor)


o_mar_nao_esta_para_peixe()
