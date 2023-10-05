def as_duas_torres():
    """
    Esta função calcula a quantidade de magia (sinal)
    necessária para que seja estabelecida a comuniação
    entre os Palantír's, que é obitida dividindo a distância
    entre as duas cidades, pela soma do diâmetro dos mesmos.
    A entrada é composta por 3 inteiros, N(0 < N < 10000),
    X e Y(0 < X, Y < 100), que indicam, respectivamente, a
    distância entre os Palantír, o diâmetro do Palantír de
    Sauron e o diâmetro do Palantír de Saruman. A saída é um
    valor real indicando o ICM da comunicação dos Palatír de
    Sauron e Saruman, com 2 casas decimais.
    :return:
    """
    n, x, y = map(int, input().split(" "))
    icm = n / (x + y)
    print(f"{icm:.2f}")


as_duas_torres()
