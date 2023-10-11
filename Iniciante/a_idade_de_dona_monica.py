def a_idade_de_dona_monica():
    """
    Esta função calcula a idade do filho mais velho de
    Dona Mônica, sabendo que Dona Monica tem três filhos
    e que a soma de suas idades é igual a idade dela.
    :return:
    """
    idades = []
    monica = int(input())
    filho1 = int(input())
    filho2 = int(input())
    filho3 = monica - filho1 - filho2
    idades.append(filho1)
    idades.append(filho2)
    idades.append(filho3)
    print(max(idades))


a_idade_de_dona_monica()
