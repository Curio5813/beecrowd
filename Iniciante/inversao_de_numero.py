def inversao_de_numero():
    """
    Leia um número com 3 dígitos e imprima ele invertido.
    :return:
    """
    num = int(input())
    str_num = str(num)
    print(f"Invertido = {str_num[::-1]}")


inversao_de_numero()
