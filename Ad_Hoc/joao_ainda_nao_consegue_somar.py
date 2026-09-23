from copy import deepcopy


def joao_ainda_nao_consegue_somar():
    """

    :return:
    """
    n = int(input())
    caso = 1
    for i in range(n):
        linha = int(input())
        linhas, tabela, temp1 = [], [], []
        for j in range(linha + 1):
            if j == linha + 1:
                while len(temp1) < linha:
                    temp1.append(0)
                linhas.extend(temp1)
                tabela.append(linhas)
                break
            if j == 0:
                temp1.append('+')
                while len(temp1) < linha + 1:
                    temp1.append(0)
                linhas.extend(temp1)
                tabela.append(linhas)
                linhas = []
                temp1 = []
            else:
                linhas.append(0)
                linhas.extend(list(map(int, input().split())))
                tabela.append(linhas)
                linhas = []
        for j in range(len(tabela)):
            for k in range(len(tabela[j])):
                print(f"{tabela[j][k]:>5}", end=' ')
            print()
        achados1, achados2, temp2, temp3, cont1, cont2, a = [], [], 0, 0, 1, 1, 1
        tabela2 = deepcopy(tabela)
        for j in range(1, len(tabela[0])):
            for k in range(1, len(tabela[j])):
                temp2, temp3 = tabela[j][0], tabela[k][0]
                while temp3 < 10000:
                    print(temp2, temp3)
                    if tabela[j][k] > 0:
                        temp3 += 1
                        if temp3 + temp2 == tabela[j][k]:
                            flag = True
                            break
                    if tabela[j][k] < 0:
                        temp3 -= 1
                        if temp3 < -10000:
                            break
                        if temp3 + temp2 == tabela[j][k]:
                            flag = True
                            break
                tabela2[j][0] = temp3
                break
        if flag:
            print(f"{caso}. YES")
            caso += 1
        if not flag:
            print(f"{caso}. NO")
            caso += 1
        for j in range(len(tabela2)):
            for k in range(len(tabela2[j])):
                print(f"{tabela2[j][k]:>5}", end=' ')
            print()
        print(achados1)


joao_ainda_nao_consegue_somar()

"""
3
3
4 -1 6
7 2 9
1 -4 3
2
1 4
3 5
2
3 6
2 5
"""