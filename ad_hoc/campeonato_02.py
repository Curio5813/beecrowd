def campeonato_02():
    """
    O sorteio das posições dos jogadores na chave decisiva da copa do mundo de
    ping-pong está deixando a todos nervosos. É que ninguém quer pegar o jogador
    mais bem ranqueado, o Master Kung, logo nas oitavas de final, ou nas quartas
    de final. Melhor que só seja possível enfrentar Master Kung na semifinal ou
    na final! Os jogadores são identificados por números inteiros de 1 a 16, sendo
    que Master Kung é o jogador de número 1. O jogador para o qual nós estamos
    torcendo, Master Lu, tem o número 9.

    A chave possui 16 posições também numeradas de 1 a 16, como na figura abaixo. A
    organização da copa vai fazer um sorteio para definir em qual posição cada jogador
    vai iniciar a chave decisiva. Nas oitavas de final, o jogador na posição 1 enfrenta
    o jogador na posição 2; o da posição 3 enfrenta o da posição 4; e assim por diante,
    como na figura.

    [imagem] (https://resources.beecrowd.com/gallery/images/problems/UOJ_2833.png)

    O objetivo deste problema é decidir em que fase da chave os jogadores Master Kung e
    Master Lu vão se enfrentar, caso vençam todas as suas respectivas partidas antes de
    se enfrentarem. Por exemplo, se o sorteio da chave determinar a seguinte ordem de
    jogadores da posição 1 até a 16: [4, 11, 3, 2, 8, 13, 14, 5, 16, 9, 12, 6, 10, 7, 1, 15],
    eles vão se enfrentar na semifinal.

    Entrada
    A primeira e única linha da entrada contém 16 números Xi (1 ≤ Xi ≤ 16) inteiros distintos,
    de valores entre 1 e 16. Ou seja, uma permutação dos inteiros entre 1 e 16. A permutação
    define a ordem dos jogadores nas posições da chave decisiva da copa.

    Saída
    Seu programa deve produzir uma única linha contendo uma das palavras seguintes, decidindo
    a fase em que vão se enfrentar os jogadores Master Kung e Master Lu, se eles vencerem todas
    as suas partidas antes de se enfrentarem: oitavas, quartas, semifinal ou final.
    :return:
    """
    oitavas = list(map(int, input().split()))
    master_kung, master_fu, fase = 0, 0, 8
    for i in range(len(oitavas)):
        if oitavas[i] == 1:
            master_kung = oitavas.index(oitavas[i]) + 1
        if oitavas[i] == 9:
            master_fu = oitavas.index(oitavas[i]) + 1
    if master_kung < master_fu and abs(master_kung - master_fu) == 1 and master_kung in [2, 4, 6, 8, 10, 12, 14]:
        print("semifinal")
    elif master_kung > master_fu and abs(master_kung - master_fu) == 1 and master_fu in [2, 4, 6, 8, 10, 12, 14]:
        print("semifinal")
    else:
        if master_fu > master_kung > 8:
            while abs(master_kung - master_fu) > 1:
                master_kung += 1
                master_fu -= 1
                fase //= 2
        elif master_fu > master_kung <= 8:
            while abs(master_kung - master_fu) > 1:
                master_kung += 1
                master_fu -= 1
                fase //= 2
        elif master_fu < master_kung > 8:
            while abs(master_kung - master_fu) > 1:
                master_kung -= 1
                master_fu += 1
                fase //= 2
        elif master_fu < master_kung <= 8:
            while abs(master_kung - master_fu) > 1:
                master_kung -= 1
                master_fu += 1
                fase //= 2
        elif 8 < master_kung > master_fu > 8:
            while abs(master_kung - master_fu) > 1:
                master_kung -= 1
                master_fu += 1
                fase //= 2
        elif 8 < master_fu > master_kung > 8:
            while abs(master_kung - master_fu) > 1:
                master_kung += 1
                master_fu -= 1
                fase //= 2
        elif master_fu > master_kung <= 8:
            while abs(master_kung - master_fu) > 1:
                master_kung += 1
                master_fu -= 1
                fase //= 2
        elif master_kung > master_fu <= 8:
            while abs(master_kung - master_fu) > 1:
                master_kung -= 1
                master_fu += 1
                fase //= 2
        if fase == 0:
            print("final")
        elif fase == 2:
            print("semifinal")
        elif fase == 4:
            print("quartas")
        elif fase == 8:
            print("oitavas")


if __name__ == '__main__':
    campeonato_02()
