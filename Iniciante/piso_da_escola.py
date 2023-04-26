def piso_da_escola():
    """
    Esta função calcula quantas lajotas do tipo 1 e
    lajotas do tipo 2 são necessários para cobrir o
    piso da escola.
    :return:
    """
    largura = int(input())
    comprimento = int(input())
    lajota1 = largura * comprimento + (largura - 1) * (comprimento - 1)
    lajota2 = (largura - 1) * 2 + (comprimento - 1) * 2
    print(lajota1)
    print(lajota2)


piso_da_escola()
