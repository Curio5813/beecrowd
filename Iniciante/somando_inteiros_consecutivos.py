def main():
    """
    Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A para cada i com os valores
    (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.
    """
    soma = 0
    an = input().split(' ')
    a, n = int(an[0]), int(an[-1])
    for k in range(0, n):
        soma += a + k
    print(soma)


if __name__ == '__main__':
    main()
