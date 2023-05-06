def sub_prime():
    """
    Esta função retorna um caracter "S" ou "N". Se sim, "S", o banco
    será capaz de pagar seus empréstimos, caso contrário, se não, "N",
    o banco não será capaz de pagar seus empréstimos.
    :return:
    """
    while True:
        dados = input().split(" ")
        b, n = int(dados[0]), int(dados[1])
        if b == 0 and n == 0:
            break
        reservas = input().split(" ")
        r1, r2, r3 = int(reservas[0]), int(reservas[1]), int(reservas[2])
        sum_d, sum_v = r1, r3
        for i in range(0, len(reservas)):
            val = input().split(" ")
            d, c, v = int(val[0]), int(val[1]), int(val[2])
            sum_d += d
            sum_v += v
        if sum_d >= sum_v:
            print("S")
        else:
            print("N")


sub_prime()
