def encaixa_ou_nao_i():
    """
    Paulinho tem em suas mãos um pequeno problema. A professora lhe
    pediu que ele construísse um programa para verificar, à partir
    de dois valores inteiros A e B, se B corresponde aos últimos
    dígitos de A.

    A entrada consiste de vários casos de teste. A primeira linha
    de entrada contém um inteiro N que indica a quantidade de casos
    de teste. Cada caso de teste consiste de dois inteiros
    A (1 ≤ A < 231 ) e B (1 ≤ B < 231) positivos. Para cada caso de
    entrada imprima uma mensagem indicando se o segundo valor encaixa
    no primeiro valor, confome exemplo abaixo.
    :return:
    """
    n = int(input())
    for i in range(n):
        a, b = input().split(" ")
        a = a[::-1]
        b = b[::-1]
        c = len(b)
        if a[0:c] == b:
            print("encaixa")
        else:
            print("nao encaixa")


encaixa_ou_nao_i()
