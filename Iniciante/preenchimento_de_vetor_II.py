def main():
    """
    Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de
    0 até T-1 repetidas vezes, conforme exemplo abaixo. Imprima o vetor N.
    """
    vetor, n = [], 0
    t = int(input())
    for k in range(0, 1000):
        while n < t:
            vetor.append(n)
            n += 1
            if len(vetor) == 1000:
                break
        if len(vetor) == 1000:
            break
        n = 0
    for k in range(0, len(vetor)):
        print(f'N[{k}] = {vetor[k]}')


if __name__ == '__main__':
    main()
