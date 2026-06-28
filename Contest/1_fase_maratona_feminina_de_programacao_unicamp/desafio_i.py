def desafio_i():
    bits = list(map(int, input().split(" ")))
    cont = 0
    for i in range(1, len(bits)):
        if bits[i] == 1:
            cont += 1
    if bits[0] == 0 and cont % 2 != 0:
        print("S")
    if bits[0] == 0 and cont % 2 == 0:
        print("N?")
    if bits[0] == 1 and cont % 2 == 0:
        print("S")
    if bits[0] == 1 and cont % 2 != 0:
        print("N?")


desafio_i()
