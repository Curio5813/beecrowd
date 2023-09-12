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
    qt = 0
    for i in titas:
        if i == "P":
            for k in range(0, len(muros)):
                if k == len(muros) - 1:
                    if muros[k] >= p:
                        muros[k] -= p
                        break
                    elif muros[k] < p:
                        muros.append(x)
                        muros[k + 1] -= p
                        qt += 1
                        break
                if muros[k] >= p:
                    muros[k] -= p
                    break
            if len(muros) == 0:
                muro -= p
                muros.append(muro)
                qt += 1
        elif i == "M":
            for k in range(0, len(muros)):
                if k == len(muros) - 1:
                    if muros[k] >= m:
                        muros[k] -= m
                        break
                    elif muros[k] < m:
                        muros.append(x)
                        muros[k + 1] -= m
                        qt += 1
                        break
                if muros[k] >= m:
                    muros[k] -= m
                    break
            if len(muros) == 0:
                muro -= m
                muros.append(muro)
                qt += 1
        elif i == "G":
            for k in range(0, len(muros)):
                if k == len(muros) - 1:
                    if muros[k] >= g:
                        muros[k] -= g
                        break
                    elif muros[k] < g:
                        muros.append(x)
                        muros[k + 1] -= g
                        qt += 1
                        break
                if muros[k] >= g:
                    muros[k] -= g
                    break
            if len(muros) == 0:
                muro -= g
                muros.append(muro)
                qt += 1
    print(qt)


attack_on_gasparini()
