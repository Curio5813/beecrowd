from math import sin, cos, sqrt


def angry_ducks():
    """
    Em uma terra distante existem duas cidades, a Nlogônia onde vivem os
    Nlogoneses, e Ducklogônia onde vivem seus vizinhos os Duckneses, já
    à algum tempo estas duas cidades estão em guerra e agora em uma tentativa
    de ganhar a guerra os Duckneses pretendem atacar a cidade da Nlogônia com
    um bodoque que atira patos, porem para que não haja erro eles pediram que
    você construa um programa que dados os valores da altura do bodoque (h), os
    pontos onde inicia (p1) e onde termina (p2) a cidade da Nlogônia, o ângulo
    do disparo ( α) e a velocidade do lançamento, calcule se o projetil atingira
    o alvo.

    Para os cálculos assuma que a aceleração da gravidade é g = 9.80665 e que
    π = 3.14159.

    Entrada
    Existem vários casos de teste, cada caso inicia com 1 valor de ponto flutuante
    h (1 ≤ h ≤ 150) indicando a altura do bodoque, a próxima linha contem 2 valores
    inteiros p1 e p2 (1 ≤ p1, p2 ≤ 9999) indicando onde inicia e onde termina a Nlogônia,
    a linha seguinte contem um inteiro n (1 ≤ n ≤ 100) indicando o numero de tentativas
    que serão feitas para acertar a Nlogônia, as n linhas seguintes contem dois valores
    de ponto flutuante com os valores do ângulo α (1 ≤ α ≤ 180) e a velocidade V (1 ≤ V ≤ 150)
    do disparo.

    O final do arquivo de entrada é determinado por EOF.

    Saída
    Para cada disparo, seu programa deve imprimir uma única linha no seguinte formato, “X -> DUCK”
    para quando o pato acertar a Nlogônia ou “X -> NUCK” quando o pato não acertar a Nlogônia, onde
    X eh a distancia máxima que o projetil atingiu até chegar ao chão (Y=0). X deve ser impresso
    com 5 casas decimais.
    :return:
    """
    while True:
        try:
            h = float(input())
            p1, p2 = input().split(" ")
            p1, p2 = int(p1), int(p2)
            n = int(input())
            g = 9.80665
            pi = 3.14159
            for i in range(n):
                angle, v0 = input().split(" ")
                angle, v0 = float(angle), float(v0)
                angle = (pi / 180) * angle
                v0x = v0 * cos(angle)
                v0y = v0 * sin(angle)
                # Equação do movimento no espaço hiperbólico, ou a parábola da parábola, que dá uma mantissa
                # para números irracionais. Muito usado na operação de satélites artificais.
                # Sua resultante é x⁴ + 2x = 0
                t = (v0y/g) + (sqrt((v0y ** 2) + 4 * (1/2) * g * h) / (2 * (1/2) * g))
                dmax = v0x * t
                if p1 <= dmax <= p2:
                    print(f"{dmax:.5f} -> DUCK")
                else:
                    print(f"{dmax:.5f} -> NUCK")
        except EOFError:
            break


angry_ducks()
