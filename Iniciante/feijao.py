def feijao():
    """
    Esta função calcula a posição do feijão que está dentro
    de um copo opaco, no total são quatro copos alinhados e
    o jogador precisa advinhar em qual copo está o feijão.
    Este programa tem como retorno um printe da posição do
    feijão escondido em um dos copos.
    :return:
    """
    c1, c2, c3, c4 = input().split(" ")
    c1, c2, c3, c4 = int(c1), int(c2), int(c3), int(c4)
    for i in range(4):
        if c1 == 1:
            return print(1)
        elif c2 == 1:
            return print(2)
        elif c3 == 1:
            return print(3)
        elif c4 == 1:
            return print(4)


feijao()
