def fuga_do_cavalo():
    """
    Seu amigo Pedro está aprendendo a jogar xadrez. Mas ele ainda
    não tem segurança de como pode movimentar o Cavalo. Desta forma,
    ele solicitou a você que desenvolvesse um programa que calcule,
    em apenas uma jogada, o número de distintos movimentos que o
    cavalo pode realizar, sem que o mesmo fique sobre o ataque de
    qualquer um dos 8 peões. Os movimentos do cavalo e dos peões
    são realizados conforme o jogo de xadrez tradicional, ou seja,
    o cavalo pode somente andar em “L”, e os peões atacar somente
    para frente em diagonal.

    Entrada
    A entrada consiste de diversos casos de teste. Cada caso de teste
    consiste em 9 linhas de entrada. A primeira linha indica a posição
    inicial do cavalo. As demais 8 linhas, representam as respectivas
    posições dos peões.

    O final da entrada consiste em uma única linha contendo somente o
    valor 0 (zero).

    Saída
    Para cada teste de caso de entrada, seu programa deve imprimir uma
    única linha, contendo a seguinte descrição:

    Caso de Teste #Y: X movimento(s).

    onde Y representa o número do respectivo caso de teste, e X representa
    a quantidade de movimentos possíveis ao cavalo realizar, em uma única
    rodada, sem que fique sobre ataque de um ou mais peões.
    :return:
    """
    casos = 0
    while True:
        cavalo, pos_cavalo, peoes, pos_peoes, pos_peoes_num, aux,\
            ataque_peoes, movimentos_cavalo, cont = "", [], [], [], [], [], [], [], 0
        colunas = "abcdefgh"
        for i in range(9):
            posicao = input()
            if posicao == "0":
                return
            else:
                if i == 0:
                    cavalo = posicao
                else:
                    peoes.append(posicao[0])
                    peoes.append(posicao[1])
                    pos_peoes.append(peoes)
                    peoes = []
        a = int(cavalo[0])
        b = int(colunas.index(cavalo[1]) + 1)
        pos_cavalo.append(a)
        pos_cavalo.append(b)
        for i in range(8):
            a = int(pos_peoes[i][0])
            b = int(colunas.index(pos_peoes[i][1]) + 1)
            aux.append(a)
            aux.append(b)
            pos_peoes_num.append(aux)
            aux = []
        for i in range(0, len(pos_peoes)):
            x = pos_peoes_num[i][0]
            y = pos_peoes_num[i][1]
            ataque_esquerda_x = x - 1
            ataque_esquerda_y = y - 1
            ataque_direita_x = x - 1
            ataque_direita_y = y + 1
            if ataque_esquerda_x >= 1 and ataque_esquerda_y >= 1:
                aux.append(ataque_esquerda_x)
                aux.append(ataque_esquerda_y)
                ataque_peoes.append(aux)
                aux = []
            if ataque_direita_x >= 1 and ataque_direita_y <= 8:
                aux.append(ataque_direita_x)
                aux.append(ataque_direita_y)
                ataque_peoes.append(aux)
                aux = []
        for i in range(1):
            x = pos_cavalo[0]
            y = pos_cavalo[1]
            baixo_esquerda_x = x - 2
            baixo_esquerda_y = y - 1
            if baixo_esquerda_x >= 1 and baixo_esquerda_y >= 1:
                aux.append(baixo_esquerda_x)
                aux.append(baixo_esquerda_y)
                movimentos_cavalo.append(aux)
                aux = []
            baixo_direita_x = x - 2
            baixo_direita_y = y + 1
            if baixo_direita_x >= 1 and baixo_direita_y <= 8:
                aux.append(baixo_direita_x)
                aux.append(baixo_direita_y)
                movimentos_cavalo.append(aux)
                aux = []
            cima_esquerda_x = x + 2
            cima_esquerda_y = y - 1
            if cima_esquerda_x <= 8 and cima_esquerda_y >= 1:
                aux.append(cima_esquerda_x)
                aux.append(cima_esquerda_y)
                movimentos_cavalo.append(aux)
                aux = []
            cima_direita_x = x + 2
            cima_direita_y = y + 1
            if cima_direita_x <= 8 and cima_direita_y <= 8:
                aux.append(cima_direita_x)
                aux.append(cima_direita_y)
                movimentos_cavalo.append(aux)
                aux = []
            esqerda_cima_x = x + 1
            esquerda_cima_y = y - 2
            if esqerda_cima_x <= 8 and esquerda_cima_y >= 1:
                aux.append(esqerda_cima_x)
                aux.append(esquerda_cima_y)
                movimentos_cavalo.append(aux)
                aux = []
            esquerda_baixo_x = x - 1
            esquerda_baixo_y = y - 2
            if esquerda_baixo_x >= 1 and esquerda_baixo_y >= 1:
                aux.append(esquerda_baixo_x)
                aux.append(esquerda_baixo_y)
                movimentos_cavalo.append(aux)
                aux = []
            direita_cima_x = x + 1
            direita_cima_y = y + 2
            if direita_cima_x <= 8 and direita_cima_y <= 8:
                aux.append(direita_cima_x)
                aux.append(direita_cima_y)
                movimentos_cavalo.append(aux)
                aux = []
            direita_baixo_x = x - 1
            direita_baixo_y = y + 2
            if direita_baixo_x >= 1 and direita_baixo_y <= 8:
                aux.append(direita_baixo_x)
                aux.append(direita_baixo_y)
                movimentos_cavalo.append(aux)
                aux = []
        for i in range(0, len(movimentos_cavalo)):
            if movimentos_cavalo[i] not in ataque_peoes:
                cont += 1
        casos += 1
        print(f"Caso de Teste #{casos}: {cont} movimento(s).")


fuga_do_cavalo()
