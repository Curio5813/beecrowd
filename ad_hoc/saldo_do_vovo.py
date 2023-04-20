def saldo_do_vovo():
    """
    A função calcula o menor saldo da conta bancária do vovô,
    retornando um printe desse saldo.
    :return:
    """
    l1 = []
    num = input().split(" ")
    d = int(num[0])
    s = int(num[1])
    for i in range(d):
        m = int(input())
        s += m
        l1.append(s)
    if len(l1) == 0:
        return print(s)
    elif len(l1) > 0:
        return print(min(l1))


saldo_do_vovo()
