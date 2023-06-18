def entrada_e_saida_lendo_e_pulando_nomes():
    """
    Esta função ler 10 nomes como entrada de dados e depois
    imprime o terceiro nome da lista, o sétimo nome da lista
    e o nono nome da lista.
    :return:
    """
    nomes = []
    for i in range(10):
        nome = input()
        nomes.append(nome)
    print(nomes[2])
    print(nomes[6])
    print(nomes[8])


entrada_e_saida_lendo_e_pulando_nomes()
