from math import sqrt, pi, acos, sin


def flores_coloridas():
    """
    Esta função calcula as areas plantadas em um jardim circular,
    com girassóis (em amarelo), no círculo maior, violetas (azuis),
    no triangulo inscrito no círculo com girassóis e rosas (vermelha),
    e de um circulo inscrito no triangulo. e retorna o valor de cada uma
    dessas áreas plantadas, ou seja, a area plantada de girassóis,
    a area plantada de violetas e a area planta de rosas.
    :return:
    """
    while True:
        try:
            a, b, c = input().split(" ")
            a, b, c = int(a), int(b), int(c)
            # Formula de Henron para calcular a área do triângulo.
            # p é a metade do perímetro.
            p = (a + b + c) / 2
            at = sqrt(p * (p - a) * (p - b) * (p - c))
            # Formula para calcular a área de um círculo inscrito
            # no triangulo dado, que é calculado como o ponto de
            # encontro das bissetrizes dos ângulos de um triângulo,
            # o incentro, um dos pontos notáveis de um triângulo.
            ai, bi, ci = (p - a), (p - b), (p - c)
            mult = ai * bi * ci
            raiz = sqrt(p * mult)
            # Enontrar o raio do círculo menor.
            r1 = raiz / p
            # Calcular a área do círculo menor.
            ac_menor = pi * r1 ** 2
            # Calcular a área do círculo maior, que circunscreve o triângulo
            # dado, tendo como centro do círculo o circuncentro, um dos
            # pontos notáveis de um triângulo, que é o encontro das mediatrizes
            # deste círculo. Usando a Lei dos cossenos: a² = b² + c² - 2bc.cos(â)
            rad = acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
            # Abaixo está a formula para encontar o valor do raio do circulo maior.
            r2 = a / (sin(rad) * 2)
            # Calcular a área do círculo maior.
            ac_maior = pi * r2 ** 2
            print(f"{(ac_maior - at):.4f} {(at - ac_menor):.4f} {ac_menor:.4f}")
        except EOFError:
            break


flores_coloridas()
