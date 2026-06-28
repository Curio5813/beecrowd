from math import sqrt


def soma_de_dois_quadrados():
    """
    Quais números inteiros podem ser representados por uma soma de dois inteiros ao quadrado?

    É essa a pergunta que seu programa deve responder!

    Por exemplo, o número 41 pode ser representado como (-4)2 + 52 = 41, já o número 7 não pode
    ser representado da mesma maneira.

    Entrada
    A entrada é composta por várias linhas, cada linha contém um inteiro com módulo menor ou igual
    a 10000.

    Saída
    Para cada linha, imprima "YES" se o número pode ser representado por uma soma de dois inteiros
    ao quadrado, caso contrário imprima "NO".
    :return:
    """
    while True:
        try:
            numero = int(input())
            if numero < 0:
                numero = abs(numero)
            flag = 0
            for i in range(0, int(sqrt(numero)) + 1):
                for j in range(0, int(sqrt(numero)) + 1):
                    if i ** 2 + j ** 2 == numero:
                        print("YES")
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                print("NO")
        except EOFError:
            break


soma_de_dois_quadrados()
