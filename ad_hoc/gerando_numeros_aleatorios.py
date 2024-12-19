def gerando_numeros_aleatorios():
    """
    John von Neumann propôs em 1946 um método de criação de sequências de
    números pseudo-aleatórios. Sua ideia é conhecida como o método do meio
    do quadrado e funciona da seguinte forma: Escolhe-se um valor inicial
    a0 que possui um comprimento de no máximo n em sua representação decimal.
    Multiplica-se o valor de a0 por ele mesmo, adiciona-se zeros a esquerda
    para obter uma representação decimal de comprimento 2 × n e toma-se os n
    dígitos centrais para formar ai. Repete-se o processo para cada ai com
    i > 0. Para este problema será utilizado n = 4.

    Exemplo 1: a0=5555, a02=30858025, a1=8580,...

    Examplo 2: a0=1111, a02=01234321, a1=2343,...

    Infelizmente, este gerador de números aleatórios não é muito bom. Dado um
    valor inicial, ele não produz todos os outros números com a mesma quantidade
    de dígitos.

    Sua tarefa é checar quantos números diferentes são produzidos para um valor
    inicial a0.

    Entrada
    A entrada contém vários casos de teste. Cada teste consite de uma linha contendo
    a0 (0 < a0 < 10000). Possivelmente, os números podem ter zeros à esquerda de
    forma a deixar cada número com exatamente 4 dígitos. A entrada é finalizada
    com uma linha contendo o valor 0.

    Obs.: Note que o terceiro caso de teste possui a maior quantidade de números
    diferentes gerados entre as entradas possíveis.

    Saída
    Para cada caso de teste, imprimir uma linha contendo o número de diferentes
    valores ai gerados por este gerador de números aleatórios quando inicializado
    com um valor a0. Note que a0 também deve ser contabilizado.
    :return:
    """
    str_aleatorio, lista, cont = "", [], 0
    a0 = input()
    lista.append(a0)
    a1 = int(a0)
    while a0 != 0:
        aleatorio = a1 * a1
        str_aleatorio = str(aleatorio)
        if len(str_aleatorio) < 8:
            while len(str_aleatorio) < 8:
                str_aleatorio = "0" + str_aleatorio
        if str_aleatorio[2:6] in lista:
            print(len(lista))
            lista, cont = [], 0
            a0 = input()
            if a0 == "0":
                break
            lista.append(a0)
            a1 = int(a0)
        else:
            lista.append(str_aleatorio[2:6])
            a1 = int(str_aleatorio[2:6])


gerando_numeros_aleatorios()
