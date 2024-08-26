def participando_de_uma_maratona():
    """
    :return:
    """
    r = int(input())
    (corredores, fotos, instantes, instantes2, querys, temp, descarte, maior,
     sucesso) = [], [], [], [], [], [], 0, 0, 0
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
    for i in range(0, len(corredores)):
        tempo = 0
        posicao = 0
        while posicao <= maior:
            if tempo < corredores[i][0]:
                tempo += 1
            elif tempo >= corredores[i][0]:
                tempo += 1
                posicao += corredores[i][1]
            temp.append(tempo)
            temp.append(posicao)
            if temp not in instantes:
                instantes.append(temp)
            temp = []
    q = int(input())
    for i in range(q):
        query = list(map(int, input().strip().split(" ")))
        querys.append(query)
    for i in range(0, len(querys)):
        tempo = 0
        posicao = 0
        instantes2 = instantes.copy()
        while posicao <= maior:
            if tempo < querys[i][0]:
                tempo += 1
            elif tempo >= querys[i][0]:
                tempo += 1
                posicao += querys[i][1]
            temp.append(tempo)
            temp.append(posicao)
            if temp not in instantes2:
                instantes2.append(temp)
            temp = []
        for j in range(0, len(fotos)):
            for k in range(0, len(instantes2)):
                if instantes2[k][0] == fotos[j][0] and fotos[j][1] <= instantes2[k][1] <= fotos[j][2]:
                    sucesso += 1
                    break
        descarte = q - sucesso
        print(descarte)
        # print(fotos)
        # print(instantes2)
        sucesso = 0


participando_de_uma_maratona()
