def escolha_dificil():
    """
    Esta função calcula o número de pessoas que não
    poderão ter suas escolhas prediletas atendidas
    entre frango, bife, e massa, dadas pela aeromoça
    de um vôo e retorna um printe com o número total
    dessas pessoas.
    :return:
    """
    cont = 0
    ca, ba, pa = input().split(" ")
    cr, br, pr = input().split(" ")
    ca, ba, pa = int(ca), int(ba), int(pa)
    cr, br, pr = int(cr), int(br), int(pr)
    dif1 = ca - cr
    dif2 = ba - br
    dif3 = pa - pr
    if dif1 < 0:
        cont += dif1 * (-1)
    if dif2 < 0:
        cont += dif2 * (-1)
    if dif3 < 0:
        cont += dif3 * (-1)
    print(cont)


escolha_dificil()
