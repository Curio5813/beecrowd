def main():
    """
    Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10].
    Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor
    lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.
    """
    vetor = []
    x = int(input())
    vetor.append(x)
    for k in range(0, 10):
        if k > 0:
            vetor.append(vetor[k - 1] * 2)
    for k in range(0, len(vetor)):
        print(f'N[{k}] = {vetor[k]}')


if __name__ == '__main__':
    main()
