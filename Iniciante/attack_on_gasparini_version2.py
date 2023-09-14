def attack_on_gasparini():
    """
    Esta função calcula a quantidade de muralhas que devem ser
    construídas para parar o ataque dos gigantes titãs. Como
    dados de entrada, na primeira linha temos a quantidade de
    titãs e a altura da muralha. Na segungda linha temos os
    tipos de titãs, "P", para pequeno, "M", para médio e "G",
    para grande. A terceira linha de entrada fornece a altura
    de cada de titãs, em ordem crescente de tamanhos, onde a
    primeira altura são para titãs pequenos, a segunda, para
    os titãs médios e a terceira para os titãs grandes. A saída
    do programa fornece a quantidade mínima de muralhas a serem
    constuídas para parar o ataque dos titãs.

    :return:
    """
    n, muro = map(int, input().split(" "))
    qt = 0
    titas = input()
    p, m, g = map(int, input().split(" "))
    total = n * muro
    for i in titas:
        if i == "P":
            qt += p
        if i == "M":
            qt += m
        if i == "G":
            qt += g
    qt_m = total // qt
    print(qt_m)


attack_on_gasparini()
