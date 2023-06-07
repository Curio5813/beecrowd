def entrada_e_saida_de_data():
    """
    Esta função recebe uma data no formato DD/MM/AA e printa na forma
    MM/DD/AA, AA/MM/DD e DD-MM-AA
    :return:
    """
    data = input().split("/")
    print(f"{data[1]}/{data[0]}/{data[2]}")
    print(f"{data[2]}/{data[1]}/{data[0]}")
    print(f"{data[0]}-{data[1]}-{data[2]}")


entrada_e_saida_de_data()
