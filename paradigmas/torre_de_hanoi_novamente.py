from math import sqrt
from time import sleep


def torre_de_hanoi_novamente():
    """
    As pessoas pararam de mover discos de uma haste para outra
    depois que eles descobriram o número de passos necessários
    para completar a tarefa. Por outro lado, elas não pararam
    de pensar sobre puzzles similares à Torre de Hanoi. Senhor S,
    como é conhecido, inventou um pequeno jogo. O jogo consiste
    de N astes e um MONTE de bolas. As bolas são numeradas 1,2,3...
    As bolas parecem comum, mas na verdade elas são mágicas. Se a
    soma dos números de duas bolas não for um quadrado perfeito
    elas irão se repelir com uma força grande quando estiverem muito
    perto, portanto, elas NUNCA podem ser colocadas encostando uma na
    outra.

    [imagem]!(https://resources.beecrowd.com/gallery/images/problems/UOJ_1166.jpg)

    O jogador deve colocar uma bola no topo de cada haste por vez. Ele
    deve primeiro tentar a bola 1, então a bola 2, depois a bola 3, assim
    por diante... Se ele falhar em fazer isto, o jogo termina. O Jogador
    deve tentar colocar o máximo de bolas possíveis nas hastes. Você pode
    ver o exemplo da figura acima, que nos mostra o melhor resultado possível
    de se obter utilizando 4 hastes.

    Entrada
    A primeira linha de entrada contem um único inteiro T (1 ≤ T ≤ 50), indicando
    o número de casos de teste Cada caso de teste contém um único inteiro N
    (1 ≤ N ≤ 50), indicando o número de varetas disponíveis.

    Saída
    Para cada caso de teste da entrada, imprima uma linha contendo um inteiro que
    indica o número máximo de bolas que podem ser colocadas. Imprima -1 se um
    número infinito de bolas pode ser colocado.
    :return:
    """
    t = int(input())
    q_perfeito, somas, bolas, a = [], 0, 0, 1
    for i in range(t):
        n = int(input())
        while len(q_perfeito) < 4:
            # print(a)
            # sleep(1)
            somas += a
            bolas += 1
            a += 1
            while sqrt(somas) == int(sqrt(somas)):
                somas += a
                if sqrt(somas) != int(sqrt(somas)):
                    somas -= a
                    q_perfeito.append(somas)
                    q_perfeito.append(a)
                    break
                bolas += 1
                a += 1
                # print(a)
                # sleep(1)
            print(q_perfeito)
        print(bolas)


torre_de_hanoi_novamente()
