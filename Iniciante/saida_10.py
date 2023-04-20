def saida_10():
    """
    Esta função tem como retorno um printe com uma
    imagem qeu vai da letra A até a letra E.
    :return:
    """
    l1 = ["A", "B", "C", "D", "E", "D", "C", "B", "A"]
    s_a = "        "
    s_f = ""
    str_img = ""
    for i in range(len(l1)):
        if i <= 4:
            str_img += s_a + l1[i]

