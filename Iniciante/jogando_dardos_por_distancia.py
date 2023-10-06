def jogando_dardos_por_distancia():
    """
    João e Maria criaram sua própria versão de jogar dardos,
    dardos por distância. Cada um joga 3 dardos, escolhendo
    qual distância irão jogar do alvo. No jogo normal de dardos,
    se pontua um número pela distância entre onde o dardo acertou
    e o centro do alvo. No jogo de João e Maria se pontua x × d
    onde d é a distancia do atirador e o alvo. Na entrada a primeira
    linha consite em um número N de casos de teste. Em cada caso
    de teste haverão 6 linhas, onde as primeiras 3 linhas correspondem
    aos arremessos de João e as próximas 3 linhas aos arremessos
    de Maria. Cada linha de um caso de teste consiste em dois
    números X e D onde X é a pontuação e D é a distância. A Saída
    consiste no vencedor de cada caso de teste.
    :return:
    """
    n = int(input())
    cont, joao, maria = 0, 0, 0
    while cont < n:
        for i in range(3):
            x, d = map(int, input().split(" "))
            joao += x * d
        for i in range(3):
            x, d = map(int, input().split(" "))
            maria += x * d
        if joao > maria:
            print("JOAO")
        elif maria > joao:
            print("MARIA")
        cont += 1
        joao = 0
        maria = 0


jogando_dardos_por_distancia()
