def escada_rolante_2():
    """
    O Shopping Boas Compras - SBC, através de sua política ambiental, está
    preocupado com o consumo de energia e, resolveu trocar todas as escadas
    rolantes por modelos mais modernos, que se desligam caso ninguém esteja
    utilizando, poupando energia.

    A nova escada rolante possui um sensor no início. Toda vez que ela está vazia
    e alguém passa pelo sensor, a escada começa a funcionar, parando de funcionar
    novamente após 10 segundos se ninguém mais passar pelo sensor. Estes 10 segundos
    representam o tempo suficiente para levar alguém de um nível ao outro.

    Preocupados em saber exatamente quanto de energia o shopping está economizando,
    o gerente pediu sua ajuda. Como eles sabem qual era o consumo da escada rolante
    antiga, eles te pediram para calcular o tempo que a nova escada ficou funcionando.

    Dados os instantes, em segundos, em que passaram pessoas pela escada rolante, você
    deve calcular quantos segundos ela ficou ligada.

    Entrada
    A primeira linha da entrada contém um inteiro N que indica o número de pessoas que
    o sensor detectou (1 ≤ N ≤ 1.000). As N linhas seguintes representam o instante em
    que a n-ésima pessoa passou pelo sensor e contém um inteiro T (0 ≤ T ≤ 10.000). Os
    tempos estão em ordem crescente, sem repetições.

    Salida
    Seu programa deve imprimir uma única linha, contendo o tempo que a escada rolante ficou
    ligada.
    :return:
    """
    pessoas = int(input())
    instantes = []
    for i in range(pessoas):
        instante = int(input())
        instantes.append(instante)
    tempo_total = instantes[-1] - instantes[0] + 10
    tempo1, tempo2 = 0, 0
    if tempo_total >= pessoas * 10 + 10:
        tempo1 = pessoas * 10
    tempo2 = tempo_total
    for i in range(1, len(instantes) - 1):
        if instantes[i] - instantes[i - 1] >= 10:
            tempo2 += 10
            tempo2 -= instantes[i] - instantes[i - 1]
    if tempo1 > tempo2 > 0:
        print(tempo2)
    elif tempo1 == 0 and tempo2 > 0:
        print(tempo2)
    else:
        print(tempo1)


escada_rolante_2()
