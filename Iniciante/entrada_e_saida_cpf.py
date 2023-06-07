def entrada_e_saida_cpf():
    """
    Esta função ler um número de CPF e printa os 4 números
    de cada parte do CPF.
    :return:
    """
    cpf = input().split(".")
    first = cpf[2][0:3]
    last = cpf[2][4:6]
    for i in range(0, len(cpf)):
        if i == 2:
            print(first)
            print(last)
        else:
            print(cpf[i])


entrada_e_saida_cpf()
