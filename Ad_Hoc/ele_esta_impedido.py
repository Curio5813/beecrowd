def ele_esta_impedido():
    """
    A Rede do Hemisfério é a maior rede de televisão de Tumbolia, um pequeno
    país situado a leste da América do Sul (ou sul da América do Leste). O
    esporte mais popular em Tumbolia, obviamente, é o futebol; muitos jogos
    são transmitidos toda semana em Tumbolia.

    A Rede do Hemisfério recebe muitos pedidos para repassar lances polêmicos;
    normalmente esses acontecem quando um jogador é dito impedido pelo juíz.
    Um jogador atacante está impedido se ele está mais próximo da linha do gol
    do oponente do que o penúltimo adversário. Um jogador não está impedido se

    ele está na mesma linha que o penúltimo adversário ou
    ele está na mesma linha que os dois últimos adversários.

    Através do uso de tecnologia de computação gráfica, a Rede do Hemisfério
    consegue tirar uma foto do campo e determinar as distâncias dos jogadores
    até a linha do gol do time defensor, mas eles ainda precisam de um programa
    que, dadas essas distâncias, decida se um jogador está impedido.

    Entrada
    O arquivo de entrada contém vários casos de teste. A primeira linha de cada
    caso de teste contém dois inteiros A e D separados por um espaço indicando,
    respectivamente, o número de jogadores atacantes e defensores envolvidos
    na jogada (2 ≤ A, D ≤ 11). A próxima linha contém A inteiros Bi separados
    por um espaço, indicando as distâncias dos jogadores atacantes até a linha
    do gol (1 ≤ Bi ≤ 104). A próxima linha contém D inteiros Cj separados por
    um espaço, indicando as distâncias dos defensores até a linha do gol (1 ≤
    Cj ≤ 104). O final da entrada é dado por A = D = 0.

    Saída
    Para cada caso de teste na entrada imprima uma linha contendo um único caractere:
    "Y" (maiúsculo) se existe um jogador atacante impedido, e "N" (maiúsculo) caso
    contrário.
    :return:
    """
    a, d = map(int, input().split(" "))
    while a != 0 and d != 0:
        a = list(map(int, input().split(" ")))
        d = list(map(int, input().split(" ")))
        d.sort()
        if min(a) >= d[1] or min(a) >= d[0] and min(a) >= d[1]:
            print("N")
        else:
            print("Y")
        a, d = map(int, input().split(" "))


ele_esta_impedido()
