from time import sleep


def robo():
    """
    Um novo robô de limpeza para um grande salão retangular
    está sendo desenvolvido. O robô vai percorrer o caminho
    definido por uma linha marcada no chão, que é coberto com
    ladrilhos quadrados, brancos e pretos: ladrilhos pretos
    indicam o caminho que o robô deve percorrer. Ao movimentar-se,
    o robô pode andar apenas em linha reta, para a frente. Parado,
    o robô pode girar para as quatro direções (Norte, Sul, Leste e
    Oeste).

    Dados um mapa indicando a cor de cada ladrilho no chão e a posição
    inicial do robô, você deve escrever um programa que determine a
    posição final do robô.

    Entrada
    A primeira linha contém dois inteiros L e C (1 ≤ L, C ≤ 1000) indicando
    as dimensões do salão (número de linhas e número de colunas), medidas em
    ladrilhos. A segunda linha contém dois inteiros A e B (1 ≤ B ≤ L, 1 ≤ B ≤ C)
    indicando respectivamente a linha e a coluna da posição inicial do robô (as
    linhas são numeradas de 1 a L, de cima para baixo; as colunas são numeradas
    de 1 a C, da esquerda para a direita). Cada uma das L linhas seguintes contém
    C inteiros, zeros ou uns. Nessa representação, o valor ‘1’ indica que o ladrilho
    corresponte é preto. O ladrilho da linha A e coluna B sempre é preto. O caminho
    do robô é definido unicamente: em nenhum momento o robô necessita fazer uma
    escolha sobre em qual direção ir (em outras palavras, todo ladrilho preto tem no
    máximo dois vizinhos pretos e o ladrilho inicial tem um vizinho preto).

    Saída
    Seu programa deve imprimir apenas uma linha, contendo dois números inteiros,
    respectivamente a linha e a coluna da posição final do robô.
    :return:
    """
    l, c = map(int, input().split(" "))
    i, j = map(int, input().split(" "))
    temp, idxs, uns = [], [], 0
    temp.append(i)
    temp.append(j)
    idxs.append(temp)
    temp = []
    i -= 1
    j -= 1
    ladrilhos = []
    grade = l * c
    cont = 0
    for k in range(l):
        ladrilho = list(map(int, input().split(" ")))
        ladrilhos.append(ladrilho)
        uns += ladrilhos[k].count(1)
    # print(uns)
    # print(i + 1, j + 1)
    if l == 1 and c == 1:
        print(1, 1)
    else:
        while True:
            cont += 1
            if cont >= grade:
                break
            if len(idxs) >= uns:
                break
            # Canto superior esqerdo --------
            if i == 0 and j == 0 and ladrilhos[i][j + 1] == 1:
                l = i
                c = j + 1
                j += 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    j -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif i == 0 and j == 0 and ladrilhos[i + 1][j] == 1:
                l = i + 1
                c = j
                i += 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            # Canto superior direito -------
            elif i == 0 and j == len(ladrilhos[i]) - 1 and ladrilhos[i][j - 1] == 1:
                l = i
                c = j - 1
                j -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    j += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif i == 0 and j == len(ladrilhos[i]) - 1 and ladrilhos[i + 1][j] == 1:
                l = i + 1
                c = j
                i += 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            # Canto inferior esquerdo
            elif i == len(ladrilhos) - 1 and j == 0 and ladrilhos[i][j + 1] == 1:
                l = i
                c = j + 1
                j += 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    j -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            # Canto inferior esquerdo
            elif i == len(ladrilhos) - 1 and j == 0 and ladrilhos[i - 1][j] == 1:
                l = i - 1
                c = j
                i -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            # Canto inferior direito
            elif i == len(ladrilhos) - 1 and j == len(ladrilhos[i]) - 1 and ladrilhos[i - 1][j] == 1:
                l = i - 1
                c = j
                i -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            # Canto inferior direito
            elif i == len(ladrilhos) - 1 and j == len(ladrilhos[i]) - 1 and ladrilhos[i][j - 1] == 1:
                l = i
                c = j - 1
                j -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    j += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            # Borda superior --------
            elif i == 0 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i][j - 1] == 1:
                l = i
                c = j - 1
                j -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    j += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif i == 0 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i + 1][j] == 1:
                l = i + 1
                c = j
                i += 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif i == 0 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i][j + 1] == 1:
                l = i
                c = j + 1
                j += 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    j -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            # Borda inferior -------------
            elif i == len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i][j + 1] == 1:
                l = i
                c = j + 1
                j += 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    j -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif i == len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i - 1][j] == 1:
                l = i - 1
                c = j
                i -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif i == len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i][j - 1] == 1:
                l = i
                c = j - 1
                j -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    j += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif i == len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i - 1][j] == 1:
                l = i - 1
                c = j
                i -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            # Borda lateral esquerda --------------------
            elif len(ladrilhos) > i > 0 == j and ladrilhos[i + 1][j] == 1:
                l = i + 1
                c = j
                i += 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif len(ladrilhos) > i > 0 == j and ladrilhos[i - 1][j] == 1:
                l = i - 1
                c = j
                i -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            # Borda lateral direita ---------
            elif len(ladrilhos) > i > 0 and j == len(ladrilhos[i]) - 1 and ladrilhos[i - 1][j] == 1:
                l = i - 1
                c = j
                i -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif len(ladrilhos) > i > 0 and j == len(ladrilhos[i]) - 1 and ladrilhos[i + 1][j] == 1:
                l = i + 1
                c = j
                i += 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            # Meio ------------------
            elif 0 < i < len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i][j - 1] == 1:
                l = i
                c = j - 1
                j -= 1
                # print(l + 1, c + 1, "Ok-02")
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    j += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif 0 < i < len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i][j + 1] == 1:
                l = i
                c = j + 1
                j += 1
                # print(l + 1, c + 1, "Ok-01")
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    j -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(idxs[-1])
                        break
            elif 0 < i < len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i + 1][j] == 1:
                l = i + 1
                c = j
                i += 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i -= 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(*idxs[-1])
                        break
            elif 0 < i < len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i - 1][j] == 1:
                l = i - 1
                c = j
                i -= 1
                # print(l + 1, c + 1)
                temp.append(l + 1)
                temp.append(c + 1)
                if temp in idxs:
                    # print(*idxs[-1])
                    i += 2
                    temp = []
                else:
                    idxs.append(temp)
                    temp = []
                    if len(idxs) == uns:
                        # print(*idxs[-1])
                        break
            # sleep(1)
        print(*idxs[-1])


robo()

"""
3 5
1 1
1 0 0 0 1
1 0 0 1 1
1 1 1 1 0


4 7
3 4
0 0 1 1 1 1 1
1 1 1 0 0 0 1
1 0 0 1 0 1 1
1 1 0 1 1 1 0
"""
