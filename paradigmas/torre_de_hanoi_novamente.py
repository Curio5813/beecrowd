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
    for i in range(t):
        lista, q_perfeito = [], []
        n = int(input())
        for j in range(n):
            for k in range(n):
                lista.append(0)
                break
            q_perfeito.append(lista)
            lista = []
        bola, idx, idx2, vezes, passos, q, flag = 1, 0, 0, 0, 0, 0, 0
        while flag != 2:
            if bola == 1:
                # print("ok0")
                q_perfeito[idx].append(bola)
                bola += 1
                q_perfeito[idx].append(bola)
            raiz_q = sqrt(sum(q_perfeito[idx][-2:]))
            raiz_int = int(sqrt(sum(q_perfeito[idx][-2:])))
            # print(q_perfeito, idx, raiz_q, raiz_int)
            # sleep(3)
            while raiz_q != raiz_int:
                print("ok1")
                if passos > n:
                    print(bola - 1)
                    flag = 2
                if flag == 0:
                    q_perfeito[idx].pop()
                    idx += 1
                if flag == 1:
                    idx += 1
                    flag = 0
                if idx >= n:
                    idx = 0
                    q_perfeito[idx].append(bola)
                    bola += 1
                else:
                    q_perfeito[idx].append(bola)
                    bola += 1
                    idx = 0
                # print(q_perfeito, idx, raiz_q, raiz_int)
                # print(q_perfeito[idx][-2:])
                # sleep(3)
                raiz_q = sqrt(sum(q_perfeito[idx][-2:]))
                raiz_int = int(sqrt(sum(q_perfeito[idx][-2:])))
            while raiz_q == raiz_int:
                passos = 0
                print("ok2")
                if flag == 0:
                    q_perfeito[idx].append(bola)
                    bola += 1
                if flag == 1:
                    bola += 1
                    flag = 0
                print(q_perfeito)
                # sleep(3)
                raiz_q = sqrt(sum(q_perfeito[idx][-2:]))
                raiz_int = int(sqrt(sum(q_perfeito[idx][-2:])))
                if raiz_q != raiz_int:
                    bola -= 1
                while raiz_q != raiz_int and flag == 0:
                    passos += 1
                    if passos > n:
                        print(bola -1)
                        flag = 2
                        break
                    print("ok3")
                    q_perfeito[idx].pop()
                    idx += 1
                    if flag == 0:
                        if idx >= n:
                            idx = 0
                            q_perfeito[idx].append(bola)
                            vezes += 1
                            if vezes > n and q_perfeito[idx][-2] == 0:
                                print("ok6")
                                print(q_perfeito)
                                vezes = 0
                                flag = 1
                                passos = 0
                                break
                        else:
                            q_perfeito[idx].append(bola)
                            vezes += 1
                            if vezes > n and q_perfeito[idx][-2] == 0:
                                print("ok6")
                                print(q_perfeito)
                                # sleep(3)
                                vezes = 0
                                flag = 1
                                passos = 0
                                break
                        print(q_perfeito)
                        # sleep(3)
                        raiz_q = sqrt(sum(q_perfeito[idx][-2:]))
                        raiz_int = int(sqrt(sum(q_perfeito[idx][-2:])))
                        if raiz_q == raiz_int:
                            passos = 0
                            bola += 1
                            break
                        print(q_perfeito)
                        # sleep(3)


torre_de_hanoi_novamente()
