def quanta_mandioca():
    """
    Está função calcula e printa o valor total (em gramas) de
    mandioca os personagens do problema comerão na casa de Dona
    Chica e também Dona Chica.
    :return:
    """
    lista, quant, quants, d_chica = [300, 1500, 600, 1000, 150], 0, 0, 225
    for i in range(5):
        mandioca = int(input())
        quant = mandioca * lista[i]
        quants += quant
    quants += d_chica
    print(quants, end="\n")


quanta_mandioca()
