def problema_no_elevador():
    """
    Esta função calcula e retorna imprimindo o número de aperto nos botões
    de um elevador que apenas tem os botões up and down para chegar
    ao andar desejado, partindo de um andar dado, o número de andares
    do edifícil, e quantos andares sobe quando aperta o botão up e desce
    quando aperta botão down. Se não for possível chegar de elevador printar
    a mensagem "use the stairs"
    :return:
    """
    f, s, g, u, d = input().split(" ")
    f, s, g, u, d = int(f), int(s), int(g), int(u), int(d)
    cont = 0
    if s < g:
        while s != g:
            s += u
            cont += 1
            if s > g:
                s -= d
                cont += 1
            if cont >= 1_000_000:
                return print("use the stairs")
        return print(cont)
    elif s > g:
        while s != g:
            s -= d
            cont += 1
            if s < g:
                s += u
                cont += 1
            if cont >= 1_000_000:
                return print("use the stairs")
        return print(cont)
    elif s == g:
        return print(cont)


problema_no_elevador()
