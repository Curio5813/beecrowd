def corrida3():
    """
    A Federação de Corridas de Charrete (FCC) organiza todo ano a Subida
    Brigite Cardoso (SBC), disputada nas ladeiras de paralelepípedo de
    Ouro Preto. A corrida é uma das mais tradicionais do esporte, completando
    100 anos em 2013. Para comemorar o centenário, a FCC pretende integrar
    dispostivos GPS às charretes, permitindo aos espectadores desfrutarem de
    dados de telemetria em tempo real.

    No mesmo viés de inovação tecnológica, a FCC transmitirá a SBC via satélite
    para todo o planeta, e quer integrar a telemetria na transmissão, indicando
    qual seria o vencedor da corrida se as charretes mantivessem suas velocidades
    até o final da corrida; ela pediu que você escrevesse um programa que, dados
    as distâncias até a linha de chegada, as velocidades e os números das duas
    charretes que lideram a corrida, determina quem seria o vencedor da corrida
    (você pode supor que as charretes não cruzam a linha de chegada simultaneamente).

    Entrada
    A entrada consiste de duas linhas; cada linha descreve uma das charretes que
    lidera a corrida. A descrição de uma charrete consiste de três inteiros N (1 ≤ N ≤ 99),
    D (0 < D ≤ 1000) e V (0 < V ≤ 50) indicando, respectivamente, o número da charrete,
    a sua distância à linha de chegada em metros, e a sua velocidade, em quilômetros
    por hora. Os números das duas charretes são distintos.

    Saída
    Imprima uma única linha, contendo um único número inteiro, indicando o número da
    charrete que seria vencedora, conforme descrito acima.
    :return:
    """
    n1, d1, v1 = map(int, input().split(" "))
    n2, d2, v2 = map(int, input().split(" "))
    t1 = d1 / v1
    t2 = d2 / v2
    if t1 < t2:
        print(n1)
    elif t2 < t1:
        print(n2)


corrida3()
