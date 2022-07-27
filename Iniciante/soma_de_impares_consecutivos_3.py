def main():
    """
    Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste
    consiste de dois inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir
    de X inclusive o próprio X se ele for ímpar. Por exemplo:
    para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
    para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13
    """
    soma = 0
    n = int(input())
    for k in range(0, n):
        x, y = input().split(' ')
        x, y = int(x), int(y)
        if x % 2 == 1:
            for i in range(x, (y * 2) + x, 2):
                soma += i
        elif x % 2 == 0:
            for i in range(x + 1, (y * 2) + x, 2):
                soma += i
        print(soma)
        soma = 0


if __name__ == '__main__':
    main()
