import decimal

def sequencia_fibo():
    """
    Esta função toma a Sequencia de Fibonnaci como parâmetro
    alterada pela seguinte operações aritméticas, a nova
    sequencia começa com fibo(A) e multiplicado fibo(B). Depois
    faz fibo(A + 1) * fibo(B + 1). O programa termina quando é
    informado A = 0, B = 0 e N = 0.
    :return:
    """
    l1 = []
    raiz = decimal.Decimal(5).sqrt()
    for i in range(0, 100_000_000 + 1):
        fibo = int(((1 + raiz) ** i - (1 - raiz) ** i) / (2 ** i * raiz))
        l1.append(fibo)
    while True:
        l2, soma = [], 0
        a, b, n = input().split(" ")
        a, b, n = int(a), int(b), int(n)
        if a == 0 and b == 0 and n == 0:
            break
        for i in range(n):
            if a >= len(l1) - 1 or b >= len(l1) - 1:
                break
            n = (l1[a] * l1[b]) % 1000000007
            soma += n
            a += 1
            b += 1
        print(soma)


sequencia_fibo()
