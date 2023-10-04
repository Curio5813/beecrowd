def bobo_da_corte():
    """
    Esta função calcula o numero de votos recebidos pelos candidatos
    a bobo da corte de um Reino. Carlos é um dos candidatos e o primeiro
    a se incriver no concurso. Caso o número de votos do comediante
    Carlos seja igual ou maior do que todos os outros candidatos, tomados
    individualmente, então o programa deve imprimir "S", caso contrário,
    "N".
    :return:
    """
    n = int(input())
    l1, maior = [], 0
    for i in range(n):
        v = int(input())
        l1.append(v)
    idx = l1.index(max(l1))
    if idx == 0:
        print("S")
    else:
        print("N")


bobo_da_corte()
