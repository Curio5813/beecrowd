import numpy as np


def procurando_palavras_na_diagonal_principal():
    """
    Em Algelandia, o passatempo preferido são os jogos de Caça Palavras.
    Um destes tem as seguintes características:

    As palavras ocorrem apenas no sentido da diagonal principal;
    As palavras podem ocorrer com letras maiúsculas e/ou minúsculas;
    Se uma dada palavra existe, ela ocorre uma única vez e em qualquer
    posição da diagonal;
    As palavras podem existir tanto na forma normal quanto invertida, ou seja,
    a leitura da diagonal pode ocorrer na forma top-down ou bottom-up.

    A primeira linha contém três inteiros: 1) N que representa a quantidade
    palavras que iremos verificar se existem no jogo, limitado por [1,100];
    2) M que representa a quantidade de linhas da matriz, limitado por [10,1000];
    3) P que representa a quantidade de colunas da matriz, limitado por [10,1000].
    Além disso, cada palavra N segue o limite: [6,100].

    Conforme a existência de cada palavra N, informe:

    1 Palavra "X" na diagonal principal
    2 Palavra "X" acima da diagonal principal
    3 Palavra "X" abaixo da diagonal principal
    4 Palavra "X" inexistente
    Onde X é a palavra procurada, além disso, X deve estar em lowercase.
    :return:
    """
    n, m, p = map(int, input().split(" "))
    palavras, caca_palavras, linha, linhas, principal, acima, \
        acimas, abaixo, abaixos, bol = [], [], [], [], "", "", [], "", [], 0
    for i in range(n):
        palavra = input().lower()
        palavras.append(palavra)
    for i in range(m):
        caca_palavra = input().lower()
        caca_palavras.append(caca_palavra)
    for i in range(0, len(caca_palavras)):
        for k in range(0, len(caca_palavras[i])):
            for j in caca_palavras[i][k]:
                linha.append(j)
        linhas.append(linha)
        linha = []
    matriz = np.array(linhas)
    diagonal_principal = matriz.diagonal(offset=0)
    diagonais_acima = [matriz.diagonal(offset=i) for i in range(1, matriz.shape[0])]
    diagonais_abaixo = [matriz.diagonal(offset=-i) for i in range(1, matriz.shape[0])]
    for i in range(0, len(diagonal_principal)):
        principal += diagonal_principal[i]
    for i in range(0, len(diagonais_acima)):
        for k in range(0, len(diagonais_acima[i])):
            acima += diagonais_acima[i][k]
        acimas.append(acima)
        acima = ""
    for i in range(0, len(diagonais_abaixo)):
        for k in range(0, len(diagonais_abaixo[i])):
            abaixo += diagonais_abaixo[i][k]
        abaixos.append(abaixo)
        abaixo = ""
    for i in range(0, len(palavras)):
        if palavras[i] in principal or palavras[i] in principal[::-1]:
            print(f'1 Palavra "{palavras[i]}" na diagonal principal')
        else:
            for k in range(0, len(acimas)):
                if palavras[i] in acimas[k] or palavras[i] in acimas[k][::-1]:
                    print(f'2 Palavra "{palavras[i]}" acima da diagonal principal')
                    bol = 1
                    break
            for k in range(0, len(abaixos)):
                if palavras[i] in abaixos[k] or palavras[i] in abaixos[k][::-1]:
                    print(f'3 Palavra "{palavras[i]}" abaixo da diagonal principal')
                    bol = 1
                    break
            else:
                if bol == 0:
                    print(f'4 Palavra "{palavras[i]}" inexistente')
                    bol = 0


procurando_palavras_na_diagonal_principal()
