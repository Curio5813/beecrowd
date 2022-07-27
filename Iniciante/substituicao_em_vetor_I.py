def main():
    """
    Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos
    do vetor X por 1. Em seguida mostre o vetor X.
    """
    vetor = []
    x = int(input())
    vetor.append(x)
    while len(vetor) < 10:
        x = int(input())
        vetor.append(x)
    for k in range(0, 10):
        if vetor[k] <= 0:
            vetor.insert(k, 1)
            vetor.pop(k + 1)
        print(f'X[{k}] = {vetor[k]}')


if __name__ == '__main__':
    main()
