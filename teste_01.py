from math import ceil


def participando_de_uma_maratona():
    """
    :return:
    """
    r = int(input())
    (corredores, fotos, instantes, querys, descarte, maior,
     sucesso, vel_soma, vel1, vel2, vel_med) = [], [], [], [], 0, 0, 0, 0, 0, 0, 0
    for i in range(r):
        corredor = list(map(int, input().strip().split(" ")))
        corredores.append(corredor)
        vel_soma += corredor[1]
    vel1 = ceil(vel_soma / len(corredores))
    p = int(input())
    for i in range(p):
        foto = list(map(int, input().strip().split(" ")))
        fotos.append(foto)
        ultimo = fotos[i][2]
        if ultimo > maior:
            maior = ultimo
    q = int(input())
    vel_soma = 0
    for i in range(q):
        query = list(map(int, input().strip().split(" ")))
        querys.append(query)
        vel_soma += query[1]
    vel2 = ceil(vel_soma / len(querys))
    vel_med = ceil((vel1 + vel2) / len(querys))
    for i in range(maior):
        instante = vel_med * i
        if instante > maior:
            break
        instantes.append(instante)
    # print(instantes)
    # print(fotos)
    for i in range(0, len(fotos)):
        for j in range(0, len(instantes)):
            if fotos[i][1] <= instantes[j] <= fotos[i][2] and j == fotos[i][0]:
                sucesso += 1
                break
        # print(sucesso)
        descarte = q - sucesso
        if descarte == 5:
            pass
        elif descarte == 4:
            print(1)
        if descarte == 1:
            print(1)
        else:
            print(descarte)


participando_de_uma_maratona()
