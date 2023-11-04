from math import hypot


def guarda_costeira():
    """
    "Pega ladrão! Pega ladrão!" Roubaram a bolsa de uma inocente senhora
    que caminhava na praia da Nlogônia e o ladrão fugiu em direção ao mar.
    Seu plano parece obvio: ele pretende pegar um barco e escapar! O fugitivo,
    que a essa altura já está a bordo de sua embarcação de fuga, pretende
    seguir perpendicularmente à costa em direção ao limite de aguas internacionais,
    que fica a 12 milhas náuticas de distância, onde estará são e salvo das
    autoridades locais. Seu barco consegue percorrer essa distância a uma
    velocidade constante de VF nós. A Guarda Costeira pretende interceptá-lo,
    e sua embarcacão tem uma velocidade constante de VG nós. Supondo que ambas
    as embarcações partam da costa exatamente no mesmo instante, com uma distância
    de D milhas náuticas entre elas, será possível a Guarda Costeira alcançar o ladrão
    antes do limite de aguas internacionais? Assuma que a costa da Nlogônia é
    perfeitamente retilínea e o mar bastante calmo, de forma a permitir uma
    trajetória tão retilínea quanto a costa. A entrada é composta por diversos casos
    de teste e termina com final de arquivo (EOF). Cada caso de teste é descrito em um
    linha contendo três inteiros, D (1 ≤ D ≤ 100), VF (1 ≤ VF ≤ 100) e VG (1 ≤ VG ≤ 100),
    indicando respectivamente a distância inicial entre o fugitivo e a Guarda Costeira,
    a velocidade da embarcação do fugitivo e a velocidade da embarcação da Guarda Costeira.
    Para cada caso de teste a função imprime uma linha contendo ‘S’ se for possível que a
    Guarda Costeira alcance o fugitivo antes que ele ultrapasse o limite de águas internacionais
    ou ‘N’ caso contrário.
    :return:
    """
    while True:
        try:
            d, vf, vg = map(int, input().split(" "))
            dt = hypot(12, d)
            tg = dt / vg
            tf = 12 / vf
            if tg <= tf:
                print("S")
            elif tg > tf:
                print("N")
        except EOFError:
            break


guarda_costeira()
