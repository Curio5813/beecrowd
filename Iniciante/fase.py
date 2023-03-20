def fase():
    """
    Está funcão calcula e printa o número mínimo de competidores
    que passaram para nova fase da Olimpíada Brasileira de Informática
    (OBI).
    :return:
    """
    n = int(input())
    k = int(input())
    compt, cont = [], k
    for i in range(n):
        p = int(input())
        compt.append(p)
    compt.sort()
    compt = compt[::-1]
    if len(compt) <= k:
        return print(len(compt))
    elif compt[k - 1] == compt[k]:
        while compt[k - 1] == compt[k]:
            if k >= len(compt) - 1:
                cont += 1
                break
            cont += 1
            k += 1
    print(cont)


fase()
