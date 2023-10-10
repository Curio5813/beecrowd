def conversao_simples_de_base():
    """
    Esta função converte um número hexadecimal em decimal,
    ou um numero decimal em hexadecimal.
    :return:
    """
    while True:
        num = input()
        if num[0:2] == "0x":
            num = int(num, 16)
            print(num)
        else:
            num = int(num)
            if num < 0:
                break
            num = hex(num)
            print(f"{num[0:2]}{num[2::].upper()}")


conversao_simples_de_base()
