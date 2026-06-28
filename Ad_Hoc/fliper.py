def fliper():
    """
    Flíper é um tipo de jogo onde uma bolinha de metal cai por um
    labirinto de caminhos até chegar na parte de baixo do labirinto.
    A quantidade de pontos que o jogador ganha depende do caminho
    que a bolinha seguir. O jogador pode controlar o percurso da
    bolinha mudando a posição de algumas portinhas do labirinto.
    Cada portinha pode estar na posição 0, que significa virada
    para a esquerda, ou na posição 1 que quer dizer virada para
    a direita. Considere o flíper da figura abaixo, que tem duas
    portinhas. A portinha P está na posição 1 e a portinha R, na
    posição 0. Desse jeito, a bolinha vai cair pelo caminho B.

    ![FIGURA](https://resources.beecrowd.com/gallery/images/contests/UOJ_177_L.png)

    Você deve escrever um programa que, dadas as posições das portinhas P e R,
    neste flíper da figura, diga por qual dos três caminhos, A, B ou C, a bolinha
    vai cair!

    Entrada
    A entrada é composta por apenas uma linha contendo dois números P (0 ou 1) e
    R (0 ou 1), indicando as posições das duas portinhas do flíper da figura.

    Saída
    A saída do seu programa deve ser também apenas uma linha, contendo uma letra
    maiúscula que indica o caminho por onde a bolinha vai cair: ‘A’, ‘B’ ou ‘C’.
    :return:
    """
    p, r = map(int, input().split(" "))
    if p == 0:
        print("C")
    if p == 1 and r == 1:
        print("A")
    if p == 1 and r == 0:
        print("B")


fliper()
