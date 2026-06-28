def a_arvore_de_natal():
    """
    Esta função calaula se uma determinada árvore serve
    ou não para ser a árvore de natal de Roberto, dado as
    seguintes condições: A árvore deve ter no mínimo 200 cm
    e não deve ser maior que 300 cm, a espessura do tronco
    da árvore deve ter 50 cm de diâmetro ou mais, e o numero
    de galhos deve ser igual ou maior que 150. A função printa
    'Sim', se a arvore de natal está de acordo com as
    especificações de Roberto ou 'Nao', caso contrário.
    :return:
    """
    n = int(input())
    for i in range(n):
        h, d, g = map(int, input().split(" "))
        if 200 <= h <= 300 and d >= 50 and g >= 150:
            print("Sim")
        else:
            print("Nao")


a_arvore_de_natal()
