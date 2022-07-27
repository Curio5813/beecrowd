def main():
    from decimal import Decimal
    """
    Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. Em cada posição
    subsequente de N (1 até 99), coloque a metade do valor armazenado na posição anterior, conforme
    o exemplo abaixo. Imprima o vetor N.
    """
    vetor, n = [], 0
    x = float(Decimal(input()))
    vetor.append(x)
    while len(vetor) < 100:
        vetor.append(float(Decimal(vetor[n] / 2)))
        n += 1
    for k in range(0, len(vetor)):
        print(f'N[{k}] = {vetor[k]:.4f}')


if __name__ == '__main__':
    main()
