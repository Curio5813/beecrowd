def sobreposicao_parcial():
    """
    :return:
    """
    while True:
        r, c = map(int, input().split(" "))
        temp, grade, grade_sobre, k, idx, str_quadro, final, maior = [], [], [], 0, 0, "", [], 0
        if r == c == 0:
            break
        else:
            for i in range(r):
                linha = input()
                temp.append(linha)
                grade.append(*temp)
                grade_sobre.append(*temp)
                temp = []
            for i in range(0, len(grade_sobre)):
                print(k)
                if i == 0:
                    final.append(grade[i])
                if i >= len(grade_sobre) - 1:
                    if grade_sobre[i - 1][k] in grade[i]:
                        str_quadro = grade_sobre[i] + grade_sobre[i - 1][idx + 1:]
                        final.append(str_quadro)
                        tamanho = len(str_quadro)
                        if tamanho > maior:
                            maior = tamanho
                    final.append(grade_sobre[i])
                    break
                if grade_sobre[i][k] in grade[i + 1] and i > 0:
                    idx = grade[i + 1].index(grade_sobre[i][k])
                    if 0 < idx <= c:
                        str_quadro = grade_sobre[i] + grade_sobre[i - 1][idx + 1:]
                        tamanho = len(str_quadro)
                        if tamanho > maior:
                            maior = tamanho
                        final.append(str_quadro)
                    else:
                        k += 1
                else:
                    k += 1
            for i in range(0, len(final)):
                print(final[i])
            if maior > c:
                print("+" * maior)
            else:
                print("+" * c)


sobreposicao_parcial()
