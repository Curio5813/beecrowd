def refrigerante():
    """
    Esta função calcula quanto Tim consegue tomar do máximo de
    refrigerante trocando uma quantidade x de cascos vazios, em
    sua posse e que durante o dia é encontrado, dados como entrada
    do programa, por um novo com refrigerante.
    :return:
    """
    e, f, c = map(int, input().split(" "))
    soma = e + f
    n = 0
    while soma >= c:
        resto = soma % c
        inteiro = soma // c
        soma = resto + inteiro
        n += inteiro
        if soma == 0:
            n += 1
            break
    print(n)


refrigerante()
