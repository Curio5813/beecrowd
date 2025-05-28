from collections import Counter


def quadro_de_medalhas():
    """
    Alguém deixou o quadro de medalhas das olimpíadas fora de ordem.
    Seu programa deve colocá-lo na ordem correta. A ordem dos países
    no quadro de medalhas é dada pelo número de medalhas de ouro. Se
    há empate em medalhas de ouro, a nação que tiver mais medalhas de
    prata fica a frente. Havendo empate em medalhas de ouro e prata,
    fica mais bem colocado o país com mais medalhas de bronze. Se dois
    ou mais países empatarem nos três tipos de medalhas, seu programa
    deve mostrá-los em ordem alfabética.

    Entrada
    A entrada é dada pelo número de países participantes N (0 ≤ N ≤ 500)
    seguido pela lista dos países, com suas medalhas de ouro O (0 ≤ O ≤ 10000),
    prata P (0 ≤ P ≤ 10000) e bronze B (0 ≤ B ≤ 10000).

    Saída
    A saída deve ser a lista de países, com suas medalhas de ouro, prata e
    bronze, na ordem correta do quadro de medalhas, com as nações mais premiadas
    aparecendo primeiro.
    :return:
    """
    n = int(input())
    quadro = []
    for i in range(n):
        entrada = input().strip().split(" ")
        pais = entrada[0]
        ouro = int(entrada[1])
        prata = int(entrada[2])
        bronze = int(entrada[3])
        quadro.append((pais, ouro, prata, bronze))
    quadro.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))
    for pais, ouro, prata, bronze in quadro:
        print(f"{pais} {ouro} {prata} {bronze}")


quadro_de_medalhas()
