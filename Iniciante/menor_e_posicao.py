def main():
    """
    Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia
    cada um dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor,
    mostrando esta informação.
    """
    n = int(input())
    x = input()
    x = x.split()
    for k in range(0, len(x)):
        x[k] = int(x[k])
    menor = x[0]
    posicao = 0
    for k in range(1, len(x)):
        if x[k] < menor:
            menor = x[k]
            posicao = k
    print(f'Menor valor: {menor}\n'
          f'Posicao: {posicao}')


if __name__ == '__main__':
    main()
