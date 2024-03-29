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
    muro, muros = x, []
    titas = input()
    p, m, g = map(int, input().split(" "))
    for j in range(n):
        muros.append(x)
    for i in titas:
        for k in range(0, len(muros)):
            if i == "P":
                if muros[k] >= p:
                    muros[k] -= p
                    break
            if i == "M":
                if muros[k] >= m:
                    muros[k] -= m
                    break
            if i == "G":
                if muros[k] >= g:
                    muros[k] -= g
                    break
    qt_m = muros.count(muro)
    qt = n - qt_m
    print(qt)


attack_on_gasparini()
