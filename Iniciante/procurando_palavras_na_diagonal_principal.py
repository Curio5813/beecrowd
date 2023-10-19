def procurando_palavras_na_diagonal_principal():
    """
    Em Algelandia, o passatempo preferido são os jogos de Caça Palavras.
    Um destes tem as seguintes características:

    As palavras ocorrem apenas no sentido da diagonal principal;
    As palavras podem ocorrer com letras maiúsculas e/ou minúsculas;
    Se uma dada palavra existe, ela ocorre uma única vez e em qualquer
    posição da diagonal;
    As palavras podem existir tanto na forma normal quanto invertida,
    ou seja, a leitura da diagonal pode ocorrer na forma top-down ou
    bottom-up.

    A primeira linha contém três inteiros: 1) N que representa a quantidade
    palavras que iremos verificar se existem no jogo, limitado por [1,100];
    2) M que representa a quantidade de linhas da matriz, limitado por [10,1000];
    3) P que representa a quantidade de colunas da matriz, limitado por [10,1000].
    Além disso, cada palavra N segue o limite: [6,100]. Esta função printa, conforme
    a existência de cada palavra N, informe:

    1 Palavra "X" na diagonal principal
    2 Palavra "X" acima da diagonal principal
    3 Palavra "X" abaixo da diagonal principal
    4 Palavra "X" inexistente
    Onde X é a palavra procurada, além disso, X deve estar em lowercase.
    :return:
    """
    m, linha, coluna = map(int, input().split(" "))
    palavras, principal = [], ""
    for i in range(m):
        palavra = input()
        palavras.append(palavra)
    for i in range(linha):
        for k in range(coluna):
            matriz = input()
            if i == k:
                principal += matriz

    print(principal)


procurando_palavras_na_diagonal_principal()
