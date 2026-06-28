def peca_perdida():
    """
    Joãozinho adora quebra-cabeças, essa é sua brincadeira favorita. O grande
    problema, porém, é que às vezes o jogo vem com uma peça faltando. Isso irrita
    bastante o pobre menino, que tem de descobrir qual peça está faltando e solicitar
    uma peça de reposição ao fabricante do jogo. Sabendo que o quebra-cabeças tem N
    peças, numeradas de 1 a N e que exatamente uma está faltando, ajude Joãozinho a
    saber qual peça ele tem de pedir.

    Escreva um programa que, dado um inteiro N e N - 1 inteiros numerados de 1 a N,
    descubra qual inteiro está faltando.

    Entrada
    A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de
    entrada padrão (normalmente o teclado). A entrada contém 2 linhas. A primeira linha
    contém um inteiro N (2 ≤ N ≤ 1.000). A segunda linha contém N - 1 inteiros numerados
    de 1 a N (sem repetições).

    Saída
    Seu programa deve imprimir, na saída padrão, uma única linha, contendo o número que
    está faltando na sequência dada.
    :return:
    """
    n = int(input())
    pecas = list(map(int, input().strip().split(" ")))
    pecas.sort()
    for i in range(1, n + 1):
        if i not in pecas:
            print(i)
            break


peca_perdida()

