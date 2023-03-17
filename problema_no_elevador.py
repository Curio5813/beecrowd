def problema_no_elevador():
    """
    Esta função calcula e retorna o número de aperto nos botões de
    um elevador que apenas tem os botões up and down para chegar
    ao andar desejado, partindo de um andar dado, o número de andares
    do edifícil, e quantos andares sobe quando aperta o botão up e o
    botão down. Se não for possível chegar de elevador printar a
    mensagem "use the stairs"
    :return:
    """
    f, s, g, u, d = input().split(" ")
    f, s, g, u, d = int(f), int(s), int(g), int(u), int(d)


problema_no_elevador()
