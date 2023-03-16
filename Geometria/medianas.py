from math import sqrt


def medianas():
    """
    Esta função calcula a área de um triangulo dados
    os comprimentos de suas medianas.
    """
    while True:
        try:
            a, b, c = input().split(" ")
            a, b, c = float(a), float(b), float(c)
            if a + b <= c or a + c <= b or b + c <= a:
                num_str = "-1.000"
                print(num_str)
            else:
                s = (a + b + c) / 2
                area = (4 / 3) * sqrt(s * (s - a) * (s - b) * (s - c))
                print(f"{area:.3f}")
        except EOFError:
            break


medianas()
