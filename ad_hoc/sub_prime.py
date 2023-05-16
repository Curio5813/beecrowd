def sub_prime():
    """
    Esta função retorna um caracter "S" ou "N". Se sim, "S", o banco
    será capaz de pagar seus empréstimos, caso contrário, se não, "N",
    o banco não será capaz de pagar seus empréstimos.
    :return:
    """
    while True:
        b_reserv, val, b_val, asw = [], [], [], ""
        dados = input().split(" ")
        b, n = int(dados[0]), int(dados[1])
        if b == 0 and n == 0:
            break
        reserv = input().split(" ")
        for i in reserv:
            b_reserv.append(int(i))
        for i in range(n):
            val = input().split(" ")
            b_val.append(val)
        for i in range(0, len(b_val)):
            for k in range(0, len(b_val[i])):
                b_val[i][k] = int(b_val[i][k])
        for i in range(0, len(b_val)):
            for k in range(0, len(b_val[i])):
                idx = b_val[i][1] - 1
                b_reserv[i] -= b_val[i][-1]
                if i >= len(b_reserv) - 1:
                    break
                b_reserv[idx] += b_val[i][-1]
                break
        if sum(b_reserv) >= 0:
            print("S")
        elif sum(b_reserv) < 0:
            print("N")


sub_prime()
