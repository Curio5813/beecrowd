def figurinhas_da_copa():
    """
    Esta função calcula o número de figurinhas carimbadas, e mais
    difíceis de se encontrar, que faltam para completar o álbum da
    copa.
    :return:
    """
    lc, la, cont = [], [], 0
    entrada = list(map(int, input().split()))
    lc = list(map(int, input().split()))
    fig = list(map(int, input().split()))
    for i in range(0, len(fig)):
        if fig[i] not in la:
            la.append(fig[i])
    for k in range(0, len(la)):
        if la[k] in lc:
            cont += 1
    print(len(lc) - cont)


figurinhas_da_copa()
