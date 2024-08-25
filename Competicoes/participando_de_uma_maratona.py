def participando_de_uma_maratona():
    """
    :return:
    """
    r = int(input())
    (corredores, fotos, instantes, instantes2, querys, temp, descarte, maior,
     sucesso, descarte) = [], [], [], [], [], [], 0, 0, 0, 0
    for i in range(r):
        corredor = list(map(int, input().strip().split(" ")))
        corredores.append(corredor)
    p = int(input())
    for i in range(p):
        foto = list(map(int, input().strip().split(" ")))
        fotos.append(foto)
        ultimo = fotos[i][2]
        if ultimo > maior:
            maior = ultimo
    q = int(input())
    for i in range(q):
        query = list(map(int, input().strip().split(" ")))
        querys.append(query)
    for i in range(0, len(corredores)):
        tempo = corredores[i][0]
        posicao = corredores[i][1]
        while posicao <= maior:
            temp.append(tempo)
            temp.append(posicao)
            tempo += 1
            posicao += corredores[i][1]
            if temp not in instantes:
                instantes.append(temp)
            temp = []
    for i in range(0, len(querys)):
        instantes2 = instantes.copy()
        tempo = querys[i][0]
        posicao = querys[i][1]
        while posicao <= maior:
            temp.append(tempo)
            temp.append(posicao)
            tempo += 1
            posicao += querys[i][1]
            if temp not in instantes:
                instantes2.append(temp)
            temp = []
        for j in range(0, len(fotos)):
            for k in range(0, len(instantes)):
                if instantes2[k][0] == fotos[j][0] and fotos[j][1] <= instantes2[k][1] <= fotos[j][2]:
                    sucesso += 1
        print(sucesso)
        # print(descarte)
        sucesso = 0
        descarte = 0
    # print(querys)
    # print(fotos)
    # print(instantes)


participando_de_uma_maratona()
