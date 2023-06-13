def frase_binaria():
    """
    Esta função recebe valores binários como entrada e converte
    em caracteres ASCII.
    :return:
    """
    while True:
        try:
            n = int(input())
            ascii_str = ""
            for k in range(n):
                binary = input()
                # Converter binário para base dez.
                decimal = int(binary, 2)
                # Converter numero na base dez em caracteres ASCII.
                ascii_char = chr(decimal)
                ascii_str += ascii_char
            print(ascii_str)
        except EOFError:
            break


frase_binaria()
