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
    n *= 9
    cont, matriz_linha, matriz_coluna, linha, coluna, colunas = 0, [], [], [], [], []
    for i in range(0, n + 1):
        if  cont % 9 == 0 and cont != 0:
            matriz_linha.append(linha)
            linha = []
            if i >= n:
                break
        linha.append(list(map(int, input().split())))
        cont += 1
    for i in range(0, len(matriz_linha)):
        for j in range(0, len(matriz_linha[i])):
            for k in range(0, len(matriz_linha[i][j])):
                coluna.append(matriz_linha[i][k][j])
            colunas.append(coluna)
            coluna = []
        matriz_coluna.append(colunas)
        colunas = []
    for i in range(0, len(matriz_linha)):
        flag1, flag2 = True, True
        for j in range(0, len(matriz_linha[i])):
            verificacao_1 = dict(Counter(matriz_linha[i][j]))
            for chave in verificacao_1:
                if verificacao_1[chave] > 1:
                    flag1 = False
            if not flag1:
                print(f"Instancia {i + 1}")
                print("NAO")
                print()
                flag1 = True
                break
        for j in range(0, len(matriz_coluna[i])):
            verificacao_2 = dict(Counter(matriz_coluna[i][j]))
            for chave in verificacao_2:
                if verificacao_2[chave] > 1:
                    flag2 = False
            if not flag2:
                print(f"Instancia {i + 1}")
                print("NAO")
                print()
                break
        if flag1 and flag2:
            print(f"Instancia {i + 1}")
            print("SIM")
            print()


if __name__ == '__main__':
    sudoku()
