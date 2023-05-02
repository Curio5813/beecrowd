def saida_10():
    """
    Esta função tem como retorno um printe de uma
    imagem que vai da letra A até a letra E, voltando
    depois para letra A.
    :return:
    """
    l1 = ["A", "B", "C", "D", "E", "D", "C", "B", "A"]
    s_antes = "       "
    s_meio = " "
    n, d = -1, 7
    for i in range(0, len(l1)):
        if i == len(l1) - 1:
            print(f"{s_antes}{l1[i]}")
            break
        if i == 0:
            print(f"{s_antes}{l1[i]}")
        elif 0 < i <= 4:
            print(f"{s_antes[0:n]}{l1[i]}{s_meio}{l1[i]}")
            n -= 1
            s_meio += " " * 2
        if n == -5:
            n += 1
        elif 4 < i:
            n += 1
            d -= 2
            print(f"{s_antes[0:n]}{l1[i]}{s_meio[0:d]}{l1[i]}")


saida_10()
