def luzes_de_natal():
    """
    Esta função calcula o número de lâmpadas queimadas consecutivas nos
    jogos de lâmpadas pisca-pisca de Natal, cada jogo com 50 lâmpadas.
    As lâmpadas queimadas são representadas pelos 1's no sistema binário
    e 0's são o número de lâmpadas funcionando. O número decimal representa
    o número de lâmpadas queimadas consecutivas, uma sequência de 1's
    até o 0 seguinte ou terminado em 1.
    :return:
    """
    jogos = int(input())
    for i in range(jogos):
        cont = 0
        maior = 0
        decimal = int(input())
        luzes = bin(decimal)
        luzes = luzes[2:]
        luzes = luzes[::-1]
        for k in luzes:
            if k == "1":
                cont += 1
                if cont > maior:
                    maior = cont
            elif k == "0" and cont >= 1:
                cont = 0
        print(maior)


luzes_de_natal()
