def sobrinho_do_meio():
    """
    Esta função calcula e printa qual o nome do sobrinho do meio
    do Tio Patinhas, dado como entrada suas idades, sabendo que
    Luisinho é mais o mais novo, Zezinho o sobrinho do meio e
    Huguinho o mais velho.
    :return:
    """
    h, z, lu = map(int, input().split(" "))
    if z < h < lu or lu < h < z:
        print("huguinho")
    elif h < z < lu or lu < z < h:
        print("zezinho")
    elif h < lu < z or z < lu < h:
        print("luisinho")


sobrinho_do_meio()
