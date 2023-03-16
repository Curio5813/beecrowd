def numbers_not_divisible_by_2_5():
    """
    Esta função cria uma lista de números inteiros positivos
    que nãa são divisiveis por 2 e por 5.
    :return:
    """
    l1 = []
    for i in range(10_000 + 1):
        if i % 2 != 0 and i % 5 != 0:
            l1.append(i)
    return l1


def ones(l1):
    """
    Esta função printa, dado qualquer inteiro n (1 ≤ n ≤ 10000)
    não divisível por 2 ou por 5, algum múltiplo
    de n que deve ser um número que é uma sequência
    de algarismos 1. Você deve então calcular e mostrar
    quantos dígitos tem o menor múltiplo de n que tem
    todos seus dígitos iguais a 1.
    :param l1:
    :return:
    """
    num, str_1, l2 = [], "", []
    while True:
        try:
            n = int(input("Digite um número inteiro: "))
            for i in range(1, len(l1)):
                str_1 = "1"
                num_1 = int(str_1)
                while num_1 % n != 0:
                    str_1 += "1"
                    num_1 = int(str_1)
                print(len(str_1))
                break
        except EOFError:
            break
    return print(*l2)


ones(numbers_not_divisible_by_2_5())
