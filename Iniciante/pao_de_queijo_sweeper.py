def main():
    """
    Está chegando a grande final do Campeonato Nlogonense de Surf Aquático, que este
    ano ocorrerá na cidade de Bonita Horeleninha (BH)! Nesta cidade, o jogo PãodeQueijoSweeper
    é bastante popular!

    O tabuleiro do jogo consiste em uma matriz de N linhas e M colunas. Cada célula da matriz
    contém um pão de queijo ou o número de pães de queijo que existem nas celulas adjacentes
    a ela. Uma célula é adjacente a outra se estiver imediatamente à esquerda, à direita,
    acima ou abaixo da célula. Note que, se não contiver um pão de queijo, uma célula deve
    obrigatoriamente conter um número entre 0 e 4, inclusive.

    Dadas as posições dos pães de queijo, determine o tabuleiro do jogo!

    Entrada
    A entrada contém vários casos de teste. A primeira linha de cada caso contém os inteiros
    N e M (1 ≤ N, M ≤ 100). As próximas N linhas contém M inteiros cada, separados por espaços,
    descrevendo os pães de queijo no tabuleiro. O j-ésimo inteiro da i-ésima linha é 1 se
    existe um pão de queijo na linha i e coluna j do tabuleiro, ou 0 caso contrário.

    A entrada termina com fim-de-arquivo (EOF).

    Saída
    Para cada caso de teste, imprima N linhas com M inteiros cada, não separados por espaços,
    descrevendo a configuração do tabuleiro. Se uma posição contém um pão de queijo, imprima
    9 para ela; caso contrário, imprima o número cuja posição deve conter.
    """
    while True:
        matrix, cont, counter, counters, cels = [], 0, [], [], []
        try:
            n, m = input().split()
            n, m = int(n), int(m)
        except EOFError:
            break
        else:
            for k in range(n):
                p_quejo = [int(x) for x in input().split()]
                matrix.append(p_quejo)
            for k in range(0, len(matrix)):
                for i in range(0, len(matrix[k])):
                    if len(matrix) == 1 and len(matrix[k]) == 1:
                        if matrix[k][i] == 0:
                            cont = 0
                            counter.append(cont)
                        elif matrix[k][i] == 1:
                            cont = 9
                            counter.append(cont)
                    elif len(matrix) == 1 and len(matrix[k]) > 1:
                        if matrix[k][i] == 0 and i == 0:
                            cont = matrix[k][i + 1]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and 0 < i < len(matrix[k]) - 1:
                            cont = matrix[k][i - 1] + matrix[k][i + 1]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and i == len(matrix[k]) - 1:
                            cont = matrix[k][i - 1]
                            counter.append(cont)
                        elif matrix[k][i] == 1:
                            cont = 9
                            counter.append(cont)
                    elif len(matrix) > 1 and len(matrix[k]) == 1:
                        if matrix[k][i] == 0 and k == 0:
                            cont = matrix[k + 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and 0 < k < len(matrix) - 1:
                            cont = matrix[k - 1][i] + matrix[k + 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and k == len(matrix) - 1:
                            cont = matrix[k - 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 1:
                            cont = 9
                            counter.append(cont)
                    elif len(matrix) > 1 and len(matrix[k]) > 1:
                        if matrix[k][i] == 0 and i == 0 and k == 0:
                            cont = matrix[k][i + 1] + matrix[k + 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and i == 0 and 0 < k < len(matrix) - 1:
                            cont = matrix[k][i + 1] + matrix[k - 1][i] + matrix[k + 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and i == 0 and k == len(matrix) - 1:
                            cont = matrix[k][i + 1] + matrix[k - 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and 0 < i < len(matrix[k]) - 1 and k == 0:
                            cont = matrix[k][i - 1] + matrix[k][i + 1] + matrix[k + 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and 0 < i < len(matrix[k]) - 1 and 0 < k < len(matrix) - 1:
                            cont = matrix[k][i - 1] + matrix[k][i + 1] + matrix[k - 1][i] + matrix[k + 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and 0 < i < len(matrix[k]) - 1 and k == len(matrix) - 1:
                            cont = matrix[k][i - 1] + matrix[k][i + 1] + matrix[k - 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and i == len(matrix[k]) - 1 and k == 0:
                            cont = matrix[k][i - 1] + matrix[k + 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and i == len(matrix[k]) - 1 and 0 < k < len(matrix) - 1:
                            cont = matrix[k][i - 1] + matrix[k - 1][i] + matrix[k + 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 0 and i == len(matrix[k]) - 1 and k == len(matrix) - 1:
                            cont = matrix[k][i - 1] + matrix[k - 1][i]
                            counter.append(cont)
                        elif matrix[k][i] == 1:
                            counter.append(9)
                counters.append(counter)
                counter = []
        for k in range(0, len(counters)):
            for i in range(0, len(counters[k])):
                print(f'{counters[k][i]}', end='')
            print('')


if __name__ == '__main__':
    main()
