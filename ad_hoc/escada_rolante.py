def escada_rolante():
    """
    Escadas rolantes sem dúvidas facilitam muito a vida
    das pessoas. Subir escadas é uma das tarefas mais
    tediosas já inventadas (após a invenção das escadas
    normais).

    Após algumas observações você percebeu que há muita
    energia gasta com escadas rolantes, pois elas continuam
    funcionando mesmo quando não há ninguém à utilizando.
    Para contornar isso, o dono de um shopping local instalou
    um sensor que verifica quando há alguém na escada rolante.
    Quando o sensor não detecta nenhuma presença, a escada rolante
    é desativada, assim economizando energia até que a próxima
    pessoa chegue.

    Para ser mais específico, o sistema funciona da seguinte maneira:
    a escada está inicialmente desativada. O tempo necessário para que
    uma pessoa chegue de um lado até o outro da escada rolante é 10
    segundos. Ou seja, se uma única pessoa se aproximar da escada rolante
    no tempo t, a escada rolante ficará ativada nos tempos t, t+1, t+2, …,
    t+8 e t+9, e será desativada no tempo t+10, momento no qual a pessoa
    já saiu da escada rolante. Tal duração pode ser prolongada caso uma ou
    mais pessoas se aproximem da escada rolante durante tal processo.

    O dono do shopping local agora pediu sua ajuda. Escreva um algoritmo
    que, dados os tempos em que as pessoas se aproximaram da escada rolante,
    diga por quantos segundos a escada ficou ativada.

    Entrada
    Haverá no máximo 30 casos de teste. Cada caso de teste inicia com uma
    linha contendo um inteiro N, indicando o número de pessoas que usaram
    a escada rolante no dia em questão (1 ≤ N ≤ 100).

    Na linha seguinte haverá N inteiros distintos, dados em ordem crescente,
    indicando o tempo t em que cada pessoa se aproximou da escada (1 ≤ t ≤ 1000).

    O último caso de teste é indicado quando N = 0, o qual não deverá ser processado.

    Saída
    Para cada caso de teste imprima uma linha, contendo um inteiro, indicando o
    número de segundos que a escada rolante ficou ativa.
    :return:
    """
    while True:
        p = int(input())
        tempo = 10
        if p == 0:
            break
        pessoas = list(map(int, input().split(" ")))
        pessoas.reverse()
        for i in range(0, len(pessoas)):
            if i >= len(pessoas) - 1:
                break
            if pessoas[i] - pessoas[i + 1] >= 10:
                tempo += 10
            if pessoas[i] - pessoas[i + 1] < 10:
                tempo += pessoas[i] - pessoas[i + 1]
        print(tempo)


escada_rolante()
