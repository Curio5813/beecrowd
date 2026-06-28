def encaixa_ou_nao_ii():
    """
    Paulinho tem em suas mãos um novo problema. Agora a sua professora
    lhe pediu que construísse um programa para verificar, à partir de
    dois valores muito grandes A e B, se B corresponde aos últimos dígitos
    de A.

    Entrada
    A entrada consiste de vários casos de teste. A primeira linha de entrada
    contém um inteiro N que indica a quantidade de casos de teste. Cada caso
    de teste consiste de dois valores A e B maiores que zero, cada um deles
    podendo ter até 1000 dígitos.

    Saída
    Para cada caso de entrada imprima uma mensagem indicando se o segundo valor
    encaixa no primeiro valor, confome exemplo abaixo.
    :return:
    """
    n = int(input())
    for i in range(n):
        digitos = input().split(" ")
        tam2 = len(digitos[1])
        digitos[0] = digitos[0][::-1]
        digitos[0] = digitos[0][0:tam2]
        digitos[0] = digitos[0][::-1]
        if digitos[1] == digitos[0]:
            print("encaixa")
        else:
            print("nao encaixa")


encaixa_ou_nao_ii()
