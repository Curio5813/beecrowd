def um_problema_facil():
    """
    Esta função recebe um valor de entrada, calcula e imprime
    a base mínima numérica para o valor dado.
    :return:
    """
    while True:
        try:
            bases = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
            n = input()
            aux, maior, bol = 0, 0, 1
            for i in range(0, len(n)):
                aux = bases.index(n[i]) + 1
                maior = aux
            print(maior)
        except EOFError:
            break


um_problema_facil()
