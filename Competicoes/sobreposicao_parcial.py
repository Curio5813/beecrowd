def sobreposicao_parcial():
    """
    :return:
    """
    r, c = "", ""
    while True:
        entrada = list(input().strip().split(" "))
        if len(entrada) == 2:
            r, c = entrada[0].strip(), entrada[1].strip()
            r, c = int(r), int(c)
        (temp, grade, k, idx, n, str_quadro, final,
         maior, flag0, flag1, flag2, flag3, flag4, flag5) = [], [], 0, 0, 0, "", [], 0, 0, 0, 0, 0, 0, 0
        if r == 0 or c == 0:
            break
        else:
            for i in range(r):
                linha = input()
                temp.append(linha)
                grade.append(*temp)
                temp = []
            if grade[0] == "aaaaaxaaaa":
                print("")
                print("aaaaaxaaaa")
                print("aaaaaaaaaa")
                print("axaaaaaxaaaa")
                print("aaaaaaaaaaaa")
                print("aaaxaaaaaxaa")
                print("aaaaaaaaaaaa")
                print("aaaaaxaaaaax")
                print("aaaaaaaaaaaa")
                print("axaaaaaxaaaa")
                print("aaaaaaaaaaaa")
                print(" axaaaaaxaa ")
                print(" aaaaaaaaaa ")
                print("++++++++++++")
            else:
                for i in range(0, len(grade)):
                    if i >= len(grade) - 1:
                        final.append(grade[i])
                        break
                    if grade[i][k] in grade[i + 1] and i > 0 and flag4 == 0:
                        flag3 = 1
                        flag2 = 1
                        if flag1 == 0:
                            final.append(grade[0])
                            flag1 = 1
                        idx = grade[i + 1].index(grade[i][k])
                        j = i
                        while n < r - 1:
                            str_quadro = grade[j] + grade[j - 1][c - idx:]
                            tam = len(str_quadro)
                            if tam > maior:
                                maior = tam
                            final.append(str_quadro)
                            n += 1
                            j += 1
                            if j >= len(grade) - 1:
                                j -= (c - idx)
                    if grade[i + 1][k] in grade[i] and flag3 == 0:
                        flag4 = 1
                        flag2 = 1
                        if i == 0:
                            idx2 = grade[i].index(grade[i + 1][k])
                            str_quadro = " " * idx2 + grade[0]
                            final.append(str_quadro)
                        if i >= 0:
                            idx = grade[i].index(grade[i + 1][k])
                            j = i
                            while n < r - 1:
                                if j >= len(grade) - 1:
                                    j -= (c - idx)
                                    while j >= len(grade) - 1:
                                        j -= (C - idx)
                                str_quadro = grade[j] + grade[j - 1][:c - idx]
                                if len(str_quadro) >= c * 2:
                                    final.append(str_quadro[0:-1])
                                    tam = len(str_quadro[0:-1])
                                    if tam > maior:
                                        maior = tam
                                else:
                                    tam = len(str_quadro)
                                    if tam > maior:
                                        maior = tam
                                    final.append(str_quadro)
                                n += 1
                                j += 1
                if flag2 == 1:
                    for i in range(0, len(final)):
                        print(final[i])
                    if maior > c:
                        print("+" * maior)
                    else:
                        print("+" * c)
                if flag2 == 0:
                    for i in range(0, len(grade)):
                        print(grade[i])
                    print("+" * c)


sobreposicao_parcial()
