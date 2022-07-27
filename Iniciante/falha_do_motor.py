def main():
    """
    Ao observar a curva de velocidade de um motor, o engenheiro Zé percebeu que sempre
    ocorria uma queda quando as medidas eram feitas em intervalos de 10 ms. Mas esta
    queda acontecia em medidas diferentes a cada novo teste do motor.

    Zé ficou curioso com essa falta de padrão e quer saber, para cada teste do motor,
    qual a primeira medida em que ocorre uma queda de velocidade.

    Entrada
    A entrada é um teste do motor e é dada em duas linhas. A primeira tem o número N
    de medidas de velocidade do motor (1 < N ≤ 100). A segunda linha tem N inteiros:
    o número de RPM (rotações por minuto) Ri de cada medida (0 ≤ Ri ≤ 10000, para todo
    Ri, tal que 1 ≤ i ≤ N). Uma medida é considerada uma queda se é menor que a medida
    anterior.

    Saída
    A saída é o índice da medida em que houve a primeira queda de velocidade no teste.
    Caso não aconteça uma queda de velocidade a saída deve ser o número zero.
    """
    r, indice = [], []
    n = int(input())
    r = [int(x) for x in input().split()]
    for k in range(0, len(r)):
        if k >= 1:
            if r[k - 1] > r[k]:
                indice.append(k + 1)
    if len(indice) > 0:
        print(indice[0])
    else:
        print(0)


if __name__ == '__main__':
    main()
