def maquina_de_cafe():
    """
    Esta função calcula e retorna um printe do menor tempo que levam os
    funcionários de uma empresa tomar um cafezinho expresso, tendo em
    consideração que os funcionários levam um minuto para tomar café
    de um andar para o outro e mais um minuto para retorna ao seu posto
    de trabalho.
    :return:
    """
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    b = a1 * 2 + a3 * 2
    c = a2 * 2 + a3 * 4
    d = a2 * 2 + a1 * 4
    if c >= b and d >= b:
        return print(b)
    elif c <= d:
        return print(c)
    elif d < c:
        return print(d)


maquina_de_cafe()
