def um_jogo_com_bolas_de_gude():
    """
    Existem n bacias, numeradas de 1 até n. Inicialmente,
    a bacia i contém mi bolas de gude. Uma rodada consiste
    em remover uma bola de gude de uma bacia. Quando uma
    bola de gude é removida da bacia i (i > 1), outra bola
    de gude é adicionada a cada uma das primeiras i-1 bacias;
    se uma bola de gude é removida da bacia 1, nenhuma nova
    bola de gude é adicionada. O jogo termina quando cada uma
    das bacias estiver vazia.

    Seu trabalho é determinar quantas rodadas são necessárias
    para o jogo terminar. Você pode assumir que o suprimento
    de bolas de gude é suficiente, e que todas as bacias são
    grandes o suficiente, de tal forma que cada rodada possível
    pode ser executada.

    Entrada
    A entrada é composta de vários casos de teste. Cada caso de
    teste é composto por uma linha, contendo um inteiro n (1 ≤ n ≤ 50),
    o número de bacias no jogo. A linha seguinte contém n inteiros mi
    (1 ≤ i ≤ n, 0 ≤ mi ≤ 1000), onde mi representa o números de bolas
    de gude na bacia i no início do jogo.

    Um único valor 0 indica o fim da entrada.

    Saída
    Para caso de texto, imprima uma linha com o número de rodadas necessárias
    para o jogo terminar. Você pode assumir que esse número cabe em um inteiro
    de 64 bits (em C/C++ você pode usar o tipo “long long” e em Java o tipo “long”).
    :return:
    """
    while True:
        n = int(input().strip())
        if n == 0:
            break
        bacias = list(map(int, input().strip().split(" ")))
        cont, rodadas, i, p_dois = 0, 0, 0, 1
        while cont < len(bacias):
            rodadas += bacias[i] * p_dois
            i += 1
            p_dois *= 2
            cont += 1
        print(rodadas)


if __name__ == '__main__':
    um_jogo_com_bolas_de_gude()
