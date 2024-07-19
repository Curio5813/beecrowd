def plantando_arvores():
    """
    O fazendeiro Jon comprou recentemente N mudas de árvores que deseja
    plantar em seu quintal. Leva 1 dia para Jon plantar uma muda (Jon não
    é particularmente trabalhador), e para cada árvore Jon sabe exatamente
    em quantos dias após o plantio ela cresce até a maturidade completa. Jon
    também gostaria de dar uma festa para seus amigos fazendeiros, mas para
    impressioná-los ele gostaria de organizar a festa somente depois que
    todas as árvores tivessem crescido. Mais precisamente, a festa pode ser
    organizada no dia seguinte, após o crescimento da última árvore.

    Ajude Jon a descobrir quando é o primeiro dia em que a festa pode acontecer.
    Jon pode escolher a ordem de plantio das árvores da maneira que quiser, por
    isso quer plantar as árvores de forma que a festa seja o mais rápido possível.

    Entrada
    A entrada consiste em duas linhas. A primeira linha contém um único inteiro N
    (1 ≤ N ≤ 100.000) denotando o número de mudas. Em seguida, segue-se uma linha
    com N inteiros Ti (1 ≤ Tᵢ ≤ 1 000 000), onde Tᵢ denota o número de dias que a
    i-ésima árvore leva para crescer.

    Saída
    Seu programa deve imprimir exatamente uma linha contendo um inteiro, denotando
    o primeiro dia em que a festa pode ser organizada. Os dias são numerados
    1, 2, 3,. . . começando do momento atual.
    :return:
    """
    n = int(input())
    cresc_arvores = list(map(int, input().strip().split(" ")))
    cresc_arvores.sort()
    cresc_arvores.reverse()
    dias = cresc_arvores[0]
    # print(cresc_arvores)
    for i in range(0, len(cresc_arvores)):
        if i >= len(cresc_arvores) - 1:
            break
        if cresc_arvores[0] == cresc_arvores[i]:
            x = i
            while cresc_arvores[x] == cresc_arvores[x + 1]:
                x += 1
            i = x
            if cresc_arvores[i] - cresc_arvores[i + 1] <= len(cresc_arvores) - 1:
                dias += 1
        else:
            if cresc_arvores[i] - cresc_arvores[i + 1] <= len(cresc_arvores) - 1:
                dias += 1
            # print(dias, cresc_arvores[i], cresc_arvores[i - 1])
    print(dias)


plantando_arvores()
