from math import lcm, gcd


def os_doces_de_candy():
    """
    Candy possui um estoque de doces de F diferentes sabores. Ela irá
    fazer vários pacotes de doces para então vendê-los. Cada pacote
    deverá ser ou um pacote contendo doces de um único sabor, ou um
    pacote sortido, contendo doces de cada sabor. Ela decidiu que um
    bom empacotamento deve honrar as seguintes condições:

    Cada doce deve ser colocado em exatamente um pacote.
    Cada pacote, independente de seu tipo, deve conter pelo menos dois doces.
    Cada pacote, independente de seu tipo, deve conter o mesmo número de doces.
    Dentro de cada pacote sortido, o número de doces de cada sabor deve ser o mesmo.
    Deve haver ao menos um pacote sortido.
    Deve haver ao menos um pacote de cada sabor.
    Candy estava pensando sobre quantos tipos de bons empacotamentos de doces ela
    poderia fazer. Dois bons empacotamentos de doces são considerados diferentes
    se e somente se eles diferem no número de pacotes sortidos, ou no número de
    doces por pacote. Como Candy irá vender seus doces durante a cerimônia de
    encerramento desta competição, você foi encorajado a responder sua questão
    tão rápido quanto possível.

    Entrada
    Cada caso de teste é descrito usando duas linhas. A primeira linha contém um
    inteiro F indicando o número de sabores (2 ≤ F ≤ 105). A segunda linha contém
    F inteiros Ci , indicando o número de doces de cada sabor (1 ≤ Ci ≤ 109 para
    cada 1 ≤ i ≤ F).

    O último caso de teste é seguido por uma linha contendo um zero.

    Saída
    Para cado caso de teste imprima um linha com um inteiro representando o número
    de diferentes bons empacotamentos de doces, de acordo com as regras dadas acima.
    :return:
    """
    while True:
        f = int(input())
        if f == 0:
            break
        sabores = sorted(list(map(int, input().split())))
        soma = sum(sabores)
        print(soma)
        diff = 1000000000 / 6
        print(1000000000 - diff)


os_doces_de_candy()
