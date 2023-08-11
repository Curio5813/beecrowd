from math import ceil


def hora_da_corrida():
    """
    Esta função calcula e printa o número mínimo de placas que Vinícios
    tem que contar, que estão distribuídas igualmente em distância, de uma
    para outra, ao redor de um lago, para percorrer, respectivamente, 10%, 20%,
    30%, 40%, 50%, 60%, 70%, 80% e 90%, da sua meta. Tendo como entrada de
    dados, o número de voltas que pretende dar ao redor do lago e a quantidade
    de placas distribuidas ao redor dele.
    :return:
    """
    v, n = map(int, input().split(" "))
    total = v * n
    percent = 10
    for i in range(1, 10):
        if i == 9:
            placas = ceil(total * (i / percent))
            print(f"{placas}")
            break
        placas = ceil(total * (i / percent))
        print(f"{placas}", end=" ")


hora_da_corrida()
