def tamanho_da_placa():
    """
    Está função calcula as dimensões da placa de pedais para
    guitarras que uma empresa fabrica e se para cada pedido dos
    clientes se esta empresa pode ou não fabricá-las.
    :return:
    """
    while True:
        try:
            x, y, m = list(map(int, input().split(" ")))
            dim = x * y
            for i in range(m):
                xi, yi = list(map(int, input().split(" ")))
                if xi * yi <= dim:
                    print("Sim")
                else:
                    print("Nao")
        except EOFError:
            break


tamanho_da_placa()
