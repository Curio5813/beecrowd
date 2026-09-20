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
        for j in range(1, len(tabela)):
            flag = False
            for k in range(1, len(tabela[j])):
                temp2, temp3 = tabela[k][0], tabela[j][0]
                while temp2 <= 10000:
                    print(temp2, temp3)
                    if temp3 + temp2 == tabela[j][k]:
                        flag = True
                        tabela[k][0] = temp2
                        print(tabela[j][0])
                        break
                    temp3 += 1
                    if temp3 == 10000:
                        temp3 = -10000
                        temp2 -= 1
        if flag:
            print(f"{caso}. YES")
            caso += 1

        for j in range(len(tabela)):
            for k in range(len(tabela[j])):
                print(f"{tabela[j][k]:>5}", end=' ')
            print()


joao_ainda_nao_consegue_somar()

"""
1
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