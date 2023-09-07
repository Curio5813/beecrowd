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
    n, x = map(int, input().split(" "))
    t = input()
    p, m, g = map(int, input().split(" "))
    total_p, total_m, total_g, total, qt = 0, 0, 0, 0, 1
    for i in range(len(t)):
        if t[i] == "P":
            total_p += p
        elif t[i] == "M":
            total_m += m
        elif t[i] == "G":
            total_g += g
    total = total_p + total_m + total_g
    if total <= x:
        return print(qt)
    elif total > x:
        while total > x and total_g > 0:
            x -= total_g
            total -= g
            total_g -= g
            x -= total_g
        while total_m > x:
            x += x
            qt += 1
            if x >= total_m:
                x -= total_m
        while total_p > x:
            x += x
            qt += qt
    print(qt)


attack_on_gasparini()
