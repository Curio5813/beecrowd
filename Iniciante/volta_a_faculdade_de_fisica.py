def cinematica():
    """
    Esta função calcula a velocidade de uma partícula qualquer,
    que sofre uma aceleração constante, e com o dobro do tempo
    em dada tragetória.
    :return:
    """
    while True:
        try:
            vi, tf, = input().split(' ')
            vi = int(vi)
            tf = int(tf)
            if tf == 0:
                print(0)
            elif tf > 0:
                a = vi / tf
                vf = a * tf + vi
                s = vf * tf
                print(int(s))
        except EOFError:
            break


cinematica()

