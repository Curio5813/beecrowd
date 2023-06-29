from statistics import mean
from math import sqrt, floor, ceil


def precisao_do_sensor():
    """
    Esta função calcula a precisão de um sensor, ou mais
    especificamente, o desvio padrão entorno da média. Tendo
    como valores de entrada as medidas obitidas e de saída
    o desvio padrão.
    :return:
    """
    h, m = map(int, input().split(" "))
    t = floor((h * 60) / m)
    med = list(map(float, input().split(" ")))
    media = mean(med)
    soma = 0
    for i in range(0, len(med)):
        soma += (med[i] - media) ** 2
    desvp = sqrt(soma / (t - 1))
    print(f"{desvp:.5f}")


precisao_do_sensor()
