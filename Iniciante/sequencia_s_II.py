def main():
    """
    Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
    S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?
    """
    s, n1, n2 = 0, 0, 2
    for k in range(0, 19):
        s += (1 + n1) / (n2 ** k)
        n1 += 2
    print(f'{s:.2f}')


if __name__ == '__main__':
    main()
