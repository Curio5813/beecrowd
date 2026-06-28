def sedex():
    """
    Esta função calcula se uma determinada bola de boliche, dado
    seu diâmetro, cabe dentro de uma caixa que será usada para
    transportar a bola até a "Só Boliche Cascavel", sabendo as
    dimensões de largura, altura e profundidade da caixa.
    :return:
    """
    n = int(input())
    a, l, p = input().split(" ")
    a, l, p = int(a), int(l), int(p)
    if a < n or l < n or p < n:
        print("N")
    else:
        print("S")


sedex()
