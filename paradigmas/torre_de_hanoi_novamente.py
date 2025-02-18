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
    lista, q_perfeito, somas, bolas, idas, a, b, flag = [], [], 0, 0, 0, 1, 0, 0
    for i in range(t):
        n = int(input())
        for j in range(n):
            for k in range(n):
                lista.append(0)
                break
            q_perfeito.append(lista)
            lista = []
        while a < 12:
            if a == 1:
                q_perfeito[b].append(a)
                bolas += 1
                a += 1
                q_perfeito[b].append(a)
            raiz_q = sqrt(sum(q_perfeito[b][-2:]))
            raiz_int = int(sqrt(sum(q_perfeito[b][-2:])))
            if raiz_q != raiz_int and b < n:
                print("ok1")
                raiz_q = sqrt(sum(q_perfeito[b][-2:]))
                raiz_int = int(sqrt(sum(q_perfeito[b][-2:])))
                q_perfeito[b].pop()
                b += 1
                if b >= n:
                    b = 0
                q_perfeito[b].append(a)
                b = 0
                a += 1
                q_perfeito[b].append(a)
                b += 1
                while raiz_q != raiz_int and b < n:
                    raiz_q = sqrt(sum(q_perfeito[b][-2:]))
                    raiz_int = int(sqrt(sum(q_perfeito[b][-2:])))
                    b += 1
                    if b >= n:
                        b = 0
                    a += 1
                    q_perfeito[b].append(a)
                    if raiz_q == raiz_int:
                        q_perfeito[b].pop()
                        b -= 1
                        q_perfeito[b].append(a)
                        a += 1
                        b = 0
                        flag = 1
                        break
                    print(q_perfeito, b)
                    sleep(3)
            raiz_q = sqrt(sum(q_perfeito[b][-2:]))
            raiz_int = int(sqrt(sum(q_perfeito[b][-2:])))
            if raiz_q == raiz_int and flag == 0:
                print("ok2")
                q_perfeito[b].append(a)
                a += 1
                raiz_q = sqrt(sum(q_perfeito[b][-2:]))
                raiz_int = int(sqrt(sum(q_perfeito[b][-2:])))
                while raiz_q == raiz_int:
                    raiz_q = sqrt(sum(q_perfeito[b][-2:]))
                    raiz_int = int(sqrt(sum(q_perfeito[b][-2:])))
                    print(q_perfeito, b, raiz_q, raiz_int)
                    print(q_perfeito[b][-2::])
                    if raiz_q == raiz_int:
                        q_perfeito[b].append(a)
                        a += 1
                    raiz_q = sqrt(sum(q_perfeito[b][-2:]))
                    raiz_int = int(sqrt(sum(q_perfeito[b][-2:])))
                    if raiz_q != raiz_int:
                        q_perfeito[b].pop()
                        a -= 1
                        break
                    print(q_perfeito, b, raiz_q, raiz_int)
                    print(q_perfeito[b][-2::])
                    sleep(3)

                a -= 1
                b += 1
            flag = 0
        print(q_perfeito)


torre_de_hanoi_novamente()
