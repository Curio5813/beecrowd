def inseto():
    """
    Esta função calcula o nivel de energia dos seres vivos e
    caso tenham menos de 8000 a funação imprime "Inseto!",
    caso o nível de energia seja maior que 8000, a função
    imprime "Mais de 8000!". A entrada é composta por vários
    casos de teste. A primeira linha contém um número inteiro
    C relativo ao número de casos de teste. Em seguida, haverá
    C linhas, com um número inteiro N (100 <= N <= 100000)
    relativo ao nível de energia de um ser vivo. Para cada valor
    lido, imprima o texto correspondente.
    :return:
    """
    c = int(input())
    for i in range(c):
        n = int(input())
        if n <= 8000:
            print("Inseto!")
        elif n > 8000:
            print("Mais de 8000!")


inseto()
