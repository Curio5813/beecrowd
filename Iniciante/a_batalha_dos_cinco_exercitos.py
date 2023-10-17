def a_batalha_dos_cinco_exercitos():
    """
    Está função recebe como entrada 6 inteiros, H, E, A, O, W e X,
    representando o número do exército de humanos, elfos, anões,
    orcs, wargs e águias, respectivamente. Se o número de exércitos
    dos humanos mais dos elfos, anões e águias for maior que dos
    orcs e wargs, o lado do bem vence e saída é um printe
    “Middle-earth is safe.”, se não, “Sauron has returned.”.
    :return:
    """
    h, e, a, o, w, x = map(int, input().split(" "))
    if h + e + a + x > o + w:
        print("Middle-earth is safe.")
    else:
        print("Sauron has returned.")


a_batalha_dos_cinco_exercitos()
