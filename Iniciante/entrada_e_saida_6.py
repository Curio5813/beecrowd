def entrada_e_saida_6():
    """
    Esta função pega um numero decimal com três casa decimais, em formato, por exemplo,
    XXXXXX.YYY e inverte a saída para YYY.XXXXXX.
    :return:
    """
    num = input().split(".")
    if num[1][0][0] == "0":
        print(f"{num[1][1::]}.{num[0]}")
    else:
        print(f"{num[1]}.{num[0]}")


entrada_e_saida_6()
