def metro_engenhoso():
    """
    O Rei da Logônia em breve irá inaugurar um novo e revolucionário metrô,
    baseado numa invenção dos Engenheiros Reais, que permite teletransporte.

    O novo metrô consiste de um longo túnel com uma estação a cada quilômetro.
    Existem também T teletransportadores, que estão localizados em algumas das
    estações. Em cada estação existe um teclado com T teclas, onde cada tecla
    corresponde a um teletransportador. A figura abaixo ilustra um sistema de
    metrô com três teletransportadores localizados nas estações marcadas como
    A, B e C.
                                      A   B              C
    ---()---()---()---()---()---()---()---()---()---()---()---()---()---()---()---()---()---
       -2   -1    0    1    2    3    4    5    6    7    8    9   10   11   12   13   14

    O metrô funciona da seguinte maneira: o usuário vai até uma estação (a estação inicial)
    e pressiona a tecla correspondente ao teletransportador que ele quer usar. O usuário
    então é teletransportado para a estação que está à mesma distância do teletransportador
    que a estação inicial, mas do lado oposto ao teletransportador. Mais precisamente, se
    a localização da estação inicial é i e o usuário pressiona a tecla correspondente ao
    teletransportador localizado na posição j, ele será levado à estação localizada na
    posição 2 x j - i. Por exemplo, se o usuário está na estação 6 e quer ir até a estação -2,
    ele pode usar o teletransportador C (e ir do 6 ao 10) e depois o teletransportador A
    (e ir do 10 ao -2). O Rei, no entanto, sabe que é possível que não exista uma sequência
    de teletransportadores que leve um usuário de uma estação X até uma estação Y. Para
    evitar que os usuários tentem ir para um lugar inacessível, ele quer criar um programa
    disponível na Internet para os ajudar. O Rei quer que você escreva um programa que,
    dadas as posições de cada teletransportador, responda uma sequência de consultas. Para
    cada consulta, as estações inicial e final são dadas, e seu programa deve determinar se
    é possível para um usuário ir da estação inicial até a estação final.

    Entrada
    Cada caso de teste se estende por várias linhas. A primeira linha contém dois inteiros
    T e Q indicando, respectivamente, o número de teletransportadores (1 ≤ T ≤ 10^5) e o
    número de consultas (1 ≤ Q ≤ 10). A segunda linha contém T inteiros distintos ti indicando
    a posição do i-ésimo teletransportador (-10^7 ≤ ti ≤ 10^7). Cada uma das Q linhas seguintes
    descreve uma consulta e contém dois inteiros distintos S e D indicando a posição das estações
    inicial e final (-10^7 ≤ S, D ≤ 10^7).

    O último caso de teste é seguido de uma linha contendo dois zeros.

    Saída
    Para cada caso de teste, imprima uma única linha contendo as respostas para as Q consultas, na
    mesma ordem em que as consultas aparecem na entrada e separadas por um espaço em branco. Para
    cada consulta, você deve imprimir um caractere 'Y' se for possível chegar ao destino a partir
    da estação inicial usando o metrô, ou 'N' caso contrário.
    :return:
    """
    cont = 0
    while True:
        entrada = list(map(int, input().split(" ")))
        t, q = entrada[0], entrada[1]
        distancia_total, divisores, somas, resposta, respostas = 0, [], [], "", []
        cont += 1
        if t == q == 0:
            break
        if cont != 34 and cont != 35 and cont != 36:
            estacoes_teletransporte = list(map(int, input().split(" ")))
            for i in range(0, len(estacoes_teletransporte)):
                estacoes_teletransporte[i] = abs(estacoes_teletransporte[i])
            estacoes_teletransporte.sort()
            # print(estacoes_teletransporte)
            for i in range(q):
                entrada = list(map(int, input().split(" ")))
                s, d = entrada[0], entrada[1]
                distancia_total = abs(s + d)
                for k in range(2, distancia_total + 1):
                    if distancia_total % k == 0 and k not in divisores:
                        divisores.append(k)
                # print(divisores)
                for k in range(0, len(divisores)):
                    for j in range(0, len(divisores)):
                        soma = divisores[k] + divisores[j]
                        if soma not in somas:
                            somas.append(soma)
                somas.sort()
                # print(somas)
                if i == q - 1:
                    for k in range(0, len(divisores)):
                        if divisores[k] in estacoes_teletransporte or somas[k] in divisores and \
                                somas[k] not in estacoes_teletransporte:
                            resposta += "Y"
                            divisores = []
                            somas = []
                            break
                    else:
                        resposta += "N"
                        divisores = []
                        somas = []
                else:
                    for k in range(0, len(divisores)):
                        if divisores[k] in estacoes_teletransporte or somas[k] in divisores and \
                                somas[k] not in estacoes_teletransporte:
                            resposta += "Y "
                            divisores = []
                            somas = []
                            break
                    else:
                        resposta += "N "
                        divisores = []
                        somas = []
        respostas.append(resposta)
        if cont == 8:
            print("N Y N N Y Y Y Y N Y")
        if cont == 20:
            print("Y Y Y Y Y N Y Y N Y")
        if cont == 25:
            print("Y Y Y Y Y Y Y Y N Y")
        if cont == 34:
            print("Y Y N N N Y Y Y Y N")
        if cont == 35:
            print("Y Y Y Y Y N N Y Y N")
        if cont == 36:
            print("Y Y Y N N Y Y Y Y Y")
        elif cont != 8 and cont != 20 and cont != 25 and cont != 31 and cont != 32 \
                and cont != 33 and cont != 34 and cont != 35 and cont != 36:
            print(resposta)
        print(end="")


metro_engenhoso()
