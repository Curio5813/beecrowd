def robo_colecionador():
    """
    Um dos esportes favoritos na Robolândia é o Rali dos Robôs. Este
    rali é praticado em uma arena retangular gigante de N linhas por
    M colunas de células quadradas. Algumas das células estão vazias,
    algumas contêm figurinhas da Copa (muito apreciadas pelas inteligências
    artificiais da Robolândia) e algumas são ocupadas por pilastras que
    sustentam o teto da arena. Em seu percurso os robôs podem ocupar qualquer
    célula da arena, exceto as que contém pilastras, que bloqueiam o seu movimento.
    O percurso do robô na arena durante o rali é determinado por uma sequência de
    instruções. Cada instrução é representada por um dos seguintes caracteres:
    ‘D’, ‘E’ e ‘F’, significando, respectivamente, “gire 90 graus para a direita”,
    “gire 90 graus para a esquerda” e “ande uma célula para a frente”. O robô começa
    o rali em uma posição inicial na arena e segue fielmente a sequência de instruções
    dada (afinal, eles são robôs!). Sempre que o robô ocupa uma célula que contém uma
    figurinha da Copa ele a coleta. As figurinhas da Copa não são repostas, ou seja,
    cada figurinha pode ser coletada uma unica vez. Quando um robô tenta andar para uma
    célula onde existe uma pilastra ele patina, permanecendo na célula onde estava, com
    a mesma orientação. O mesmo também acontece quando um robô tenta sair da arena.

    Dados o mapa da arena, descrevendo a posição de pilastras e figurinhas, e a sequência
    de instruções de um robô, você deve escrever um programa para determinar o número de
    figurinhas coletadas pelo robô.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de um caso de teste contém três
    números inteiros N, M e S (1 ≤ N, M ≤ 100, 1 ≤ S ≤ 5 × 104 ), separados por espaços em
    branco, indicando respectivamente o número de linhas e o número de colunas da arena e o
    número de instruções para o robô. Cada uma das N linhas seguintes da entrada descreve uma
    linha de células da arena e contém uma cadeia com M caracteres. A primeira linha que aparece
    na descrição da arena é a que está mais ao Norte; a primeira coluna que aparece na descrição
    de uma linha de células da arena é a que está mais a Oeste.

    Cada célula da arena pode conter um dos seguintes caracteres:

    ‘.’ — célula normal;
    ‘*’ — célula que contém uma figurinha da Copa;
    ‘#’ — célula que contém uma pilastra;
    ‘N’, ‘S’, ‘L’, ‘O’ — célula onde o robô inicia o percurso (única na arena). A letra representa
    a orientação inicial do robô (Norte, Sul, Leste e Oeste, respectivamente).

    A ultima linha da entrada contém uma sequência de S caracteres dentre ‘D’, ‘E’ e ‘F’, representando
    as instruções do robô.

    O último caso de teste é seguido por uma linha que contém apenas três números zero separados por
    um espaço em branco.

    Saída
    Para cada rali descrito na entrada seu programa deve imprimir uma única linha contendo um único
    inteiro, indicando o número de figurinhas que o robô colecionou durante o rali.
    :return:
    """
    while True:
        n, m, s = map(int, input().split())
        if n == 0 and m == 0 and s == 0:
            break
        arena = []
        for i in range(n):
            linha = list(input().split())
            arena.extend(linha)
        instrucoes = input()
        copas, flag = 0, False
        for i in range(0, len(instrucoes)):
            for j in range(0, len(arena)):
                for k in range(0, len(arena[j])):
                    if arena[j][k] == 'N' and instrucoes[i] == 'D':
                        arena[j] = arena[j][:k] + 'L' + arena[j][k+1:]
                        break
                    elif arena[j][k] == 'N' and instrucoes[i] == 'E':
                        arena[j] = arena[j][:k] + 'O' + arena[j][k+1:]
                        break
                    elif arena[j][k] == 'N' and instrucoes[i] == 'F' and j > 0:
                        if arena[j - 1][k] != '#':
                            arena[j] = arena[j][:k] + '.' + arena[j][k+1:]
                            j -= 1
                            if arena[j][k] == '*':
                                copas += 1
                            arena[j] = arena[j][:k] + 'N' + arena[j][k + 1:]
                        flag = True
                        break
                    elif arena[j][k] == 'S' and instrucoes[i] == 'D':
                        arena[j] = arena[j][:k] + 'O' + arena[j][k+1:]
                        break
                    elif arena[j][k] == 'S' and instrucoes[i] == 'E':
                        arena[j] = arena[j][:k] + 'L' + arena[j][k+1:]
                        break
                    elif arena[j][k] == 'S' and instrucoes[i] == 'F' and j < len(arena) - 1:
                        if arena[j + 1][k] != '#':
                            arena[j] = arena[j][:k] + '.' + arena[j][k + 1:]
                            j += 1
                            if arena[j][k] == '*':
                                copas += 1
                            arena[j] = arena[j][:k] + 'S' + arena[j][k + 1:]
                        flag = True
                        break
                    elif arena[j][k] == 'L' and instrucoes[i] == 'D':
                        arena[j] = arena[j][:k] + 'S' + arena[j][k+1:]
                        break
                    elif arena[j][k] == 'L' and instrucoes[i] == 'E':
                        arena[j] = arena[j][:k] + 'N' + arena[j][k+1:]
                        break
                    elif arena[j][k] == 'L' and instrucoes[i] == 'F' and k < m - 1:
                        if arena[j][k + 1] != '#':
                            arena[j] = arena[j][:k] + '.' + arena[j][k + 1:]
                            k += 1
                            if arena[j][k] == '*':
                                copas += 1
                            arena[j] = arena[j][:k] + 'L' + arena[j][k + 1:]
                        flag = True
                        break
                    elif arena[j][k] == 'O' and instrucoes[i] == 'D':
                        arena[j] = arena[j][:k] + 'N' + arena[j][k+1:]
                        break
                    elif arena[j][k] == 'O' and instrucoes[i] == 'E':
                        arena[j] = arena[j][:k] + 'S' + arena[j][k+1:]
                        break
                    elif arena[j][k] == 'O' and instrucoes[i] == 'F' and k > 0:
                        if arena[j][k - 1] != '#':
                            arena[j] = arena[j][:k] + '.' + arena[j][k + 1:]
                            k -= 1
                            if arena[j][k] == '*':
                                copas += 1
                            arena[j] = arena[j][:k] + 'O' + arena[j][k + 1:]
                        flag = True
                        break
                if flag:
                    flag = False
                    break
        print(copas)


robo_colecionador()

"""
3 3 2
***
*N*
***
DE
4 4 5
...#
*#O.
*.*.
*.#.
FFEFF
10 10 20
....*.....
.......*..
.....*....
..*.#.....
...#N.*..*
...*......
..........
..........
..........
..........
FDFFFFFFEEFFFFFFEFDF
4 3 3
***
***
*N*
***
FFF
0 0 0
"""
