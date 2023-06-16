def entrada_e_saida_com_virgula():
    """
    Esta função ler uma frase como entrada e divide em duas,
    onde o ponto de divisão é uma e única vírgula que existe
    em todas as entradas de dados dos casos-testes.
    :return:
    """
    frase = input().split(",")
    print(frase[0])
    print(frase[1])


entrada_e_saida_com_virgula()
