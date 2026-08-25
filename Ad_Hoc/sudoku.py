from collections import Counter


def sudoku():
    """
    O jogo de Sudoku espalhou-se rapidamente por todo o mundo, tornando-se
    hoje o passatempo mais popular em todo o planeta. Muitas pessoas, entretanto,
    preenchem a matriz de forma incorreta, desrespeitando as restrições do jogo.
    Sua tarefa neste problema é escrever um programa que verifica se uma matriz
    preenchida é ou não uma solução para o problema.

    A matriz do jogo é uma matriz de inteiros 9 x 9 . Para ser uma solução do
    problema, cada linha e coluna deve conter todos os números de 1 a 9. Além
    disso, se dividirmos a matriz em 9 regiões 3 x 3, cada uma destas regiões
    também deve conter os números de 1 a 9. O exemplo abaixo mostra uma matriz
    que é uma solução do problema.

    [imagem](https://judge.beecrowd.com/pt/problems/view/1383)!

    Entrada
    São dadas várias instâncias. O primeiro dado é o número n > 0 de matrizes na
    entrada. Nas linhas seguintes são dadas as n matrizes. Cada matriz é dada em
    9 linhas, em que cada linha contém 9 números inteiros.

    Saída
    Para cada instância seu programa deverá imprimir uma linha dizendo "Instancia k",
    onde k é o número da instância atual. Na segunda linha, seu programa deverá
    imprimir "SIM" se a matriz for a solução de um problema de Sudoku, e "NAO" caso
    contrário. Imprima uma linha em branco após cada instância.
    :return:
    """
    n = int(input())
    n1 = n
    n *= 9
    cont, matriz_linha, matriz_coluna, linha, coluna, colunas = 0, [], [], [], [], []
    # Entrada das matrizes do jogo de sudoku
    for i in range(0, n + 1):
        if  cont % 9 == 0 and cont != 0:
            matriz_linha.append(linha)
            linha = []
            if i >= n:
                break
        linha.append(list(map(int, input().split())))
        cont += 1
    (cont1, cont2, m, q, p, matriz, quadrado_sudo, quadrados,
     matriz_quadrados) = 1, 0, 0, 0, 0, [], [], [], []
    # Mapeia os quadrados do jogo de sudoku
    while m < n1:
        q, p = 0, 0
        while p < 3:
            for j in range(0, len(matriz_linha[m][0])):
                for k in range(q, len(matriz_linha[m][p]) + 3):
                    if cont2 == 3 and cont2 != 0:
                        quadrados.extend(quadrado_sudo)
                        quadrado_sudo = []
                        cont2 = 0
                        break
                    quadrado_sudo.append(matriz_linha[m][j][k])
                    cont2 += 1
                if cont1 % 3 == 0 and cont1 != 0:
                    matriz.append(quadrados)
                    quadrados = []
                    if cont1 == 9:
                        matriz_quadrados.append(matriz)
                        matriz = []
                        cont1 = 1
                        break
                cont1 += 1
            q += 3
            p += 1
        m += 1
    # Mapeia as colunas do jogo de sudoku
    for i in range(0, len(matriz_linha)):
        for j in range(0, len(matriz_linha[i])):
            for k in range(0, len(matriz_linha[i][j])):
                coluna.append(matriz_linha[i][k][j])
            colunas.append(coluna)
            coluna = []
        matriz_coluna.append(colunas)
        colunas = []
    flag1, flag2, flag3, temp, temp2 = [], [], [], [], []
    # Verifica de há erros nas linhas do jogo de sudoku
    for i in range(0, len(matriz_linha)):
        for j in range(0, len(matriz_linha[i])):
            verificacao_1 = dict(Counter(matriz_linha[i][j]))
            for chave in verificacao_1:
                if verificacao_1[chave] > 1:
                    temp.append(False)
                    break
            if temp:
                break
        if not temp:
            temp.append(True)
            temp2.append(*temp)
            temp = []
        else:
            temp2.append(*temp)
            temp = []
    flag1.append(temp2)
    temp, temp2 = [], []
    # Verifica se há erros nas colunas do jogo de sudoku
    for i in range(0, len(matriz_coluna)):
        for j in range(0, len(matriz_coluna[i])):
            verificacao_2 = dict(Counter(matriz_coluna[i][j]))
            for chave in verificacao_2:
                if verificacao_2[chave] > 1:
                    temp.append(False)
                    break
            if temp:
                break
        if not temp:
            temp.append(True)
            temp2.append(*temp)
            temp = []
        if temp:
            temp2.append(*temp)
            temp = []
    flag2.append(temp2)
    temp, temp2 = [], []
    # Verifica se há erros nos quadrados do jogo de sudoku
    for i in range(0, len(matriz_quadrados)):
        for j in range(0, len(matriz_quadrados[i])):
            verificacao_3 = dict(Counter(matriz_quadrados[i][j]))
            for chave in verificacao_3:
                if verificacao_3[chave] > 1:
                    temp.append(False)
                    break
            if temp:
                break
        if not temp:
            temp.append(True)
            temp2.append(*temp)
            temp = []
        if temp:
            temp2.append(*temp)
            temp = []
    flag3.append(temp2)
    flag3_cord, cont4, cont5, j = [[]], 0, 0, 0
    # Filtra as matrizes menores, os quadrados, que formam o jogo
    for i in range(0, len(flag3)):
        while j < len(flag3[i]):
            if flag3[i][j]:
                cont4 += 1
                if cont4 == 3:
                    flag3_cord[0].append(True)
                    cont4 = 0
            if not flag3[i][j]:
                cont5 += 1
                while cont5 < 3:
                    cont5 += 1
                    j += 1
                flag3_cord[0].append(False)
                cont5 = 0
            j += 1
    # Dá a resposta de cada jogo se a soluação está certa ou errada
    for i in range(0, len(flag1)):
        for j in range(0, len(flag1[i])):
            if flag1[i][j] == True and flag2[i][j] == True and flag3_cord[i][j] == True:
                print(f"Instancia {j + 1}")
                print("SIM")
                print()
            else:
                print(f"Instancia {j + 1}")
                print(f"NAO")
                print()


if __name__ == '__main__':
    sudoku()
