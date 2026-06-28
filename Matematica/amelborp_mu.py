def amelborp_mu():
    """
    O número reverso de um número natural N é o número que obtemos
    quando lemos os dígitos de N da direita para a esquerda. Por exemplo,
    o número reverso de 1234 é 4321 e o número reverso de 150 (um número
    com 3 dígitos) é 51 (um número com 2 dígitos). Neste problema, dizemos
    que um número é bem-revertível se é estritamente menor que seu número
    reverso. Exemplos de números bem-revertíveis são 1234, 15 e 819.

    Entrada
    A única linha da entrada consiste de um único inteiro positivo K (K ≤ 18).

    Saída
    A única linha da saída deve consistir unicamente do número de números com
    exatos K dígitos que são bem-revertíveis.
    :return:
    """
    k = int(input())
    numeros_reversos = [0, 36, 360, 4005, 40050, 404550, 4045500, 40495500, 404955000,
                        4049955000, 40499550000, 404999550000, 4049995500000, 40499995500000,
                        404999955000000, 4049999955000000, 40499999550000000, 404999999550000000]
    print(numeros_reversos[k - 1])


amelborp_mu()
