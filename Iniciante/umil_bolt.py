def umil_bolt():
    """
    Esta função printa o melhor resultado do dia obtido por Bolt
    em suas sequências de treinamentos diários.
    :return:
    """
    while True:
        try:
            t = int(input())
            l1 = []
            for i in range(t):
                treino = float(input())
                l1.append(treino)
            print(min(l1))
        except EOFError:
            break


umil_bolt()
