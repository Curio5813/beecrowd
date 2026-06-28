def simulador():
    """
    Séculos após a invasão alienígena, quando a humanidade já está
    completamente reconstruída, foram encontrados um conjunto de
    programas escritos em uma linguagem obsoleta, chamada Java++. Por
    curiosidade histórica, você foi designado a tentar entender oque
    estes programas faziam.

    Sua tarefa é escrever um simulador para estes programas, e como teste
    inicial, o simulador deve ser capaz de calcular o resultado da última
    variável atribuída de cada programa.

    Entrada
    Cada entrada consiste de um programa. O programa só contem 2 tipos de
    instruções. Uma para atribuir uma variável e outra para executar uma
    soma.

    As instruções de declaração são no formato:

    A := B

    Onde A é um nome de variável válido e B é um inteiro positivo.

    As instruções de soma são no formato:

    A := B + C

    Onde A é um nome de variável válido e B ou C são ou um nome de variável
    válido ou um inteiro positivo.

    Os tokens deste programa são sempre separados por espaço e as instruções
    são separadas por uma quebra de linha.

    São nomes de variáveis válidos todas as combinações de até 8 letras minúsculas.

    Os programas tem, no máximo, 2000 instruções.

    Variáveis são atribuídas, no máximo, 1 vez.

    Saída
    A saída consiste de apenas 1 linha, contendo apenas um número inteiro, referente
    ao valor a última variável atribuída, seja por uma atribuição direta ou por uma
    soma.
    :return:
    """
    instrucoes = []
    while True:
        try:
            linha = input().strip()
        except EOFError:
            break
        if linha == "":
            break
        instrucoes.append(linha.split())
    memoria = {}
    for instr in instrucoes:
        var = instr[0]
        if len(instr) == 3:
            valor = int(instr[2])
        else:
            x = instr[2]
            y = instr[4]
            valor = (memoria[x] if x in memoria else int(x)) + \
                    (memoria[y] if y in memoria else int(y))
        memoria[var] = valor
    ultima_var = instrucoes[-1][0]
    print(memoria[ultima_var])


simulador()
