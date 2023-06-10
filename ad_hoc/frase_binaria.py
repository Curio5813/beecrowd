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
                for i in range(0, len(binary), 8):
                    # Convert 8 bits of binary to decimal and then to an ASCII character
                    decimal = int(binary, 2)
                    ascii_char = chr(decimal)
                    # Add ASCII character to the string
                    ascii_str += ascii_char
            print(ascii_str)
        except EOFError:
            break


frase_binaria()
