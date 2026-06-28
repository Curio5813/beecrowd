def sequencia_secreta():
    """
    Esta função calcula o número máximo de sequência entre os números
    1 e 2 sem repetição. A função retorna e printa esse número máximo.
    :return:
    """
    n = int(input())
    # o valor da variável cont começa em 1 para que o código
    # abaixo funcione, mas o problema terá em todas as
    # sequências secretas um valor maior ou igual a 3.
    l1, k, cont = [], 0, 1
    for i in range(n):
        num = int(input())
        l1.append(num)
    b = k + 1
    while k <= len(l1) - 1:
        while l1[k] == 1 and l1[b] != 2 or l1[k] == 2 and l1[b] != 1:
            b += 1
            if b == len(l1) - 1:
                if l1[b - 1] == 1 and l1[b] == 2 or l1[b - 1] == 2 and l1[b] == 1:
                    cont += 1
                    return print(cont)
                else:
                    return print(cont)
        else:
            cont += 1
            k = b
            if k == len(l1) - 2:
                if l1[k] == 1 and l1[k + 1] == 2 or l1[k] == 2 and l1[k + 1] == 1:
                    cont += 1
                    return print(cont)
                else:
                    return print(cont)
    return print(cont)


sequencia_secreta()
