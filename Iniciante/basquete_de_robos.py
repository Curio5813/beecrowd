def basquete_de_robo():
    """
    Esta função calcula a quantidade de pontos feita pelo os
    robos, sabendo a distânica do arremeso. Cada distância de
    arremeso tem uma pontuação. Se d <= 800 cm, a cesta vale 1
    ponto, 800 < d <= 1400, vale 2 pontos e se 1400 < d <= 2000,
    a cesta vale 3 pontos.
    :return:
    """
    d = int(input())
    if d <= 800:
        print(1)
    elif 800 < d <= 1400:
        print(2)
    elif 1400 < d <= 2000:
        print(3)


basquete_de_robo()
