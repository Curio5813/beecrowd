from collections import Counter


def perguntas_mais_frequentes():
    """
    Muitos sites na internet adicionam uma sessão chamada “Perguntas
    mais Frequentes” que, como o nome já diz, contém as perguntas mais
    feitas pelos usuários que utilizam o site.

    O portal do URI costuma receber muitas perguntas de seus usuários,
    então Neilor imaginou que seria uma boa ideia adicionar uma sessão
    de Perguntas mais Frequentes no site. Como o Neilor anda muito ocupado
    ultimamente, ele pediu a sua ajuda para adicionar essa sessão.

    Dados os identificadores de perguntas feitas pelos usuários, diga o número
    de perguntas que serão adicionadas na nova sessão do site. Uma pergunta é
    classificada como “frequente” quando ela é feita ao menos K vezes.

    Entrada
    Haverá diversos casos de teste. Cada caso de teste inicia com dois inteiros N e K
    (1 ≤ N ≤ 1000, 1 ≤ K ≤ 100), indicando o número de perguntas realizadas, e o número
    de vezes que uma pergunta deve ser feita para ser considerada “frequente”,
    respectivamente.

    Em seguida haverá N inteiros P (1 ≤ P ≤ 100), cada um indicando o número de uma
    determinada pergunta.

    O último caso de teste é indicado quando N = K = 0, o qual não deverá ser processado.

    Saída
    Para cada caso de teste imprima uma linha, contendo um inteiro, indicando o número
    de perguntas que serão adicionadas na nova sessão do site.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    n, k = entrada[0], entrada[1]
    while n != 0 and k != 0:
        cont = 0
        perguntas = list(map(int, input().strip().split(" ")))
        num_p = dict(Counter(sorted(perguntas)))
        for pergunta in num_p.values():
            if pergunta >= k:
                cont += 1
        print(cont)
        entrada = list(map(int, input().strip().split(" ")))
        n, k = entrada[0], entrada[1]


perguntas_mais_frequentes()
