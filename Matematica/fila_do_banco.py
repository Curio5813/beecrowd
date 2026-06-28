from math import  factorial


def fila_do_banco():
    """
    André, Bruno e Carlos são amigos a um bom tempo, e se tem uma
    coisa que eles sabem um sobre o outro é o quanto eles são pontuais.
    André é conhecido por ser sempre o último a chegar em um compromisso
    entre o três, e Carlos é sempre o primeiro. Bruno sempre chega
    antes de André, mas nunca antes de Carlos.

    Chegou o fim do mês e os três precisam ir ao banco para pagar algumas
    contas. Contando com eles, há N pessoas na fila para usar o caixa.
    Sabendo o quanto eles são pontuais entre si, de quantas maneiras possíveis
    a fila do banco pode estar ordenada?

    Lembre-se que as regras acima só se aplicam entre eles, por exemplo,
    Carlos sempre chega antes que Bruno e André, mas pode chegar depois de
    outras pessoas na fila. Duas ordenações de fila são consideradas diferentes
    se ao menos uma pessoa está em um lugar diferente nas duas ordenações.

    Entrada
    Haverá diversos casos de teste. Cada caso de teste inicia com um inteiro
    N (3 ≤ N ≤ 10⁵), indicando o número de pessoas na fila, incluindo André,
    Bruno e Carlos.

    O último caso de teste é indicado quando N = 0.

    Saída
    Para cada caso de teste imprima uma linha contendo um inteiro, representando
    o número de maneiras que a fila do banco pode estar ordenada. Como o resultado
    pode ser um valor muito alto, imprima o resultado com resto de divisão em
    1000000009.
    :return:
    """
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            p = n - 3
            arranjos = (factorial(n) // factorial(n - p)) % 1000000009
            print(arranjos)


fila_do_banco()
