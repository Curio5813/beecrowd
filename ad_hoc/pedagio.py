def pedagio():
    """
    Esta função calcula os custos de uma viagem considerando
    o desgaste das peças do automóvel e custos com pedágio.
    A função retorna e imprimi o custo total da viagem.
    :return:
    """
    s, d = input().split(" ")
    s, d = int(s), int(d)
    k, p = input().split(" ")
    k, p = int(k), int(p)
    cont, c_total = 0, 0
    c1 = k * s
    while s >= d:
        s -= d
        cont += 1
    c2 = cont * p
    c_total = c1 + c2
    return print(c_total)


pedagio()
