def sequencia_de_threebonacci():
    """
    Um número pertence à sequência de Threebonacci caso pertença à sequência
    de Fibonacci (assuma que o primeiro termo da série é o 1) e atenda pelo
    menos um dos últimos critérios abaixo:

    1 – A representação do número possui pelo menos um dígito 3.

    2 – O número é múltiplo de 3.

    Entrada
    Cada caso de teste contém um inteiro N (1 ≤ N ≤ 60 ). A entrada termina com
    o fim de arquivo (EOF).

    Saída
    Para cada caso de teste imprima uma linha contendo o N-ésimo termo da série
    de Threebonacci.
    :return:
    """
    while True:
        try:
            n = int(input())
            a, b, p = 1, 2, 3
            threebonacci = []
            while len(threebonacci) < n:
                num_str1 = str(a)
                if a % 3 == 0:
                    threebonacci.append(a)
                elif "3" in num_str1:
                    threebonacci.append(a)
                a = b
                b = p
                p = a + b
            print(threebonacci[-1])
        except EOFError:
            break


if __name__ == '__main__':
    sequencia_de_threebonacci()
