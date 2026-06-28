def nem_tudo_e_greve_versao_hard():
    """
    Uma vez, enquanto estudavamos pra Maratona de Porgramção, Tobias e eu
    nos deparamos com um problema interesante, espero que vocês também
    gostem.

    Existe uma escada com N degraus. Você pode escolher entre descer 1, 2, ou 3
    degraus por vez a cada movimento. De quantas maneiras diferentes você poderia
    descer essa escada com N degraus?

    Entrada
    Um único número inteiro N (1 ≤ N ≤ 100.000), o número de degraus na escada.

    Saída
    Um único inteiro, o número combinações de formas diferentes de descer a escada.
    A resposta pode ser um pouco grande, então imprima o resto da divisão pelo nosso
    primo favorito (109+7).
    :return:
    """
    n = int(input())
    a, b, c, p = 1, 1, 2, 0
    primo = 10 ** 9 + 7
    if n == 1:
        return print(1)
    if n == 2:
        return print(2)
    if n == 3:
        return print(4)
    else:
        for i in range(3, n + 1):
            p = (a + b + c) % primo
            a, b, c = b, c, p
        print(p)


nem_tudo_e_greve_versao_hard()
