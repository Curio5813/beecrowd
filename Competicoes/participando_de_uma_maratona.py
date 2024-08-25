def participando_de_uma_maratona():
    """
    :return:
    """
    r = int(input())
    (corredores, fotos, instantes, querys, temp, descarte, maior, flag,
     sucesso, descarte) = [], [], [], [], [], 0, 0, 0, 0, 0
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
    for i in range(0, len(querys)):
        tempo = querys[i][0]
        posicao = querys[i][1]
        while posicao <= maior:
            temp.append(tempo)
            temp.append(posicao)
            tempo += 1
            posicao += querys[i][1]
            if temp not in instantes:
                instantes.append(temp)
            temp = []
        for j in range(0, len(fotos)):
            for k in range(0, len(instantes)):
                if instantes[k][0] == fotos[j][0] and fotos[j][1] <= instantes[k][1] <= fotos[j][2]:
                    sucesso += 1
        descarte = q - sucesso
        print(descarte)
        # print(fotos)
        # print(instantes)
        sucesso = 0
        instantes = []


participando_de_uma_maratona()
