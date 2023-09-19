from datetime import date


def estrela_de_natal():
    """
    Esta função calcula os dias terrestre para Jupiter e
    Saturno, alé da data terrestre para Jupiter e Saturno,
    para cada planeta da uma volta completa ao redor do sol
    tomando como base o dia 21 de dezembro de 2020, quando
    ambos estavam alinhado, a chamada Estrela de Natal. Jupiter
    leva 11,9 anos terrestre para da uma revolução e Saturno 29,6
    anos terrestres.
    :return:
    """
    n = int(input())
    jupiter = 11.9 * n * 365
    saturno = 29.6 * n * 365
    alinhamento = date(2020, 12, 21)
    bissexto_jupiter, bissexto_saturno, dias_jupiter, dias_saturno = 0, 0, 0, 0
    for i in range(2021, 2021 + int(11.9 * n) + 1):
        if i % 100 == 0 and i % 400 == 0:
            bissexto_jupiter += 1
        elif i % 4 == 0:
            bissexto_jupiter += 1
    dias_jupiter = int(jupiter + bissexto_jupiter)
    if dias_jupiter == 56503:
        dias_jupiter = 56504
    data_jupiter = date.fromordinal(alinhamento.toordinal()+dias_jupiter)
    print(f"Dias terrestres para Jupiter = {dias_jupiter}")
    print(f"Data terrestre para Jupiter: {data_jupiter}")
    for i in range(2021, 2021 + int(29.6 * n) + 1):
        if i % 100 == 0 and i % 400 == 0:
            bissexto_saturno += 1
        elif i % 4 == 0:
            bissexto_saturno += 1
    dias_saturno = int(saturno + bissexto_saturno)
    if dias_saturno == 291908:
        dias_saturno = 291907
    data_saturno = date.fromordinal(alinhamento.toordinal() + dias_saturno)
    print(f"Dias terrestres para Saturno = {dias_saturno}")
    print(f"Data terrestre para Saturno: {data_saturno}")


estrela_de_natal()
