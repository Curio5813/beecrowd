from math import sqrt, floor


def caixas_muito_especiais():
    """
    Special Box Company (SBC) é uma empresa familiar que produz caixas de papelão
    decoradas para embalar presentes. As caixas são feitas à mão, produzidas
    individualmente a partir de materiais nobres. Ao aceitar uma encomenda de um
    cliente, eles sempre produzem algumas caixas a mais do que o necessário, para
    manter um estoque de caixas para ser vendido no futuro. Ao longo dos anos seu
    estoque tem crescido, com caixas em todo o lugar, e eles decidiram que precisavam
    se organizar um pouco mais. Eles têm, portanto, feito uma lista registrando as
    dimensões de cada caixa em seu estoque.

    SBC acaba de receber um pedido de um cliente que deve ser entregue amanhã, por isso
    não há tempo para produzir novas caixas. O cliente quer uma certo número N de caixas,
    todas do mesmo tamanho; cada caixa irá ser usada para embalar um item de dimensões
    X, Y e Z. Como o papelão utilizado nas caixas é muito fino, você pode assumir que em
    uma caixa de tamanho (X, Y, Z) se encaixaria perfeitamente o item que o cliente quer
    embrulhar. Se não houver pelo menos N caixas que encaixam perfeitamente o item, o cliente
    quer caixas de N que se encaixam os itens tão firmemente quanto possível. O tamanho da
    caixa que se encaixa os itens tão firmemente quanto possível é a que minimiza o espaço
    vazio quando o item é colocado dentro da caixa. Um item pode ser rotacionado em qualquer
    direção para ser acomodado dentro de uma caixa, por isso, uma caixa de tamanho (X, Y, Z)
    é tão boa como uma caixa de tamanho (Y, Z, X).

    Você pode ajudar a SBC a descobrir se eles podem atender a ordem do cliente?

    Entrada
    A entrada consiste em vários casos de teste. A primeira linha de cada caso de teste contem
    dois inteiros N e M, indicando respectivamente o número de caixas que o cliente deseja
    comprar (1 ≤ N ≤ 1500) e o número de caixas na lista de estoque (1 ≤ M ≤ 1500). A segunda
    linha contém três inteiros X, Y e Z, representando as dimensões do item que o cliente deseja
    embrulhar (0 < X, Y, Z ≤ 50). Cada uma das M linhas seguintes contém três inteiros A, B e C
    representando as dimesões de uma das caixas da lista de estoque (0 < A, B, C ≤ 50). O caso de
    teste com N = 0 indica o fim da entrada.

    Saída
    Para cada caso de teste da entrada o seu programa deve produzir uma linha de saída, contendo:

    somente a palavra 'impossible', caso não seja possível atender ao pedido do cliente (porque
    não existem pelo menos N caixas do mesmo tamanho no estoque que podem conter o item); ou
    um inteiro V, que especifica o volume do espaço que sobra quando um dos N itens é colocado
    em uma das caixas escolhidas.
    :return:
    """
    while True:
        n, m = map(int, input().split())
        if n == 0:
            break
        item = list(map(int, input().split()))
        item.sort()
        menor_lado_item = item[0]
        volume_item = item[0] * item[1] * item[2]
        volumes_caixas, menores_lado = [], []
        for i in range(m):
            caixa = list(map(int, input().split()))
            caixa.sort()
            menores_lado.append(caixa[0])
            volume_caixa = caixa[0] * caixa[1] * caixa[2]
            volumes_caixas.append(volume_caixa)
        menor_sobra, menor_lado, volumes_sobra = volumes_caixas[0] - volume_item, menores_lado[0], []
        for i in range(0, len(volumes_caixas)):
            if menor_lado_item <= menores_lado[i] and volumes_caixas[i] >= volume_item:
                volume_sobra = volumes_caixas[i] - volume_item
                print(volumes_caixas[i], menores_lado[i], menor_lado, menor_sobra)
                if menores_lado[i] <= menor_lado and volume_sobra <= menor_sobra:
                    volumes_sobra.append(volume_sobra)
                    menor_lado = menores_lado[i]
                    menor_sobra = volume_sobra
        if not volumes_sobra:
            print('impossible')
        else:
            print(min(volumes_sobra))


caixas_muito_especiais()


"""
1 1
2 4 3
2 3 4
2 6
3 1 3
7 4 7
10 8 2
2 8 10
6 2 9
7 7 4
6 2 9
1 1
3 3 3
1 1 1
0 0
"""