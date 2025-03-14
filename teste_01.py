import math


def is_perfect_square(n):
    """Verifica se um número é um quadrado perfeito."""
    return math.isqrt(n) ** 2 == n


def max_balls_in_rods(n):
    """Determina o número máximo de bolas que podem ser colocadas nas hastes."""
    rods = [[] for _ in range(n)]  # Inicializa N hastes vazias
    ball = 1

    while True:
        placed = False
        for rod in rods:
            if not rod or is_perfect_square(rod[-1] + ball):
                rod.append(ball)
                placed = True
                break

        if not placed:
            print(rods)
            return ball - 1  # Retorna o número máximo de bolas colocadas

        ball += 1


# Leitura de entrada
t = int(input())
for _ in range(t):
    n = int(input())
    print(max_balls_in_rods(n))

