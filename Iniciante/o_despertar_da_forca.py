def main():
    """
    Há muito tempo atrás, em uma galáxia muito, muito distante...

    Após o declínio do Império, sucateiros estão espalhados por todo o universo
    procurando por um sabre de luz perdido. Todos sabem que um sabre de luz emite
    um padrão de ondas específico: 42 cercado por 7 em toda a volta. Você tem um
    sensor de ondas que varre um terreno com N x M células. Veja o exemplo abaixo
    para um terreno 4 x 7 com um sabre de luz nele (na posição (2, 4)).

                        =====================
                        11 12  7  7  7 13 14
                        15  6  7 42  7  7 42
                        98 -5  7  7  7 42  7
                        -1 42  3  9  7  7  7
                        ====================

    Você deve escrever um programa que, dado um terreno N x M, procura pelo padrão
    do sabre de luz nele. Nenhuma varredura tem mais do que um padrão de sabre de
    luz.

    Entrada
    A primeira linha da entrada tem dois números positivos N e M, representando,
    respectivamente, o número de linhas e de colunas varridos no terreno (3 ≤ N, M ≤ 1000).
    Cada uma das próximas N linhas tem M inteiros, que descrevem os valores lidos
    em cada célula do terreno (-100 ≤ Tij ≤ 100, para 1 ≤ i ≤ N e 1 ≤ j ≤ M).

    Saída
    A saída é uma única linha com 2 inteiros X e Y separados por um espaço. Eles
    representam a coordenada (X,Y) do sabre de luz, caso encontrado. Se o terreno
    não tem um padrão de sabre de luz, X e Y são ambos zero.
    """
    t, posicao = [], []
    n, m = input().split()
    n, m = int(n), int(m)
    for k in range(n):
        num = [int(x) for x in input().split()]
        t.append(num)
    for k in range(0, len(t)):
        for i in range(0, len(t[k])):
            if 0 < k < len(t) - 1 and 0 < i < len(t[k]) - 1:
                if t[k][i] == 42 and t[k][i - 1] == 7 and t[k][i + 1] == 7 and \
                        t[k - 1][i] == 7 and t[k - 1][i - 1] == 7 and t[k - 1][i + 1] == 7 and \
                        t[k + 1][i] == 7 and t[k + 1][i - 1] == 7 and t[k + 1][i + 1] == 7:
                    posicao.append(k + 1)
                    posicao.append(i + 1)
    if len(posicao) > 0:
        print(*posicao)
    else:
        print('0 0')


if __name__ == '__main__':
    main()
