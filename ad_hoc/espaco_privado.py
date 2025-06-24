from functools import total_ordering
from mimetypes import guess_type


def espaco_privado():
    """
    As pessoas vão ao cinema em grupos (ou sozinhas), mas normalmente só se preocupam
    em se socializar dentro desse grupo. Sendo escandinavo, cada grupo de pessoas
    gostaria de se sentar em pelo menos um espaço separado de qualquer outro grupo de
    pessoas para garantir sua privacidade, a menos, é claro, que eles se sentem no final
    de uma fileira. O número de assentos por fila no cinema começa em X e diminui com um
    assento por fila (até um número de 1 assento por fila). O número de grupos de tamanhos
    variados é dado como um vetor (N1,..., Nn), onde N1 é o número de pessoas que vão
    sozinhas, N2 é o número de pessoas que vão como um par, etc. Calcule a largura do assento,
    X, da fila mais larga, que criará uma solução que acomoda todos (grupos de) visitantes
    usando o menor número possível de filas de assentos. O cinema também tem capacidade
    limitada, por isso a fila mais larga não pode ultrapassar 12 lugares.

    Entrada
    A primeira linha de entrada contém um único inteiro n (1 ≤ n ≤ 12), fornecendo o tamanho do
    maior grupo no caso de teste.

    Em seguida, segue uma linha com n inteiros, o i-ésimo inteiro (indexado em 1) denotando o
    número de grupos de i pessoas que precisam estar sentados.

    Saída
    Um único número; o tamanho da menor fileira mais larga que acomodará todos os convidados.
    Se esse número for maior que 12, a saída será impossível.
    :return:
    """
    n = int(input())
    grupos = list(map(int, input().strip().split(" ")))
    pessoas, fila, fileira = 0, [], 1
    grupos.reverse()
    for i in range(n, 0, -1):
        fila.append(i)
    for i in range(0, len(fila)):
        pessoas += fila[i] * grupos[i]
    print(pessoas)
    print(fila)
    print(grupos)

espaco_privado()
