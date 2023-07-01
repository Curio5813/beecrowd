def digitos():
    """
    Esta função calcula o número de digitos de um número "n"
    elevado a "m".
    :return:
    """
    c = int(input())
    for i in range(c):
        n, m = map(int, input().split(" "))
        power = n ** m
        power = str(power)
        print(len(power))


digitos()
