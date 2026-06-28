def tacografo():
    """
    Esta função calcula e retorna um printe com a distância
    total percorrida por um determinado caminhões dado suas
    velocidades e o intervalos de tempo.
    :return:
    """
    n = int(input())
    km = 0
    for k in range(n):
        t, v = input().split(" ")
        t, v = int(t), int(v)
        km += v * t
    return print(km)


tacografo()
