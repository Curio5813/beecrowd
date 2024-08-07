from math import sqrt


def kikoho():
    """
    Todo fã de Dragon Ball conhece o famoso ataque do personagem
    Tenshinhan, o KIKOHO. Recentemente Tenshi, para os íntimos,
    foi batalhar com o guerreiro Cell. Foi uma batalha épica, ele
    conseguiu acertar alguns ataques em Cell, mas infelizmente ele
    não o venceu. Porém ficou satisfeito com a área total que seu
    ataque cobriu. Vamos aderir que o ataque de Tenshi é basicamente
    um triângulo, ele não sabe qual é a área que esse ataque chegou
    a ter, mas ele sabe em quais pontos se encontram os vértices do
    triângulo formado.

    Você pode ajudar Tenshi informando qual a área total que o seu ataque
    teve?

    Veja um exemplo de como é seu ataque e como se assemelha a um triângulo.


    Entrada
    A primeira linha de entrada contém um inteiro N (1 <= N <= 20) representando
    a quantidade de casos de teste. As próximas N linhas contém 3 pares de coordenadas
    no plano cartesiano, (X1, Y1, X2, Y2, X3, Y3) (-700 <= Xi, Yi <= 1000), informando
    os vértices do triângulo que o ataque formou depois de atingir o chão. É garantido
    que os pontos dados formam um triângulo.

    Saída
    A saída deve mostrar qual a área do KIKOHO de Tenshi, com 3 casas decimais.
    :return:
    """
    n = int(input())
    for i in range(n):
        ax, ay, bx, by, cx, cy = map(int, input().strip().split(" "))
        # achar os lados do triângulo usando calculando a distância
        # entre seus vértices.
        l1 = sqrt((ax - bx) ** 2 + (ay - by) ** 2)
        l2 = sqrt((ax - cx) ** 2 + (ay - cy) ** 2)
        l3 = sqrt((bx - cx) ** 2 + (by - cy) ** 2)

        s = (l1 + l2 + l3) / 2  # Semiperimetro do triângulo.

        # Usando a Formula de Henron.
        area = sqrt(s * (s - l1) * (s - l2) * (s - l3))
        print(f"{area:.3f}")


kikoho()
