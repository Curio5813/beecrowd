from math import floor


def vamos_fechar():
    """
    No início do ano o Governo Federal anunciou um bloqueio no
    orçamento de várias Universidades Federais de todo o país e
    muitas delas já afirmaram não ter condições de manter as
    atividades até o final do segundo semestre letivo de 2019.
    A UFSC por exemplo, só terá recursos para funcionar até meados
    de outubro, porém não se sabe a data exata que ela irá fechar.

    Hoje, dia 20 de setembro, o setor financeiro liberou o valor
    disponível em caixa e a estimativa de custo diário para manter
    a universidade aberta. Como a equipe econômica da universidade
    está ocupada tentando achar soluções para estender o funcionamento
    da instituição, você foi convidado a ajudar calculando por mais
    quantos dias a UFSC ficará aberta e informar a data que ela irá
    fechar.

    A UFSC só continuará aberta enquanto houver recursos para manter a
    universidade durante um dia inteiro, no momento que o restante do
    dinheiro em caixa não for suficiente para arcar com o curto diário,
    a UFSC fecha.

    Entrada
    A entrada é composta por uma única linha com dois números inteiros C e G
    (1 < C, G < 2³¹) que representam respectivamente o valor em caixa que a
    UFSC tem atualmente e o gasto diário para manter a universidade aberta.
    O custo de hoje já foi descontado do valor em caixa disponibilizado.

    Saída
    Imprima, conforme o exemplo fornecido, uma única linha contendo o dia que
    UFSC irá fechar caso o Governo não realize o desbloqueio das verbas.

    É garantido que a data para o fechamento da UFSC está entre 21 de setembro e
    31 de outubro.
    :return:
    """
    c, g = map(int, input().split(" "))
    dias = floor(c / g)
    fecha = 21 + dias
    if fecha > 30:
        fecha = fecha - 30
        if fecha >= 31:
            print(f"A UFSC fecha dia 31 de outubro.")
        elif fecha < 31:
            print(f"A UFSC fecha dia {fecha} de outubro.")
    else:
        print(f"A UFSC fecha dia {fecha} de setembro.")


vamos_fechar()
