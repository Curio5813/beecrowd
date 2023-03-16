def flutuacao_do_pib():
    """
    Esta função tem como retorno a flutuação do pib entre
    o primeiro e segundo anos, dado a taxas de variação
    para cada ano.
    :return:
    """
    f1, f2 = input().split(" ")
    f1, f2 = float(f1), float(f2)
    pib_float = (((1 + f1 / 100) * (1 + f2 / 100)) - 1) * 100
    return print(f"{pib_float:.6f}")


flutuacao_do_pib()
