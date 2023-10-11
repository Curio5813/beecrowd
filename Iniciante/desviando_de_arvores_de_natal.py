def desviando_de_arvores_de_natal():
    """
    Esta função calcula o numero mínimo de toque necessário
    para percorrer uma determinada distancia 'M', num jogo
    que você deve desviar-se de árvores de natal no caminho.
    :return:
    """
    while True:
        m = int(input())
        aux, obst, cont, pos = [], [], 0, "c"
        if m == 0:
            break
        for i in range(m):
            aux = list(map(int, input().split(" ")))
            obst.append(aux)
        for i in range(0, len(obst)):
            if i == 0:
                cont += 0
                pos = "c"
            elif i == 1:
                if obst[i][0] == 0 and obst[i][1] == 0 and obst[i][2] == 0:
                    cont += 0
                    pos = "c"
                elif obst[i][0] == 1 and obst[i][1] == 0 and obst[i][2] == 0:
                    cont += 0
                    pos = "c"
                elif obst[i][0] == 1 and obst[i][1] == 1 and obst[i][2] == 0:
                    cont += 1
                    pos = "r"
                elif obst[i][0] == 1 and obst[i][1] == 0 and obst[i][2] == 1:
                    cont += 0
                    pos = "c"
                elif obst[i][0] == 0 and obst[i][1] == 1 and obst[i][2] == 1:
                    cont += 1
                    pos = "l"
                elif obst[i][0] == 0 and obst[i][1] == 1 and obst[i][2] == 0 and i < len(obst) - 1:
                    if obst[i + 1][0] == 0 and obst[i + 1][2] == 1:
                        cont += 1
                        pos = "l"
                    elif obst[i + 1] == 1 and obst[i + 1][2] == 0:
                        cont += 1
                        pos = "r"


desviando_de_arvores_de_natal()
