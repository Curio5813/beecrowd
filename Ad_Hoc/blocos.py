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
        str_caixas, total, temp = "", 0, []
        caixas = list(input().split(" "))
        for j in range(0, len(caixas)):
            str_caixas += caixas[j]
        for j in range(0, len(str_caixas)):
            if j == 0:
                cont = str_caixas.count(str_caixas[j])
                total += cont ** 2
                temp.append(str_caixas[j])
            elif j > 0 and str_caixas[j] not in temp:
                cont = str_caixas.count(str_caixas[j])
                total += cont ** 2
                temp.append(str_caixas[j])
        print(f"Case {caso}: {total}")


blocos()
