def main():
    """
    Ler um número inteiro N e calcular todos os seus divisores.
    """
    div, divisores = 1, []
    n = int(input())
    while div <= n:
        if n % div == 0:
            divisores.append(div)
        div += 1
    for k in range(0, len(divisores)):
        print(divisores[k])


if __name__ == '__main__':
    main()
