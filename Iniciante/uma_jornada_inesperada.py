def uma_jornada_inesperada():
    """
    Esta função calcula quantos dias levam para que Bilbo, Gandalf e
    os anões, levam para chegar da Vila dos Hobbits até a Montanha
    Solitária. O calculo se dá dividindo o número de anões, além
    de Bilbo e Gandalf, pela distância entre a Vila dos Hobbits e
    a Montanha Mágica.
    :return:
    """
    n, x = map(int, input().split(" "))
    dias = x / (n + 2)
    print(f"{dias:.2f}")


uma_jornada_inesperada()
