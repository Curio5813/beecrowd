def top_n():
    """
    Esta função retorna o menor valor entre as categorias que
    o time pode ter se classificado. É bom observar que o menor
    valor de cada catergoria é a melhor possição na categoria.
    """
    k = int(input())
    if k == 1:
        return print("Top 1")
    elif 2 <= k <= 3:
        return print("Top 3")
    elif 4 <= k <= 5:
        return print("Top 5")
    elif 6 <= k <= 10:
        return print("Top 10")
    elif 11 <= k <= 25:
        return print("Top 25")
    elif 26 <= k <= 50:
        return print("Top 50")
    elif 51 <= k <= 100:
        return print("Top 100")


top_n()
