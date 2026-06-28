def planejamento_de_evento():
    """
    Como você não compareceu à reunião geral anual do Nordic Club of Pin
    Collectors (NCPC), você foi unanimemente eleito para organizar a
    excursão deste ano para Pin City. Você é livre para escolher uma série
    de fins de semana neste outono, e deve encontrar um hotel adequado para
    a hospedagem, de preferência o mais barato possível.

    Você tem algumas restrições: O custo total da viagem deve estar dentro do
    orçamento, é claro. Todos os participantes devem ficar no mesmo hotel, para
    evitar catástrofes que aconteceram nos anos passados, onde membros se perderam
    na cidade e nunca mais foram vistos.

    Entrada
    A primeira linha da entrada consiste de quatro inteiros: N (1 ≤ N ≤ 200), que
    é o número de participantes, B (1 ≤ B ≤ 500000), que é o orçamento, H (1 ≤ H ≤ 18),
    que é o número de hotéis a considerar, e W (1 ≤ W ≤ 13), que é o número de semanas
    que você pode escolher. Em seguida, há duas linhas para cada um dos H hotéis.
    A primeira linha fornece P (1 ≤ P ≤ 10000), que é o preço por uma pessoa se hospedar
    no fim de semana no hotel. A segunda linha contém W inteiros A (0 ≤ A ≤ 1000), que
    é o número de camas disponíveis para cada fim de semana no hotel.

    Saída
    Imprima o custo mínimo da hospedagem de um grupo. Caso o custo não seja possível para
    o orçamento, imprima “stay home”.
    :return:
    """
    n, b, h, w = map(int, input().strip().split(" "))
    camas, custos = [], []
    for i in range(h):
        preco = int(input())
        camas = list(map(int, input().strip().split(" ")))
        for j in range(0, len(camas)):
            if camas[j] >= n:
                custo_total = preco * n
                custos.append(custo_total)
    if len(custos) > 0:
        if min(custos) > b:
            print("stay home")
        else:
            print(min(custos))
    if len(custos) == 0:
        print("stay home")


planejamento_de_evento()
