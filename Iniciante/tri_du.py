def main():
    """
    Tri-du é um jogo de cartas derivado do popular jogo de Truco. O jogo utiliza um baralho
    normal de 52 cartas, com treze cartas de cada naipe, mas os naipes são ignorados. Apenas
    o valor das cartas,considerados como inteiros de 1 a 13, são utilizados.

    No jogo, cada jogador recebe três cartas. As regras são simples:

    Um trio (três cartas de mesmo valor) ganha de uma dupla (duas cartas de mesmo valor).
    Um trio formado por cartas de maior valor ganha de um trio formado por cartas de menor valor.
    Uma dupla formada por cartas de maior valor ganha de uma dupla formada por cartas de menor valor.
    Note que o jogo pode não ter ganhador em muitas situações; nesses casos, as cartas distribuídas
    são devolvidas ao baralho, que é embaralhado e uma nova partida é iniciada

    Um jogador já recebeu duas das cartas que deve receber, e conhece seus valores. Sua tarefa é
    escrever um programa para determinar qual o valor da terceira carta que maximiza a probabilidade
    de esse jogador ganhar o jogo.

    Entrada
    A entrada consiste de uma única linha que contém dois inteiros, A (1 ≤ A ≤ 13) e B (1 ≤ B ≤ 13)
    indicando os valores das duas primeiras cartas recebidas.

    Saída
    Seu programa deve produzir uma única linha com um inteiro representando o valor da carta que
    maximiza a probabilidade de o jogador ganhar a partida.
    """
    c1, c2 = input().split()
    c1, c2 = int(c1), int(c2)
    if c1 > c2:
        print(c1)
    elif c2 > c1:
        print(c2)
    elif c1 == c2:
        print(c1)


if __name__ == '__main__':
    main()
