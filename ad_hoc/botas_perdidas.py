def botas_perdidas():
    """
    A divisão de Suprimentos de Botas e Calçados do Exército comprou
    um grande número de pares de botas de vários tamanhos para seus
    soldados. No entanto, por uma falha de empacotamento da fábrica
    contratada, nem todas as caixas entregues continham um par de botas
    correto, com duas botas do mesmo tamanho, uma para cada pé. O sargento
    mandou que os recrutas retirassem todas as botas de todas as caixas para
    reembalá-las, desta vez corretamente.

    Quando o sargento descobriu que você sabia programar, ele solicitou com
    a gentileza habitual que você escrevesse um programa que, dada a lista
    contendo a descrição de cada bota entregue, determina quantos pares corretos
    de botas poderão ser formados no total.

    Entrada
    A entrada é composta por diversos casos de teste e termina com final de arquivo
    (EOF). A primeira linha de um caso de teste contém um inteiro N (2 ≤ N ≤ 10 4),
    N é par, indicando o número de botas individuais entregues. Cada uma das N linhas
    seguintes descreve uma bota, contendo um número inteiro M (30 ≤ M ≤ 60) e uma letra
    L, separados por uma espaço em branco. M indica o número da bota e L indica o pé da
    bota: L = 'D' indica que a bota é para o pé direito, L = 'E' indica que a bota é
    para o pé esquerdo.

    Saída
    Para cada caso de teste imprima uma linha contendo um único número inteiro indicando
    o número total de pares corretos que podem ser formados.
    :return:
    """
    while True:
        try:
            esquerdo, direito, cont = [], [], 0
            n = int(input())
            for i in range(n):
                m = input().split(" ")
                if m[1] == "E":
                    esquerdo.append(int(m[0]))
                elif m[1] == "D":
                    direito.append(int(m[0]))
            for i in range(30, 60 + 1):
                if i in esquerdo and i in direito:
                    bot_e = esquerdo.count(i)
                    bot_d = direito.count(i)
                    if bot_e <= bot_d:
                        cont += bot_e
                    elif bot_d < bot_e:
                        cont += bot_d
            print(cont)
        except EOFError:
            break


botas_perdidas()
