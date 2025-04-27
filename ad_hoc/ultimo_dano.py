def ultimo_dano():
    """
    André e Beto estão jogando um jogo de computador que recompensa os
    jogadores de uma maneira bem particular: apenas aquele que der o
    último dano para derrotar um monstro leva todo o ouro que o mesmo
    deixar para trás. Isso implica que, mesmo que outros jogadores tenham
    ajudado a derrotar o monstro, apenas aquele que atacar por último será
    recompensado.

    André está intrigado com este sistema, e pediu sua ajuda. Dado o número
    de pontos de vida do monstro, o dano dado por André e Beto, e o tempo de
    espera necessário para que dois ataques sucessivos sejam realizados, descubra
    quem dará o último dano ao monstro, o derrotando e recebendo o ouro.

    No início ambos André e Beto irão atacar, infringindo At e Bt pontos de dano
    ao monstro, respectivamente. Após cada ataque, tanto André quanto Beto tem
    que esperar exatos Ad e Bd segundos, respectivamente, antes de atacar novamente.
    Sempre que André e Beto puderem atacar ao mesmo no tempo (como no início), André
    tem a prioridade e ataca primeiro. Um monstro é derrotado quando seus pontos de
    vida chegam a menor ou igual a zero.

    Entrada
    A primeira linha contém um inteiro T, indicando o número de casos de teste a seguir.

    Cada caso de teste inicia com quatro inteiros At, Ad, Bt e Bd (1 ≤ At, Ad, Bt, Bd ≤ 100),
    indicando o dano de ataque e o tempo de espera entre dois ataques consecutivos de André
    e Beto, respectivamente.

    Em seguida haverá um inteiro H (1 ≤ H ≤ 10000), indicando o número de pontos de vida do
    monstro.

    Saída
    Para cada caso de teste imprima uma linha contendo um nome, sendo ele “Andre” caso este
    seja o último a atacar o monstro, ou “Beto” caso contrário.
    :return:
    """
    t = int(input())
    for i in range(t):
        tempo, tempo_a, tempo_b, mostro = 0, 0, 0, 0
        at, ad, bt, bd = map(int, input().split(" "))
        monstro = int(input())
        while monstro > 0:
            if tempo > 0:
                tempo += 1
                if tempo % tempo_a == 0:
                    monstro -= at
                    tempo_a += ad
                    if monstro <= 0:
                        print("Andre")
                        break
                if tempo % tempo_b == 0:
                    monstro -= bt
                    tempo_b += bd
                    if monstro <= 0:
                        print("Beto")
                        break
            if tempo == 0:
                monstro -= at
                tempo_a += ad
                if monstro <= 0:
                    print("Andre")
                    break
                monstro -= bt
                tempo_b += bd
                if monstro <= 0:
                    print("Beto")
                    break
                tempo += 1


ultimo_dano()
