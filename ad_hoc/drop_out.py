def drop_out():
    """
    Drop Out é o nome de um simples jogo de cartas, que é jogado
    com um baralho normal de 52 cartas. As cartas são ordenadas
    da seguinte maneira: (Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete,
    Rainha, Rei), com o Ás sendo o menor deles, e o Rei o maior.
    O naipe das cartas é desconsiderado. Os jogadores (no mínimo dois)
    sentam em volta de uma mesa, um baralho é embaralhado e colocado ]
    no centro da mesa, com as cartas de face voltada para baixo. No
    início do jogo, todos os jogadores estão "ativos". O jogo se prossegue
    em turnos. Em cada turno, os jogadores ativos recebem uma carta do
    baralho, no sentido horário, independente da posição onde estão sentados.
    Os jogadores que recebem a menor carta no turno são eliminados do jogo
    e tornam-se "inativos". Note que até quatro jogadores podem ser eliminados
    em cada turno. O jogo termina quando resta somente um jogador ativo, o qual
    é o vencedor. Se todo o baralho acabar antes dos turnos terminarem, o jogo
    termina e todos os jogadores ativos no início do último turno são vencedores.

    Dado o número de jogadores, seus nomes e um baralho de cartas embaralhadas,
    você deve escrever um programa que simule o jogo e determine o vencedor ou
    vencedores.

    Entrada
    A entrada contém diversos casos de teste. Cada caso de teste consiste de seis
    linhas. A primeira linha contém um inteiro N, indicando o número de jogadores
    no jogo (2 ≤ N ≤ 20). A segunda linha contém uma lista dos nomes dos jogadores,
    separados por espaços. O nome de um jogador é composto de no máximo 16 letras
    do alfabeto inglês (de 'A' até 'Z' e 'a' até 'z'). As cartas são entregues aos
    jogadores na ordem dada na lista. As próximas quatro linhas contém a descrição
    do baralho embaralhado. As cartas são representadas por inteiros de 1 a 13
    (1, 11, 12 e 13 representam, respectivamente, as cartas Ás, Valete, Rainha e Rei).
    O baralho é descrito em quatro linhas de treze inteiros cada, separados por
    um único espaço. O baralho é listado de cima para baixo, então a primeira carta
    entregue é a primeira carta listada. O final da entrada é indicado por N = 0.

    A entrada deve ser lida da entrada padrão.

    Saída
    Para cada caso de teste na entrada, seu programa deve produzir uma linha de saída,
    contendo o nome do vencedor ou vencedores. A lista de vencedores deve aparecer na
    mesma ordem dada na entrada, e cada nome deve ser seguido por um espaço.

    A saída deve ser escrita na saída padrão.
    :return:
    """
    while True:
        n = int(input())
        cartas, cont, qtd, resultado, booleano = [], 0, 0, {()}, 0
        resultado.discard(())
        if n == 0:
            break
        else:
            jogadores = input().split(" ")
            for i in range(4):
                carta = list(map(int, input().split(" ")))
                cartas.extend(carta)
            for i in range(52):
                cont = qtd
                qtd += len(jogadores)
                idx = cartas[cont:qtd]
                for k in range(0, len(idx)):
                    resultado = set(idx)
                    if len(resultado) == 1:
                        booleano = 1
                        break
                    else:
                        minimo = min(idx)
                        while minimo in idx and len(idx) >= len(jogadores):
                            jogadores.pop(idx.index(minimo))
                            idx.pop(idx.index(minimo))
                        break
                if booleano == 1:
                    break
            for i in range(0, len(jogadores)):
                print(f"{jogadores[i]}", end=" ")
            print("")


drop_out()
