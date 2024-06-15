def jogo_de_varetas():
    """
    Há muitos jogos divertidos que usam pequenas varetas
    coloridas. A variante usada neste problema envolve a
    construção de retângulos. O jogo consiste em, dado um
    conjunto de varetas de comprimentos variados, desenhar
    retângulos no chão, utilizando as varetas como lados
    dos retângulos, sendo que cada vareta pode ser utilizada
    em apenas um retângulo, e cada lado de um retângulo é formado
    por uma única vareta. Nesse jogo, duas crianças recebem dois
    conjuntos iguais de varetas. Ganha o jogo a criança que desenhar
    o maior número de retângulos com o conjunto de varetas.

    Dado um conjunto de varetas de comprimentos inteiros, você deve
    escrever um programa para determinar o maior número de retângulos
    que é possível desenhar.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de um caso
    de teste contém um inteiro N que indica o número de diferentes
    comprimentos de varetas (1 ≤ N ≤ 1.000) no conjunto. Cada uma das N
    linhas seguintes contém dois números inteiros Ci e Vi , representando
    respectivamente um comprimento (1 ≤ Ci ≤ 10.000) e o número de varetas
    com esse comprimento (1 ≤ Vi ≤ 1.000). Cada comprimento de vareta
    aparece no máximo uma vez em um conjunto de teste (ou seja, os valores
    Ci são distintos). O ﬁnal da entrada é indicado por N = 0.

    Saída
    Para cada caso de teste da entrada seu programa deve produzir uma única linha
    na saída, contendo um número inteiro, indicando o número máximo de retângulos
    que podem ser formados com o conjunto de varetas dado.
    :return:
    """
    while True:
        n = int(input())
        varetas, sobras, retangulos,  = [], [], 0
        if n == 0:
            break
        else:
            for i in range(n):
                entrada = list(map(int, input().split(" ")))
                varetas.append(entrada)
            for i in range(0, len(varetas)):
                for j in range(0, len(varetas[i])):
                    if varetas[i][1] >= 4 and varetas[i][1] % 4 == 0:
                        retangulos += varetas[i][1] // 4
                        break
                    if varetas[i][1] > 4 and varetas[i][1] % 4 != 0:
                        sobras.append(varetas[i][1] % 4)
                        retangulos += varetas[i][1] // 4
                        break
                    if 2 <= varetas[i][1] < 4:
                        sobras.append(varetas[i][1])
                        break
            if len(sobras) < 2:
                print(retangulos)
            else:
                for i in range(0, len(sobras)):
                    for j in range(i + 1, len(sobras)):
                        if sobras[i] >= 2 and sobras[j] >= 2:
                            retangulos += (sobras[i] + sobras[j]) // 4
                            sobras[i] = 0
                            sobras[j] = 0
                            break
                print(retangulos)


jogo_de_varetas()
