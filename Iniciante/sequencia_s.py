def main():
    """
    Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
    S = 1 + 1/2 + 1/3 + … + 1/100
    """
    s = 0
    for k in range(1, 101):
        s += 1 / k
    print(f'{s:.2f}')


if __name__ == '__main__':
    main()
