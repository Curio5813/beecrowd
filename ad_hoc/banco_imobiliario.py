def banco_imobiliario():
    """
    Monopólio (conhecido no Brasil como Banco Imobiliário) é um
    dos jogos mais famosos do mundo, com 750 milhões de cópias
    vendidas. Durante o jogo, os jogadores podem comprar propriedades
    que estejam disponíveis, vendê-las para que elas voltem a ficar
    disponíveis, e cobrar aluguel pelo uso de uma determinada propriedade
    por outro jogador. O objetivo do jogo é acumular a maior quantidade
    de dinheiro possível.

    O jogo é composto por um tabuleiro e um conjunto de cédulas de dinheiro.
    Três amigos, Dália, Elói e Félix, querem jogar uma partida de Monopólio,
    mas o irmãozinho menor de Dália escondeu as cédulas de dinheiro. Os três
    amigos decidiram jogar a partida assim mesmo, anotando em um papel todas
    as operações que ocorreram durante o jogo (compras, vendas e pagamentos
    de aluguéis). Assim que eles pararam de jogar, perceberam que levaria muito
    tempo para descobrir quanto dinheiro cada um acumulou. Eles então pediram
    sua ajuda para determinar esses valores.

    Sua tarefa é escrever um programa que, a partir dos registros de jogadas
    realizados pelos três jogadores, determine a quantidade de dinheiro acumulada
    por cada um dos jogadores.

    Entrada
    A entrada contém um único conjunto de testes, que deve ser lido do dispositivo
    de entrada padrão (normalmente o teclado). A primeira linha da entrada contém
    dois inteiros, I e N que indicam respectivamente as quantias de dinheiro que
    Dália, Elói e Félix possuem no início do jogo (1 ≤ I ≤ 1000000) e o número de
    operações realizadas durante o jogo (1 ≤ N ≤ 10000). Note que os três jogadores
    iniciam a partida com a mesma quantidade de dinheiro. Os jogadores são representados
    na entrada sempre pela letra inicial de seu nome (‘D’, ‘E’ ou ‘F’). As N linhas
    contém as operações ocorridas durante o jogo. Cada linha pode ter um dos formatos
    abaixo:

    Compra — a letra C, seguida da letra inicial de um jogador J e de um inteiro X que
    representa o valor gasto por J na compra (0 < X ≤ 1000000). Exemplo: ‘C D 1000’.
    Venda — a letra V, seguida da letra inicial de um jogador J e de um inteiro X que
    representa o valor recebido por J na venda (0 < X ≤ 1000000). Exemplo: ‘V E 200’.
    Aluguel — a letra A, seguida da letra inicial de um jogador J que recebe o aluguel,
    da letra inicial do jogador K que paga o aluguel e de um inteiro X que representa o
    valor do aluguel (J != K e 0 ≤ X ≤ 1000000). Exemplo: ‘A F D 500’.
    Os valores intermediários e totais acumulados por cada jogador estão entre 0 e 1000000.

    Saída
    Seu programa deve imprimir, na saída padrão, uma única linha composta de três inteiros
    que correspondem à quantidade de dinheiro acumulada por Dália, Elói e Félix, nesta ordem.
    :return:
    """
    i, n = map(int, input().split(" "))
    dalia, eloi, felix, d_dalia, p_dalia, d_eloi, p_eloi, d_felix, p_felix = i, i, i, 0, 0, 0, 0, 0, 0
    for j in range(n):
        operacoes = input().split(" ")
        valor = int(operacoes[-1])
        for k in range(0, len(operacoes)):
            if operacoes[0] == 'C':
                if operacoes[1] == "D":
                    if valor >= dalia + p_dalia:
                        d_dalia += valor - (dalia + p_dalia)
                        dalia -= dalia
                    else:
                        dalia -= valor
                    break
                if operacoes[1] == "E":
                    if valor >= eloi + p_eloi:
                        d_eloi += valor - (eloi + p_eloi)
                        eloi -= eloi
                    else:
                        eloi -= valor
                    break
                if operacoes[1] == "F":
                    if valor >= felix + p_felix:
                        d_felix += valor - (felix + p_felix)
                        felix -= felix
                    else:
                        felix -= valor
                    break
            if operacoes[0] == 'V':
                if operacoes[1] == "D":
                    dalia += valor
                    if dalia > 1_000_000:
                        dalia = 1_000_000
                        p_dalia += dalia - 1_000_000
                    break
                if operacoes[1] == "E":
                    eloi += valor
                    if eloi > 1_000_000:
                        eloi = 1_000_000
                        p_eloi += eloi - 1_000_000
                    break
                if operacoes[1] == "F":
                    felix += valor
                    if felix > 1_000_000:
                        felix = 1_000_000
                        p_felix += felix - 1_000_000
                    break
            if operacoes[0] == 'A':
                if operacoes[1] == "D" and operacoes[2] == "E":
                    if valor >= eloi + p_eloi:
                        d_eloi = valor - (eloi + p_eloi)
                        eloi -= eloi
                        dalia += valor
                    else:
                        dalia += valor
                        eloi -= valor
                    if dalia > 1_000_000:
                        dalia = 1_000_000
                        p_dalia = dalia - 1_000_000
                    break
                if operacoes[1] == "D" and operacoes[2] == "F":
                    if valor >= felix + p_felix:
                        d_felix = valor - (felix + p_felix)
                        felix -= felix
                        dalia += valor
                    else:
                        dalia += valor
                        felix -= valor
                    if dalia > 1_000_000:
                        dalia = 1_000_000
                        p_dalia = dalia - 1_000_000
                    break
                if operacoes[1] == "E" and operacoes[2] == "D":
                    if valor >= dalia + p_dalia:
                        d_dalia += valor - (dalia + p_dalia)
                        dalia -= dalia
                        eloi += valor
                    else:
                        dalia -= valor
                        eloi += valor
                    if eloi > 1_000_000:
                        eloi = 1_000_000
                        p_eloi = eloi - 1_000_000
                    break
                if operacoes[1] == "F" and operacoes[2] == "D":
                    if valor >= dalia + p_dalia:
                        d_dalia += valor - (dalia + p_dalia)
                        dalia -= dalia
                        felix += valor
                    else:
                        dalia -= valor
                        felix += valor
                    if felix > 1_000_000:
                        felix = 1_000_000
                        p_felix += felix - 1_000_000
                    break
                if operacoes[1] == "E" and operacoes[2] == "F":
                    if valor >= felix + p_felix:
                        d_felix += valor - (felix + p_felix)
                        felix -= felix
                        eloi += valor
                    else:
                        eloi += valor
                        felix -= valor
                    if eloi > 1_000_000:
                        eloi = 1_000_000
                        p_eloi += eloi - 1_000_000
                    break
                if operacoes[1] == "F" and operacoes[2] == "E":
                    if valor >= eloi + p_eloi:
                        d_eloi += valor - (eloi + p_eloi)
                        eloi -= eloi
                        felix += valor
                    else:
                        eloi -= valor
                        felix += valor
                    if felix > 1_000_000:
                        felix = 1_000_000
                        felix = felix - 1_000_000
                    break
    print(dalia, eloi, felix)


banco_imobiliario()
