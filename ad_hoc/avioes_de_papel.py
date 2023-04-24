def avioes_de_papel():
    """
    Esta função retorna printando uma string "S", caso
    seja possível construir aviões de papel com as folhas
    compradas e o número de aviões de papel que cada
    competidor deve construir, ou, "N", caso não seja possível.
    :return:
    """
    ent = input().split(" ")
    c, p, f = int(ent[0]), int(ent[1]), int(ent[2])
    if c * f <= p:
        print("S")
    elif c * f > p:
        print("N")


avioes_de_papel()
