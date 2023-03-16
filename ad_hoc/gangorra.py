def gangorra():
    """
    Esta função calcula o equilíbrio de uma gangorra onde duas
    crianças brincam. E mostra através da formula P1 * C1 = P2 * C2,
    onde, P1 e C1 é o peso da criança e o comprimento da gangorra do
    lado esquerdo. P2 e C2 é o peso da criança e comprimento da gangorra
    do lado direito. Se a gangorra estiver equilibrada, imprima "0".
    Se estiver desequilibra de modo que a criança que a criança do lado
    esquerdo estja na parte imprima -1, caso contrário imprima 1.
    """
    p1, c1, p2, c2 = input().split(" ")
    p1, c1, p2, c2 = int(p1), int(c1), int(p2), int(c2)
    if p1 * c1 == p2 * c2:
        print(0)
    elif p1 * c1 > p2 * c2:
        print(-1)
    else:
        print(1)


gangorra()
