from math import factorial


def fatorial_de_novo():
    """
    Mateus, um calouro de engenharia, está desenvolvendo uma nova notação
    posicional para representar números inteiros. Ele o apelidou de "A
    Curious Method" ("Um Método Curioso"), representado pela sigla ACM.
    A notação ACM usa os mesmos dígitos que a notação decimal, isto é, de
    0 a 9.

    Para converter um número A da notação ACM para a notação decimal, você
    deve adicionar k termos, onde k é o número de dígitos de A (na notação ACM),
    O valor do i-ésimo termo, correspondente ao i-ésimo dígito ai, contando da
    direita para a esquerda, é ai × i!. Por exemplo, 719ACM é equivalente a
    5310, já que 7 × 3! + 1 × 2! + 9 × 1! = 53.

    Mateus acabou de iniciar seus estudos sobre teoria dos números, e provavelmente
    não sabe quais propriedades um sistema numérico deve ter, mas no momento, ele
    só está interessado em converter um número de ACM para decimal. Você pode ajudá-lo?

    Entrada
    Cada caso de teste é dado por uma única linha não-nula contendo, no máximo, 5
    dígitos, representando um número na notação ACM. A linha não possui zeros no
    início.

    O último caso de teste é representado por uma linha contendo um único zero.

    Saída
    Para cada caso de teste, escreva uma única linha contendo a representação decimal
    do número ACM correspondente.
    :return:
    """
    n = int(input())
    while n != 0:
        digitos, soma, num = [], 0, n
        while num > 0:
            resto = num % 10
            digitos.append(resto)
            num //= 10
        digitos.reverse()
        tam = len(digitos)
        for i in range(0, len(digitos)):
            soma += digitos[i] * factorial(tam)
            tam -= 1
        print(soma)
        n = int(input())


fatorial_de_novo()
