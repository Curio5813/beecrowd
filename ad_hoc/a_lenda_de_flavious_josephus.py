def a_lenda_de_flavious_josephus():
    """
    A função calcula a posição da pessoa que a vida
    será salva tendo como paradigma sua posição em
    relação ao número da lista, ou seja, do seus outros
    companheiros.
    """
    nc = int(input())
    c = 0
    for j in range(nc):
        num = list(map(int, input().split(" ")))
        n, a, l2 = num[0], num[1], []
        for i in range(1, n + 1):
            l2.append(i)
        while len(l2) > 1:
            while len(l2) > 1:
                if a > len(l2):
                    a -= len(l2)
                    break
                else:
                    l2.pop(a - 1)
                    a += num[1] - 1
        c += 1
        print(f"Case {c}: {l2[0]}")


a_lenda_de_flavious_josephus()
