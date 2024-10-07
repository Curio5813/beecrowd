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
    temp, idxs = [], []
    i -= 1
    j -= 1
    ladrilhos = []
    for k in range(l):
        ladrilho = list(map(int, input().split(" ")))
        ladrilhos.append(ladrilho)
    print(i + 1, j + 1)
    while True:
        # Canto superior esqerdo --------
        if i == 0 and j == 0 and ladrilhos[i][j + 1] == 1:
            l = i
            c = j + 1
            j += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif i == 0 and j == 0 and ladrilhos[i + 1][j] == 1:
            l = i + 1
            c = j
            i += 1
            print(l + 1, c + 1)
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        # Canto superior direito -------
        elif i == 0 and j == len(ladrilhos[i]) - 1 and ladrilhos[i][j - 1] == 1:
            l = i
            c = j - 1
            j -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif i == 0 and j == len(ladrilhos[i]) - 1 and ladrilhos[i + 1][j] == 1:
            l = i + 1
            c = j
            i += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        # Canto inferior esquerdo
        elif i == len(ladrilhos) - 1 and j == 0 and ladrilhos[i][j + 1] == 1:
            l = i
            c = j + 1
            j += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        # Canto inferior esquerdo
        elif i == len(ladrilhos) - 1 and j == 0 and ladrilhos[i - 1][j] == 1:
            l = i - 1
            c = j
            i -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        # Canto inferior direito
        elif i == len(ladrilhos) - 1 and j == len(ladrilhos[i]) - 1 and ladrilhos[i - 1][j] == 1:
            l = i - 1
            c = j
            i -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        # Canto inferior direito
        elif i == len(ladrilhos) - 1 and j == len(ladrilhos[i]) - 1 and ladrilhos[i][j - 1] == 1:
            l = i
            c = j - 1
            j -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        # Borda superior --------
        elif i == 0 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i][j + 1] == 1:
            l = i
            c = j + 1
            j += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif i == 0 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i + 1][j + 1] == 1:
            l = i + 1
            c = j + 1
            i + 1
            j += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif i == 0 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i][j - 1] == 1:
            l = i
            c = j - 1
            j -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif i == 0 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i + 1][j - 1] == 1:
            l = i + 1
            c = j - 1
            i += 1
            j -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        # Borda inferior -------------
        elif i == len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i][j + 1] == 1:
            l = i
            c = j + 1
            j += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif i == len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i - 1][j] == 1:
            l = i - 1
            c = j
            i -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif i == len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i][j - 1] == 1:
            l = i
            c = j - 1
            j -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif i == len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) - 1 and ladrilhos[i - 1][j] == 1:
            l = i - 1
            c = j
            i -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        # Borda lateral esquerda --------------------
        elif len(ladrilhos) > i > 0 == j and ladrilhos[i + 1][j] == 1:
            l = i + 1
            c = j
            i += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif len(ladrilhos) > i > 0 == j and ladrilhos[i - 1][j] == 1:
            l = i - 1
            c = j
            i -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif len(ladrilhos) > i > 0 == j and ladrilhos[i + 1][j + 1] == 1:
            l = i + 1
            c = j + 1
            i += 1
            j += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif len(ladrilhos) > i > 0 == j and ladrilhos[i - 1][j + 1] == 1:
            l = i - 1
            c = j + 1
            i -= 1
            j += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        # Borda lateral direira ---------
        elif len(ladrilhos) > i > 0 and j == len(ladrilhos[i]) - 1 and ladrilhos[i + 1][j] == 1:
            l = i + 1
            c = j
            i += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif len(ladrilhos) > i > 0 and j == len(ladrilhos[i]) - 1 and ladrilhos[i - 1][j] == 1:
            l = i + 1
            c = j - 1
            i += 1
            j -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        # Meio ------------------
        elif 0 < i < len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) and ladrilhos[i][j + 1] == 1:
            l = i
            c = j + 1
            j += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif 0 < i < len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) and ladrilhos[i][j - 1] == 1:
            l = i
            c = j - 1
            j -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif 0 < i < len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) and ladrilhos[i + 1][j] == 1:
            l = i + 1
            c = j
            i += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif 0 < i < len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) and ladrilhos[i - 1][j] == 1:
            l = i - 1
            c = j
            i -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif 0 < i < len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) and ladrilhos[i + 1][j + 1] == 1:
            l = i + 1
            c = j + 1
            i += 1
            j += 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        elif 0 < i < len(ladrilhos) - 1 and 0 < j < len(ladrilhos[i]) and ladrilhos[i - 1][j - 1] == 1:
            l = i - 1
            c = j - 1
            i -= 1
            j -= 1
            print(l + 1, c + 1)
            temp.append(l + 1)
            temp.append(c + 1)
            if temp in idxs:
                print(*idxs[-1])
                break
            else:
                idxs.append(temp)
                temp = []
        sleep(1)


robo()
