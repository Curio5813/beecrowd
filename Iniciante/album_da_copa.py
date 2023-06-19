def album_da_copa():
    """
    Está função recebe como entrada a quantidade total de figurinhas que
    tem o album para colar e a quantidade de figurinhas já comptadas. A
    função printa como saída a quantidade de figurinhas que faltam para
    completar o album.
    :return:
    """
    l1 = []
    n = int(input())
    m = int(input())
    for k in range(m):
        fig = int(input())
        if fig not in l1:
            l1.append(fig)

    print(n - len(l1))


album_da_copa()
