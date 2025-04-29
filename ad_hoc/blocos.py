def blocos():
    """
    Na descrição do problema AD-HOC 1331.
    :return:
    """
    t = int(input())
    caso = 0
    for i in range(t):
        n = int(input())
        caso += 1
        str_caixas, maior1, maior2, maior3, cont = "", 0, 0, 0, 0
        caixas = list(input().split(" "))
        for j in range(0, len(caixas)):
            str_caixas += caixas[j]
        for j in range(0, len(str_caixas)):
            caixa1, caixa2, caixa3, = 0, 0, 0
            maior1, maior2, maior3 = 0, 0, 0
            idx1_i, idx1_f, idx2_i, idx2_f, idx3_i, idx3_f = 0, 0, 0, 0, 0, 0
            for k in range(0, len(str_caixas)):
                if str_caixas[k] == '1':
                    caixa1 += 1
                    if caixa1 > maior1:
                        maior1 = caixa1
                        idx1_f = k + 1
                        idx1_i = idx1_f - maior1
                else:
                    caixa1 = 0

                if str_caixas[k] == '2':
                    caixa2 += 1
                    if caixa2 > maior2:
                        maior2 = caixa2
                        idx2_f = k + 1
                        idx2_i = idx2_f - maior2
                else:
                    caixa2 = 0

                if str_caixas[k] == '3':
                    caixa3 += 1
                    if caixa3 > maior3:
                        maior3 = caixa3
                        idx3_f = k + 1
                        idx3_i = idx3_f - maior3
                else:
                    caixa3 = 0

            if maior1 >= maior2 and maior1 >= maior3 and maior1 > 0:
                cont += len(str_caixas[idx1_i:idx1_f]) ** 2
                str_caixas = str_caixas[:idx1_i] + str_caixas[idx1_f:]
            elif maior2 >= maior1 and maior2 >= maior3 and maior2 > 0:
                cont += len(str_caixas[idx2_i:idx2_f]) ** 2
                str_caixas = str_caixas[:idx2_i] + str_caixas[idx2_f:]
            elif maior3 >= maior1 and maior3 >= maior2 and maior3 > 0:
                cont += len(str_caixas[idx3_i:idx3_f]) ** 2
                str_caixas = str_caixas[:idx3_i] + str_caixas[idx3_f:]
            else:
                break
        print(f"Case {caso}: {cont}")


blocos()
