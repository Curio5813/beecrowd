def diamantes_e_areia():
    """
    João está trabalhando em uma mina, tentando retirar o máximo
    que consegue de diamantes "<>". Ele deve excluir todas as
    particulas de areia "." do processo e a cada retirada de diamante,
    novos diamantes poderão se formar. Se ele tem como uma entrada
    .<...<<..>>....>....>>>., três diamantes são formados. O primeiro
    é retirado de <..>, resultando  .<...<>....>....>>>. Em seguida o
    segundo diamante é retirado, restando .<.......>....>>>. O terceiro
    diamante é então retirado, restando no final .....>>>., sem
    possibilidade de extração de novo diamante.

    Entrada
    Deve ser lido um valor inteiro N que representa a quantidade de casos
    de teste. Cada linha a seguir é um caso de teste que contém até 1000
    caracteres, incluindo "<,>, ."

    Saída
    Você deve imprimir a quantidade de diamantes possíveis de serem extraídos
    em cada caso de entrada.
    :return:
    """
    n = int(input())
    for i in range(n):
        lapidacao, cont = [], 0
        dimantes_bruto = input()
        for k in dimantes_bruto:
            if k == "<":
                lapidacao.append(k)
            if k == ">" and len(lapidacao) > 0:
                lapidacao.pop()
                cont += 1
        print(cont)


diamantes_e_areia()
