def corrida():
    """
    Esta função calcula a onde a garrada de água deve ficar
    em uma pista circular de atletismo para que o atleta
    faça o percurso do treino e termine onde a garrafa está.
    """
    c, n = input().split(" ")
    c, n, cont = int(c), int(n), 0
    if c % n != 0:
        while c % n != 0:
            c -= 1
            cont += 1
        return print(cont)
    else:
        return print(0)


corrida()
