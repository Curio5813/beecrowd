def main():
    from math import sqrt
    """
    No tower defense Magic and Sword, o jogador pode lançar magias de área para derrotar
    as unidades inimigas. As magias são elementais: fogo, água, ar e terra, e a região
    afetada é determinada por um círculo cujo raio depende do nível da magia.

    A tabela abaixo lista cada magia, o dano e o respectivo raio por nível:

        MAGIA                                DANO        LEVEL1      LEVEL2       LEVEL3
    =====================================================================================
        FIRE    UM METEORO É CONJURADO        200          20          30           50
                PARA ELIMINAR AS UNIDADES
                INIMIGAS.

        WATER   UMA TSUNAMI ARRASTA OS        300          10          25           40
                INIMIGOS COM A FORÇA
                DAS ÁGUAS.

        EARTH   UM TERREMOTO ABALA AS         400          25          55           70
                UNIDADES INIMIGAS,
                CAUSANDO DANO MASSIVO

        AIR     UM TORNADO MINA AS FORÇAS     100          18          38           60
                INIMIGAS COM A VELOCIDADE
                DO AR

    As unidades inimigas são delimitadas por um retângulo de largura w e altura h,
    com canto inferior esquerdo posicionado no ponto (x0, y0). O inimigo sofrerá dano
    caso seu retângulo delimitador tenha qualquer intercessão com a área deﬁnida pelo
    círculo da magia.

    Dada a posição e o retângulo delimitador da unidade inimiga, o centro da explosão
    e o identiﬁcador e o nível da magia, determine o dano sofrido pela unidade. Caso a
    unidade esteja fora do alcance da magia, o dano sofrido é igual a zero.
    
    Entrada
    A entrada consiste em T (1 ≤ T ≤ 1000) casos de teste, onde o valor de T é informado
    na primeira linha da entrada. Cada caso de teste é composto por duas linhas. A
    primeira contém quatro número inteiros que repre-sentam as dimensões w e h (1 ≤ w, h ≤ 1000)
    do retângulo e as coordenadas x0 e y0 (0 ≤ x0, y0 ≤ 1000) do canto inferior esquerdo.
    A segunda linha do caso de teste contém uma string com o identiﬁcador da magia
    (ﬁre para fogo, water para água, earth para terra e air para ar), o nível N desta magia
    (1 ≤ N ≤ 3) e as coordenadas cx e cy (0 ≤ cx, cy ≤ 1000) do centro da área da explosão.

    Saída
    Para cada caso de teste, a saída deve ser o valor do dano recebido pela unidade, seguido
    de uma quebra de linha.
    """
    ident = ['fire', 'water', 'earth', 'air']
    dano = [200, 300, 400, 100]
    t = int(input())
    for k in range(t):
        w, h, x0, y0 = input().split()
        w, h, x0, y0 = int(w), int(h), int(x0), int(y0)
        atck, n, cx, cy = input().split()
        n, cx, cy = int(n), int(cx), int(cy)
        if atck == ident[0] and n == 1:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[0])
            elif cx < x0 and cy < y0 and (sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2)) <= (sqrt(20 ** 2)):
                print(dano[0])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(20 ** 2):
                print(dano[0])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(20 ** 2):
                print(dano[0])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(20 ** 2):
                print(dano[0])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(20 ** 2):
                print(dano[0])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(20 ** 2):
                print(dano[0])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(20 ** 2):
                print(dano[0])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(20 ** 2):
                print(dano[0])
            else:
                print(0)
        elif atck == ident[0] and n == 2:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[0])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(30 ** 2):
                print(dano[0])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(30 ** 2):
                print(dano[0])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(30 ** 2):
                print(dano[0])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(30 ** 2):
                print(dano[0])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(30 ** 2):
                print(dano[0])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(30 ** 2):
                print(dano[0])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(30 ** 2):
                print(dano[0])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(30 ** 2):
                print(dano[0])
            else:
                print(0)
        elif atck == ident[0] and n == 3:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[0])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(50 ** 2):
                print(dano[0])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(50 ** 2):
                print(dano[0])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(50 ** 2):
                print(dano[0])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(50 ** 2):
                print(dano[0])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(50 ** 2):
                print(dano[0])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(50 ** 2):
                print(dano[0])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(50 ** 2):
                print(dano[0])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(50 ** 2):
                print(dano[0])
            else:
                print(0)
        elif atck == ident[1] and n == 1:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[1])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(10 ** 2):
                print(dano[1])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(10 ** 2):
                print(dano[1])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(10 ** 2):
                print(dano[1])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(10 ** 2):
                print(dano[1])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(10 ** 2):
                print(dano[1])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(10 ** 2):
                print(dano[1])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(10 ** 2):
                print(dano[1])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(10 ** 2):
                print(dano[1])
            else:
                print(0)
        elif atck == ident[1] and n == 2:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[1])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[1])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[1])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[1])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[1])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[1])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[1])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[1])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[1])
            else:
                print(0)
        elif atck == ident[1] and n == 3:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[1])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(40 ** 2):
                print(dano[1])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(40 ** 2):
                print(dano[1])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(40 ** 2):
                print(dano[1])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(40 ** 2):
                print(dano[1])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(40 ** 2):
                print(dano[1])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(40 ** 2):
                print(dano[1])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(40 ** 2):
                print(dano[1])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(40 ** 2):
                print(dano[1])
            else:
                print(0)
        elif atck == ident[2] and n == 1:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[2])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[2])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[2])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[2])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[2])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[2])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[2])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[2])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(25 ** 2):
                print(dano[2])
            else:
                print(0)
        elif atck == ident[2] and n == 2:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[2])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(55 ** 2):
                print(dano[2])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(55 ** 2):
                print(dano[2])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(55 ** 2):
                print(dano[2])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(55 ** 2):
                print(dano[2])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(55 ** 2):
                print(dano[2])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(55 ** 2):
                print(dano[2])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(55 ** 2):
                print(dano[2])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(55 ** 2):
                print(dano[2])
            else:
                print(0)
        elif atck == ident[2] and n == 3:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[2])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(70 ** 2):
                print(dano[2])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(70 ** 2):
                print(dano[2])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(70 ** 2):
                print(dano[2])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(70 ** 2):
                print(dano[2])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(70 ** 2):
                print(dano[2])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(70 ** 2):
                print(dano[2])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(70 ** 2):
                print(dano[2])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(70 ** 2):
                print(dano[2])
            else:
                print(0)
        elif atck == ident[3] and n == 1:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[3])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(18 ** 2):
                print(dano[3])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(18 ** 2):
                print(dano[3])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(18 ** 2):
                print(dano[3])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(18 ** 2):
                print(dano[3])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(18 ** 2):
                print(dano[3])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(18 ** 2):
                print(dano[3])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(18 ** 2):
                print(dano[3])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(18 ** 2):
                print(dano[3])
            else:
                print(0)
        elif atck == ident[3] and n == 2:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[3])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(38 ** 2):
                print(dano[3])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(38 ** 2):
                print(dano[3])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(38 ** 2):
                print(dano[3])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(38 ** 2):
                print(dano[3])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(38 ** 2):
                print(dano[3])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(38 ** 2):
                print(dano[3])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(38 ** 2):
                print(dano[3])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(38 ** 2):
                print(dano[3])
            else:
                print(0)
        elif atck == ident[3] and n == 3:
            if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
                print(dano[3])
            elif cx < x0 and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(60 ** 2):
                print(dano[3])
            elif cx < x0 and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(60 ** 2):
                print(dano[3])
            elif cx < x0 and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(60 ** 2):
                print(dano[3])
            elif cx > x0 + w and cy < y0 and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(60 ** 2):
                print(dano[3])
            elif cx > x0 + w and y0 <= cy <= y0 + h and sqrt((x0 + w - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(60 ** 2):
                print(dano[3])
            elif cx > x0 + w and cy > y0 + h and sqrt((x0 - cx) ** 2 + (y0 + h - cy) ** 2) <= sqrt(60 ** 2):
                print(dano[3])
            elif cy < y0 and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(60 ** 2):
                print(dano[3])
            elif cy > y0 + h and x0 <= cx <= cx + w and sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) <= sqrt(60 ** 2):
                print(dano[3])
            else:
                print(0)


if __name__ == '__main__':
    main()
