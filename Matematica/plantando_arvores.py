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
    dias, comparar,diff = 0, cresc_arvores[0], 0
    # print(cresc_arvores)
    for i in range(1, len(cresc_arvores)):
        if i == 1 and comparar + 1 >= cresc_arvores[i] + i + 1:
            dias += comparar + 1
        if i == 1 and comparar + 1 < cresc_arvores[i] + i + 1:
            dias += cresc_arvores[i] + i + 1
            comparar = cresc_arvores[i] + i + 1
        if i > 1 and comparar + 1 < cresc_arvores[i] + i + 1:
            dias += cresc_arvores[i] + i + 1 - (comparar + 1)
            comparar = cresc_arvores[i] + i + 1
    print(dias + 1)


if __name__ == "__main__":
    plantando_arvores()


"""
4
2 3 4 3
6
39 38 9 35 39 20
6
20 18 18 18 18 18
"""