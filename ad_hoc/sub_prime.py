def sub_prime():
    """
    Esta função retorna um caracter "S" ou "N". Se sim, "S", o sitema
    bancário será capaz de pagar seus empréstimos, caso contrário, se
    não, "N", o sistema bancário não será capaz de pagar seus empréstimos.
    :return:
    """
    while True:
        v = input().split(" ")
        b, n = int(v[0]), int(v[1])
        print(f"{b} {n}")
        if b == 0 and n == 0:
            break
        resv = list(map(int, input().split(" ")))
        for i in range(b):
            divd = list(map(int, input().split(" ")))
            print(resv)
            if resv[0] + resv[1] - divd[2] >= 0:
                resv[0] = resv[0] + resv[1] - divd[2]
                if i == b - 1:
                    print("S")
            else:
                print("N")
                break


sub_prime()
