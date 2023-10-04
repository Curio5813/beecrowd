def balao_de_honra():
    """
    Esta função imprime a posição de uma Letra no Alfabeto.
    a Entrada consiste Um único caracter L, uma letra maiúscula
    ('A'-'Z') do alfabeto. A saída é um inteiro, que representa
    a posição da letra no alfabeto.
    :return:
    """
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letra = input()
    print(alfabeto.index(letra) + 1)


balao_de_honra()
