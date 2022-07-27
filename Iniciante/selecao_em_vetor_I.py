def main():
    """
    Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam
    um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.
    """
    vetor = []
    x = float(input())
    vetor.append(x)
    while len(vetor) < 100:
        x = float(input())
        vetor.append(x)
    for k in range(0, len(vetor)):
        if vetor[k] <= 10:
            print(f'A[{k}] = {vetor[k]:.1f}')


if __name__ == '__main__':
    main()
