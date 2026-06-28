def receita_de_bolo():
    """
    João deseja fazer bolos para seus amigos, usando uma receita que indica
    que devem ser usadas 2 xícaras de farinha de trigo, 3 ovos e 5 colheres
    de sopa de leite. Em casa ele tem A xícaras de farinha de trigo, B ovos e
    C colheres de sopa de leite.

    João não tem muita prática com a cozinha, e portanto ele só se arriscará a
    fazer medidas exatas da receita de bolo (por exemplo, se ele tiver material
    suficiente para fazer mais do que 2 e menos do que 3 bolos, ele fará somente
    2 bolos). Sabendo disto, ajude João escrevendo um programa que determine qual
    a quantidade máxima de bolos que ele consegue fazer.

    Entrada
    A entrada é dada em uma única linha, que contém três números inteiros A, B e C,
    (1 ≤ A, B e C ≤ 100) indicando respectivamente o número de xícaras de farinha
    de trigo, o número de ovos e o número de colheres de sopa de leite que João tem
    em casa.

    Saída
    Seu programa deve imprimir uma única linha, contendo um único inteiro, a quantidade
    máxima de bolos que João consegue fazer.
    :return:
    """
    ingredientes = list(map(int, input().split(" ")))
    bolos = []
    for i in range(0, len(ingredientes)):
        if i == 0:
            qt = ingredientes[i] // 2
            bolos.append(qt)
        if i == 1:
            qt = ingredientes[i] // 3
            bolos.append(qt)
        if i == 2:
            qt = ingredientes[i] // 5
            bolos.append(qt)
    print(min(bolos))


receita_de_bolo()
